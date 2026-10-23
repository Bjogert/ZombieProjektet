import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools import cottage_metadata as cm


def header(origin=(120, 120), broken=False, order=(0, 1, 2)):
    def ints(*items):
        return struct.pack('<' + 'i' * len(items), *items)
    x, y = origin
    rows = [('livingroom', (x, y, 6, 6), 6),
            ('bedroom', (x, y + 6, 4, 4), 1),
            ('bathroom', (x + 4, y + 6, 2, 4), 1)]
    data = b'LOTH' + ints(1, 1) + b'synthetic_tile\n' + ints(8, 8, 0, 1, 3)
    for i in order:
        name, rect, n = rows[i]
        n = 0 if broken else n
        data += name.encode() + b'\n' + ints(0, 1, *rect, n)
        data += ints(2, rect[0], rect[1]) * n
    data += ints(3, 1, 0, 1, 1, 1, 2) if broken else ints(1, 3, 0, 1, 2)
    return data + bytes(range(256)) * 4


class CottageMetadataTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.reference, self.source = self.root / 'reference', self.root / 'source'
        for folder, cell_y, x, y, name in ((self.reference, 0, 120, 120, 'cottage.pzw'),
                                         (self.source, 1, 175, 133, 'roads.pzw')):
            (folder / 'export').mkdir(parents=True)
            (folder / 'house.tbx').write_bytes(b'identical synthetic TBX fixture')
            (folder / name).write_text(f'<world><GenerateLots><worldOrigin origin="0,0"/></GenerateLots>'
                f'<cell x="0" y="{cell_y}"><lot x="{x}" y="{y}" level="0" width="6" height="10" map="house.tbx"/></cell></world>')
        (self.reference / 'export/0_0.lotheader').write_bytes(header())
        self.original = header((175, 177), True, (2, 0, 1))
        for y in range(3):
            for x in range(2):
                for name, value in ((f'{x}_{y}.lotheader', self.original),
                                    (f'world_{x}_{y}.lotpack', b'physical tiles and room IDs'),
                                    (f'chunkdata_{x}_{y}.bin', b'navigation')):
                    (self.source / 'export' / name).write_bytes(value)
        self.manifest = {'width': 1, 'height': 2, 'integration': {
            'format': 'synthetic-roadside-v1', 'cell': [0, 1],
            'building': {'origin': [175, 133], 'rotation': 0, 'size': [6, 10], 'tbx': 'house.tbx'}}}
        self.save_manifest()

    def save_manifest(self):
        (self.source / 'manifest.json').write_text(json.dumps(self.manifest))

    def run_stage(self, output='stage'):
        return cm.stage(self.reference / 'cottage.pzw', self.source, self.root / output)

    def test_translates_reference_objects_without_changing_room_ids_or_other_bytes(self):
        before = {p.name: p.read_bytes() for p in (self.source / 'export').iterdir()}
        self.run_stage()
        patched = cm.read(self.root / 'stage/export/0_1.lotheader')
        original = cm.read(self.source / 'export/0_1.lotheader')
        self.assertEqual(patched['buildings'], [[1, 2, 0]])
        self.assertEqual([r['objects'] for r in patched['rooms']],
                         [[(2, 179, 183)], [(2, 175, 177)] * 6, [(2, 175, 183)]])
        for a, b in zip(original['rooms'], patched['rooms']):
            self.assertEqual({k: v for k, v in a.items() if k != 'objects'},
                             {k: v for k, v in b.items() if k != 'objects'})
        self.assertEqual(original['prefix'], patched['prefix'])
        self.assertEqual(original['suffix'], patched['suffix'])
        after = {p.name: p.read_bytes() for p in (self.root / 'stage/export').iterdir()}
        self.assertEqual([n for n in before if before[n] != after[n]], ['0_1.lotheader'])
        self.assertEqual(before, {p.name: p.read_bytes() for p in (self.source / 'export').iterdir()})
        self.run_stage('repeat')
        self.assertEqual((self.root / 'stage/metadata-provenance.json').read_bytes(),
                         (self.root / 'repeat/metadata-provenance.json').read_bytes())
        with self.assertRaises(FileExistsError):
            self.run_stage()

    def test_rejects_mismatched_tbx_geometry_metadata_and_incomplete_export(self):
        changes = [
            ('house.tbx', b'different house'),
            ('export/0_1.lotheader', header((174, 177), True)),
            ('export/0_1.lotheader', header((175, 177), False)),
            ('export/0_1.lotheader', self.original[:-1]),
            ('export/world_0_1.lotpack', b''),
        ]
        for relative, value in changes:
            with self.subTest(relative=relative, size=len(value)):
                path = self.source / relative
                previous = path.read_bytes()
                path.write_bytes(value)
                with self.assertRaises(ValueError):
                    self.run_stage()
                self.assertFalse((self.root / 'stage').exists())
                path.write_bytes(previous)
        self.manifest['integration']['building']['origin'][0] += 1
        self.save_manifest()
        with self.assertRaises(ValueError):
            self.run_stage()
        self.assertFalse((self.root / 'stage').exists())

    def test_rejects_out_of_room_objects_and_unsupported_suffix(self):
        path = self.reference / 'export/0_0.lotheader'
        data = cm.read(path)
        data['rooms'][0]['objects'][0] = (2, 119, 120)
        path.write_bytes(cm.encode(data))
        with self.assertRaises(ValueError):
            self.run_stage()
        self.assertFalse((self.root / 'stage').exists())
        path.write_bytes(header() + b'extra')
        with self.assertRaises(ValueError):
            self.run_stage()


if __name__ == '__main__':
    unittest.main()
