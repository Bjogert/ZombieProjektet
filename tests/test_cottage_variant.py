import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from tools import cottage_variant


class CottageVariantTests(unittest.TestCase):
    def test_requested_size_has_complete_rooms_ceiling_and_valid_objects(self):
        source=Path('assets/buildings/swedish_cottage_01.tbx').read_bytes()
        for width,height in ((8,12),(6,9),(9,12),(11,17)):
            data=cottage_variant.generate(source,width,height)
            self.assertEqual(data,cottage_variant.generate(source,width,height))
            root=ET.fromstring(data)
            self.assertEqual((int(root.get('width')),int(root.get('height'))),(width,height))
            floors=root.findall('floor')
            cells=lambda el:[int(n) for n in el.text.replace('\n','').split(',') if n.strip()]
            rooms=cells(floors[0].find('rooms'))
            self.assertEqual(len(rooms),width*height)
            self.assertEqual(set(rooms),{1,2,3})
            ceiling=cells(floors[1].find('tiles'))
            self.assertEqual(len(ceiling),(width+1)*(height+1))
            self.assertEqual(ceiling.count(4),width*height)
            self.assertEqual(len(floors[0].findall("object[@type='door']")),3)
            self.assertEqual(len(floors[0].findall("object[@type='window']")),7)
            for obj in floors[0].findall('object'):
                x,y=int(obj.get('x')),int(obj.get('y'))
                self.assertTrue(0<=x<=width and 0<=y<=height)
                if obj.get('type')=='furniture':
                    self.assertTrue(x<width and y<height)
                    if obj.get('FurnitureTiles')=='3':
                        self.assertEqual(rooms[y*width+x],2)
                        self.assertEqual(rooms[(y+1)*width+x],2)
        self.assertEqual(source,Path('assets/buildings/swedish_cottage_01.tbx').read_bytes())

    def test_roof_surfaces_cover_every_column_without_flat_gap(self):
        source = Path('assets/buildings/swedish_cottage_01.tbx').read_bytes()
        for width in range(6, 13):
            with self.subTest(width=width):
                root = ET.fromstring(cottage_variant.generate(source, width, 12))
                covered = set()
                for roof in root.findall("floor/object[@type='roof']"):
                    x, span = int(roof.get('x')), int(roof.get('width'))
                    kind = roof.get('RoofType')
                    # Official roof primitives have finite slope coverage.
                    if kind == 'PeakNS':
                        self.assertLessEqual(span, 6, 'Old peak leaves a flat central gap')
                    elif kind == 'Peak30NS':
                        self.assertIn(span, (1, 3, 5, 7, 9, 11))
                    else:
                        self.assertIn(kind, ('Slope30W', 'Slope30E'))
                        self.assertLessEqual(span, 6)
                    self.assertEqual((roof.get('y'), roof.get('height')), ('0', '12'))
                    for column in range(x, x + span):
                        self.assertNotIn(column, covered, 'Roof surfaces overlap')
                        covered.add(column)
                self.assertEqual(covered, set(range(width)))

    def test_invalid_sizes_and_unrecognized_source_rejected(self):
        source=Path('assets/buildings/swedish_cottage_01.tbx').read_bytes()
        for w,h in ((True,12),(8.5,12),(5,12),(13,12),(8,8),(8,19)):
            with self.assertRaises(ValueError): cottage_variant.generate(source,w,h)
        with self.assertRaises(ValueError): cottage_variant.generate(b'<building/>',8,12)
        reordered = ET.fromstring(source)
        objects = reordered.find('floor').findall('object')
        objects[13].set('FurnitureTiles', '3')
        with self.assertRaises(ValueError):
            cottage_variant.generate(ET.tostring(reordered), 8, 12)
