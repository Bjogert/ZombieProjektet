"""Join a fictional cottage/garden to the local road prototype; official export required."""
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from tools import placement_source, road_source
from tools.build_m0 import SIZE
from tools.building_styles import unique_override_keys


def plan(data, choices):
    road = road_source.plan(data)
    sx, sy = road['start']
    cx, cy = sx // SIZE, sy // SIZE
    lx, ly = sx % SIZE, sy % SIZE
    source = {'defaults': {'house': 'swedish_cottage_01', 'rotation': 0, 'garden': None},
              'buildings': [{'id': 'roadside-cottage', 'origin': [lx + 25, ly + 25]}]}
    layers, buildings, copies, envelopes = placement_source.resolve(source, choices)
    building = buildings[0]
    if building['rotation'] != 0:
        raise ValueError('Roadside fixture supports only rotation 0')
    terrain = road_source.terrain_cells(road).get((cx, cy), {})
    _, x0, y0, x1, y1 = envelopes[0]
    if any(y * SIZE + x in terrain for y in range(y0, y1) for x in range(x0, x1)):
        raise ValueError('House/garden/access overlaps road or staging pad')
    ox, oy = building['origin']
    driveway = {(x, y) for x in range(lx + 7, lx + 10) for y in range(ly + 8, oy + 5)}
    driveway |= {(x, y) for x in range(lx + 7, ox) for y in range(oy + 3, oy + 5)}
    # Three-square vehicle approach, narrowing to the existing two-square garden entrance.
    driveway |= {(x, oy + 2) for x in range(lx + 7, ox - 5)}
    ground = layers['0_Floor']
    for x, y in driveway:
        index = y * SIZE + x
        if layers['0_Furniture'][index] is not None:
            raise ValueError('Driveway obstructed by garden furniture')
        if ground[index] == road_source.GRASS:
            ground[index] = road_source.GRAVEL
    for index, tile in terrain.items():
        ground[index] = tile
    return {'cell': (cx, cy), 'layers': layers, 'building': building, 'copies': copies,
            'spawn': [cx * SIZE + ox + 1, cy * SIZE + oy + 4],
            'driveway': sorted(driveway)}


def build(source, choices_path, output, tiles, game):
    data = json.loads(source.read_text(encoding='utf-8'))
    choices = json.loads(choices_path.read_text(encoding='utf-8'), object_pairs_hook=unique_override_keys)
    p = plan(data, choices)
    road_source.build(source, output, tiles, game, {p['cell']: p['layers']})
    world = ET.parse(output / 'roads.pzw')
    cx, cy = p['cell']
    cell = world.find(f"cell[@x='{cx}'][@y='{cy}']")
    b = p['building']
    ET.SubElement(cell, 'lot', x=str(b['origin'][0]), y=str(b['origin'][1]), level='0',
                  width=str(b['size'][0]), height=str(b['size'][1]), map=b['tbx'])
    for name, content in p['copies'].items():
        (output / name).write_bytes(content)
    world.write(output / 'roads.pzw', encoding='utf-8', xml_declaration=True)
    manifest_path = output / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    manifest['integration'] = {'format': 'synthetic-roadside-v1', 'cell': p['cell'],
                               'building': b, 'spawn': p['spawn'],
                               'choices_sha256': hashlib.sha256(choices_path.read_bytes()).hexdigest()}
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print('Synthetic roadside authoring ready; official export and game checks remain required.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source', 'choices', 'output', 'tiles', 'game'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    try:
        build(args.source, args.choices, args.output, args.tiles, args.game)
    except (OSError, ValueError) as error:
        parser.error(str(error))
