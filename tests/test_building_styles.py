import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("building_styles", ROOT / "tools" / "building_styles.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestBuildingStyles(unittest.TestCase):
    def setUp(self):
        self.geojson = json.loads((ROOT / "data" / "sample" / "buildings.geojson").read_text())
        self.styles = json.loads((ROOT / "config" / "house_styles.json").read_text())

    def test_reproducibility(self):
        self.assertEqual(
            module.build_manifest(self.geojson, self.styles, seed=47),
            module.build_manifest(self.geojson, self.styles, seed=47),
        )

    def test_barn_style(self):
        result = module.build_manifest(self.geojson, self.styles)
        barn = next(b for b in result["buildings"] if b["building_type"] == "barn")
        self.assertEqual(barn["style"], "falu_red_white_corners")

    def test_missing_id_is_an_error(self):
        self.geojson["features"][0].pop("id")
        with self.assertRaises(ValueError):
            module.build_manifest(self.geojson, self.styles)

    def test_non_building_is_ignored(self):
        self.geojson["features"][0]["properties"]["building"] = "no"
        result = module.build_manifest(self.geojson, self.styles)
        self.assertEqual(len(result["buildings"]), 1)


if __name__ == "__main__":
    unittest.main()
