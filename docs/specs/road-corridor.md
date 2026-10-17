# Getaboda–Agunnaryd 1:1 road corridor

Approved by the creator on 2026-10-17: start at 1:1, build a drivable road toward Agunnaryd, test in the game and provide screenshots. Compression is deferred until actual driving evidence supports it.

## Behavior and boundary
Generate a separate experimental map from a locally processed, connected OSM route. Preserve metric distances using one ground square per metre, translation and north-to-game-Y inversion only. Source coordinates remain immutable. The extracted route connects road nodes near the Getaboda and Agunnaryd place labels; these are not verified house entrances. Current route length is approximately 5.09 km.

Inputs: normalized EPSG:3006 JSON segments with stable source IDs, endpoint coordinates, widths, surfaces and provenance. Outputs: deterministic multi-cell TMX/PZW authoring files, a manifest and a separate Build 42 package after official WorldEd export. No raw geometry is committed or sent to cloud tools.

Use stock road/ground resources, provisional 5 m gravel and 7 m asphalt widths where widths are unknown, a small synthetic starting pad and a functioning test car. Keep all width/pad choices distinct from measured geography. Plain surrounding ground is sufficient. No realistic houses, gardens, forest, population or final survival balance is implied.

## Acceptance
- Connected route with no scaling/compression; cross-cell road coverage remains continuous.
- Source input unchanged; repeat authoring output deterministic.
- Reject disconnected segments, nonfinite coordinates, invalid widths, non-1:1 scale, non-ground crossings and existing output directories.
- Validate every required runtime-cell export before packaging; exclude game artwork, raw source input and temporary QA code.
- Actual Build 42.21.0 game test: spawn, car starts and moves, travel from start to finish, road transitions and cell boundaries load; screenshots and logs saved.
- Existing mods and valuable saves remain intact. Use a fresh test save.

Automated tests prove transforms/raster continuity/packaging behavior. Only game observation proves driving. Engine performance with houses, zombies and dense vegetation remains unverified.
