"""Prepare a synthetic cottage map for official WorldEd Generate Lots 8x8.

The TBX is a separate lot, interpreted by WorldEd. No custom binary exporter or
game artwork is included. Run with python -m tools.build_cottage.
"""
import argparse
import json
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from tools.build_m0 import SIZE, make_tmx, write_png
from tools.garden_source import garden_layers

ROOT = Path(__file__).resolve().parents[1]


def build(output, tiles, game, cottage, garden=None):
    source = ET.parse(cottage).getroot()
    width, height = int(source.get('width', 0)), int(source.get('height', 0))
    if source.tag != 'building' or not (6 <= width <= 12 and 9 <= height <= 18):
        raise ValueError('Expected a supported rectangular cottage TBX')
    if output.exists():
        raise FileExistsError(f'Refusing to replace existing source: {output}')
    if not (game / 'media/newtiledefinitions.tiles').is_file():
        raise FileNotFoundError('Expected Project Zomboid media/newtiledefinitions.tiles')
    ground = [('blends_natural_01', 16)] * SIZE ** 2
    for y in range(100, 151):
        for x in range(110, 115):
            ground[y * SIZE + x] = ('blends_street_01', 0)
    for y in range(122, 125):
        for x in range(115, 120):
            ground[y * SIZE + x] = ('blends_street_01', 0)
    layers = {'0_Floor': ground}
    if garden is not None:
        if (width, height) != (6, 10):
            raise ValueError('The fixed garden currently requires a 6 x 10 cottage')
        template = json.loads(garden.read_text(encoding='utf-8'))
        if template['house_size'] != [6, 10]:
            raise ValueError('Garden template must fit the 6 x 10 cottage')
        for name, values in garden_layers(template, (120, 120)).items():
            target = layers.setdefault(name, [None] * SIZE ** 2)
            for index, tile in enumerate(values):
                if tile is not None:
                    target[index] = tile
    tilesets = sorted({tile[0] for values in layers.values() for tile in values if tile})
    tmx = make_tmx(tiles, layers, [], tilesets)
    output.mkdir(parents=True)
    (output / 'cottage.tmx').write_bytes(tmx)
    shutil.copyfile(cottage, output / 'swedish_cottage_01.tbx')
    write_png(output / 'cottage_ZombieSpawnMap.png', 30, 30)
    (output / 'export').mkdir()
    world = ET.Element('world', version='1.0', width='1', height='1')
    lots = ET.SubElement(world, 'GenerateLots')
    ET.SubElement(lots, 'exportdir', path='export')
    ET.SubElement(lots, 'ZombieSpawnMap', path='cottage_ZombieSpawnMap.png')
    ET.SubElement(lots, 'TileDefFolder', path=(game / 'media').resolve().as_posix())
    ET.SubElement(lots, 'worldOrigin', origin='0,0')
    cell = ET.SubElement(world, 'cell', x='0', y='0', map='cottage.tmx')
    # Official WorldEd worldwriter.cpp lot attributes; TBX maps resolve natively.
    ET.SubElement(cell, 'lot', x='120', y='120', level='0', width=str(width), height=str(height),
                  map='swedish_cottage_01.tbx')
    ET.ElementTree(world).write(output / 'cottage.pzw', encoding='utf-8', xml_declaration=True)
    print(f'Authoring source: {output / "cottage.pzw"}; NOT compiled or playtested.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tiles', type=Path, required=True)
    parser.add_argument('--game', type=Path, required=True)
    parser.add_argument('--cottage', type=Path, default=ROOT / 'assets/buildings/swedish_cottage_01.tbx')
    parser.add_argument('--garden', type=Path, help='Optional relative-coordinate garden JSON')
    args = parser.parse_args()
    build(args.output, args.tiles, args.game, args.cottage, args.garden)
