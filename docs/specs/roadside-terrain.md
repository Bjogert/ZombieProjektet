# Small roadside terrain prototype

TERRAIN-01 adds a reversible, seeded landscape around the synthetic cottage
approach. It demonstrates roadside styling without claiming real land cover.

`tools.integration_source --terrain-seed INTEGER` enables one bounded patch in
the cottage cell. Omitting it preserves the existing authoring output. Stock
grass-edge overlays soften a narrow gravel shoulder outside the existing road
and driveway; small vegetation clusters sit farther away. Existing road/pad
surfaces, all driveway squares, the house, its garden and access ring survive.
Record seed, algorithm version, bounds and counts in the integration manifest.
Use local stock tile references only; redistribute no artwork.

Acceptance:
- Same inputs/seed produce identical layers; changing seed varies vegetation.
- Source/choices remain unchanged. Preserve every road/driveway surface and
  garden object, with a vegetation-free margin around access and the house.
- Invalid seeds fail before creating output. Edits stay in one bounded patch.
- Official export and mandatory cottage metadata gate precede packaging.
- A fresh game test checks visible vegetation/edges, house access and unchanged
  fixture probes. Capture before/after views and remove temporary QA code.
- Continuous vehicle movement remains unverified until sustained control exists.

Vanilla vegetation may replace authored sprite names during load or growth.
Validate visible objects and their supported runtime replacements rather than
requiring exact source names. A fixed seed reproduces authoring placement, not
identical runtime appearance across seasons or elapsed game time.

This is a design sample, not an accepted final palette or full-corridor pass.
No trees, source land-cover classification, new mechanics or asset dependency.
