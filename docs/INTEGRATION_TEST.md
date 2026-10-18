# Roadside integration — INTEGRATE-01

## Result on 2026-10-18

The synthetic cottage, deck/garden and road fixture now passes **25 of 25 runtime
probes**, manual light/door/exterior checks and a clean save/reload in 42.21.0.
A bounded compatibility stage repairs the pinned official export's room metadata
using an official zero-cell export of the identical TBX. The original export is
retained and still rejected by packaging. No physical tiles or room IDs change.
Creator acceptance, real Getaboda geometry and continuous road driving remain
separate. The initial failed trial below is historical reproduction evidence.

## Corrected artifact and fresh verification

Reference: `build/room-metadata-reference/cottage.pzw`, officially exported with
WorldEd 2026-09-16, Generate Lots 8x8, origin 0,0, one thread. The exact rotation-0
TBX at (120,120) produces one building, three rooms and eight room objects. The
same TBX at the roadside position produces three buildings and zero objects.
This proves a position-dependent metadata defect for this fixture; it does not
claim every coordinate-related exporter issue has been diagnosed.

```powershell
python -m tools.cottage_metadata --reference-world build/room-metadata-reference/cottage.pzw --source build/roadside-r1 --output build/roadside-corrected-r2
python -m tools.road_source package --source build/roadside-corrected-r2 --output build/roadside-package-r2
```

The first command stages a new export and provenance record. It requires matching
TBX bytes, translated room geometry, ground/roof levels, a valid reference and
exactly the observed three-singleton-building/zero-object failure. It preserves
the target room order/IDs, rectangles, tile table and 1024-byte zombie suffix.
Only reference room objects and building membership are translated. Unsupported
layouts, already-correct metadata, missing exports and existing outputs fail.
This is a limited compatibility transformation of official output, not a general
exporter. Revisit it when the official tool is updated.

Only `0_7.lotheader` changes among **486 exported files**. All 485 other files,
including every lotpack and navigation chunk, remain byte-identical. The old
source export is untouched. The metadata packaging gate remains mandatory.

Corrected ZIP: `build/roadside-package-r2/ZombieProjektetRoadside.zip`, SHA-256
`8bd36df17f7cdcc90cfd4db9ca948aee7644980d352ca2f62a177574aceb03dd`.
Fresh save: `2026-10-18_09-34-31`, Custom Sandbox, no zombies, Custom Occupation,
only the integration mod. Same Steam version `42.21.0 / 4a0e9546ec`.

- All 25 read-only probes pass, including shared building identity across the
  three rooms and all 44 driveway edges. The 23 original cottage/garden probes
  remain green (60 indoor/ceiling squares, collision, doors/windows/lights,
  furniture, 24 outdoor deck floors, 11 flower tiles and clear access).
- Closed-door daylight is visible. The living-room switch changes Turn on to
  Turn off. The entrance opens and ordinary context-menu walking traverses the
  house, deck and driveway, then around the exterior. The initial diagnostic had
  walked the full driveway to the road pad; this run also probes all 44 edges.
- The pitched roof renders from the front/south side and fades for player
  visibility from behind. Exterior/roof screenshots are actual game captures.
- Normal exit saves the character. With the QA Lua removed, the same save loads
  at the retained exterior position and renders the house/roof correctly.
  Both runs exit normally; no runtime exception is observed. Stock font,
  fluid-name and recipe-icon warnings remain, so this is not an error-free
  engine-log claim.
- All **493 installed files match the corrected package** after cleanup. The
  prior road-only mod and original default mod selection are preserved.

Evidence: `build/roadside-corrected-r2/evidence/`, especially
`game-initial-console.txt`, `game-clean-reload-console.txt`,
`export-verification.json`, `final-verification.json`, `interior-light.png`,
`exterior-roof.png` and `clean-reload.png`. Reference export screenshot lives in
`build/room-metadata-reference/`. Original failed evidence remains below.

## Implemented behavior

`tools/integration_source.py` reuses validated placement layers and the road
rasterizer. It places stable ID `roadside-cottage` 25 squares east and south of
the road's starting pad, with the existing unrotated cottage and the separately
saved optional garden. A three-square gravel approach narrows to the existing
two-square garden entrance. Road surfaces, deck, furniture and entrance tiles
are preserved. Invalid choices, unsupported rotations, overlap and out-of-cell
placements fail before authoring files are created.

The package has its own `ZombieProjektetRoadside` mod ID, `RoadsideTest` map,
indoor spawn and map-scoped test vehicle setup. Existing road-only packaging and
four-orientation placement fixtures remain supported. The integration fixture
deliberately supports only rotation zero; automatic real-footprint fitting is
outside this delivery.

## Reproduction

Use new output directories. The road input is the existing registered local
snapshot; do not print or upload raw coordinates or the generated manifest.

```powershell
python -m tools.integration_source --source build/road-source/corridor.json --choices examples/roadside_choices.json --output build/roadside-r1 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid"
```

Open `roads.pzw` in the official 2026-09-16 WorldEd distribution. Generate Lots
8x8 / All Cells, origin 0,0, one thread, with the supplied game TileDefs and export
directory. This trial produces 162 runtime cells / 486 binary files.

```powershell
python -m tools.road_source package --source build/roadside-r1 --output build/roadside-package-check
```

With the recorded export, the current command must reject `0_7.lotheader` with
`rooms=3, area=60, buildings=3, objects=0`. Do not remove the metadata gate to
make the build green. The previously verified `build/cottage-garden-r2/export/0_0.lotheader`
passes the same cottage metadata check.

## Automated and export evidence

- **42 Python tests pass**, including five integration tests. Tests cover the
  driveway connection, preservation of road/garden surfaces and inputs, repeat
  generation, rejected placements, separate deterministic packaging, missing
  exports, split buildings, missing room objects, truncated metadata and invalid
  room membership.
- Garden disabled, then enabled by the same stable ID: both variants officially
  exported. The change affects only the three runtime files for cell `0_7`;
  all other 483 runtime files match. Both exports have the same metadata defect.
- Repeating the garden-enabled authoring produces **109 byte-identical files**.
  Original normalized road input and saved choices are unchanged.
- The cottage TBX is byte-identical to the reviewed library variant. Runtime
  furniture exists despite the missing *header metadata objects*; those are
  distinct checks, not contradictory results.

## Initial failed game trial (before correction)

- Steam **42.21.0, 4a0e9546ec**, windowed 1280 x 720.
- Fresh Custom Sandbox save `2026-10-18_08-54-30`, no zombies, Custom Occupation,
  only the new integration mod enabled. Existing fixtures and saves retained.
- Diagnostic ZIP created before the metadata gate:
  `build/roadside-package-r1/ZombieProjektetRoadside.zip`, SHA-256
  `ba3b7cda8f8487927172095ef7ffa164df0c8c85985e0a8e9a1b32699978a31e`.
- Read-only temporary QA derived from `tools/qa_placements.lua`: all 23 original
  cottage/garden probes pass. There are 60 indoor squares, 60 ceiling squares,
  three doors, seven windows, three light switches, expected furniture, four
  blocking walls, 24 outdoor deck floors, 11 flower tiles and clear garden access.
- Additional driveway check: **44 edges, zero blocked edges, zero missing floors**.
- Additional building identity check across living room, bedroom and bathroom:
  **FAIL**. This agrees with the export summary and parsed header.
- Manual checks: spawned inside with the entrance closed; visible daylight;
  operated the light switch (menu changed from Turn on to Turn off); opened the
  entrance and walked onto the deck, along the full gravel driveway and onto the
  road's asphalt staging pad. The test SUV is present. Roof surfaces
  render from outside, but final roof/cutaway acceptance remains open with the
  building metadata defect. No full-route driving claim.
- Save/reload acceptance is deferred until a corrected export can be installed
  into a fresh diagnostic save. Normal exit logged `GameThread exited.` The
  temporary QA file was removed, all 493 installed diagnostic files match their
  pre-gate package, and the previous default mod selection was restored. The
  previously installed road-only mod remains byte-identical. The failed map is
  not left running or selected for a new game by default.

## Initial diagnosis (subsequently tested above)

The failure is reproduced in both garden variants at authoring cell `(0,6)`;
the earlier cottage at `(0,0)` has correct metadata. This narrows the investigation
to export coordinates/room grouping; it does not prove the complete root cause.
The [official exporter source at the inspected revision](https://github.com/timbaker/pzworlded/blob/4da5e78969dfeb27d913305fe5b7ea28eecad2c8/src/editor/lotfilesmanager256.cpp)
translates room rectangles to runtime-cell coordinates, while room-object
generation indexes the combined source grid. Coordinate handling is the leading
hypothesis, still requiring a minimal controlled reproduction.

The subsequent controlled zero-cell export, bounded metadata transformation and
fresh game/reload evidence are recorded above. No replacement map exporter or
new survival system is introduced. Generalize only after another fixture proves
it necessary; real-footprint fitting still waits for verified source geometry.

## Local evidence

Ignored `build/roadside-r1/evidence/` contains export screenshots, the read-only
QA script, input/authoring/package comparisons, original mod selection and prior
road-mod hashes. `game-console.txt` records the runtime probes and clean exit;
`final-verification.json` records cleanup and package parity.
`interior-light.png`, `roadside-garden.png` and `road-connection.png` are actual game
captures of this diagnostic version. `build/roadside-input/test-suite-final.txt`
records the final automated run. Developer evidence is local; source geodata and
proprietary tile artwork are not committed.

Agent entrypoint/skill checks, overview marker checks and whitespace checks pass.
Manual comparison confirms the English human overview and HTML describe the same
failed integration gate. Final self-review found no further implementation blocker
within the bounded generation/validation change; the game defect above remains open.

The sustained-driving control gate also remains open. The supported native
control API exposes key taps rather than held-key durations; a new Escape tap
did not open the old road save's menu. No reliable accelerate/steer/stop sequence
was established, and no repeated input loop or teleport was counted as a drive.
