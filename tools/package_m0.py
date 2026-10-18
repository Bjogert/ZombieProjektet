"""Package the official WorldEd 8x8 export, never game artwork or TileDefs.

Header checks identify this export format; they do not prove game compatibility.
Use a fresh output directory. This command never installs or enables a mod.
"""
import argparse
import io
import shutil
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {'m0': ('ZombieProjektetM0', 'M0Sweden'),
            'cottage': ('ZombieProjektetCottage', 'CottageTest'),
            'garden': ('ZombieProjektetGarden', 'CottageGardenTest'),
            'placements': ('ZombieProjektetPlacements', 'PlacementTest')}


def validate_header(path):
    _header_stream(path)


def _header_stream(path):
    stream = io.BytesIO(path.read_bytes())
    if stream.read(8) != b'LOTH\x01\0\0\0':
        raise ValueError(f'Expected Build 42 LOTH version 1: {path}')
    def integer():
        data = stream.read(4)
        if len(data) != 4:
            raise ValueError(f'Truncated header: {path}')
        return struct.unpack('<i', data)[0]
    count = integer()
    if not 0 < count < 4096:
        raise ValueError(f'Invalid tile count: {path}')
    for _ in range(count):
        name = stream.readline()
        if not name.endswith(b'\n') or len(name) > 256:
            raise ValueError(f'Invalid tile name: {path}')
    if (integer(), integer()) != (8, 8):
        raise ValueError(f'Expected Build 42 8x8 chunks: {path}')
    return stream


def validate_cottage_metadata(path, *, expected_area=60):
    """Reject the observed nonzero-cell WorldEd metadata regression.

    This gate is deliberately limited to our single three-room cottage fixture.
    It reads official output; it never repairs or replaces the exporter.
    """
    if type(expected_area) is not int or not 54 <= expected_area <= 216:
        raise ValueError('Expected a supported cottage area from 54 to 216 squares')
    stream = _header_stream(path)

    def integer():
        data = stream.read(4)
        if len(data) != 4:
            raise ValueError(f'Truncated cottage metadata: {path}')
        return struct.unpack('<i', data)[0]

    def count(limit):
        value = integer()
        if not 0 <= value <= limit:
            raise ValueError(f'Invalid cottage metadata count: {path}')
        return value

    integer(), integer()  # Minimum and maximum map level.
    rooms = count(32)
    objects = 0
    area = 0
    for _ in range(rooms):
        name = stream.readline(257)
        if not name.endswith(b'\n') or len(name) > 256:
            raise ValueError(f'Invalid cottage room name: {path}')
        if integer() != 0:
            raise ValueError('Cottage rooms must be on the ground floor')
        for _ in range(count(32)):
            x, y, width, height = (integer() for _ in range(4))
            if not (0 <= x < x + width <= 256 and 0 <= y < y + height <= 256):
                raise ValueError('Cottage room lies outside its runtime cell')
            area += width * height
        n = count(128)
        objects += n
        for _ in range(n):
            integer(), integer(), integer()  # Tile meta enum and local x/y.
    buildings = count(32)
    memberships = [[integer() for _ in range(count(32))] for _ in range(buildings)]
    if (rooms, area, buildings, objects) != (3, expected_area, 1, 8) or sorted(memberships[0]) != [0, 1, 2]:
        raise ValueError(f'Invalid cottage export metadata: rooms={rooms}, area={area}, '
                         f'buildings={buildings}, objects={objects}; expected 3, {expected_area}, 1, 8. '
                         'Keep this export diagnostic-only; repair and recheck official export.')


def package(export, output, profile='m0'):
    mod_name, map_name = PROFILES[profile]
    files = []
    # One 300-square authoring cell overlaps four 256-square runtime cells.
    for x in range(2):
        for y in range(2):
            for name in (f'{x}_{y}.lotheader', f'world_{x}_{y}.lotpack', f'chunkdata_{x}_{y}.bin'):
                path = export / name
                if not path.is_file() or path.stat().st_size == 0:
                    raise FileNotFoundError(f'Missing/nonempty WorldEd export required: {path}')
                files.append(path)
            validate_header(export / f'{x}_{y}.lotheader')
    if output.exists():
        raise FileExistsError(f'Refusing to replace existing package: {output}')
    mod = output / mod_name
    shutil.copytree(ROOT / 'mod' / mod_name, mod)
    maps = mod / '42' / 'media' / 'maps' / map_name
    for path in files:
        shutil.copy2(path, maps / path.name)
    archive_path = output / (mod_name + '.zip')
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(mod.rglob('*')):
            if path.is_file():
                info = zipfile.ZipInfo(path.relative_to(output).as_posix())
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes())
    print(f'Package: {archive_path}; NOT VERIFIED IN GAME.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--profile', choices=PROFILES, default='m0')
    args = parser.parse_args()
    package(args.export, args.output, args.profile)
