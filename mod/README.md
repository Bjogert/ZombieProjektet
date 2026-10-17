# Project Zomboid M0 test mod

`ZombieProjektetM0/` is a source skeleton. Install only the compiled package.
No game artwork or TileDefs are bundled. Layout is synthetic, not Getaboda.

From the repository root, with Python 3.12 (standard library only):

```powershell
python tools/build_m0.py --output build/m0 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid"
```

Use a fresh output directory; generation refuses to overwrite existing work.
Open `build/m0/m0.pzw` in official WorldEd. Activate **The World** tab,
then **File > Generate Lots 8x8 > All Cells**. Keep the prefilled paths,
origin `0,0`, and one thread. Do not use 10x10 export.
Expected: one building, one room, one room rectangle, two room objects,
and no Generate Lots Errors dialog. Then:

```powershell
python tools/package_m0.py --export build/m0/export --output build/package-m0
```

The ZIP contains `ZombieProjektetM0` for `%USERPROFILE%/Zomboid/mods`.
Stop if that destination already exists; do not overwrite an unknown installation.
Packager checks header signatures/chunk size and required files, not runtime correctness.
Keep `common/media/maps/.gitkeep`: Build 42.21 skips the versioned map directory
when that shared maps directory does not exist. The final spawn is indoors at
(121,124,0), so a randomized locked door can be opened normally from inside.
Agent game tests verified separate-world selection, loading, walking out/in,
daylight with the door closed and a working light switch. Runtime collision
queries block all four walls and allow clear floor/path movement. All 80 room
squares have an upper floor; the flat roof renders from outdoors. Human
acceptance remains open. The tested lighting package is `build/package-m0-r4`,
exported from `build/m0-lighting`; older saves cache the older house.

Optional diagnostics: copy `tools/qa_m0.lua` into the installed test mod's
`42/media/lua/client/` while the game is closed, then load the M0 test save.
The `[ZombieProjektet QA]` log lines query the actual loaded squares without
changing gameplay. Remove this temporary copy after QA. It is excluded from
normal packages. These checks supplement visual testing; they do not test rain,
night-time lighting after power loss, multiplayer or every possible wall edge.
See [editor setup and evidence](../docs/test-reports/M0-BUILD42.md) and
[HTML playtest instructions](../docs/PLAYTEST_M0.html).
