"""Synthetic design tests; these do not verify PZ integration or loot balance."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from tools.household_briefs import build_brief, main, validate_catalog, write_brief

ROOT = Path(__file__).resolve().parents[1]


class HouseholdBriefTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'data/design/household_seeds.json').read_text(encoding='utf-8'))
        self.request = json.loads((ROOT / 'data/design/household_example.json').read_text(encoding='utf-8'))

    def build(self):
        return build_brief(self.catalog, self.request)

    def test_catalog_and_twenty_fictional_seeds(self):
        validate_catalog(self.catalog)
        self.assertEqual(len(self.catalog['people']), 20)
        self.assertEqual(sum(p['pronouns'] == 'he/him' for p in self.catalog['people']), 10)
        self.assertEqual(sum(p['pronouns'] == 'she/her' for p in self.catalog['people']), 10)

    def test_identical_requests_are_identical(self):
        self.assertEqual(self.build(), self.build())

    def test_resident_order_does_not_matter(self):
        before = self.build()
        self.request['resident_ids'].reverse()
        self.assertEqual(before, self.build())

    def test_catalog_order_does_not_matter(self):
        before = self.build()
        self.catalog['people'].reverse()
        self.catalog['themes'].reverse()
        self.assertEqual(before, self.build())

    def test_other_building_does_not_advance_shared_random_state(self):
        before = self.build()
        other = dict(self.request, building_id='other-synthetic-house', seed=42)
        build_brief(self.catalog, other)
        self.assertEqual(before, self.build())

    def test_people_auto_selection_is_reproducible(self):
        del self.request['resident_ids']
        self.request['resident_count'] = 2
        self.assertEqual(self.build(), self.build())
        self.assertEqual(len(self.build()['residents']), 2)

    def test_names_pronouns_and_background_do_not_change_theme_selection(self):
        before = self.build()['shared_themes']
        for person in self.catalog['people']:
            person['name'], person['pronouns'], person['background'] = 'Different', 'they/them', 'Different invented story'
        self.assertEqual(before, self.build()['shared_themes'])

    def test_no_mutation_or_shared_references(self):
        catalog, request = copy.deepcopy(self.catalog), copy.deepcopy(self.request)
        result = self.build()
        result['residents'][0]['interests'].append('not_real')
        self.assertEqual(self.catalog, catalog)
        self.assertEqual(self.request, request)

    def test_preserves_personal_needs_for_both_residents(self):
        result = self.build()
        residents = {r['id']: r for r in result['residents']}
        self.assertIn('hunting', residents['nils']['interests'])
        self.assertIn('gardening', residents['birgitta']['interests'])

    def test_theme_weights_have_traceable_support(self):
        self.request['theme_overrides'] = ['hunting_storage']
        result = self.build()['shared_themes'][0]
        self.assertEqual(result['theme_id'], 'hunting_storage')
        self.assertEqual(result['supported_by'], ['nils'])
        self.assertEqual(result['weight'], 2)

    def test_specialist_theme_needs_a_motive_or_explicit_override(self):
        result = self.build()
        self.assertIn({'theme_id': 'music_corner', 'reason': 'no motivating interest or context'}, result['excluded_themes'])
        self.request['theme_overrides'] = ['music_corner']
        self.assertEqual(self.build()['shared_themes'][0]['theme_id'], 'music_corner')

    def test_hunter_can_live_in_town(self):
        self.request.update(context='town_centre', theme_overrides=['hunting_storage'])
        self.assertEqual(self.build()['shared_themes'][0]['theme_id'], 'hunting_storage')

    def test_garden_requires_space_not_a_rural_label(self):
        self.request.update(spaces=['kitchen', 'living_room', 'bedroom'], theme_limit=5)
        result = self.build()
        self.assertNotIn('garden_hobby', [t['theme_id'] for t in result['shared_themes']])
        self.assertIn({'theme_id': 'garden_hobby', 'reason': 'no compatible space'}, result['excluded_themes'])

    def test_override_preserved_when_seed_changes(self):
        self.request['theme_overrides'] = ['reading_corner', 'coffee_visits']
        for seed in (0, 17, 1000000):
            self.request['seed'] = seed
            self.assertTrue(set(self.request['theme_overrides']) <= {t['theme_id'] for t in self.build()['shared_themes']})

    def test_no_duplicate_themes(self):
        self.request['theme_limit'] = 5
        for seed in range(30):
            self.request['seed'] = seed
            ids = [t['theme_id'] for t in self.build()['shared_themes']]
            self.assertEqual(len(ids), len(set(ids)))

    def test_insufficient_space_is_reported_not_fabricated(self):
        self.request.update(spaces=['garden'], theme_limit=5, theme_overrides=[])
        result = self.build()
        self.assertEqual(len(result['shared_themes']), 1)
        self.assertEqual(result['unfilled_theme_slots'], 4)

    def test_output_is_not_game_content(self):
        result = self.build()
        self.assertTrue(result['fictional'])
        self.assertEqual(result['status'], 'design_brief_not_game_content')
        self.assertNotIn('items', result)
        self.assertNotIn('placements', result)
        self.assertEqual(len(result['catalog_sha256']), 64)

    def test_many_buildings_have_variation(self):
        del self.request['resident_ids']
        self.request['resident_count'] = 2
        combinations = set()
        for index in range(30):
            self.request['building_id'] = f'fictional-{index}'
            result = self.build()
            combinations.add(tuple(r['id'] for r in result['residents']))
        self.assertGreater(len(combinations), 10)

    def test_invalid_requests_fail_closed(self):
        mutations = [
            ('politics', 'anything'), ('real_resident', 'someone'),
            ('seed', True), ('seed', -1), ('seed', 1.2), ('seed', '1'),
            ('theme_limit', 0), ('theme_limit', 6), ('context', 'unknown'),
            ('spaces', ['nonexistent']), ('spaces', []), ('spaces', ['kitchen','kitchen']),
            ('building_id', '../address'), ('building_id', ''),
            ('resident_ids', ['missing']), ('resident_ids', []), ('resident_ids', ['nils','nils']),
            ('resident_count', 1), ('theme_overrides', ['unknown']),
            ('theme_overrides', ['reading_corner','reading_corner']),
            ('theme_overrides', ['reading_corner','coffee_visits','music_corner','kitchen_hobby']),
            ('resources', 'rich'), ('life_event', 'crime'), ('schema_version', 2),
        ]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                request = dict(self.request, **{key:value})
                with self.assertRaises(ValueError):
                    build_brief(self.catalog, request)

    def test_incompatible_override_fails(self):
        self.request.update(spaces=['garden'], theme_overrides=['reading_corner'])
        with self.assertRaises(ValueError):
            self.build()

    def test_invalid_catalogs_fail(self):
        for mutation in ('duplicate_person','duplicate_theme','bad_weight','bad_interest','bad_space','bad_context'):
            with self.subTest(mutation=mutation):
                bad = copy.deepcopy(self.catalog)
                if mutation == 'duplicate_person': bad['people'].append(copy.deepcopy(bad['people'][0]))
                elif mutation == 'duplicate_theme': bad['themes'].append(copy.deepcopy(bad['themes'][0]))
                elif mutation == 'bad_weight': bad['themes'][0]['base_weight'] = -1
                elif mutation == 'bad_interest': bad['themes'][0]['interests'] = ['not_known']
                elif mutation == 'bad_space': bad['themes'][0]['requires_any_space'] = ['cloud']
                elif mutation == 'bad_context': bad['themes'][0]['context_bonus'] = {'cloud':1}
                with self.assertRaises(ValueError): validate_catalog(bad)

    def test_write_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'brief.json'
            self.assertTrue(write_brief(path, self.build()))
            before = path.read_bytes()
            self.assertFalse(write_brief(path, self.build()))
            self.assertEqual(path.read_bytes(), before)

    def test_manual_edits_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'brief.json'
            write_brief(path, self.build())
            edited = self.build()
            edited['manual_note'] = 'Keep the inherited cabinet'
            path.write_text(json.dumps(edited), encoding='utf-8')
            before = path.read_bytes()
            with self.assertRaises(ValueError): write_brief(path, self.build())
            self.assertEqual(path.read_bytes(), before)

    def test_library_change_requires_review_not_silent_reroll(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'brief.json'
            write_brief(path, self.build())
            before = path.read_bytes()
            self.catalog['version'] = '0.2.0'
            with self.assertRaises(ValueError): write_brief(path, self.build())
            self.assertEqual(path.read_bytes(), before)

    def test_invalid_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'brief.json'
            path.write_text('not json', encoding='utf-8')
            with self.assertRaises(ValueError): write_brief(path, self.build())
            self.assertEqual(path.read_text(), 'not json')

    def test_cli_smoke(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'brief.json'
            argv = ['--request',str(ROOT/'data/design/household_example.json'),'--output',str(output)]
            self.assertEqual(main(argv), 0)
            self.assertEqual(main(argv), 0)
            self.assertEqual(json.loads(output.read_text(encoding='utf-8')), self.build())

    def test_cli_reports_bad_input(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / 'bad.json'
            bad.write_text('[]', encoding='utf-8')
            self.assertEqual(main(['--request',str(bad),'--output',str(Path(directory)/'output.json')]), 1)


if __name__ == '__main__':
    unittest.main()
