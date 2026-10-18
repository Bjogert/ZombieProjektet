# Roadside integration — INTEGRATE-01

## Result on 2026-10-18

The cottage, optional deck/garden and road prototype now generate together in a
separate synthetic fixture. Initial game diagnostics passed **24 of 25 probes**,
but the shared building identity probe failed. Official WorldEd exported three
buildings for the cottage's three rooms and zero room metadata objects, rather
than one building and eight objects. **INTEGRATE-01 has not passed acceptance.**

The packager now rejects this known failure before creating an output folder.
The earlier diagnostic ZIP and local save remain reproduction evidence, not a
release or a creator acceptance request. No real Getaboda house is represented.

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

## Actual game trial

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

## Diagnosis and next experiment

The failure is reproduced in both garden variants at authoring cell `(0,6)`;
the earlier cottage at `(0,0)` has correct metadata. This narrows the investigation
to export coordinates/room grouping; it does not prove the complete root cause.
The [official exporter source at the inspected revision](https://github.com/timbaker/pzworlded/blob/4da5e78969dfeb27d913305fe5b7ea28eecad2c8/src/editor/lotfilesmanager256.cpp)
translates room rectangles to runtime-cell coordinates, while room-object
generation indexes the combined source grid. Coordinate handling is the leading
hypothesis, still requiring a minimal controlled reproduction.

Next: export the identical one-cottage fixture at zero and nonzero cell positions,
compare room grouping/object metadata, and verify a supported exporter correction.
Then repeat fresh-spawn, walking, roof and save/reload QA. Keep the original export
as evidence. No ad hoc binary repair, new survival system or replacement exporter
has been introduced. PIPELINE-01 remains independent ready work if export repair
needs an external tool change.

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
