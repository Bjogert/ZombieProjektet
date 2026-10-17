import base64
import struct
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

from tools import build_cottage, build_m0


class TestCottageSource(unittest.TestCase):
    def test_repeatable_terrain_and_separate_building_reference(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            tiles, game = root / 'tiles', root / 'game'
            tiles.mkdir()
            (game / 'media').mkdir(parents=True)
            (game / 'media/newtiledefinitions.tiles').write_bytes(b'fixture')
            for name in ('blends_natural_01', 'blends_street_01'):
                build_m0.write_png(tiles / (name + '.png'), 1024, 4096)
            cottage = Path(__file__).resolve().parents[1] / 'assets/buildings/swedish_cottage_01.tbx'
            original = cottage.read_bytes()
            for name in ('first', 'second'):
                build_cottage.build(root / name, tiles, game, cottage)
            self.assertEqual(original, cottage.read_bytes())
            self.assertEqual((root / 'first/cottage.tmx').read_bytes(),
                             (root / 'second/cottage.tmx').read_bytes())
            world = ET.parse(root / 'first/cottage.pzw')
            lot = world.find('cell/lot')
            self.assertEqual((lot.get('x'), lot.get('y'), lot.get('level')), ('120', '120', '0'))
            self.assertEqual((root / 'first' / lot.get('map')).read_bytes(), original)
            terrain = ET.parse(root / 'first/cottage.tmx')
            self.assertEqual(len(terrain.findall('layer')), 1)
            self.assertEqual(len(terrain.findall('objectgroup/object')), 0)
            data = terrain.find('layer/data').text
            gids = struct.unpack('<90000I', zlib.decompress(base64.b64decode(data)))
            # All squares have ground; the former M0 interior is now plain grass.
            self.assertTrue(all(gids))
            self.assertEqual(gids[124 * 300 + 121], gids[0])
            self.assertNotEqual(gids[123 * 300 + 119], gids[0])
            with self.assertRaises(FileExistsError):
                build_cottage.build(root / 'first', tiles, game, cottage)

    def test_missing_cottage_never_creates_output(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            with self.assertRaises(FileNotFoundError):
                build_cottage.build(root / 'out', root, root, root / 'absent.tbx')
            self.assertFalse((root / 'out').exists())
