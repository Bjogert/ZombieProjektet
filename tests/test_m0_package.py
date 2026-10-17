import tempfile
import struct
import unittest
import zipfile
from pathlib import Path

from tools import package_m0


class TestM0Package(unittest.TestCase):
    def test_missing_export_never_creates_a_mod(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            with self.assertRaises(FileNotFoundError):
                package_m0.package(root / 'export', root / 'result')
            self.assertFalse((root / 'result').exists())

    def test_legacy_header_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            header = Path(d) / '0_0.lotheader'
            header.write_bytes(b'\0' * 64)
            with self.assertRaisesRegex(ValueError, 'Build 42'):
                package_m0.validate_header(header)

    def test_package_excludes_tools_and_has_stable_contents(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            export = root / 'export'
            export.mkdir()
            header = b'LOTH' + struct.pack('<ii', 1, 1) + b'blends_natural_01_16\n' + struct.pack('<ii', 8, 8)
            for x in range(2):
                for y in range(2):
                    (export / f'{x}_{y}.lotheader').write_bytes(header)
                    (export / f'world_{x}_{y}.lotpack').write_bytes(b'test fixture')
                    (export / f'chunkdata_{x}_{y}.bin').write_bytes(b'test fixture')
            (export / 'newtiledefinitions.tiles').write_bytes(b'must not ship')
            for name in ('one', 'two'):
                package_m0.package(export, root / name)
            self.assertEqual((root / 'one/ZombieProjektetM0.zip').read_bytes(),
                             (root / 'two/ZombieProjektetM0.zip').read_bytes())
            with zipfile.ZipFile(root / 'one/ZombieProjektetM0.zip') as archive:
                self.assertFalse(any(n.endswith('.tiles') for n in archive.namelist()))
                self.assertIn('ZombieProjektetM0/42/media/maps/M0Sweden/spawnpoints.lua', archive.namelist())
                # B42 MapGroups skips versioned maps unless this shared directory exists.
                self.assertIn('ZombieProjektetM0/common/media/maps/.gitkeep', archive.namelist())
            with self.assertRaises(FileExistsError):
                package_m0.package(export, root / 'one')

            package_m0.package(export, root / 'cottage', profile='cottage')
            with zipfile.ZipFile(root / 'cottage/ZombieProjektetCottage.zip') as archive:
                names = archive.namelist()
                self.assertIn('ZombieProjektetCottage/42/media/maps/CottageTest/spawnpoints.lua', names)
                self.assertIn('ZombieProjektetCottage/common/media/maps/.gitkeep', names)
                self.assertFalse(any('M0Sweden' in n or 'ZombieProjektetM0' in n for n in names))

            package_m0.package(export, root / 'garden', profile='garden')
            with zipfile.ZipFile(root / 'garden/ZombieProjektetGarden.zip') as archive:
                names = archive.namelist()
                self.assertIn('ZombieProjektetGarden/42/media/maps/CottageGardenTest/spawnpoints.lua', names)
                self.assertIn('ZombieProjektetGarden/common/media/maps/.gitkeep', names)
                self.assertFalse(any('ZombieProjektetCottage/' in n or 'qa_' in n for n in names))

            package_m0.package(export, root / 'placements', profile='placements')
            with zipfile.ZipFile(root / 'placements/ZombieProjektetPlacements.zip') as archive:
                names = archive.namelist()
                self.assertIn('ZombieProjektetPlacements/42/media/maps/PlacementTest/spawnpoints.lua', names)
                self.assertIn('ZombieProjektetPlacements/common/media/maps/.gitkeep', names)
                self.assertFalse(any('qa_' in n or n.endswith('.tiles') for n in names))
