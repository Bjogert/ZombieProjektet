# Building placement tools — TOOLS-01

## Tested artifact and scope

This separate synthetic fixture contains four copies of the rectangular cottage,
each with a deck and garden, facing the four map directions. It is not Getaboda.
The test joins saved choices by stable building ID to actual WorldEd authoring
output. The older style-only GeoJSON manifest and its broader color palette
remain separate; arbitrary source geometry fitting is not implemented.

- Source: `examples/placement_fixture.json`; separate choices:
  `examples/placement_choices.json`.
- Templates: `assets/buildings/cottage_rotations/` and
  `assets/gardens/cottage_garden_01.json`.
- Authoring: `build/placements-r1/`; repeat: `build/placements-repeat/`.
- Official 2026-09-16 WorldEd Generate Lots 8x8, All Cells, origin 0,0, one thread,
  installed game TileDefs: **4 buildings, 12 rooms, 12 room rectangles, 32 room
  objects**, with no export error.
- Package: `build/package-placements-r1/ZombieProjektetPlacements.zip`.
- SHA-256: `b63b3e41a4109899407c0c946b6ad39648e963d32e6f3b6a014223fdc653a02d`.
- Game menu: Steam **42.21.0**, `4a0e9546ec`.
- Fresh Sandbox save: `2026-10-17_20-23-10`, Custom Occupation, no zombies.
- Only `ZombieProjektetPlacements` enabled for this run. Earlier mods and saves
  retained. Agent runtime and manual checks passed; creator acceptance is open.

## Reproduce

From the repository root, choose fresh output folders:

```powershell
python -m tools.placement_source --input examples/placement_fixture.json --choices examples/placement_choices.json --output build/placements-r1 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid"
```

Open `placements.pzw` in WorldEd and export with File > Generate Lots 8x8 > All
Cells, using the supplied settings. Then:

```powershell
python -m tools.package_m0 --profile placements --export build/placements-r1/export --output build/package-placements-r1
```

Copy the resulting `ZombieProjektetPlacements` folder to the user's Zomboid mods
directory, enable **ZombieProjektet - Building tools test**, and start a new Solo
Custom Sandbox save in that world, with Custom Occupation. The package's spawn
point is specific to this fixture. Other synthetic maps use the same origin and
must not be combined with this one in a save.

## Saved choice workflow

The placement source stores a stable `id` and integer northwest `origin` for each
building, plus explicit defaults. The choices file stores only per-ID corrections:

```json
{"fixture-north": {"rotation": 90}, "fixture-east": {"garden": null}}
```

Supported house: `swedish_cottage_01`; garden: `cottage_garden_01` or `null`;
clockwise angles: 0, 90, 180, 270. The selected TBX, dimensions, source checksum
and choices are recorded in `resolved-buildings.json`. Editing that output is
temporary; edit the separate choices file to preserve a correction.

Regeneration reads the same inputs into a new output folder. It never replaces
inputs or an existing output. A new game save is still necessary after changing
compiled map content. Geometry fitting and source-ID matching for real Getaboda
buildings require a later permitted data step; this tool makes no such inference.

The collision-prevention check uses conservative rectangular envelopes containing
each house, garden and access ring. It can reject interlocking layouts that might
be playable; relaxing it needs explicit access checks. It is intentionally small,
not a parcel-layout solver. The fixed spawn belongs to the supplied fixture.

## Automated and independent review

32 tests pass. Tests cover known quarter-turn positions and directional sprites,
stable-ID choices through reordered/regenerated PZW and garden output, adding an
unrelated building, unchanged input, malformed/unknown choices, duplicate IDs,
out-of-cell and overlapping placements, and all four source files' rooms,
furniture orientations and 60 ceiling squares. The actual eight authoring files
also match byte for byte across `placements-r1` and `placements-repeat`.
The second source was separately opened and exported in WorldEd: all 12 binary
export files match, and packaging that export produces the same ZIP SHA-256.
This verifies repeatability on this installed toolchain, not across tool versions.

The independent read-only reviewer found no blockers and additionally verified
exact rotated room/furniture occupancy, ceiling positions and four corner trims,
CLI duplicate-key rejection and the 16-file separate package boundary. No artwork,
TileDefs or QA scripts are included in the package. This is code/source review,
not independent game reproduction.

The final saved-evidence review also found no blockers. It independently checked
the 92 PASS records and clean exit, all eight authoring and 12 export files,
matching ZIP hashes, 16-file installed parity and the saved screenshots. Manual
walking sequences rely on the operator's observations and still images; they
were not replayed by the reviewer.

## Runtime evidence

All **92 structural/runtime probes passed** (23 per house): 60 indoor squares,
60 upper-floor ceiling squares, three doors, seven windows, three light switches,
eight directional furniture counts, four wall collision edges, 24 deck floor
squares classified outdoors, 11 flower tiles, two outdoor chairs, one outdoor
table and zero blocked reserved garden-access edges.

`tools/qa_placements.lua` was temporarily installed for these read-only probes.
It waits for each house's area to stream and does not change doors, rooms,
furniture, character position or sandbox settings. It is absent from the ZIP.

Manual checks in the same save:

| Fixture / clockwise angle | Observation |
| --- | --- |
| West / 0 | Spawned indoors with the entrance closed and usable daylight. Operated the living-room light switch, opened the door and walked onto the deck. Exterior pitched roof rendered after walking away. |
| North / 90 | Walked the rotated deck. The exterior door was locked by the game; opened a window, climbed inside, opened the entrance from inside and walked out through it. The rotated furnishings and roof were visually inspected. |
| East / 180 | Opened an altan-facing window and climbed inside because the entrance was locked. Opened the door from inside and walked out across the deck. Rear-facing kitchen furniture and the bed remained correctly assembled; the roof returned outside. |
| South / 270 | Opened a window, climbed into the bedroom, walked through the interior doorway, opened the locked entrance from inside and walked out. Bed, kitchen, deck furniture, white trim, pitched roof and flowerbeds rendered. |

The closed-door interiors were visible; electric switch interaction was repeated
in the west fixture only. All four switch sets passed object checks. Vanilla
random door locks remain enabled: a red **Open Door** action outside does not
indicate a blocked doorway. The three locked entrances became usable from inside
without breaking windows or altering the map. Wall/roof cutaway and unseen-room
darkness follow the game's visibility system.

The game exited normally after saving (`GameThread exited.`). The temporary
installed QA file was removed, and all **16 installed files match the ZIP**, with
no extra files. The fresh save remains available; the game is closed. The latest
fixture remains selected in `mods/default.txt`; its previous setting is backed up
in the evidence directory. Existing test mods and saves were retained.

No failed probe or runtime exception was observed. Baseline stock font, texture,
fluid and Lua warnings and a piano-icon fallback remain in the console. The
`PlacementTest/objects.lua` warning is expected because this fixture defines no
authored zones. This is a technical building fixture, not a survival-ready town.

Local evidence is retained in ignored `build/placements-r1/evidence/`.
- `worlded-export.png`, `worlded-repeat.png`: both official export completions.
- `north-interior.png`, `east-interior.png`, `south-interior.png`: rotated rooms.
- `south-exterior.png`: roof, deck, seating and flowerbeds.
- `east-door-exit.png`, `south-door-exit.png`: traversed doorways and roof return.
- `west-roof-and-east.png`: two orientations in the same world.
- `console-final.txt`: all 92 probes and clean exit.
- `verification.json`: authoring/export parity, installed-file parity and ZIP hash.
- `default-mods-before.txt`: previous global mod selection.

Creator acceptance is open. No multiplayer, seating-animation, seasonal-growth,
survival-balance or arbitrary-angle support is claimed.
