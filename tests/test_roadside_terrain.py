import copy
import unittest

from tests.test_integration_source import route_fixture
from tools import integration_source, road_source


class RoadsideTerrainTests(unittest.TestCase):
    def test_seeded_patch_preserves_road_garden_and_clear_access(self):
        data = route_fixture()
        choices = {'roadside-cottage': {'garden': 'cottage_garden_01'}}
        inputs = copy.deepcopy((data, choices))
        plain = integration_source.plan(data, choices)
        patch = integration_source.plan(data, choices, terrain_seed=42)
        self.assertEqual((data, choices), inputs)
        self.assertEqual(patch, integration_source.plan(data, choices, terrain_seed=42))
        other = integration_source.plan(data, choices, terrain_seed=43)
        self.assertNotEqual(patch['layers'], other['layers'])
        self.assertEqual(patch['building'], plain['building'])
        self.assertEqual(patch['copies'], plain['copies'])
        self.assertEqual(patch['driveway'], plain['driveway'])
        protected = set(plain['driveway'])
        protected |= {(i % 300, i // 300) for i in road_source.terrain_cells(road_source.plan(data))[(0, 0)]}
        # Known fixture house/garden/access envelope; include all decoration.
        protected |= {(x, y) for x in range(170, 182) for y in range(173, 187)}
        for x, y in protected:
            i = y * 300 + x
            for name, values in plain['layers'].items():
                self.assertEqual(patch['layers'][name][i], values[i])
            self.assertIsNone(patch['layers']['0_FloorOverlay'][i])
        changed = []
        plants = 0
        empty = [None] * 300**2
        for i in range(300**2):
            x, y = i % 300, i // 300
            if any(values[i] != plain['layers'].get(name, empty)[i]
                   for name, values in patch['layers'].items()):
                changed.append((x, y))
            if patch['layers']['0_Furniture'][i] != plain['layers']['0_Furniture'][i]:
                plants += 1
                self.assertTrue(all((x + dx, y + dy) not in protected
                                    for dx in (-1, 0, 1) for dy in (-1, 0, 1)))
        self.assertGreater(plants, 5)
        self.assertGreater(patch['terrain']['shoulder_squares'], 10)
        self.assertTrue(changed)
        self.assertTrue(all(138 <= x < 193 and 138 <= y < 197 for x, y in changed))

    def test_invalid_seed_rejected_and_optional_mode_is_explicit(self):
        plain = integration_source.plan(route_fixture(), {})
        self.assertNotIn('terrain', plain)
        self.assertNotIn('0_FloorOverlay', plain['layers'])
        for seed in (True, -1, 2**32, '42', 3.5):
            with self.assertRaises(ValueError):
                integration_source.plan(route_fixture(), {}, terrain_seed=seed)


if __name__ == '__main__':
    unittest.main()
