import copy
import json
import tempfile
import struct
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from tools import integration_source, road_source
from tools.build_m0 import write_png
from tools.package_m0 import validate_cottage_metadata


def cottage_header(buildings=((0, 1, 2),), include_objects=True):
    def ints(*values):
        return struct.pack('<' + 'i' * len(values), *values)
    data = b'LOTH' + ints(1, 1) + b'blends_natural_01_16\n' + ints(8, 8, 0, 1, 3)
    for name, rect, objects in (
        ('livingroom', (175, 175, 6, 6), 6),
        ('bedroom', (175, 181, 4, 4), 1),
        ('bathroom', (179, 181, 2, 4), 1),
    ):
        objects = objects if include_objects else 0
        data += name.encode() + b'\n' + ints(0, 1, *rect, objects)
        data += ints(0, rect[0], rect[1]) * objects
    return data + ints(len(buildings)) + b''.join(ints(len(ids), *ids) for ids in buildings)


def route_fixture():
    return {'crs': 'EPSG:3006', 'metres_per_square': 1,
            'start': [1000, 2000], 'end': [1100, 2000],
            'route': [{'coordinates': [[1000, 2000], [1100, 2000]],
                       'width': 5, 'surface': 'gravel'}],
            'attribution': 'Synthetic integration test'}


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tiles, self.game = self.root / 'tiles', self.root / 'game'
        self.tiles.mkdir()
        (self.game / 'media').mkdir(parents=True)
        (self.game / 'media/newtiledefinitions.tiles').touch()
        for name in ('blends_natural_01', 'blends_street_01', 'carpentry_02',
                     'floors_exterior_tilesandstone_01', 'vegetation_ornamental_01',
                     'furniture_seating_outdoor_01', 'furniture_tables_low_01',
                     'vegetation_foliage_01', 'blends_grassoverlays_01'):
            write_png(self.tiles / (name + '.png'), 1024, 4096)
        self.source, self.choices = self.root / 'road.json', self.root / 'choices.json'
        self.source.write_text(json.dumps(route_fixture()))
        self.choices.write_text('{"roadside-cottage":{"garden":"cottage_garden_01"}}')

    def generate(self, name):
        output = self.root / name
        integration_source.build(self.source, self.choices, output, self.tiles, self.game)
        return output

    def test_cottage_driveway_and_saved_garden_align_without_changing_road(self):
        data = route_fixture()
        before = copy.deepcopy(data)
        choices = {'roadside-cottage': {'garden': 'cottage_garden_01'}}
        p = integration_source.plan(data, choices)
        self.assertEqual(data, before)
        self.assertEqual(p['building']['origin'], [175, 175])
        self.assertEqual(p['spawn'], [176, 179])
        ground = p['layers']['0_Floor']
        for y in range(158, 180):
            self.assertEqual(ground[y * 300 + 158], road_source.ASPHALT if y <= 160 else road_source.GRAVEL)
        for x in range(158, 171):
            self.assertEqual(ground[179 * 300 + x], road_source.GRAVEL if x < 170 else ('floors_exterior_tilesandstone_01', 0))
        self.assertEqual(ground[179 * 300 + 170], ('floors_exterior_tilesandstone_01', 0))
        self.assertEqual(ground[179 * 300 + 171], ('carpentry_02', 56))
        for index, tile in road_source.terrain_cells(road_source.plan(data))[(0, 0)].items():
            self.assertEqual(ground[index], tile)
        self.assertEqual(p['building']['garden'], 'cottage_garden_01')
        self.assertEqual(p['layers']['0_Furniture'][173 * 300 + 171], ('vegetation_ornamental_01', 16))

    def test_choice_change_and_repeat_preserve_inputs_and_lot(self):
        before = self.source.read_bytes(), self.choices.read_bytes()
        bare = integration_source.plan(route_fixture(), {})
        self.assertFalse(any(bare['layers']['0_Furniture']))
        first, second = self.generate('first'), self.generate('second')
        self.assertEqual(before, (self.source.read_bytes(), self.choices.read_bytes()))
        self.assertEqual({p.name: p.read_bytes() for p in first.iterdir() if p.is_file()},
                         {p.name: p.read_bytes() for p in second.iterdir() if p.is_file()})
        lot = ET.parse(first / 'roads.pzw').find("cell[@x='0'][@y='0']/lot")
        self.assertEqual((lot.get('x'), lot.get('y'), lot.get('map')), ('175', '175', 'cottage_0.tbx'))
        with self.assertRaises(FileExistsError):
            self.generate('first')

    def test_invalid_choices_and_road_overlap_fail_before_writing(self):
        for choices in ({'unknown': {}}, {'roadside-cottage': {'rotation': 90}},
                        {'roadside-cottage': {'garden': 'missing'}}):
            self.choices.write_text(json.dumps(choices))
            with self.assertRaises(ValueError):
                self.generate('bad')
            self.assertFalse((self.root / 'bad').exists())
        self.choices.write_text('{}')
        data = route_fixture()
        data['end'] = [1100, 1900]
        data['route'][0]['coordinates'][1] = data['end']
        self.source.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'overlaps road'):
            self.generate('bad')
        self.assertFalse((self.root / 'bad').exists())
        data = route_fixture()
        data['end'] = [1100, 2130]
        data['route'][0]['coordinates'][1] = data['end']
        self.source.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'outside'):
            self.generate('bad')
        self.assertFalse((self.root / 'bad').exists())

    def test_terrain_export_is_repeatable_and_preserves_lot_and_other_cells(self):
        plain = self.generate('plain')
        for name in ('terrain', 'repeat'):
            integration_source.build(self.source, self.choices, self.root / name,
                                     self.tiles, self.game, terrain_seed=42)
        files = lambda folder: {p.name: p.read_bytes() for p in folder.iterdir() if p.is_file()}
        patch = files(self.root / 'terrain')
        self.assertEqual(patch, files(self.root / 'repeat'))
        self.assertEqual({k for k, v in files(plain).items() if patch[k] != v},
                         {'manifest.json', 'road_0_0.tmx'})
        metadata = json.loads(patch['manifest.json'])['integration']['terrain']
        self.assertEqual(metadata['seed'], 42)
        self.assertGreater(metadata['vegetation_squares'], 5)
        with self.assertRaises(ValueError):
            integration_source.build(self.source, self.choices, self.root / 'badseed',
                                     self.tiles, self.game, terrain_seed=-1)
        self.assertFalse((self.root / 'badseed').exists())

    def test_package_requires_export_and_is_scoped_to_its_own_map(self):
        source = self.generate('authoring')
        with self.assertRaises(FileNotFoundError):
            road_source.package(source, self.root / 'missing')
        self.assertFalse((self.root / 'missing').exists())
        header = cottage_header()
        for y in range(2):
            for x in range(3):
                for name, data in ((f'{x}_{y}.lotheader', header),
                                   (f'world_{x}_{y}.lotpack', b'test'),
                                   (f'chunkdata_{x}_{y}.bin', b'test')):
                    (source / 'export' / name).write_bytes(data)
        (source / 'export/qa.lua').write_text('not for distribution')
        road_source.package(source, self.root / 'package')
        road_source.package(source, self.root / 'repeat')
        archive = self.root / 'package/ZombieProjektetRoadside.zip'
        self.assertEqual(archive.read_bytes(), (self.root / 'repeat' / archive.name).read_bytes())
        with zipfile.ZipFile(archive) as z:
            self.assertTrue(all(n.startswith('ZombieProjektetRoadside/') for n in z.namelist()))
            self.assertFalse(any(n.endswith(('.json', '.tbx', '.png', 'qa.lua')) for n in z.namelist()))
            self.assertIn(b'posX=176,posY=179', z.read('ZombieProjektetRoadside/42/media/maps/RoadsideTest/spawnpoints.lua'))
            lua = z.read('ZombieProjektetRoadside/42/media/lua/client/RoadTestSetup.lua')
            self.assertIn(b'local TEST_MAP = "RoadsideTest"', lua)
            self.assertIn(b'getWorld():getMap() ~= TEST_MAP', lua)

        # Both observed metadata failures must prevent creation of a package.
        for i, broken in enumerate((cottage_header(((0,), (1,), (2,))),
                                    cottage_header(include_objects=False))):
            (source / 'export/0_0.lotheader').write_bytes(broken)
            output = self.root / f'rejected-{i}'
            with self.assertRaisesRegex(ValueError, 'Invalid cottage export metadata'):
                road_source.package(source, output)
            self.assertFalse(output.exists())

    def test_metadata_gate_rejects_truncation_and_invalid_room_membership(self):
        path = self.root / 'header'
        valid = cottage_header()
        path.write_bytes(valid)
        validate_cottage_metadata(path)
        for data in (valid[:-1], cottage_header(((0, 0, 2),)), cottage_header(())):
            path.write_bytes(data)
            with self.assertRaises(ValueError):
                validate_cottage_metadata(path)


if __name__ == '__main__':
    unittest.main()
