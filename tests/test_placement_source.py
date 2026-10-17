import base64
import copy
import json
import struct
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

from tools.build_m0 import write_png
from tools.placement_source import build


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = {'house': 'swedish_cottage_01', 'rotation': 0, 'garden': 'cottage_garden_01'}


class TestPlacementSource(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tiles, self.game = self.root / 'tiles', self.root / 'game'
        self.tiles.mkdir()
        (self.game / 'media').mkdir(parents=True)
        (self.game / 'media/newtiledefinitions.tiles').write_bytes(b'fixture')
        for name in ('blends_natural_01', 'carpentry_02', 'floors_exterior_tilesandstone_01',
                     'vegetation_ornamental_01', 'furniture_seating_outdoor_01', 'furniture_tables_low_01'):
            write_png(self.tiles / (name + '.png'), 1024, 4096)
        self.source = {'defaults': DEFAULT.copy(), 'buildings': [
            {'id': 'demo-a', 'origin': [120, 120]}, {'id': 'demo-b', 'origin': [145, 120]}]}

    def generate(self, name, source=None, choices=None):
        output = self.root / name
        build(output, self.tiles, self.game, self.source if source is None else source,
              {} if choices is None else choices)
        return output

    def test_separate_choices_survive_reordering_and_regeneration(self):
        choices = {'demo-a': {'rotation': 90}, 'demo-b': {'garden': None}}
        before = copy.deepcopy((self.source, choices))
        first = self.generate('first', choices=choices)
        reordered = copy.deepcopy(self.source)
        reordered['buildings'].reverse()
        again = self.generate('again', reordered, choices)
        self.assertEqual((self.source, choices), before)
        self.assertEqual({p.name: p.read_bytes() for p in first.iterdir() if p.is_file()},
                         {p.name: p.read_bytes() for p in again.iterdir() if p.is_file()})
        lots = ET.parse(first / 'placements.pzw').findall('cell/lot')
        self.assertEqual([(p.get('x'), p.get('width'), p.get('height'), p.get('map')) for p in lots],
                         [('120', '10', '6', 'cottage_90.tbx'), ('145', '6', '10', 'cottage_0.tbx')])
        terrain = ET.parse(first / 'placements.tmx')
        layer = terrain.find("layer[@name='0_Furniture']/data")
        gids = struct.unpack('<90000I', zlib.decompress(base64.b64decode(layer.text)))
        chair_start = int(terrain.find("tileset[@name='furniture_seating_outdoor_01']").get('firstgid'))
        self.assertEqual(gids[116 * 300 + 124], chair_start + 17)
        self.assertEqual(gids[125 * 300 + 141], 0)  # demo-b has no garden
        reordered['buildings'].append({'id': 'demo-c', 'origin': [175, 120]})
        extended = self.generate('extended', reordered, choices)
        old = json.loads((first / 'resolved-buildings.json').read_text())['buildings']
        new = json.loads((extended / 'resolved-buildings.json').read_text())['buildings']
        self.assertEqual(old, new[:2])
        with self.assertRaises(FileExistsError):
            self.generate('first')

    def test_invalid_choices_and_overlaps_fail_before_output(self):
        for choices in ({'missing': {'rotation': 90}}, {'demo-a': {'rotation': 45}},
                        {'demo-a': {'rotation': True}}, {'demo-a': {'garden': 'absent'}},
                        {'demo-a': {'house': '../other'}}, {'demo-a': {'typo': 1}}):
            with self.subTest(choices=choices), self.assertRaises(ValueError):
                self.generate('bad', choices=choices)
            self.assertFalse((self.root / 'bad').exists())
        for record in ({'id': 'demo-a', 'origin': [180, 120]},
                       {'id': 'demo-c', 'origin': [120, 120]},
                       {'id': 'demo-c', 'origin': [124, 115]},
                       {'id': 'demo-c', 'origin': [0, 0]},
                       {'id': 'demo-c', 'origin': [120.5, 170]}):
            source = copy.deepcopy(self.source)
            source['buildings'].append(record)
            with self.subTest(record=record), self.assertRaises(ValueError):
                self.generate('bad', source)
            self.assertFalse((self.root / 'bad').exists())

    def test_all_variant_sources_keep_ceiling_furniture_and_room_counts(self):
        for angle, expected_size in ((0, (6, 10)), (90, (10, 6)), (180, (6, 10)), (270, (10, 6))):
            with self.subTest(angle=angle):
                root = ET.parse(ROOT / f'assets/buildings/cottage_rotations/cottage_{angle}.tbx').getroot()
                self.assertEqual((int(root.get('width')), int(root.get('height'))), expected_size)
                floors = root.findall('floor')
                rooms = [int(i) for i in floors[0].find('rooms').text.replace('\n', '').split(',') if i.strip()]
                self.assertEqual([rooms.count(i) for i in (1, 2, 3)], [36, 16, 8])
                ceiling = floors[1].find("tiles[@layer='Floor']")
                self.assertIsNotNone(ceiling)
                self.assertEqual(sum(int(i) > 0 for i in ceiling.text.replace('\n', '').split(',') if i.strip()), 60)
                for furniture in root.findall('furniture'):
                    self.assertEqual({e.get('orient') for e in furniture.findall('entry')}, set('WNES'))
                    self.assertTrue(all(e.findall('tile') for e in furniture.findall('entry')))
