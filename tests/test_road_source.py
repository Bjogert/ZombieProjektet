import json
import tempfile
import unittest
import struct
import zipfile
from pathlib import Path
from tools import road_source


def fixture():
    return {
        "crs": "EPSG:3006",
        "metres_per_square": 1,
        "route": [
            {
                "id": "test/one",
                "coordinates": [[1000, 2000], [1600, 2000]],
                "width": 5,
                "surface": "gravel",
            },
            {
                "id": "test/two",
                "coordinates": [[1600, 2000], [1600, 2400]],
                "width": 7,
                "surface": "asphalt",
            },
        ],
        "start": [1000, 2000],
        "end": [1600, 2400],
        "attribution": "Synthetic test",
    }


class RoadSourceTests(unittest.TestCase):
    def test_metric_transform_and_continuous_road_across_cells(self):
        plan = road_source.plan(fixture())
        start, end = plan["start"], plan["end"]
        self.assertEqual((end[0] - start[0], end[1] - start[1]), (600, -400))
        self.assertAlmostEqual(plan["distance_m"], 1000)
        for x in range(start[0], start[0] + 601):
            self.assertIn((x, start[1]), plan["roads"])
        for y in range(end[1], start[1] + 1):
            self.assertIn((end[0], y), plan["roads"])
        self.assertNotIn((start[0] + 10, start[1] + 4), plan["roads"])

    def test_rejects_broken_route_and_compression(self):
        data = fixture()
        data["route"][1]["coordinates"][0] = [1605, 2000]
        with self.assertRaisesRegex(ValueError, "connected"):
            road_source.plan(data)
        data = fixture()
        data["metres_per_square"] = 2
        with self.assertRaisesRegex(ValueError, "1:1"):
            road_source.plan(data)
        data = fixture()
        data["route"][0]["width"] = float("nan")
        with self.assertRaises(ValueError):
            road_source.plan(data)

    def test_grade_crossings_and_bad_endpoints_are_rejected(self):
        for tags in (
            {"layer": "1"},
            {"bridge": "yes"},
            {"bridge": "movable"},
            {"tunnel": "yes"},
            {"tunnel": "building_passage"},
        ):
            data = fixture()
            data["route"][0]["tags"] = tags
            with self.assertRaisesRegex(ValueError, "crossing"):
                road_source.plan(data)
        data = fixture()
        data["end"] = [1600, 2500]
        with self.assertRaisesRegex(ValueError, "Endpoints"):
            road_source.plan(data)

    def test_repeat_build_preserves_source_and_missing_exports_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tiles = root / "tiles"
            tiles.mkdir()
            game = root / "game"
            (game / "media").mkdir(parents=True)
            (game / "media/newtiledefinitions.tiles").touch()
            for name in ["blends_natural_01", "blends_street_01"]:
                road_source.write_png(tiles / (name + ".png"), 1024, 5120)
            source = root / "source.json"
            source.write_text(json.dumps(fixture()))
            before = source.read_bytes()
            for name in ["one", "two"]:
                road_source.build(source, root / name, tiles, game)
            self.assertEqual(source.read_bytes(), before)
            for file in (root / "one").glob("*"):
                if file.is_file():
                    self.assertEqual(
                        file.read_bytes(), (root / "two" / file.name).read_bytes()
                    )
            with self.assertRaises(FileExistsError):
                road_source.build(source, root / "one", tiles, game)
            with self.assertRaises(FileNotFoundError):
                road_source.package(root / "one", root / "bad")
            self.assertFalse((root / "bad").exists())

    def test_package_covers_partial_runtime_cells_and_excludes_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            export = source / "export"
            export.mkdir(parents=True)
            (source / "manifest.json").write_text(
                json.dumps(
                    {
                        "width": 2,
                        "height": 1,
                        "start": [150, 150],
                        "end": [450, 150],
                        "attribution": "Synthetic fixture",
                    }
                )
            )
            header = (
                b"LOTH"
                + struct.pack("<ii", 1, 1)
                + b"blends_natural_01_16\n"
                + struct.pack("<ii", 8, 8)
            )
            for y in range(2):
                for x in range(3):
                    (export / f"{x}_{y}.lotheader").write_bytes(header)
                    (export / f"world_{x}_{y}.lotpack").write_bytes(b"fixture")
                    (export / f"chunkdata_{x}_{y}.bin").write_bytes(b"fixture")
            (export / "qa.lua").write_text("excluded")
            for name in ["one", "two"]:
                road_source.package(source, root / name)
            self.assertEqual(
                (root / "one/ZombieProjektetRoadTest.zip").read_bytes(),
                (root / "two/ZombieProjektetRoadTest.zip").read_bytes(),
            )
            with zipfile.ZipFile(root / "one/ZombieProjektetRoadTest.zip") as archive:
                names = archive.namelist()
                self.assertEqual(sum(n.endswith(".lotheader") for n in names), 6)
                self.assertFalse(
                    any("qa.lua" in n or n.endswith(".json") for n in names)
                )


if __name__ == "__main__":
    unittest.main()
