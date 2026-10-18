"""Stage the single-cottage WorldEd 2026-09-16 metadata workaround.

Requires an official zero-cell export of identical TBX bytes. Only the observed
three-singleton-buildings/zero-objects regression is supported. Physical tiles,
room IDs and both input exports are preserved. Fresh game verification is required.
"""
import argparse
import copy
import hashlib
import json
import math
import shutil
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

from tools.package_m0 import _header_stream, validate_cottage_metadata


def read(path):
    stream = _header_stream(path)

    def integer():
        data = stream.read(4)
        if len(data) != 4:
            raise ValueError('Truncated cottage header')
        return struct.unpack('<i', data)[0]

    def count(limit):
        n = integer()
        if not 0 <= n <= limit:
            raise ValueError('Unsupported cottage metadata count')
        return n

    if (integer(), integer()) != (0, 1):
        raise ValueError('Only the ground-floor cottage with roof level 1 is supported')
    prefix = stream.getvalue()[:stream.tell()]
    rooms = []
    for _ in range(count(3)):
        name = stream.readline(257)
        if not name.endswith(b'\n') or len(name) > 256:
            raise ValueError('Invalid room name')
        floor = integer()
        rects = [tuple(integer() for _ in range(4)) for _ in range(count(1))]
        objects = [tuple(integer() for _ in range(3)) for _ in range(count(128))]
        if floor != 0 or len(rects) != 1:
            raise ValueError('Unsupported cottage room geometry')
        x, y, w, h = rects[0]
        if not (0 <= x < x + w <= 256 and 0 <= y < y + h <= 256):
            raise ValueError('Room outside runtime cell')
        if any(kind < 0 or not (x <= ox < x + w and y <= oy < y + h)
               for kind, ox, oy in objects):
            raise ValueError('Room object outside room')
        rooms.append({'name': name, 'floor': floor, 'rects': rects, 'objects': objects})
    buildings = [[integer() for _ in range(count(3))] for _ in range(count(3))]
    suffix = stream.read()
    if len(suffix) != 1024:
        raise ValueError('Unsupported zombie-map suffix')
    return {'prefix': prefix, 'rooms': rooms, 'buildings': buildings, 'suffix': suffix}


def encode(data):
    def ints(*items):
        return struct.pack('<' + 'i' * len(items), *items)
    result = data['prefix'] + ints(len(data['rooms']))
    for room in data['rooms']:
        result += room['name'] + ints(room['floor'], len(room['rects']))
        result += b''.join(ints(*r) for r in room['rects'])
        result += ints(len(room['objects'])) + b''.join(ints(*o) for o in room['objects'])
    result += ints(len(data['buildings']))
    result += b''.join(ints(len(ids), *ids) for ids in data['buildings'])
    return result + data['suffix']


def single_lot(world):
    tree = ET.parse(world)
    origin = tree.find('GenerateLots/worldOrigin')
    lots = [(cell, lot) for cell in tree.findall('cell') for lot in cell.findall('lot')]
    if origin is None or origin.get('origin') != '0,0' or len(lots) != 1:
        raise ValueError('Expected one cottage lot and zero world origin')
    cell, lot = lots[0]
    if tuple(lot.get(k) for k in ('width', 'height', 'level')) != ('6', '10', '0'):
        raise ValueError('Expected ground-floor 6x10 cottage')
    filename = lot.get('map', '')
    if not filename or Path(filename).name != filename or ':' in filename:
        raise ValueError('TBX must be beside the authoring world')
    cx, cy = int(cell.get('x')), int(cell.get('y'))
    x, y = int(lot.get('x')), int(lot.get('y'))
    if min(cx, cy, x, y) < 0 or x + 6 > 300 or y + 10 > 300:
        raise ValueError('Unsupported authoring position')
    gx, gy = cx * 300 + x, cy * 300 + y
    if gx % 256 + 6 > 256 or gy % 256 + 10 > 256:
        raise ValueError('Cottage crosses a runtime boundary')
    return (cx, cy), (x, y), (gx % 256, gy % 256), f'{gx//256}_{gy//256}.lotheader', filename


def stage(reference_world, source, output):
    if output.exists():
        raise FileExistsError(output)
    manifest_bytes = (source / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    integration = manifest.get('integration', {})
    if integration.get('format') != 'synthetic-roadside-v1':
        raise ValueError('Expected synthetic roadside manifest')
    ref_cell, _, ref_origin, ref_name, ref_tbx = single_lot(reference_world)
    cell, origin, dst_origin, name, tbx = single_lot(source / 'roads.pzw')
    b = integration['building']
    if (list(cell), list(origin), tbx, 0, [6, 10]) != (
            integration['cell'], b['origin'], b['tbx'], b['rotation'], b['size']):
        raise ValueError('Manifest and cottage lot disagree')
    if ref_cell != (0, 0) or ref_name != '0_0.lotheader':
        raise ValueError('Reference must be wholly inside runtime cell zero')
    tbx_bytes = (source / tbx).read_bytes()
    if not tbx_bytes or tbx_bytes != (reference_world.parent / ref_tbx).read_bytes():
        raise ValueError('Reference and target TBX differ')
    reference_header = reference_world.parent / 'export' / ref_name
    validate_cottage_metadata(reference_header)
    ref, dst = read(reference_header), read(source / 'export' / name)
    if sorted(dst['buildings']) != [[0], [1], [2]] or len(dst['rooms']) != 3 or any(
            room['objects'] for room in dst['rooms']):
        raise ValueError('Target is not the supported split-building/zero-object failure')

    def keys(header, position):
        x, y = position
        result = [(r['name'], r['floor'], tuple((a-x, b-y, w, h) for a, b, w, h in r['rects']))
                  for r in header['rooms']]
        if len(set(result)) != 3:
            raise ValueError('Cottage rooms must match uniquely')
        return result

    ref_keys, dst_keys = keys(ref, ref_origin), keys(dst, dst_origin)
    if set(ref_keys) != set(dst_keys):
        raise ValueError('Reference and target room geometry differ')
    mapping = [dst_keys.index(k) for k in ref_keys]
    corrected = copy.deepcopy(dst)
    dx, dy = dst_origin[0] - ref_origin[0], dst_origin[1] - ref_origin[1]
    for i, j in enumerate(mapping):
        corrected['rooms'][j]['objects'] = [(kind, x+dx, y+dy) for kind, x, y in ref['rooms'][i]['objects']]
    corrected['buildings'] = [[mapping[i] for i in ids] for ids in ref['buildings']]
    result = encode(corrected)
    files = []
    for y in range(math.ceil(manifest['height'] * 300 / 256)):
        for x in range(math.ceil(manifest['width'] * 300 / 256)):
            for filename in (f'{x}_{y}.lotheader', f'world_{x}_{y}.lotpack', f'chunkdata_{x}_{y}.bin'):
                path = source / 'export' / filename
                if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
                    raise ValueError('Incomplete official export')
                files.append(path)
    if name not in {f.name for f in files}:
        raise ValueError('Cottage outside manifest bounds')
    sha = lambda data: hashlib.sha256(data).hexdigest()
    provenance = {'format': 'single-cottage-metadata-v1', 'official_tool': 'WorldEd 2026-09-16',
                  'tbx_sha256': sha(tbx_bytes), 'reference_header_sha256': sha(reference_header.read_bytes()),
                  'manifest_sha256': sha(manifest_bytes), 'changed_header': name,
                  'before_sha256': sha((source / 'export' / name).read_bytes()),
                  'after_sha256': sha(result), 'room_id_mapping': mapping,
                  'input_exports_sha256': {f.name: sha(f.read_bytes()) for f in files}}
    (output / 'export').mkdir(parents=True)
    for path in files:
        shutil.copy2(path, output / 'export' / path.name)
    (output / 'export' / name).write_bytes(result)
    validate_cottage_metadata(output / 'export' / name)
    (output / 'manifest.json').write_bytes(manifest_bytes)
    (output / 'metadata-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
    print('Staged one cottage metadata correction; physical exports preserved. Game verification required.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-world', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        stage(args.reference_world, args.source, args.output)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
