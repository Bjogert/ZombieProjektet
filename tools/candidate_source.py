"""Author one provisional local building candidate; official export is separate."""
import argparse
from collections import deque
import hashlib
import json
import math
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

from tools.build_m0 import SIZE, make_tmx, write_png
from tools.building_styles import unique_override_keys
from tools.cottage_variant import generate
from tools.garden_source import garden_layers
from tools.road_source import GRASS, GRAVEL, ASPHALT

ROOT = Path(__file__).resolve().parents[1]


def plan(source, building_id, choices):
    frame = source['frame']
    if (frame['rotation_degrees'], frame['metres_per_square'], frame['size']) != (45, 1, 256):
        raise ValueError('Expected the approved 45-degree 1:1 core')
    placements = source['placements']
    ids = [p['building_id'] for p in placements]
    if len(ids) != len(set(ids)) or building_id not in ids:
        raise ValueError('Expected one unique selected candidate')
    if not isinstance(choices, dict) or set(choices) - set(ids):
        raise ValueError('Unknown candidate choice')
    for choice in choices.values():
        if (not isinstance(choice, dict) or set(choice) != {'garden'}
                or type(choice['garden']) is not bool):
            raise ValueError('Only a boolean garden choice is supported')
    selected = next(p for p in placements if p['building_id'] == building_id)
    ox, oy, width, height = (selected[k] for k in ('x', 'y', 'width', 'height'))
    if (any(type(v) is not int for v in (ox, oy, width, height))
            or not 6 <= width <= 12 or not 9 <= height <= 18
            or selected['orientation'] != 0
            or not (6 <= ox < ox + width + 2 < 256 and 3 <= oy < oy + height + 3 < 256)):
        raise ValueError('Unsupported candidate size, placement or rotation')
    occupied = set()
    for p in placements:
        values = [p[k] for k in ('x', 'y', 'width', 'height')]
        if (any(type(v) is not int for v in values) or not 0 < p['width'] <= 32
                or not 0 < p['height'] <= 32
                or not (0 <= p['x'] < p['x'] + p['width'] <= 256
                        and 0 <= p['y'] < p['y'] + p['height'] <= 256)):
            raise ValueError('Candidate outside bounded core')
        squares = {(x, y) for y in range(p['y'], p['y'] + p['height'])
                   for x in range(p['x'], p['x'] + p['width'])}
        if occupied & squares:
            raise ValueError('Candidate footprints overlap')
        occupied |= squares
    ground, furniture = [GRASS] * SIZE**2, [None] * SIZE**2
    roads = set()
    for road in source['roads']:
        points, road_width = road['coordinates'], road['width']
        if (type(road_width) not in (int, float) or not math.isfinite(road_width)
                or not 2 <= road_width <= 16 or len(points) < 2
                or any(len(p) != 2 or any(type(v) not in (int, float)
                       or not math.isfinite(v) or not 0 <= v <= 256 for v in p) for p in points)):
            raise ValueError('Invalid bounded road geometry or width')
        tile = GRAVEL if road.get('surface') in ('gravel', 'fine_gravel', 'compacted',
                  'unpaved', 'ground', 'dirt') else ASPHALT
        for a, b in zip(points, points[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            den = dx * dx + dy * dy
            if den == 0:
                raise ValueError('Zero-length road segment')
            radius = road_width / 2
            for y in range(max(0, math.floor(min(a[1], b[1]) - radius)),
                           min(256, math.ceil(max(a[1], b[1]) + radius) + 1)):
                for x in range(max(0, math.floor(min(a[0], b[0]) - radius)),
                               min(256, math.ceil(max(a[0], b[0]) + radius) + 1)):
                    t = max(0, min(1, ((x + .5 - a[0]) * dx + (y + .5 - a[1]) * dy) / den))
                    if (x + .5 - a[0] - t * dx)**2 + (y + .5 - a[1] - t * dy)**2 <= radius**2:
                        roads.add((x, y))
                        ground[y * SIZE + x] = tile
    if not roads or occupied & roads:
        raise ValueError('Missing road or road overlaps a candidate')
    garden = choices.get(building_id, {}).get('garden', False)
    if garden:
        template = json.loads((ROOT / 'assets/gardens/cottage_garden_01.json').read_text())
        template['house_size'] = [width, height]
        template['clear_routes'] = [[-5, 3, 5, 2], [-1, 0, 1, height],
            [-1, -1, width + 2, 1], [width, 0, 1, height], [-1, height, width + 2, 1]]
        for patch in template['patches']:
            if patch['rect'][1] == 11:
                patch['rect'][1] = height + 1
                if patch['rect'][0] == 5:
                    patch['rect'][0] = width - 1
        for name, values in garden_layers(template, (ox, oy)).items():
            target = ground if name == '0_Floor' else furniture
            for i, tile in enumerate(values):
                if tile is not None:
                    point = (i % SIZE, i // SIZE)
                    if point in roads or point in occupied:
                        raise ValueError('Garden overlaps road or another candidate')
                    target[i] = tile
    blocked = occupied | {(i % SIZE, i // SIZE) for i, tile in enumerate(furniture) if tile}

    def clear(p):
        return all(0 <= x < 256 and 0 <= y < 256 and (x, y) not in blocked
                   for x, y in (p, (p[0], p[1] + 1)))

    start = (ox - 5, oy + 3)
    queue, previous, end = deque([start]), {start: None}, None
    if not clear(start):
        raise ValueError('Entrance approach obstructed')
    while queue:
        point = queue.popleft()
        if point in roads and (point[0], point[1] + 1) in roads:
            end = point
            break
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            next_point = (point[0] + dx, point[1] + dy)
            if next_point not in previous and clear(next_point):
                previous[next_point] = point
                queue.append(next_point)
    if end is None:
        raise ValueError('No clear two-square approach to road')
    access = {(x, y) for x in range(ox - 5, ox) for y in (oy + 3, oy + 4)}
    while end is not None:
        access.update((end, (end[0], end[1] + 1)))
        end = previous[end]
    if access & blocked:
        raise ValueError('Access obstructed')
    for x, y in access:
        if ground[y * SIZE + x] == GRASS:
            ground[y * SIZE + x] = GRAVEL
    return {'building': {'id': building_id, 'origin': [ox, oy], 'size': [width, height]},
            'layers': {'0_Floor': ground, '0_Furniture': furniture},
            'spawn': [ox + 1, oy + 3], 'access': [list(p) for p in sorted(access)],
            'road_squares': len(roads), 'garden': garden}


def build(register, layout, choices_path, building_id, output, tiles, game):
    if output.exists():
        raise FileExistsError('Refusing existing authoring output')
    paths = {'registry': register / 'registry.json', 'source': register / 'source.geojson',
             'provenance': register / 'source.json', 'layout': layout, 'choices': choices_path}
    raw = {key: path.read_bytes() for key, path in paths.items()}
    data = {key: json.loads(value, object_pairs_hook=unique_override_keys)
            for key, value in raw.items() if key != 'source'}
    digest = hashlib.sha256(raw['source']).hexdigest()
    if any(data[key].get(field) != digest for key, field in
           (('registry', 'source_sha256'), ('provenance', 'sha256'), ('layout', 'source_sha256'))):
        raise ValueError('Candidate source hashes differ')
    records = {b['id']: b for b in data['registry']['buildings']}
    if len(records) != len(data['registry']['buildings']) or any(
            p['building_id'] not in records for p in data['layout']['placements']):
        raise ValueError('Layout contains an unregistered identity')
    result = plan(data['layout'], building_id, data['choices'])
    width, height = result['building']['size']
    cottage = generate((ROOT / 'assets/buildings/swedish_cottage_01.tbx').read_bytes(), width, height)
    if not (game / 'media/newtiledefinitions.tiles').is_file():
        raise FileNotFoundError('Game TileDefs missing')
    names = sorted({v[0] for values in result['layers'].values() for v in values if v})
    tmx = make_tmx(tiles, result['layers'], [], names)
    world = ET.Element('world', version='1.0', width='1', height='1')
    lots = ET.SubElement(world, 'GenerateLots')
    for tag, attrs in [('exportdir', {'path': 'export'}),
        ('ZombieSpawnMap', {'path': 'candidate_ZombieSpawnMap.png'}),
        ('TileDefFolder', {'path': (game / 'media').resolve().as_posix()}),
        ('worldOrigin', {'origin': '0,0'})]:
        ET.SubElement(lots, tag, **attrs)
    cell = ET.SubElement(world, 'cell', x='0', y='0', map='candidate.tmx')
    ox, oy = result['building']['origin']
    ET.SubElement(cell, 'lot', x=str(ox), y=str(oy), level='0', width=str(width),
                  height=str(height), map='candidate.tbx')
    receipt = {k: v for k, v in result.items() if k != 'layers'}
    receipt.update(format='provisional-candidate-pilot-v1',
                   input_sha256={k: hashlib.sha256(v).hexdigest() for k, v in raw.items()},
                   assumptions=['rectangular fit', 'residential use', 'west entrance',
                                'generic interior', 'garden design', 'access path',
                                'plain ground outside known road', 'road width/surface fallback'])
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.candidate-', dir=output.parent) as temp:
        staged = Path(temp) / 'ready'
        staged.mkdir()
        (staged / 'export').mkdir()
        (staged / 'candidate.tbx').write_bytes(cottage)
        (staged / 'candidate.tmx').write_bytes(tmx)
        write_png(staged / 'candidate_ZombieSpawnMap.png', 30, 30)
        ET.ElementTree(world).write(staged / 'candidate.pzw', encoding='utf-8', xml_declaration=True)
        (staged / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
        staged.rename(output)
    return {'buildings': 1, 'road_squares': result['road_squares'],
            'access_squares': len(result['access']), 'garden': result['garden']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('register', 'layout', 'choices', 'output', 'tiles', 'game'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--building-id', required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.register, args.layout, args.choices, args.building_id,
                           args.output, args.tiles, args.game)))
