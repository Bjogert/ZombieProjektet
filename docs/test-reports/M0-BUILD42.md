# M0 evidence — 2026-10-17

**AGENT SMOKE TESTED / HUMAN ACCEPTANCE PENDING. Issue #2 remains open.**

## Environment

Git, GitHub CLI, Python 3.12.10 and Steam already installed. No new Python dependencies.
Game directory: `C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid`.
Steam app 108600, build ID `25485521`, no beta selection recorded in appmanifest.
Fresh `C:\Users\rober\Zomboid\console.txt`, line 58:
`version=42.21.0 4a0e9546ec demo=false`. Matches the
[42.21 Stable announcement](https://projectzomboid.com/blog/news/2026/09/42-21-stable-released/).
The old 2024 log was not used to establish this version. Started the game from
its installation working directory; automation launcher initially exposed no window.
The later agent-driven map tests are recorded below. No pre-existing user save was loaded or modified; two new test saves were created.

## Downloads and configuration

From [TIS tools](https://projectzomboid.com/tools/), both listed 2026-09-16:

| Archive | SHA-256 |
|---|---|
| windows-TileZed+WorldEd.zip | f6c27296d60c4da013e11a32cb2e12952bc1fa7de99743379c22b65de8f51f68 |
| Tiles.zip | 5bf254f0bef40e078db8f19f6cd3be6962c7d6366516ffafd98c96474ce24c36 |

Archives in `C:\PZModding\Tools`; extracted to `Official-2026-09-16` there.
Includes WorldEd, TileZed, BuildingEd and Qt6. Executable version fields are blank;
archive date plus hash identify tested tools. No administrator action, runtime
installer, Steam modification or system-wide setting change was performed.
Only new current-user editor settings under `HKCU/Software/TheIndieStone`:

| Key | Value name | Value |
|---|---|---|
| TileZed | ConfigDirectory | C:/PZModding/Tools/Official-2026-09-16/windows/TileZed |
| TileZed/Tilesets | TilesDirectory | C:/PZModding/Tools/Official-2026-09-16/Tiles |
| PZWorldEd | TilesDirectory | same Tiles root |
| TileZed | TilePropertiesFiles (REG_MULTI_SZ) | installed game's media/newtiledefinitions.tiles |

WorldEd openFiles session points at `build/m0/m0.pzw`; normal File > Open also works.
Editors use the Tiles root; generator's --tiles instead points to Tiles/2x.

## Experiments and actual fixes

- Initial startup failed: Tilesets.txt missing. Setting ConfigDirectory fixed it.
- WorldEd loaded/rendered our TMX. Inspected official graphics/properties and chose
  full grass tile blends_natural_01_16 instead of the initial sand.
- First 8x8 export wrote files but reported Hole in floor at 0,0,0 and elsewhere.
  Export TileDefFolder alone did not configure the floor check's TileDefWatcher.
  Adding shared TileZed TilePropertiesFiles fixed the warnings. An isolated copy
  of TileDefs did not help and was removed. No patched game files are needed.
- Corrected RoomDefs: TMX isometric object coordinates are pixels divided by
  tileheight 32. Final header confirms room z=0, rectangle (120,120,10,8), rather
  than the initial incorrect (3,3,2,1). Upper-level tile positions shift -3 per level.
- Final File > Generate Lots 8x8 > All Cells completed without an error dialog:
  **Buildings 1; Rooms 1; Room rects 1; Room objects 2**. Completion was visually
  inspected in this chat. It does not prove collision or a usable entrance.

Source cross-check:
[Tim Baker basements](https://github.com/timbaker/pzworlded/tree/4da5e78969dfeb27d913305fe5b7ea28eecad2c8),
src/libtiled/mapreader.cpp, src/editor/preferences.cpp, lotfilesmanager256.cpp,
BuildingEditor/buildingfloor.cpp. Exact correspondence with downloaded binaries
is not established; observed export behavior is the primary evidence.

## Reproduction and outputs

Commands/manual step: [mod README](../../mod/README.md).
`tools/build_m0.py` creates deterministic original 300x300 TMX/PZW and black
30x30 zombie-density PNG, referencing external tiles without copying art.
Road x=110..114,y=100..150. House x=120..129,y=120..127. West door (120,124),
wood floor, table, chair and simple flat roof. Stock materials are placeholders,
not a completed Swedish facade. No actual Getaboda data or private interior.

One 300-square authoring cell overlaps four 256-square runtime cells. Export includes
0_0, 0_1, 1_0, 1_1 lotheaders, world_*.lotpack and chunkdata_*.bin: 12 files.
Packager checks LOTH v1 signatures, 8x8 dimensions and required nonempty files.
It does not validate every LOT byte or certify runtime compatibility.
`42/mod.info`, `common/media/maps/`, map.info and absolute-coordinate spawnpoint
(posX=121,posY=124,posZ=0) use the
[TIS versioned design](https://theindiestone.com/forums/topic/72103-tidy-up-time/)
and installed game's spawnpoint examples. Menu selection was verified after the shared-directory fix below.

Generated: build/m0 and final build/package-m0-r3 (Git ignored). Installed:
`C:\Users\rober\Zomboid\mods\ZombieProjektetM0`. Activated for the authorized test; only this test mod is enabled.
ZIP excludes graphics PNGs, TileDefs, game code and editor binaries.

## Acceptance

| Criterion | Evidence / status |
|---|---|
| Exact stable version | Fresh startup log: 42.21.0, default Steam branch |
| Tool startup/source load | Verified in official WorldEd |
| B42 binary export | Verified, final export without errors |
| Reproducible source/package | Automated; manual export documented; second developer pending |
| Mod discovered / separate world selectable | PASS after shared-directory fix, real game UI |
| Spawn, ground, road | PASS, second fresh save with indoor spawn |
| Door and entering/leaving | PASS, open/close inside, walk outside and back in |
| Direct wall collision / roof behavior | Not established by this smoke test |
| Interior visibility | FAIL with closed door: windowless/unlit room becomes black; visible with door open |
| Critical map loading errors | No crash or critical map-load error observed; warnings discussed below |
| Human screenshot/log | Agent screenshots/log captured; human acceptance pending |

Checks: python -m unittest discover -s tests -v (11 tests),
python tools/check_agent_setup.py, python tools/render_dashboard.py --check,
git diff --check. Tests do not establish gameplay acceptance.

## Rights and automation follow-up

Official tools retain bundled GPL/BSD/Qt notices. Tiles are proprietary TIS assets
for local mapping, not MIT artwork; neither graphics nor downloaded archives are
redistributed with our code. Our layout is original. No geodata imported.

[Unjammer/PZ_Mapping_Tools](https://github.com/Unjammer/PZ_Mapping_Tools),
source 70e8b77 (2026-09-27), inspected: GPL-2.0 (or later where stated), BSD library,
Qt5 and component-specific notices. Docs/source describe OSM generation, native
256-cell projects, Lua building automation and LOT export. No unofficial executable
was installed or run; functionality and generated OSM quality are unverified.
Evaluate a small synthetic example there after M0 before creating our own exporter.
Existing Python style manifests remain design data only.

Next: [human playtest](../PLAYTEST_M0.html). Direct wall collision, roof behavior,
lighting improvement and human acceptance remain. Keep M0 and Issue #2 open.

## Review and remaining risk

Reviewed the source/metadata, generator, package allowlist, tests and human docs
against Issue #2: no full GIS pipeline or unverified custom binary exporter added.
Both generation and packaging refuse existing output directories. Tests cover
repeatability, room coordinate units, doorway placement, legacy header rejection,
missing export refusal and exclusion of external TileDefs. Source assets remain
external references. Agent gameplay evidence follows; it does not close the human acceptance gate.

Startup baseline also logged SQLITE_ERROR (8 values for 7 columns) and a Lua color
warning before this mod was enabled. These are not attributed to the test map;
if a new test save is blocked, inspect the fresh log before changing old user data.

## Agent-driven game test (2026-10-17)

The creator authorized Codex to operate the real game and capture screenshots.
This is real runtime evidence, not a human playtest or Python-only verification.
Fullscreen did not accept automated mouse input reliably. Options were backed up
outside the Steam installation and the game restarted at 1280x720 windowed.

Initial runtime checks: mod discovery and activation PASS; original package's
separate-world selection FAIL. Root cause confirmed from installed 42.21.0
MapGroups.class: createGroups checks common/media/maps and continues to the next
mod when it is absent, before scanning the version directory. Adding the empty
common/media/maps directory immediately made a second, separate world selectable.
Regression assertion added to ZIP contents. No vanilla lots dependency was added.

First new Sandbox save: 2026-10-17_09-13-38, zombies None. World loaded in 23 seconds;
player spawned on authored path, grass and road rendered. Original outdoor spawn
at (118,124,0) logged the expected no-room warning and the default randomized house
door was locked. Context menu explicitly reported Door Is Locked. Move the spawn
inside the authored livingroom to (121,124,0), allowing normal inside-door opening;
no unlocking cheat or new game mechanic. A regression test checks spawn-in-room.
Second fresh Sandbox save: `2026-10-17_09-20-56`, character Mickey Bowles,
Custom Occupation, zombies None. Fresh console reports loading took 10 seconds;
no no-room spawn warning. Player starts indoors. Initial scene is black inside
the house. Opening the door through its context menu makes the floor, walls,
player, table and chair visible. Walk to successfully leaves through the doorway
onto the path and returns inside. Close Door works and reproduces the black room;
Open Door restores visibility. The house currently has no windows/light objects;
the precise engine lighting cause has not been isolated. Do not claim the dark
interior is fixed. Direct wall pushing and roof visibility from outside were not
independently verified. No combat, zombie balance or multiplayer test was run.

Fresh log includes baseline font/script messages and a warning that M0Sweden has
no objects.lua (this minimal map has no authored zones). No map-load crash,
exception or critical LOT loading error was observed during this test. Full log
preserved outside Git as work/playtest/second-map-console.txt in the task workspace.

Game left running, paused with door open in the second save, at 1280x720 windowed
for immediate user testing. Original display options backup is retained at
work/playtest/options-before.ini in the task workspace; fullscreen was not restored
because that would interrupt the ready test. No original saves were removed.

Screenshots retained as task outputs: 01-testmod-aktiverad.png,
02-kartval-fore-fix.png, 03-separat-testvarld.png, 04-startposition.png,
05-dorren-last-fore-startpunktsfix.png, 06-inomhus-renderingsfel.png,
07-inne-oppen-dorr.png, 08-utanfor-huset.png, 09-tillbaka-inne.png,
10-pausat-infor-ditt-test.png. These are raw game captures, not concept images.
The second-save source fixes are packaged in build/package-m0-r3; exported lots
are unchanged from the successfully loaded WorldEd export.
