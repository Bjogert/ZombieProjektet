#!/usr/bin/env python3
"""Deterministic fictional design briefs, NOT a PZ placement or loot generator.

Only standard-library dependencies. Outputs are separate from game/source data.
Existing different output files are never replaced, including human edits.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import re
import sys
from typing import Any

GENERATOR_VERSION = '0.1.0'
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / 'data/design/household_seeds.json'
SPACES = {'kitchen', 'living_room', 'bedroom', 'storage', 'garage', 'workshop',
          'garden', 'wardrobe', 'hallway', 'spare_room'}
CONTEXTS = {'countryside', 'rural_village', 'planned_neighbourhood', 'town_centre'}
HABITS = {
    'orderliness': {'tidy', 'mixed', 'relaxed'},
    'repair_preference': {'repair', 'reuse', 'buy_used', 'buy_new'},
    'social_style': {'private', 'small_circle', 'hosting'},
    'cooking_style': {'daily', 'simple', 'batch', 'enthusiastic'},
}


def _object(value: Any, required: set[str], optional: set[str], label: str) -> None:
    if not isinstance(value, dict):
        raise ValueError(f'{label} must be an object')
    missing, extra = required - value.keys(), value.keys() - required - optional
    if missing or extra:
        raise ValueError(f'{label}: missing {sorted(missing)}, unknown {sorted(extra)}')


def _text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be nonempty text')


def _integer(value: Any, low: int, high: int, label: str) -> None:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f'{label} must be an integer from {low} to {high}')


def _strings(value: Any, label: str, *, allow_empty: bool = False) -> None:
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValueError(f'{label} must be a list' + ('' if allow_empty else ' with entries'))
    for item in value:
        _text(item, label)
    if len(set(value)) != len(value):
        raise ValueError(f'{label} contains duplicates')


def validate_catalog(catalog: dict[str, Any]) -> None:
    _object(catalog, {'schema_version', 'version', 'status', 'provenance', 'contexts', 'people', 'themes'}, set(), 'catalog')
    _integer(catalog['schema_version'], 1, 1, 'catalog.schema_version')
    for key in ('version', 'status', 'provenance'):
        _text(catalog[key], f'catalog.{key}')
    if catalog['status'] != 'experimental_design':
        raise ValueError('This planner supports experimental_design catalogs only')
    _strings(catalog['contexts'], 'contexts')
    if set(catalog['contexts']) != CONTEXTS:
        raise ValueError('Use the four existing environment contexts')
    ids: set[str] = set()
    interests: set[str] = set()
    if not isinstance(catalog['people'], list) or not catalog['people']:
        raise ValueError('people must be a nonempty list')
    for person in catalog['people']:
        _object(person, {'id', 'name', 'pronouns', 'background', 'interests', 'habits'}, set(), 'person')
        for key in ('id', 'name', 'pronouns', 'background'):
            _text(person[key], f'person.{key}')
        if not re.fullmatch(r'[a-z][a-z0-9_]*', person['id']) or person['id'] in ids:
            raise ValueError('Invalid or duplicate person ID')
        ids.add(person['id'])
        _strings(person['interests'], 'person.interests')
        interests.update(person['interests'])
        _object(person['habits'], set(HABITS), set(), 'habits')
        for key, choices in HABITS.items():
            if not isinstance(person['habits'][key], str) or person['habits'][key] not in choices:
                raise ValueError(f'Invalid habit: {key}')
    ids.clear()
    if not isinstance(catalog['themes'], list) or not catalog['themes']:
        raise ValueError('themes must be a nonempty list')
    for theme in catalog['themes']:
        _object(theme, {'id', 'interests', 'requires_any_space', 'base_weight', 'context_bonus', 'notes'}, set(), 'theme')
        _text(theme['id'], 'theme.id')
        _text(theme['notes'], 'theme.notes')
        if not re.fullmatch(r'[a-z][a-z0-9_]*', theme['id']) or theme['id'] in ids:
            raise ValueError('Invalid or duplicate theme ID')
        ids.add(theme['id'])
        _strings(theme['interests'], 'theme.interests')
        if not set(theme['interests']) <= interests:
            raise ValueError('Theme uses an unknown interest')
        _strings(theme['requires_any_space'], 'theme.requires_any_space')
        if not set(theme['requires_any_space']) <= SPACES:
            raise ValueError('Theme uses an unknown space')
        _integer(theme['base_weight'], 0, 100, 'base_weight')
        if not isinstance(theme['context_bonus'], dict):
            raise ValueError('context_bonus must be an object')
        for context, bonus in theme['context_bonus'].items():
            if context not in CONTEXTS:
                raise ValueError('Unknown bonus context')
            _integer(bonus, 0, 20, 'context bonus')


def _validate_request(request: dict[str, Any], people: dict[str, Any]) -> None:
    _object(request, {'schema_version', 'building_id', 'seed', 'context', 'spaces', 'theme_limit', 'resources', 'life_event'},
            {'resident_ids', 'resident_count', 'theme_overrides'}, 'request')
    _integer(request['schema_version'], 1, 1, 'request.schema_version')
    _text(request['building_id'], 'building_id')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,79}', request['building_id']):
        raise ValueError('Use an opaque building ID, not an address or coordinates')
    _integer(request['seed'], 0, 2**63 - 1, 'seed')
    for key, allowed in (
        ('context', CONTEXTS),
        ('resources', {'tight', 'modest', 'comfortable'}),
        ('life_event', {'established_home', 'recent_move', 'inherited_home', 'renovation'}),
    ):
        if not isinstance(request[key], str) or request[key] not in allowed:
            raise ValueError(f'Unknown {key}')
    _strings(request['spaces'], 'spaces')
    if not set(request['spaces']) <= SPACES:
        raise ValueError('Unknown space in request')
    _integer(request['theme_limit'], 1, 5, 'theme_limit')
    if ('resident_ids' in request) == ('resident_count' in request):
        raise ValueError('Supply resident_ids OR resident_count, not both')
    if 'resident_ids' in request:
        _strings(request['resident_ids'], 'resident_ids')
        _integer(len(request['resident_ids']), 1, 4, 'number of residents')
        if not set(request['resident_ids']) <= people.keys():
            raise ValueError('Unknown resident ID')
    else:
        _integer(request['resident_count'], 1, min(4, len(people)), 'resident_count')
    _strings(request.get('theme_overrides', []), 'theme_overrides', allow_empty=True)
    if len(request.get('theme_overrides', [])) > request['theme_limit']:
        raise ValueError('More overrides than theme_limit')


def _rng(request: dict[str, Any], stream: str) -> random.Random:
    key = [GENERATOR_VERSION, request['seed'], request['building_id'], stream]
    digest = hashlib.sha256(json.dumps(key, ensure_ascii=False).encode('utf-8')).digest()
    return random.Random(int.from_bytes(digest, 'big'))


def build_brief(catalog: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    """Plan motifs only. Identities and stories are fictional; no game files touched."""
    validate_catalog(catalog)
    people = {p['id']: p for p in catalog['people']}
    _validate_request(request, people)
    resident_ids = request.get('resident_ids')
    if resident_ids is None:
        resident_ids = _rng(request, 'residents').sample(sorted(people), request['resident_count'])
    residents = [people[i] for i in sorted(resident_ids)]
    spaces = set(request['spaces'])
    overrides = sorted(request.get('theme_overrides', []))
    eligible, excluded = {}, []
    for theme in sorted(catalog['themes'], key=lambda t: t['id']):
        if not spaces.intersection(theme['requires_any_space']):
            excluded.append({'theme_id': theme['id'], 'reason': 'no compatible space'})
            continue
        supporters = [p['id'] for p in residents if set(p['interests']).intersection(theme['interests'])]
        # Relative design weights, NOT real-world demographic probabilities.
        weight = theme['base_weight'] + 2 * len(supporters) + theme['context_bonus'].get(request['context'], 0)
        if weight == 0 and theme['id'] not in overrides:
            excluded.append({'theme_id': theme['id'], 'reason': 'no motivating interest or context'})
            continue
        eligible[theme['id']] = {'theme_id': theme['id'], 'weight': weight, 'supported_by': supporters,
                                  'notes': theme['notes']}
    if not set(overrides) <= eligible.keys():
        raise ValueError('Override theme is unknown or incompatible with available space')
    selected = [eligible[i] for i in overrides]
    pool = [entry for key, entry in eligible.items() if key not in overrides]
    rng = _rng(request, 'shared_themes')
    while pool and len(selected) < request['theme_limit']:
        draw = rng.randrange(sum(entry['weight'] for entry in pool))
        for index, entry in enumerate(pool):
            draw -= entry['weight']
            if draw < 0:
                selected.append(pool.pop(index))
                break
    # Sort catalog lists so cosmetic file order does not change provenance hash.
    canonical = dict(catalog, people=sorted(catalog['people'], key=lambda p: p['id']),
                     themes=sorted(catalog['themes'], key=lambda t: t['id']))
    digest = hashlib.sha256(json.dumps(canonical, ensure_ascii=False, sort_keys=True).encode('utf-8')).hexdigest()
    # Deep-copy output: callers must not mutate the catalog through returned profiles.
    result = {
        'schema_version': 1, 'generator_version': GENERATOR_VERSION,
        'catalog_version': catalog['version'], 'catalog_sha256': digest,
        'status': 'design_brief_not_game_content', 'fictional': True,
        'building_id': request['building_id'], 'seed': request['seed'],
        'context': request['context'], 'spaces': sorted(spaces),
        'resources': request['resources'], 'life_event': request['life_event'],
        'residents': residents, 'shared_themes': selected, 'theme_overrides': overrides,
        'excluded_themes': excluded,
        'unfilled_theme_slots': request['theme_limit'] - len(selected),
        'limits': ['No furniture coordinates, item IDs or loot changes.',
                   'Habits, resources and life event are designer inputs, not implemented layout rules.',
                   'Preserve each resident\'s personal interests; shared motifs are not their complete possessions.',
                   'Names, pronouns, occupations and story text do not affect selection weights.',
                   'Existing outputs are frozen; changes require an explicitly reviewed new output.'],
    }
    return json.loads(json.dumps(result, ensure_ascii=False))


def write_brief(path: Path, brief: dict[str, Any]) -> bool:
    """Create a new file, or accept an identical one. Never replace different data."""
    text = json.dumps(brief, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open('x', encoding='utf-8', newline='\n') as handle:
            handle.write(text)
    except FileExistsError:
        try:
            existing = json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, OSError) as exc:
            raise ValueError('Existing output is unreadable; left unchanged') from exc
        if existing != brief:
            raise ValueError('Existing output differs; left unchanged. Review a new output instead of rerolling.')
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, default=DEFAULT_CATALOG)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        catalog = json.loads(args.catalog.read_text(encoding='utf-8'))
        request = json.loads(args.request.read_text(encoding='utf-8'))
        created = write_brief(args.output, build_brief(catalog, request))
    except (ValueError, OSError) as exc:
        print(f'Household brief failed: {exc}', file=sys.stderr)
        return 1
    print('Design brief created; not game content.' if created else 'Identical frozen brief; no changes.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
