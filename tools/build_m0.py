"""Create original M0 authoring files; WorldEd performs the binary game export.

No game artwork is copied. Uses only Python's standard library.
The official editor authors 300-square cells and exports B42 via Generate Lots 8x8.
"""
import argparse
import base64
import struct
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

SIZE = 300
TILESETS = (
    'blends_natural_01', 'blends_street_01', 'floors_interior_tilesandwood_01',
    'walls_exterior_house_01', 'fixtures_doors_01',
    'furniture_tables_low_01', 'furniture_seating_indoor_01',
    'fixtures_windows_01', 'lighting_indoor_01',
)


def make_layers():
    layers = {name: [None] * SIZE ** 2 for name in (
        '0_Floor', '0_Walls', '0_Doors', '0_Windows',
        '0_Furniture', '0_WallFurniture', '1_Floor')}
    ground = layers['0_Floor']
    for y in range(SIZE):
        for x in range(SIZE):
            ground[y * SIZE + x] = ('blends_natural_01', 16)
    for y in range(100, 151):
        for x in range(110, 115):
            ground[y * SIZE + x] = ('blends_street_01', 0)
    for y in range(123, 126):
        for x in range(115, 120):
            ground[y * SIZE + x] = ('blends_street_01', 0)
    for y in range(120, 128):
        for x in range(120, 130):
            ground[y * SIZE + x] = ('floors_interior_tilesandwood_01', 40)
            # Isometric TMX levels shift three squares per level in WorldEd.
            layers['1_Floor'][(y - 3) * SIZE + x - 3] = ('floors_interior_tilesandwood_01', 40)
    walls = layers['0_Walls']
    for y in range(120, 128):
        walls[y * SIZE + 120] = ('walls_exterior_house_01', 0)
        walls[y * SIZE + 130] = ('walls_exterior_house_01', 0)
    for x in range(120, 130):
        walls[120 * SIZE + x] = ('walls_exterior_house_01', 1)
        walls[128 * SIZE + x] = ('walls_exterior_house_01', 1)
    walls[120 * SIZE + 120] = ('walls_exterior_house_01', 2)
    walls[128 * SIZE + 130] = ('walls_exterior_house_01', 3)
    walls[124 * SIZE + 120] = ('walls_exterior_house_01', 10)
    layers['0_Doors'][124 * SIZE + 120] = ('fixtures_doors_01', 0)
    walls[122 * SIZE + 120] = ('walls_exterior_house_01', 8)
    walls[120 * SIZE + 125] = ('walls_exterior_house_01', 9)
    layers['0_Windows'][122 * SIZE + 120] = ('fixtures_windows_01', 0)
    layers['0_Windows'][120 * SIZE + 125] = ('fixtures_windows_01', 1)
    layers['0_WallFurniture'][123 * SIZE + 120] = ('lighting_indoor_01', 1)
    layers['0_Furniture'][123 * SIZE + 126] = ('furniture_tables_low_01', 0)
    layers['0_Furniture'][125 * SIZE + 126] = ('furniture_seating_indoor_01', 56)
    return layers


def write_png(path, width, height):
    """Write a black RGB PNG, used only for the zero-zombie density image."""
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    image = b'\x89PNG\r\n\x1a\n'
    image += chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    image += chunk(b'IDAT', zlib.compress((b'\0' + b'\0' * width * 3) * height))
    image += chunk(b'IEND', b'')
    path.write_bytes(image)


def make_tmx(tiles):
    root = ET.Element('map', version='1.0', orientation='isometric',
                      width=str(SIZE), height=str(SIZE), tilewidth='64', tileheight='32')
    gids = {}
    first = 1
    for name in TILESETS:
        path = (tiles / (name + '.png')).resolve()
        header = path.read_bytes()[:24]
        if header[:8] != b'\x89PNG\r\n\x1a\n':
            raise ValueError(f'Invalid PNG: {path}')
        width, height = struct.unpack('>II', header[16:24])
        count = (width // 128) * (height // 256)
        ts = ET.SubElement(root, 'tileset', firstgid=str(first), name=name,
                           tilewidth='128', tileheight='256')
        ET.SubElement(ts, 'image', source=path.as_posix(), width=str(width), height=str(height))
        gids[name] = (first, count)
        first += count
    for name, values in make_layers().items():
        data = []
        for tile in values:
            gid = 0
            if tile:
                start, count = gids[tile[0]]
                if not 0 <= tile[1] < count:
                    raise ValueError(f'Tile outside tilesheet: {tile}')
                gid = start + tile[1]
            data.append(gid)
        layer = ET.SubElement(root, 'layer', name=name, width=str(SIZE), height=str(SIZE))
        encoded = ET.SubElement(layer, 'data', encoding='base64', compression='zlib')
        encoded.text = base64.b64encode(zlib.compress(struct.pack(f'<{len(data)}I', *data))).decode()
    rooms = ET.SubElement(root, 'objectgroup', name='0_RoomDefs', width=str(SIZE), height=str(SIZE))
    ET.SubElement(rooms, 'object', name='livingroom', type='RoomDef',
                  x=str(120 * 32), y=str(120 * 32), width=str(10 * 32), height=str(8 * 32))
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def build(output, tiles, game):
    # Resolve and validate all required resources before writing anything.
    tmx = make_tmx(tiles)
    if not (game / 'media' / 'newtiledefinitions.tiles').is_file():
        raise FileNotFoundError('Expected Project Zomboid media/newtiledefinitions.tiles')
    if output.exists():
        raise FileExistsError(f'Refusing to replace existing source: {output}')
    output.mkdir(parents=True)
    (output / 'm0.tmx').write_bytes(tmx)
    write_png(output / 'm0_ZombieSpawnMap.png', 30, 30)
    export = output / 'export'
    export.mkdir()
    world = ET.Element('world', version='1.0', width='1', height='1')
    lots = ET.SubElement(world, 'GenerateLots')
    ET.SubElement(lots, 'exportdir', path='export')
    ET.SubElement(lots, 'ZombieSpawnMap', path='m0_ZombieSpawnMap.png')
    ET.SubElement(lots, 'TileDefFolder', path=(game / 'media').resolve().as_posix())
    ET.SubElement(lots, 'worldOrigin', origin='0,0')
    ET.SubElement(world, 'cell', x='0', y='0', map='m0.tmx')
    ET.ElementTree(world).write(output / 'm0.pzw', encoding='utf-8', xml_declaration=True)
    print(f'Authoring source: {output / "m0.pzw"}; NOT a compiled or playtested mod.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tiles', type=Path, required=True, help='Tiles/2x directory')
    parser.add_argument('--game', type=Path, required=True, help='Read-only game installation')
    args = parser.parse_args()
    build(args.output, args.tiles, args.game)
