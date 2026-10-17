# Persistent building style overrides — OVERRIDE-01

## Purpose and boundary

Keep an individually chosen building style when regenerating the existing design manifest. This slice uses the fictional fixtures in `data/sample/`. It does not import real geography, generate playable map files or establish a real building's appearance.

## Contract

The optional `--overrides` file is a JSON object keyed by the existing stable GeoJSON feature ID. Each value contains exactly one string field, `style`:

```json
{
  "demo-barn-2": {"style": "white_plaster"}
}
```

The style must occur in `default_styles` or any `building_styles` list in the chosen style configuration. A manual choice takes precedence over the building type's deterministic defaults, even when that type would not automatically select it. Omitting `--overrides`, or supplying `{}`, retains the existing generated selections and manifest format.

IDs match the manifest's string `source_id`. Overrides must match eligible building polygons in the current input: IDs absent from the input, or attached only to ignored features, are errors. Invalid styles, unsupported fields, non-object entries and duplicate JSON keys are errors. A CLI validation error exits nonzero before writing the output, with a diagnostic identifying the problem. The output path cannot replace the source, style configuration or override file, including aliases to an existing input file.

Source geometry and override inputs remain unchanged. The tool does not infer IDs, migrate stale IDs or write generated defaults back into overrides. Correct the override file explicitly if a building is removed from the input.

## Example

Run from the repository root:

```powershell
python tools/building_styles.py --input data/sample/buildings.geojson --overrides data/sample/building-style-overrides.json --output build/building-styles.json
```

The fictional barn deliberately uses a configured style outside its automatic selection to demonstrate precedence. This is a test input, not a proposed change to the cottage's design.

## Acceptance and verification

- A manual style replaces the generated style; unrelated buildings retain their complete records.
- Repeating the run produces identical output; reordering input features preserves the manifest.
- Original geometry, properties and the separate override data remain unchanged.
- Unknown styles, malformed entries, duplicate keys and unmatched IDs fail explicitly.
- The public CLI supports both the original invocation and `--overrides`; invalid overrides preserve an existing output file.

Automated checks are in `tests/test_building_styles.py`, including CLI subprocess tests with temporary files. No new dependencies are required. Run `python -m unittest discover -s tests -v` for the full suite.

These checks prove manifest persistence only. Applying styles to game assets and demonstrating corrections surviving regeneration of a playable map remain later integration work. No raw Lantmäteriet data or third-party art is used by this slice.
