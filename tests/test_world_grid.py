import math
import unittest

from tools.world_grid import to_grid, from_grid


class WorldGridTests(unittest.TestCase):
    def test_approved_rotation_preserves_metric_distances_and_round_trips(self):
        origin = (500000, 6300000)
        east = to_grid((500010, 6300000), origin)
        north = to_grid((500000, 6300010), origin)
        self.assertAlmostEqual(east[0], math.sqrt(50))
        self.assertAlmostEqual(east[1], -math.sqrt(50))
        self.assertAlmostEqual(north[0], -math.sqrt(50))
        self.assertAlmostEqual(north[1], -math.sqrt(50))
        self.assertAlmostEqual(math.dist(east, north), math.sqrt(200))
        for point in (origin, (500010, 6300000), (499983.8, 6299975.3)):
            grid = to_grid(point, origin, offset=(20, 40))
            restored = from_grid(grid, origin, offset=(20, 40))
            self.assertAlmostEqual(restored[0], point[0])
            self.assertAlmostEqual(restored[1], point[1])

    def test_invalid_coordinates_are_rejected(self):
        for bad in ((True, 2), (float('nan'), 2), (1, float('inf')), (1,), 'bad'):
            for function in (to_grid, from_grid):
                with self.assertRaises(ValueError):
                    function(bad, (500000, 6300000))
