"""Build a synthetic one-cell fixture from stable IDs and separate saved choices.

Run as python -m tools.placement_source. Official WorldEd performs binary export.
This bounded library supports one rectangular cottage, four reviewed orientations
and an optional garden. It does not read geodata or fit templates to real houses.
"""
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from tools.build_m0 import SIZE, make_tmx, write_png
from tools.building_styles import unique_override_keys
from tools.garden_source import garden_layers

ROOT = Path(__file__).resolve().parents[1]
CHOICES = {'house', 'rotation', 'garden'}


def build(output, tiles, game, source, choices):
    """Validate all placements and resources before writing a new output folder."""
    if output.exists():
        raise FileExistsError(f'Refusing to replace existing output: {output}')
    if not isinstance(source, dict) or set(source) != {'defaults', 'buildings'}:
        raise ValueError('Source must contain defaults and buildings')
    defaults, records = source['defaults'], source['buildings']
    if not isinstance(defaults, dict) or set(defaults) != CHOICES:
        raise ValueError('Defaults must specify house, rotation and garden')
    if not isinstance(records, list) or not records:
        raise ValueError('At least one synthetic building is required')
    if not isinstance(choices, dict):
        raise ValueError('Choices must be an object keyed by stable building ID')
    ids = set()
    for record in records:
        if not isinstance(record, dict) or set(record) != {'id', 'origin'}:
            raise ValueError('Each building must contain id and origin')
        identifier = record['id']
        if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
            raise ValueError('Building IDs must be unique nonempty strings')
        ids.add(identifier)
        origin = record['origin']
        if not isinstance(origin, list) or len(origin) != 2 or any(type(v) is not int for v in origin):
            raise ValueError('Building origin must contain two integers')
    if set(choices) - ids:
        raise ValueError('Choices contain unknown building IDs')
    layers = {'0_Floor': [('blends_natural_01', 16)] * SIZE ** 2,
              '0_Furniture': [None] * SIZE ** 2}
    manifest, envelopes, copies = [], [], {}
    for record in sorted(records, key=lambda r: r['id']):
        identifier = record['id']
        override = choices.get(identifier, {})
        if not isinstance(override, dict) or set(override) - CHOICES:
            raise ValueError(f'Invalid choices for {identifier}')
        selected = defaults | override
        house, rotation, garden = (selected[k] for k in ('house', 'rotation', 'garden'))
        if house != 'swedish_cottage_01':
            raise ValueError(f'Unsupported house template: {house}')
        if type(rotation) is not int or rotation not in (0, 90, 180, 270):
            raise ValueError('Rotation must be 0, 90, 180 or 270 degrees')
        if garden not in (None, 'cottage_garden_01'):
            raise ValueError(f'Unsupported garden template: {garden}')
        tbx = ROOT / f'assets/buildings/cottage_rotations/cottage_{rotation}.tbx'
        data = tbx.read_bytes()
        building = ET.fromstring(data)
        width, height = (6, 10) if rotation in (0, 180) else (10, 6)
        if building.tag != 'building' or (building.get('width'), building.get('height')) != (str(width), str(height)):
            raise ValueError(f'House variant dimensions disagree with rotation: {tbx}')
        ox, oy = record['origin']
        # Reserve the house and an access ring even when the garden is disabled.
        x0, y0, x1, y1 = ox - 1, oy - 1, ox + width + 1, oy + height + 1
        additions = {}
        if garden is not None:
            template = json.loads((ROOT / f'assets/gardens/{garden}.json').read_text(encoding='utf-8'))
            if template['house_size'] != [6, 10]:
                raise ValueError('Garden must fit the unrotated cottage')
            additions = garden_layers(template, (ox, oy), rotation=rotation)
            occupied = [i for values in additions.values() for i, tile in enumerate(values) if tile]
            x0 = min(x0, min(i % SIZE for i in occupied))
            y0 = min(y0, min(i // SIZE for i in occupied))
            x1 = max(x1, max(i % SIZE for i in occupied) + 1)
            y1 = max(y1, max(i // SIZE for i in occupied) + 1)
        if not (0 <= x0 < x1 <= SIZE and 0 <= y0 < y1 <= SIZE):
            raise ValueError(f'Building or access outside authoring cell: {identifier}')
        for other, a, b, c, d in envelopes:
            if x0 < c and a < x1 and y0 < d and b < y1:
                raise ValueError(f'Building/garden/access envelopes overlap: {identifier}, {other}')
        envelopes.append((identifier, x0, y0, x1, y1))
        for layer, values in additions.items():
            for i, tile in enumerate(values):
                if tile is not None:
                    layers[layer][i] = tile
        copies[tbx.name] = data
        manifest.append({'id': identifier, 'origin': record['origin'], **selected,
                         'size': [width, height], 'tbx': tbx.name,
                         'tbx_sha256': hashlib.sha256(data).hexdigest()})
    if not (game / 'media/newtiledefinitions.tiles').is_file():
        raise FileNotFoundError('Expected Project Zomboid media/newtiledefinitions.tiles')
    tilesets = sorted({tile[0] for values in layers.values() for tile in values if tile})
    tmx = make_tmx(tiles, layers, [], tilesets)
    world = ET.Element('world', version='1.0', width='1', height='1')
    lots = ET.SubElement(world, 'GenerateLots')
    ET.SubElement(lots, 'exportdir', path='export')
    ET.SubElement(lots, 'ZombieSpawnMap', path='placements_ZombieSpawnMap.png')
    ET.SubElement(lots, 'TileDefFolder', path=(game / 'media').resolve().as_posix())
    ET.SubElement(lots, 'worldOrigin', origin='0,0')
    cell = ET.SubElement(world, 'cell', x='0', y='0', map='placements.tmx')
    for entry in manifest:
        ET.SubElement(cell, 'lot', x=str(entry['origin'][0]), y=str(entry['origin'][1]),
                      level='0', width=str(entry['size'][0]), height=str(entry['size'][1]), map=entry['tbx'])
    output.mkdir(parents=True)
    (output / 'export').mkdir()
    (output / 'placements.tmx').write_bytes(tmx)
    for name, data in sorted(copies.items()):
        (output / name).write_bytes(data)
    write_png(output / 'placements_ZombieSpawnMap.png', 30, 30)
    ET.ElementTree(world).write(output / 'placements.pzw', encoding='utf-8', xml_declaration=True)
    result = {'format': 'zombieprojektet-synthetic-placements-v1', 'buildings': manifest}
    (output / 'resolved-buildings.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'Authoring source: {output / "placements.pzw"}; NOT compiled or playtested.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'choices', 'output', 'tiles', 'game'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    try:
        source, choices = [json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_override_keys)
                           for path in (args.input, args.choices)]
        build(args.output, args.tiles, args.game, source, choices)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
