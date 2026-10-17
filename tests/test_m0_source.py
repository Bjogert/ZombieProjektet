import tempfile
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from tools import build_m0


class TestM0Source(unittest.TestCase):
    def test_room_has_daylight_and_an_accessible_light_switch(self):
        layers = build_m0.make_layers()
        # Two closed stock windows admit daylight without leaving an empty wall.
        for x, y, wall, window in ((120, 122, 8, 0), (125, 120, 9, 1)):
            self.assertEqual(layers['0_Walls'][y * 300 + x], ('walls_exterior_house_01', wall))
            self.assertEqual(layers['0_Windows'][y * 300 + x], ('fixtures_windows_01', window))
        # The west-facing stock switch controls room lighting from inside.
        self.assertEqual(layers['0_WallFurniture'][123 * 300 + 120], ('lighting_indoor_01', 1))
        self.assertEqual(layers['0_Furniture'][123 * 300 + 121], None)

    def test_spawn_is_in_the_authored_room(self):
        # Starting indoors lets the player unlock a normally randomized house door.
        path = Path(__file__).resolve().parents[1] / 'mod/ZombieProjektetM0/42/media/maps/M0Sweden/spawnpoints.lua'
        x, y, z = map(int, re.search(r'posX\s*=\s*(\d+),\s*posY\s*=\s*(\d+),\s*posZ\s*=\s*(\d+)', path.read_text()).groups())
        self.assertTrue(120 <= x < 130 and 120 <= y < 128 and z == 0)

    def test_house_has_room_floor_and_clear_entrance(self):
        layers = build_m0.make_layers()
        # West door at (120, 124); both sides must be walkable floor.
        self.assertEqual(layers['0_Walls'][124 * 300 + 120], ('walls_exterior_house_01', 10))
        self.assertEqual(layers['0_Doors'][124 * 300 + 120], ('fixtures_doors_01', 0))
        self.assertEqual(layers['0_Floor'][124 * 300 + 121], ('floors_interior_tilesandwood_01', 40))
        self.assertEqual(layers['0_Furniture'][124 * 300 + 121], None)
        self.assertEqual(layers['0_Furniture'][124 * 300 + 119], None)

    def test_repeatable_tmx_contains_room_and_external_asset_references(self):
        with tempfile.TemporaryDirectory() as d:
            tiles = Path(d) / 'tiles'
            tiles.mkdir()
            for name in build_m0.TILESETS:
                build_m0.write_png(tiles / (name + '.png'), 1024, 4096)
            first = build_m0.make_tmx(tiles)
            self.assertEqual(first, build_m0.make_tmx(tiles))
            root = ET.fromstring(first)
            self.assertEqual((root.get('width'), root.get('height')), ('300', '300'))
            room = root.find("objectgroup[@name='0_RoomDefs']/object")
            self.assertEqual(room.get('name'), 'livingroom')
            # Isometric TMX object coordinates are pixels, divided by tileheight=32.
            self.assertEqual((room.get('x'), room.get('y')), ('3840', '3840'))
            self.assertEqual((room.get('width'), room.get('height')), ('320', '256'))
            self.assertTrue(all(Path(i.get('source')).is_absolute() for i in root.findall('tileset/image')))

    def test_missing_tiles_fail_before_source_is_written(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                build_m0.make_tmx(Path(d))
