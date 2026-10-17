import copy
import json
import unittest
from pathlib import Path

from tools.garden_source import garden_layers


TEMPLATE = Path(__file__).resolve().parents[1] / 'assets/gardens/cottage_garden_01.json'


class TestGardenSource(unittest.TestCase):
    def test_quarter_turns_move_deck_and_directional_chairs_together(self):
        template = json.loads(TEMPLATE.read_text())
        # Original chair (-4,5), around a 6x10 footprint, anchored at (20,20).
        expected = [(16, 25, 16), (24, 16, 17), (29, 24, 19), (25, 29, 18)]
        before = copy.deepcopy(template)
        for rotation, (x, y, sprite) in zip((0, 90, 180, 270), expected):
            with self.subTest(rotation=rotation):
                layers = garden_layers(template, (20, 20), size=64, rotation=rotation)
                self.assertEqual(layers['0_Furniture'][y * 64 + x],
                                 ('furniture_seating_outdoor_01', sprite))
                self.assertEqual(sum(t == ('carpentry_02', 56)
                                     for t in layers['0_Floor']), 24)
        self.assertEqual(template, before)
        for rotation in (45, -90, 360, True):
            with self.assertRaises(ValueError):
                garden_layers(template, (20, 20), size=64, rotation=rotation)

    def test_template_translates_repeatably_and_keeps_access_clear(self):
        original = TEMPLATE.read_bytes()
        template = json.loads(original)
        before = copy.deepcopy(template)
        first = garden_layers(template, (120, 120))
        second = garden_layers(template, (180, 170))
        self.assertEqual(first, garden_layers(template, (120, 120)))
        self.assertEqual(template, before)
        self.assertEqual(TEMPLATE.read_bytes(), original)
        for layer in first:
            occupied = {(i % 300 - 120, i // 300 - 120): tile
                        for i, tile in enumerate(first[layer]) if tile}
            translated = {(i % 300 - 180, i // 300 - 170): tile
                          for i, tile in enumerate(second[layer]) if tile}
            self.assertEqual(occupied, translated)
        self.assertEqual(first['0_Floor'][123 * 300 + 119], ('carpentry_02', 56))
        self.assertEqual(first['0_Furniture'][118 * 300 + 117], ('vegetation_ornamental_01', 16))
        self.assertEqual(sum(t == ('carpentry_02', 56) for t in first['0_Floor']), 24)
        for y in (123, 124):
            for x in range(115, 120):
                self.assertIsNone(first['0_Furniture'][y * 300 + x])
        for x, y in ((119, 119), (126, 119), (119, 130), (126, 130)):
            self.assertIsNone(first['0_Furniture'][y * 300 + x])
        for y in range(120, 130):
            for x in range(120, 126):
                self.assertTrue(all(layer[y * 300 + x] is None for layer in first.values()))

    def test_rejects_house_route_bounds_and_duplicate_placements(self):
        template = json.loads(TEMPLATE.read_text())
        for rect in ([0, 0, 1, 1], [-1, 3, 1, 1], [-1, -1, 1, 1],
                     [-121, 0, 1, 1], [-4, -2, 1, 1]):
            with self.subTest(rect=rect):
                bad = copy.deepcopy(template)
                bad['patches'].append({'layer': '0_Furniture', 'rect': rect,
                                       'tile': ['vegetation_ornamental_01', 16]})
                with self.assertRaises(ValueError):
                    garden_layers(bad, (120, 120))

    def test_rejects_invalid_dimensions_layers_and_tile_references(self):
        template = json.loads(TEMPLATE.read_text())
        for change in ({'rect': [-4, 1, 0, 6]}, {'rect': [-4, 1, True, 6]},
                       {'layer': '1_Floor'}, {'tile': ['../invalid', 0]},
                       {'tile': ['carpentry_02', -1]}):
            with self.subTest(change=change):
                bad = copy.deepcopy(template)
                bad['patches'][0].update(change)
                with self.assertRaises(ValueError):
                    garden_layers(bad, (120, 120))
