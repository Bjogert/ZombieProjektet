import copy
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import road_extract as re


def way(wid, nodes, coordinates, **tags):
    return {'id': wid, 'nodes': nodes, 'coordinates': coordinates,
            'tags': {'highway': 'residential', **tags}}


class RoadExtractionTests(unittest.TestCase):
    def fixture(self):
        return [way(10, [1, 2, 3], [(10, 10), (20, 10), (30, 10)], surface='gravel')]

    def route(self, ways, start=(10, 10), end=(30, 10)):
        return re.route(ways, start, end, max_snap=3)

    def test_connected_route_is_deterministic_and_preserves_source(self):
        ways = self.fixture()
        before = copy.deepcopy(ways)
        result = self.route(ways)
        self.assertEqual(result['distance_m'], 20)
        self.assertEqual(result['start'], (10, 10))
        self.assertEqual(result['end'], (30, 10))
        self.assertEqual([s['id'] for s in result['route']], ['osm/way/10/1-2', 'osm/way/10/2-3'])
        self.assertEqual([s['width'] for s in result['route']], [5, 5])
        self.assertEqual(result, self.route(list(reversed(ways))))
        self.assertEqual(ways, before)
        self.assertEqual(result['uncertainties']['segments_missing_access'], 2)

    def test_oneway_reverse_roundabout_and_access_precedence(self):
        base = self.fixture()[0]
        for tags in ({'oneway': 'yes'}, {'junction': 'roundabout'}, {'highway': 'motorway'}):
            w = copy.deepcopy(base)
            w['tags'].update(tags)
            self.assertEqual(self.route([w])['distance_m'], 20)
            with self.assertRaisesRegex(ValueError, 'connected'):
                self.route([w], (30, 10), (10, 10))
        w = copy.deepcopy(base)
        w['tags']['oneway'] = '-1'
        self.assertEqual(self.route([w], (30, 10), (10, 10))['distance_m'], 20)
        for tags in ({'access': 'private'}, {'motor_vehicle': 'no'}, {'oneway': 'reversible'},
                     {'access:conditional': 'yes @ (Mo-Fr)'}, {'motorcar': 'destination'}):
            w = copy.deepcopy(base)
            w['tags'].update(tags)
            with self.assertRaises(ValueError):
                self.route([w])
        w = copy.deepcopy(base)
        w['tags'].update(access='private', motor_vehicle='no', motorcar='yes')
        self.assertEqual(self.route([w])['distance_m'], 20)

    def test_unsupported_crossings_are_excluded_and_geometric_crossing_is_not_a_junction(self):
        for tags in ({'bridge': 'movable'}, {'tunnel': 'building_passage'}, {'layer': '1'}, {'ford': 'yes'}):
            w = copy.deepcopy(self.fixture()[0])
            w['tags'].update(tags)
            with self.assertRaises(ValueError):
                self.route([w])
        ways = [way(1, [1, 2], [(10, 20), (30, 20)]),
                way(2, [3, 4], [(20, 10), (20, 30)])]
        with self.assertRaisesRegex(ValueError, 'connected'):
            self.route(ways, (10, 20), (20, 30))

    def test_missing_surface_is_explicit_and_snap_distance_is_bounded(self):
        w = self.fixture()[0]
        del w['tags']['surface']
        result = self.route([w])
        self.assertEqual(result['route'][0]['surface'], None)
        self.assertEqual(result['route'][0]['width'], 7)
        self.assertEqual(result['uncertainties']['segments_missing_surface'], 2)
        with self.assertRaisesRegex(ValueError, 'snap'):
            self.route([w], (0, 0))
        with self.assertRaisesRegex(ValueError, 'distinct'):
            self.route([w], (10, 10), (11, 10))

    def test_invalid_or_conflicting_nodes_do_not_silently_change_geometry(self):
        for bad in (way(20, [4, 5], [(10, 10), (float('nan'), 20)]),
                    way(20, [1, 4], [(99, 99), (40, 10)])):
            with self.assertRaises(ValueError):
                self.route(self.fixture() + [bad])

    def test_equal_length_alternatives_are_stable_and_selection_is_bounded(self):
        ways = [way(10, [1, 2, 4], [(10, 10), (20, 0), (30, 10)]),
                way(20, [1, 3, 4], [(10, 10), (20, 20), (30, 10)])]
        self.assertEqual(self.route(ways), self.route(list(reversed(ways))))
        self.assertEqual({s['way_id'] for s in self.route(ways)['route']}, {10})
        with self.assertRaisesRegex(ValueError, 'outside'):
            re.route(ways, (10, 10), (30, 10), 3, [0, 0, 25, 25])


@unittest.skipUnless(importlib.util.find_spec('osmium') and importlib.util.find_spec('pyproj'),
                     'Install requirements-geodata.txt for local PBF/projection integration tests')
class LocalSourceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.source = self.root / 'synthetic.osm'
        self.registry = self.root / 'registry.json'
        self.xml = '''<osm version="0.6">
          <node id="1" lon="15" lat="60"><tag k="place" v="village"/></node>
          <node id="2" lon="15.001" lat="60"><tag k="place" v="village"/></node>
          <node id="3" lon="16" lat="61"/>
          <way id="10"><nd ref="1"/><nd ref="2"/><tag k="highway" v="residential"/></way>
          <way id="20"><nd ref="3"/><nd ref="99"/><tag k="highway" v="residential"/></way>
        </osm>'''
        self.write_source(self.xml)

    def write_source(self, text):
        self.source.write_text(text)
        self.record = {'dataset_id': 'synthetic', 'url': 'https://example.org/synthetic.osm',
                       'snapshot': 'test', 'license': 'ODbL-1.0', 'attribution': 'Synthetic test',
                       'sha256': hashlib.sha256(self.source.read_bytes()).hexdigest(),
                       'place_node_ids': [1, 2], 'bounds_epsg3006': [499900, 6651300, 500200, 6651500],
                       'max_snap_m': 100}
        self.registry.write_text(json.dumps(self.record))

    def test_local_extract_projects_and_repeats_without_source_mutation_or_console_geometry(self):
        before = self.source.read_bytes(), self.registry.read_bytes()
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            re.extract(self.source, self.registry, self.root / 'first')
            re.extract(self.source, self.registry, self.root / 'second')
        result = json.loads((self.root / 'first/corridor.json').read_text())
        self.assertAlmostEqual(result['start'][0], 500000, places=3)
        self.assertAlmostEqual(result['start'][1], 6651411.19, places=2)
        self.assertTrue(55 < result['distance_m'] < 57)
        self.assertEqual(result['uncertainties']['incomplete_ways_excluded'], {'outside_known_selection': 1})
        self.assertNotIn('6651411', log.getvalue())
        for name in ('corridor.json', 'provenance.json'):
            self.assertEqual((self.root / 'first' / name).read_bytes(),
                             (self.root / 'second' / name).read_bytes())
        self.assertEqual(before, (self.source.read_bytes(), self.registry.read_bytes()))
        with self.assertRaises(FileExistsError):
            re.extract(self.source, self.registry, self.root / 'first')

    def test_bad_checksum_incomplete_selected_way_and_invalid_registration_leave_no_output(self):
        self.source.write_text(self.xml + ' ')
        with self.assertRaisesRegex(ValueError, 'checksum'):
            re.extract(self.source, self.registry, self.root / 'bad')
        self.assertFalse((self.root / 'bad').exists())
        self.write_source(self.xml.replace('<nd ref="2"/>', '<nd ref="99"/>'))
        with self.assertRaisesRegex(ValueError, 'No eligible'):
            re.extract(self.source, self.registry, self.root / 'bad')
        self.assertFalse((self.root / 'bad').exists())
        self.record['max_snap_m'] = 10000
        self.registry.write_text(json.dumps(self.record))
        with self.assertRaises(ValueError):
            re.extract(self.source, self.registry, self.root / 'bad')
        self.assertFalse((self.root / 'bad').exists())

    def test_incomplete_nearby_way_is_reported_but_never_partially_routed(self):
        self.write_source(self.xml.replace('<nd ref="3"/>', '<nd ref="1"/>'))
        re.extract(self.source, self.registry, self.root / 'out')
        result = json.loads((self.root / 'out/corridor.json').read_text())
        self.assertEqual(result['uncertainties']['incomplete_ways_excluded'], {'near_selection': 1})
        self.assertEqual({s['way_id'] for s in result['route']}, {10})


if __name__ == '__main__':
    unittest.main()
