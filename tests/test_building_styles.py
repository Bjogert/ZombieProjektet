import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
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

    def test_manual_style_wins_over_generated_default(self):
        overrides = {"demo-barn-2": {"style": "white_plaster"}}
        result = module.build_manifest(self.geojson, self.styles, overrides=overrides)
        barn = next(b for b in result["buildings"] if b["source_id"] == "demo-barn-2")
        self.assertEqual(barn["style"], "white_plaster")

    def test_overrides_are_repeatable_and_do_not_change_other_buildings_or_inputs(self):
        overrides = {"demo-barn-2": {"style": "white_plaster"}}
        original_source = copy.deepcopy(self.geojson)
        original_overrides = copy.deepcopy(overrides)
        baseline = module.build_manifest(self.geojson, self.styles, seed=47)
        result = module.build_manifest(self.geojson, self.styles, seed=47, overrides=overrides)
        self.assertEqual(
            result,
            module.build_manifest(self.geojson, self.styles, seed=47, overrides=overrides),
        )
        reordered = copy.deepcopy(self.geojson)
        reordered["features"].reverse()
        self.assertEqual(
            result,
            module.build_manifest(reordered, self.styles, seed=47, overrides=overrides),
        )
        baseline_by_id = {b["source_id"]: b for b in baseline["buildings"]}
        for building in result["buildings"]:
            original = baseline_by_id[building["source_id"]]
            if building["source_id"] == "demo-barn-2":
                self.assertEqual(building, {**original, "style": "white_plaster"})
            else:
                self.assertEqual(building, original)
        self.assertEqual(self.geojson, original_source)
        self.assertEqual(overrides, original_overrides)

    def test_unknown_style_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "Unknown style.*demo-house-1.*neon_pink"):
            module.build_manifest(
                self.geojson, self.styles, overrides={"demo-house-1": {"style": "neon_pink"}}
            )

    def test_invalid_override_structure_is_an_error(self):
        for overrides in (
            [],
            {"demo-house-1": "white_plaster"},
            {"demo-house-1": {}},
            {"demo-house-1": {"style": None}},
            {"demo-house-1": {"style": ["white_plaster"]}},
            {"demo-house-1": {"style": "white_plaster", "geometry": {}}},
            {123: {"style": "white_plaster"}},
        ):
            with self.subTest(overrides=overrides), self.assertRaisesRegex(ValueError, "[Oo]verride"):
                module.build_manifest(self.geojson, self.styles, overrides=overrides)

    def test_unmatched_override_id_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "Unmatched override IDs: missing-house"):
            module.build_manifest(
                self.geojson, self.styles, overrides={"missing-house": {"style": "white_plaster"}}
            )

    def test_override_for_ignored_feature_is_unmatched(self):
        self.geojson["features"][0]["properties"]["building"] = "no"
        with self.assertRaisesRegex(ValueError, "Unmatched override IDs: demo-house-1"):
            module.build_manifest(
                self.geojson, self.styles, overrides={"demo-house-1": {"style": "white_plaster"}}
            )

    def test_missing_id_is_an_error(self):
        self.geojson["features"][0].pop("id")
        with self.assertRaises(ValueError):
            module.build_manifest(self.geojson, self.styles)

    def test_non_building_is_ignored(self):
        self.geojson["features"][0]["properties"]["building"] = "no"
        result = module.build_manifest(self.geojson, self.styles)
        self.assertEqual(len(result["buildings"]), 1)


class TestBuildingStylesCLI(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)
        self.source = self.folder / "buildings.geojson"
        self.styles = self.folder / "house_styles.json"
        self.overrides = self.folder / "style-overrides.json"
        self.output = self.folder / "generated" / "manifest.json"
        self.source.write_bytes((ROOT / "data/sample/buildings.geojson").read_bytes())
        self.styles.write_bytes((ROOT / "config/house_styles.json").read_bytes())
        self.overrides.write_bytes((ROOT / "data/sample/building-style-overrides.json").read_bytes())

    def run_cli(self, *extra_args, output=None):
        return subprocess.run(
            [sys.executable, str(ROOT / "tools/building_styles.py"),
             "--input", str(self.source), "--styles", str(self.styles),
             "--output", str(output or self.output), *extra_args],
            capture_output=True, text=True, check=False,
        )

    def test_cli_applies_overrides_and_regenerates_identical_output(self):
        original_inputs = {
            path: path.read_bytes() for path in (self.source, self.styles, self.overrides)
        }
        baseline_run = self.run_cli()
        self.assertEqual(baseline_run.returncode, 0, baseline_run.stderr)
        baseline = json.loads(self.output.read_text(encoding="utf-8"))
        first_run = self.run_cli("--overrides", str(self.overrides))
        self.assertEqual(first_run.returncode, 0, first_run.stderr)
        first_output = self.output.read_bytes()
        result = json.loads(first_output)
        self.assertEqual([b["source_id"] for b in result["buildings"]],
                         ["demo-barn-2", "demo-house-1"])
        expected = copy.deepcopy(baseline)
        expected["buildings"][0]["style"] = "white_plaster"
        self.assertEqual(result, expected)
        second_run = self.run_cli("--overrides", str(self.overrides))
        self.assertEqual(second_run.returncode, 0, second_run.stderr)
        self.assertEqual(first_output, self.output.read_bytes())
        self.assertEqual({path: path.read_bytes() for path in original_inputs}, original_inputs)

    def test_cli_rejects_invalid_overrides_without_replacing_output(self):
        self.output.parent.mkdir()
        self.output.write_text("existing manifest", encoding="utf-8")
        for overrides, message in (
            ({"demo-house-1": {"style": "neon_pink"}}, "Unknown style"),
            ({"missing-house": {"style": "white_plaster"}}, "Unmatched override IDs"),
            (None, "Overrides must be an object"),
        ):
            with self.subTest(overrides=overrides):
                self.overrides.write_text(json.dumps(overrides), encoding="utf-8")
                result = self.run_cli("--overrides", str(self.overrides))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(self.output.read_text(encoding="utf-8"), "existing manifest")

    def test_cli_cannot_overwrite_input_files(self):
        for path in (self.source, self.styles, self.overrides):
            with self.subTest(path=path.name):
                original = path.read_bytes()
                result = self.run_cli("--overrides", str(self.overrides), output=path)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Output must not overwrite", result.stderr)
                self.assertEqual(path.read_bytes(), original)

    def test_cli_rejects_duplicate_override_keys(self):
        for raw_json, message in (
            ('{"demo-barn-2":{"style":"white_plaster"},'
             '"demo-barn-2":{"style":"red_wood"}}', "Duplicate override key: demo-barn-2"),
            ('{"demo-barn-2":{"style":"white_plaster","style":"red_wood"}}',
             "Duplicate override key: style"),
        ):
            with self.subTest(raw_json=raw_json):
                self.overrides.write_text(raw_json, encoding="utf-8")
                result = self.run_cli("--overrides", str(self.overrides))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
