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
            'garden': ('ZombieProjektetGarden', 'CottageGardenTest')}


def validate_header(path):
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
