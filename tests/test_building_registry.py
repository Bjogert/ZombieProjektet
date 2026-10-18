import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from tools import building_registry as br


GIS = all(importlib.util.find_spec(name) for name in ('shapely', 'pyproj'))


def rectangle():
    return {'type': 'Feature', 'id': 'provider:release:1', 'properties': {},
            'geometry': {'type': 'Polygon', 'coordinates': [[[500000, 6300000],
                [500006, 6300000], [500006, 6300010], [500000, 6300010], [500000, 6300000]]]}}


@unittest.skipUnless(GIS, 'Optional geodata dependencies required')
class BuildingRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input, self.source = self.root/'input.json', self.root/'source.json'
        self.output = self.root/'register'
        self.feature = rectangle()
        self.write_input([self.feature])

    def write_input(self, features, crs=3006):
        self.input.write_text(json.dumps({'type':'FeatureCollection','features':features}))
        self.metadata = {'provider':'Synthetic provider', 'release':'test-1',
            'url':'https://example.org/buildings', 'license':'Synthetic fixture',
            'attribution':'Synthetic test', 'crs':crs,
            'sha256':hashlib.sha256(self.input.read_bytes()).hexdigest(),
            'selection':{'center':[500000,6300000], 'radius_m':750}}
        self.source.write_text(json.dumps(self.metadata))

    def test_known_measurements_and_repeat_preserve_identity_and_choices(self):
        result = br.build(self.input, self.source, self.output)
        self.assertEqual(result['registered'], 1)
        p = self.output/'registry.json'
        registry=json.loads(p.read_text())
        b=registry['buildings'][0]
        self.assertEqual(b['measurements']['area_m2'],60)
        self.assertEqual(b['measurements']['rectangle_sides_m'],[6,10])
        self.assertEqual(b['measurements']['rectangle_occupancy'],1)
        self.assertEqual(b['measurements']['long_axis_degrees_from_north'],0)
        self.assertIsNone(b['building_use'])
        self.assertTrue(all(v is None for v in b['appearance'].values()))
        b['observations']=[{'property':'facade_color','value':'red','method':'creator_observation'}]
        p.write_text(json.dumps(registry))
        choices=self.output/'choices.json'
        choices.write_text(json.dumps({b['id']:{'garden':'cottage_garden_01'}}))
        before={f.name:f.read_bytes() for f in self.output.iterdir()}
        br.build(self.input,self.source,self.output)
        self.assertEqual(before,{f.name:f.read_bytes() for f in self.output.iterdir()})

    def test_projection_axis_order_and_rotated_shape(self):
        from pyproj import Transformer
        from shapely import affinity
        from shapely.geometry import shape, mapping
        g=affinity.rotate(shape(self.feature['geometry']),30,origin='centroid')
        self.feature['geometry']=mapping(g)
        self.write_input([self.feature])
        br.build(self.input,self.source,self.output)
        b=json.loads((self.output/'registry.json').read_text())['buildings'][0]
        self.assertAlmostEqual(b['measurements']['area_m2'],60,places=3)
        self.assertEqual(b['measurements']['long_axis_degrees_from_north'],150)
        inverse=Transformer.from_crs(3006,4326,always_xy=True)
        f=rectangle()
        f['geometry']['coordinates']=[[list(inverse.transform(*p)) for p in f['geometry']['coordinates'][0]]]
        self.write_input([f],4326)
        br.build(self.input,self.source,self.root/'geographic')
        b=json.loads((self.root/'geographic/registry.json').read_text())['buildings'][0]
        self.assertAlmostEqual(b['measurements']['area_m2'],60,places=3)
        self.assertEqual(b['measurements']['rectangle_sides_m'],[6,10])

    def test_bad_geometry_ids_hash_and_extent_leave_no_output(self):
        bowtie=rectangle()
        bowtie['geometry']['coordinates']=[[[500000,6300000],[500006,6300010],
            [500000,6300010],[500006,6300000],[500000,6300000]]]
        distant=rectangle()
        distant['geometry']['coordinates']=[[[x+2000,y] for x,y in rectangle()['geometry']['coordinates'][0]]]
        three=rectangle()
        three['geometry']['coordinates']=[[[*p,0] for p in three['geometry']['coordinates'][0]]]
        for features in ([bowtie],[distant],[three],[rectangle(),rectangle()],[]):
            with self.subTest(features=len(features)):
                self.write_input(features)
                with self.assertRaises(ValueError): br.build(self.input,self.source,self.output)
                self.assertFalse(self.output.exists())
        self.write_input([rectangle()])
        self.input.write_text(self.input.read_text()+' ')
        with self.assertRaisesRegex(ValueError,'hash'): br.build(self.input,self.source,self.output)
        self.assertFalse(self.output.exists())

    def test_source_refresh_and_registry_corruption_cannot_reset_choices(self):
        br.build(self.input,self.source,self.output)
        before={p.name:p.read_bytes() for p in self.output.iterdir()}
        self.feature['geometry']['coordinates'][0][1][0]+=1
        self.write_input([self.feature])
        with self.assertRaisesRegex(ValueError,'reconciliation'):
            br.build(self.input,self.source,self.output)
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.output.iterdir()})
        self.write_input([rectangle()])
        p=self.output/'registry.json'
        registry=json.loads(p.read_text()); registry['buildings'][0]['source_alias']='bad'
        p.write_text(json.dumps(registry))
        with self.assertRaisesRegex(ValueError,'identity'):
            br.build(self.input,self.source,self.output)


if __name__=='__main__': unittest.main()
