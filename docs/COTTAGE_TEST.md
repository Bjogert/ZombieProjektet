# Representative cottage test — COTTAGE-01

**Developer evidence; contains synthetic test layout details.**

## Artifact and toolchain

- Original source: `assets/buildings/swedish_cottage_01.tbx`, fictional 6 x 10 cottage.
- Official mapping tools: 2026-09-16 Windows distribution, already installed locally.
- WorldEd: Generate Lots 8x8 / All Cells, origin 0,0, one thread, installed game's
  `media/newtiledefinitions.tiles`; export completed with 1 building, 3 rooms,
  3 room rectangles and 8 room objects, without an export error dialog.
- Package: `build/package-cottage/ZombieProjektetCottage.zip`.
- SHA-256: `fc40c3b5060d3c62e9611c4c3db5259433d15d75b6287fd62fb4ae39ef27f6dc`.
- Separate local installation: `%USERPROFILE%/Zomboid/mods/ZombieProjektetCottage`.
  M0 remains installed. Select only the cottage map mod for this test.
- Runtime target observed in the menu: 42.21.0, `4a0e9546ec`, Steam.

## Reproduce the authoring and package

Run from the repository root, choosing fresh output folders:

```powershell
python -m tools.build_cottage --output build/cottage --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid"
```

Open `build/cottage/cottage.pzw` in WorldEd, select the world tab, then File →
Generate Lots 8x8 → All Cells. The generated PZW supplies the export folder,
black zombie-density image and read-only TileDef folder. Accept the settings.
After the completion dialog:

```powershell
python tools/package_m0.py --export build/cottage/export --output build/package-cottage --profile cottage
```

The original TBX is copied into the build directory and interpreted as a separate
lot by WorldEd. The generated terrain contains no replacement M0 house. Only
original layout and tile names are committed; no proprietary artwork or TileDefs.
WorldEd's previous unsaved M0 settings were preserved in the ignored local
`build/m0-lighting/m0-session-backup.pzw` before opening the cottage project.

## Checks

Automated source/package checks pass. Independent read-only review found no
blocking code findings and verified M0 TMX output byte-for-byte against `b24eedd`.
The tests cover deterministic terrain, unchanged source TBX, separate lot and
package identities, required common map directory and output protection.

The 24-test Python suite, agent setup check, overview marker check and diff
whitespace check pass. These checks do not establish game behavior.

## In-game results (2026-10-17)

Fresh Sandbox save: `2026-10-17_18-49-33`, Custom Occupation, no zombies, only
`ZombieProjektetCottage` enabled. M0 and earlier saves were retained.

| Check | Observed result |
| --- | --- |
| World selection and indoor spawn | Pass in 42.21.0 (`4a0e9546ec`) |
| Entrance | Opened inside, walked out, closed/opened outside, walked back in |
| Closed-door daylight | Floor, walls and furnishings visible with the entrance closed |
| Living-room light switch | Turned on and off; room tint changed and context action changed between Turn off / Turn on |
| Living-room window | Opened and closed; context action changed between Close Window / Open Window |
| Furnishings | Bed, fridge, stove, toilet and living-room furniture rendered |
| Wall collision | All four wall-edge probes blocked movement |
| Open space | Entry interior and outdoor-path probes returned clear |
| Ceiling and indoor classification | All 60 occupied squares have an upper floor and are indoors |
| Runtime objects | 3 doors, 7 windows and 3 light switches |
| Roof appearance | Pitched roof rendered from the front/outside; walls/roof fade when needed for player visibility |
| Save/exit | Window closed normally; log records saving and GameThread exit; save database updated |

`tools/qa_cottage.lua` supplied the 11 read-only runtime probes at game start.
All printed PASS. It was temporarily installed under the test mod's
`42/media/lua/client/`, removed after testing, and never included in the ZIP.
Manual UI observations establish the interaction/appearance results separately.
One window and one light switch were operated; the counts do not prove every
window/switch, appliance, loot table or interior door interaction.

An independent read-only reviewer checked the saved logs/screenshots, package
hash, test-source copy and all 16 installed files against the ZIP after probe
removal. No blocking evidence or code findings remained. This is review of the
lead's saved evidence, not a second independent run of the game.

Local evidence is retained under the ignored `build/cottage/evidence/` folder:
`worlded-export.png`, `closed-door.png`, `exterior.png`, `light-on.png`,
`light-off.png`, `window-open.png`, `window-closed.png`, and `console-final.txt`.
The console includes baseline font/texture/fluid warnings and a missing
`CottageTest/objects.lua` warning: this small test map has no authored zones.
No runtime exception or failed cottage QA probe was observed during this test.
This is a load/interaction test, not a full survival, zoning or multiplayer test.

## Fresh playtest

Enable **ZombieProjektet - Swedish cottage test**, start Solo → Custom Sandbox,
select the cottage test world, use Custom Occupation and create a new save.
Never reuse an M0 or valuable existing save; both test maps use synthetic origin
coordinates. Start inside near the entrance, verify daylight with the door closed,
light-switch response, doors, a window and the exterior roof.

Creator acceptance and approval of the provisional stock exterior palette remain
open. This prototype does not represent Getaboda or prove style override
persistence in generated playable maps.
