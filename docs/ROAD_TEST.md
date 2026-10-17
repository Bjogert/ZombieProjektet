# Getaboda–Agunnaryd road test

Status: playable prototype installed; spawn, vehicle motion and sampled runtime road loading verified. **Continuous start-to-finish driving remains unverified.** Creator acceptance remains open.

## Scope and source

The creator approved a 1:1 driving experiment on 2026-10-17. A connected OSM road chain links road nodes near the Getaboda and Agunnaryd place labels. The chain is 5,087.55 m long, through Bygdevägen to Brånavägen (G 599). The endpoints are approximately 61 m and 42 m from the respective source place points; they are not surveyed house entrances.

Source: OSM France Kronoberg PBF snapshot 2026-10-17T01:27:19Z, SHA-256 `4d459da057e3c0132f879177947295dc4b208e9698460377f7a1c378aa0327c8`. Source way IDs: 58601063, 1448143904, 375694943 and 375694481. Attribution: © OpenStreetMap contributors, ODbL 1.0; see <https://www.openstreetmap.org/copyright>. Raw source and normalized coordinates remain local under the current data-handling decision. The local package is not a public release.

The first road is tagged gravel; subsequent sections are tagged asphalt. Widths of 5 m and 7 m are provisional design choices. Both endpoint pads are synthetic. Plain grass surrounds the road; buildings, vegetation, traffic, elevation and realistic scenery are not implemented here. Side roads are omitted in this corridor experiment.

A local audit of the four selected OSM ways found no `oneway`, `access`, `motor_vehicle`, `bridge`, `tunnel` or `layer` tags. Missing tags are not surveyed proof of unrestricted access. The local route extractor is currently an experiment at `build/municipality-draft/route_corridor.py`; the committed generator starts from its normalized JSON contract, not directly from arbitrary OSM regions.

## Build and package

`tools/road_source.py` accepts locally normalized EPSG:3006 segments. It translates easting and reverses northing into game coordinates, at one metre per square, without scaling or distorting source geometry. Rasterization quantizes coverage to the game's grid. Original source coordinates are not overwritten.

Authoring extent: 15 × 7 cells of 300 squares, or 4,500 × 2,100 squares. Official WorldEd 2026-09-16 exported 162 runtime cells in the 8 × 8 chunk format. All 486 required runtime files passed packaging checks. Their uncompressed total is 115,304,371 bytes. Empty partial edge areas are padding, not additional surveyed land.

```powershell
python -m tools.road_source build --source build/road-source/corridor.json --output build/roads-r1 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game 'C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid'
# Open roads.pzw in official WorldEd; File > Generate Lots 8x8 > All Cells.
# Use origin 0,0, the installed game's media folder, and one thread.
python -m tools.road_source package --source build/roads-r1 --output build/roads-package-r1
```

The dedicated mod ID is `ZombieProjektetRoadTest`, map `GetabodaRoadTest`. Use a fresh Custom Sandbox save with Custom Occupation and no zombies for the initial test. A repaired, fuelled SUV and its key are created at the starting pad. Existing cottage mods and saves are retained. This map occupies its own world; it must not be combined with overlapping test maps.

## Evidence and limits

- 37 automated tests passed, including known metric offsets, connected raster coverage across cells, deterministic generation/package bytes, immutable source input, invalid routes and missing runtime exports.
- Official WorldEd reported `Finished!`, with zero buildings and rooms as intended.
- Build 42.21.0 recognizes the new map and loads a fresh outdoor spawn. Save: `2026-10-17_23-02-48`.
- Initial visibility was limited by generated weather. A temporary local QA override removed fog for inspection. Car creation and normal context-menu walking have been observed.
- Temporary QA seated the driver and enabled the game's cruise control. The engine ran and the vehicle moved 66.47 m from its starting position, at approximately 10 km/h (highest sampled speed 10.18 km/h). This straight test left the starting pad and continued onto grass; it does **not** prove following the route or negotiating bends.
- A separate runtime scan teleported the character to 52 positions, every 100 m plus the endpoint. All 52 had a road floor, covering 25 runtime cells; the scan interval logged no errors. Both gravel and asphalt loaded. These are sampled load checks, not continuous driving, exhaustive seam checks or a frame-rate benchmark.
- Normal context-menu walking on the gravel road was observed. Screenshots show the actual running game, including provisional square road edges and ordinary visibility shading. Edge blending and scenery remain future work.
- Native key taps did not reliably control the game. Several temporary Lua diagnostic attempts failed against this build's API; their errors are retained in the QA log. Scheduling checkpoint teleports on `OnTick` resolved the earlier position-reset issue. No failed attempt is counted as a pass.
- Repeated generation produced byte-identical 105 TMX files, PZW and spawn PNG. Manifest content was identical (the first manifest had an earlier manual key-order correction). Repackaging the same official export produced a byte-identical ZIP. A second official WorldEd export was not performed for this road prototype.
- Package: `build/roads-package-r2/ZombieProjektetRoadTest.zip`, 687,773 bytes, SHA-256 `efa211cbc3d1ea9f64bb5370c494244cdc54948c7076ef2bd5f16b9830568505`. The small ZIP reflects repetitive plain terrain, not a finished town.
- Local evidence: `build/roads-r1/evidence/console-runtime-qa.txt`, `runtime-summary.json`, `gravel-road-in-game.jpg`, `asphalt-road-in-game.jpg` and `test-car-at-start.jpg`. Temporary diagnostics stay under ignored `build/`; they are excluded from both ZIPs.
- The original diagnostic car was replaced at the starting pad in this disposable save. All temporary Lua files and the command file were removed. All 493 installed files match the ZIP contents. A clean restart loaded the saved character and car, and the game was left paused at the start. The fog returned with ordinary game weather after removing the QA override.
- Clean-reload evidence is `console-clean-reload.txt` and `clean-reload-paused.jpg`. There are no QA callbacks or road-mod Lua exceptions in that run. The log still reports font textures, fluid-container name sanitization and a Piano recipe icon fallback in stock game files; it is not an error-free engine log.
- This sparse corridor does not establish performance for the entire municipality or for populated scenery, multiplayer, survival balance or travel enjoyment.

## Remaining gate

Complete a continuous vehicle trip from the Getaboda pad to the Agunnaryd pad with reliable steering, recording transitions, travel time and any loading stalls. Keep this technical QA with the lead; do not label the corridor fully driving-tested until it passes. The creator can inspect the prototype now without treating that as technical acceptance. No compression decision is justified by the current sparse-map checks alone.

## Review

Solo specification and code-quality review against `dcc64c` found that the complete-trip acceptance criterion is still open. A gap in bridge/tunnel rejection was reproduced with additional OSM tag values and fixed; the road tests pass. Generation, export/package completeness, rights separation and installed-file parity were reviewed. The full suite has 37 passing tests; agent setup, overview markers and whitespace checks pass. This is a draft prototype, not a release or independent game reproduction.
