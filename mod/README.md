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
See [editor setup and evidence](../docs/test-reports/M0-BUILD42.md) and
[HTML playtest instructions](../docs/PLAYTEST_M0.html).
