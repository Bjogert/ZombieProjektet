import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from tools import candidate_source
from tools.build_m0 import write_png


def fixture():
    return {
        'source_sha256': 'a' * 64,
        'frame': {'rotation_degrees': 45, 'metres_per_square': 1, 'size': 256},
        'placements': [{'building_id': 'house-a', 'x': 120, 'y': 120,
                        'width': 8, 'height': 12, 'orientation': 0}],
        'roads': [{'coordinates': [[100, 90], [100, 160]], 'width': 5,
                   'surface': 'gravel'}],
    }


class CandidateSourceTests(unittest.TestCase):
    def test_authoring_is_repeatable_and_checks_registered_source_before_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            register, tiles, game = root / 'register', root / 'tiles', root / 'game'
            register.mkdir()
            tiles.mkdir()
            (game / 'media').mkdir(parents=True)
            (game / 'media/newtiledefinitions.tiles').write_bytes(b'fixture')
            for name in ('blends_natural_01', 'blends_street_01'):
                write_png(tiles / (name + '.png'), 1024, 4096)
            raw = b'{"type":"FeatureCollection","features":[]}'
            digest = hashlib.sha256(raw).hexdigest()
            (register / 'source.geojson').write_bytes(raw)
            (register / 'source.json').write_text(json.dumps({'sha256': digest}))
            (register / 'registry.json').write_text(json.dumps({
                'source_sha256': digest, 'buildings': [{'id': 'house-a'}]}))
            layout = root / 'layout.json'
            source = fixture()
            source['source_sha256'] = digest
            layout.write_text(json.dumps(source))
            choices = root / 'choices.json'
            choices.write_text('{"house-a":{"garden":false}}')
            before = {p: p.read_bytes() for p in [*register.iterdir(), layout, choices]}
            for name in ('first', 'repeat'):
                candidate_source.build(register, layout, choices, 'house-a', root / name, tiles, game)
            files = lambda p: {f.relative_to(p): f.read_bytes() for f in p.rglob('*') if f.is_file()}
            self.assertEqual(files(root / 'first'), files(root / 'repeat'))
            lot = ET.parse(root / 'first/candidate.pzw').find('cell/lot')
            self.assertEqual([lot.get(k) for k in ('x', 'y', 'width', 'height')],
                             ['120', '120', '8', '12'])
            self.assertEqual(before, {p: p.read_bytes() for p in before})
            (register / 'source.geojson').write_bytes(raw + b' ')
            with self.assertRaisesRegex(ValueError, 'hashes'):
                candidate_source.build(register, layout, choices, 'house-a', root / 'bad', tiles, game)
            self.assertFalse((root / 'bad').exists())

    def test_road_house_garden_and_connected_access_preserve_inputs(self):
        source = fixture()
        choices = {'house-a': {'garden': True}}
        before = copy.deepcopy((source, choices))
        result = candidate_source.plan(source, 'house-a', choices)
        self.assertEqual(result['building']['size'], [8, 12])
        self.assertEqual(result['spawn'], [121, 123])
        self.assertEqual(result['layers']['0_Floor'][120 * 300 + 100],
                         ('blends_street_01', 48))
        self.assertEqual(result['layers']['0_Floor'][123 * 300 + 118],
                         ('carpentry_02', 56))
        self.assertTrue(all(result['layers']['0_Furniture'][y * 300 + x] is None
                            for x, y in result['access']))
        for x in range(102, 120):
            self.assertIn([x, 123], result['access'])
        self.assertEqual((source, choices), before)
        self.assertEqual(result, candidate_source.plan(source, 'house-a', choices))
        plain = candidate_source.plan(source, 'house-a', {'house-a': {'garden': False}})
        self.assertEqual(plain['building'], result['building'])
        self.assertTrue(all(v is None for v in plain['layers']['0_Furniture']))

    def test_invalid_layout_and_choices_are_rejected(self):
        for update in ({'orientation': 90}, {'x': 254}, {'width': 13}, {'x': 99}):
            source = fixture()
            source['placements'][0].update(update)
            with self.subTest(update=update), self.assertRaises(ValueError):
                candidate_source.plan(source, 'house-a', {})
        for choices in ({'missing': {'garden': True}}, {'house-a': {'garden': 'yes'}},
                        {'house-a': {'unknown': True}}):
            with self.assertRaises(ValueError):
                candidate_source.plan(fixture(), 'house-a', choices)
        for points in ([[100, float('nan')], [100, 160]], [[100, 100]]):
            source = fixture()
            source['roads'][0]['coordinates'] = points
            with self.assertRaises(ValueError):
                candidate_source.plan(source, 'house-a', {})

    def test_seeded_landscape_preserves_candidates_roads_garden_and_access(self):
        source = fixture()
        source['placements'].append({'building_id': 'reserved', 'x': 132, 'y': 130,
                                     'width': 5, 'height': 8, 'orientation': 0})
        choice = {'house-a': {'garden': True, 'terrain_seed': 42}}
        before = copy.deepcopy((source, choice))
        plain = candidate_source.plan(source, 'house-a', {'house-a': {'garden': True}})
        decorated = candidate_source.plan(source, 'house-a', choice)
        self.assertEqual(decorated, candidate_source.plan(source, 'house-a', choice))
        self.assertEqual(before, (source, choice))
        self.assertEqual(plain['building'], decorated['building'])
        self.assertEqual(plain['access'], decorated['access'])
        protected = {(x, y) for x in range(114, 130) for y in range(118, 135)}
        protected |= {(x, y) for x in range(131, 138) for y in range(129, 139)}
        protected |= {tuple(p) for p in plain['access']}
        for i, floor in enumerate(plain['layers']['0_Floor']):
            x, y = i % 300, i // 300
            if (x, y) in protected or floor != candidate_source.GRASS or x >= 256 or y >= 256:
                self.assertEqual(decorated['layers']['0_Floor'][i], floor)
                self.assertEqual(decorated['layers']['0_Furniture'][i], plain['layers']['0_Furniture'][i])
        self.assertGreater(decorated['terrain']['vegetation_squares'], 0)
        self.assertGreater(decorated['terrain']['shoulder_squares'], 0)
        varied = candidate_source.plan(source, 'house-a', {'house-a': {'garden': True, 'terrain_seed': 43}})
        self.assertNotEqual(decorated['layers'], varied['layers'])
        edge = fixture()
        edge['placements'][0].update(x=240, y=239)
        edge['roads'][0]['coordinates'] = [[220, 205], [220, 256]]
        bounded = candidate_source.plan(edge, 'house-a', choice)
        self.assertEqual(bounded['terrain']['bounds'][2:], [256, 256])
        for i, floor in enumerate(bounded['layers']['0_Floor']):
            if i % 300 >= 256 or i // 300 >= 256:
                self.assertEqual(floor, candidate_source.GRASS)
                self.assertIsNone(bounded['layers']['0_Furniture'][i])
                self.assertIsNone(bounded['layers']['0_FloorOverlay'][i])
        for seed in (True, -1, 2**32, '42', None):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                candidate_source.plan(source, 'house-a', {'house-a': {'garden': True, 'terrain_seed': seed}})
