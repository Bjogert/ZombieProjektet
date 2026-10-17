# Cottage deck and garden test — COTTAGE-02

## Tested artifact

- Original fictional garden: `assets/gardens/cottage_garden_01.json`.
- House: unchanged `assets/buildings/swedish_cottage_01.tbx`, 6 x 10 tiles.
- Authoring output: `build/cottage-garden-r2/` (the earlier unexported folder was
  superseded after moving the northern flowerbed clear of the corner route).
- Official mapping tools: 2026-09-16 Windows distribution.
- WorldEd Generate Lots 8x8 / All Cells, origin 0,0, one thread, installed game
  TileDefs. Export completed with 1 building, 3 rooms, 3 room rectangles and
  8 room objects; no export error dialog.
- Package: `build/package-garden/ZombieProjektetGarden.zip`.
- SHA-256: `af337be87358d24b6a524d1e9233de48ea3b9a3155abef149e155c2c9ef5c034`.
- Installation: `%USERPROFILE%/Zomboid/mods/ZombieProjektetGarden`.
- Game: Steam 42.21.0, `4a0e9546ec`, observed in menu and screenshots.
- Fresh Sandbox save: `2026-10-17_19-50-42`, Custom Occupation, no zombies,
  only `ZombieProjektetGarden` enabled. Previous M0/cottage mods and saves retained.

## Reproduce

Run from the repository root, choosing output folders that do not already exist:

```powershell
python -m tools.build_cottage --output build/cottage-garden-r2 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid" --garden assets/gardens/cottage_garden_01.json
```

Open the generated `cottage.pzw` in WorldEd. Use File → Generate Lots 8x8 →
All Cells with the supplied export folder and TileDef folder. After completion:

```powershell
python tools/package_m0.py --export build/cottage-garden-r2/export --output build/package-garden --profile garden
```

Copy the generated `ZombieProjektetGarden` directory into the user's Zomboid
mods directory. Enable **ZombieProjektet - Cottage garden test**, choose Solo →
Custom Sandbox and the cottage garden world, then Custom Occupation and a new
save. Do not combine the synthetic M0/cottage/garden maps in one save: they use
the same origin. Existing valuable saves must not be used for this experiment.

The bare cottage command still works without `--garden`; its terrain is unchanged.
Only original layout data and stock tile references are committed, not game art.

## Automated and editor evidence

All 28 Python tests pass, as do the agent setup, overview marker and whitespace
checks. Translation at two house origins produces the same relative layout,
without modifying the input. Tests reject house overlap, blocked reserved routes
(including corners), duplicate placement, out-of-cell rectangles, invalid tile
references and missing tile resources before output is created. The copied TBX
is byte-identical to the source. The existing bare-cottage output remains
byte-identical to base commit `5f21f17` in the independent code review.

The template reserves a continuous perimeter and entrance approach. The generator
does not infer arbitrary door/window access or understand every stock object's
collision flags; official export and actual game checks remain necessary.

## In-game observations (2026-10-17)

| Check | Result |
| --- | --- |
| World selection and spawn | Garden test world loaded; player started indoors |
| Wooden deck | 24 wooden floor squares, all classified outdoors |
| Outdoor objects | 11 flowerbed tiles, two chairs and one table found |
| Clear routes | All 36 perimeter edges and five entrance-approach edges returned clear |
| Furniture collision | Moving toward the table's occupied square returned blocked |
| Cottage regression probes | Four walls block; entry/path clear; all 60 room squares indoors and ceiling-covered; 3 doors, 7 windows, 3 switches |
| Door and walking | Opened entrance inside, walked across deck, re-entered and exited, walked around gable/long side/northern corner, returned to deck and closed entrance outside |
| Visuals | Wooden planks, white outdoor furniture, three colored flowerbeds and shrubs rendered; pitched roof rendered from the exterior |
| Save/exit | Closed normally; final log records saving and `GameThread exited.` |

`tools/qa_garden.lua` and `tools/qa_cottage.lua` were temporarily installed in
the test mod's `42/media/lua/client/`. They only read runtime state. All seven
garden and eleven cottage probes printed PASS. They were removed after the
game exited and were never in the ZIP. All 16 installed files then matched the
ZIP byte-for-byte, with no extra files.

An independent read-only reviewer verified the saved log, screenshots, package
hash, installed-file parity, unchanged TBX and retained previous saves/mods,
with no blocking findings. This reviews the lead's evidence; it is not a second
game reproduction. Chair presence is counted; chair collision was not separately
probed, while table collision was.

Local evidence is in the ignored `build/cottage-garden-r2/evidence/` directory:

- `worlded-export.png`: official export completion.
- `roof-and-flowerbeds.png`: exterior roof and gable planting.
- `garden-layout.png`: garden arrangement with the game's wall/roof cutaway.
- `deck-and-flowers.png`: closer deck, furniture and flowerbed view.
- `console-final.txt`: runtime probes, baseline warnings and clean exit.
- `default-mods-before.txt`: previous mod-selection configuration.

The game hides walls/roof where needed for player visibility; the cutaway images
do not mean the roof was removed. Stock font/texture/fluid/Lua warnings remain,
as does a missing `CottageGardenTest/objects.lua` warning because this test has no
authored zones. No runtime exception or failed QA probe was observed. This is not
a full survival, erosion, seasonal-growth, gardening, seating-animation or
multiplayer test. Light/window interactions were proven in COTTAGE-01 and were
not repeated here; this run checks the unchanged house structure and entrance.

## Reuse and remaining work

The [garden source guide](../assets/gardens/README.md) explains relative placement.
The deck, surfaces and planting are a separate layer around the unchanged house.
They can be translated and edited without altering house or geographic source.
Real Getaboda dimensions, orientation, entrances and permitted source data must
guide later adaptation. This fictional garden is not evidence about any property.

Rotation, fitting arbitrary footprints/parcels and connecting stable-ID garden
choices to playable generation remain future work. The existing style-override
manifest is separate. Creator approval of the stock exterior and landscaping,
and independent reproduction in the game, remain open.
