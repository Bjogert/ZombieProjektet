# Rural showcase — game evidence

## Scope and artifact

The creator requested a convincing complete fictional countryside plot on
2026-10-18, replacing real Getaboda likeness as this test's immediate goal.
This is one playable composition, not the completed geographic V1 or a complete
building catalogue. Creator visual acceptance is separate from technical QA.

Source: `assets/buildings/rural_cottage_01.tbx` and
`assets/gardens/rural_plot_01.json`. The 6 x 10 dwelling has a pale yellow
clapboard exterior, divided-light white windows and a two-slope gable roof.
The plot adds a furnished timber deck, barbecue, foundation planting, shrubs,
separate garden seating, bird bath, bin, wood storage, crates, picket boundaries,
clear approaches and stock conifers beyond the maintained lawn.

The template uses vanilla tile references only. No game artwork, restricted
geodata or real-house imagery is included. The house/garden/export tools are
existing code; the only packaging change adds the separate `rural` profile.

Tested artifact: `build/rural-showcase-r5/package/ZombieProjektetRural.zip`.
SHA-256: `6db8488b265ecc40f7535a943bd1730175f1ea536ba57561e06537b78584bd45`.
Installed mod ID: `ZombieProjektetRural`; map: `RuralShowcase`.
Game: **42.21.0, 4a0e9546ec, Steam**.

## Source follow-up — 2026-10-23

Source revision `05b9948` refines the accepted composition: a smaller service
pad, a separate paved seating area, less regular shrub/flower groups and a more
furnished interior. It preserves the dwelling geometry, roof, openings and deck.
See [source checks and exact placements](../assets/gardens/RURAL_PLOT.md).
The optional rural probe now checks both tiles of the moved wood stack.

The next authoring input is `build/rural-showcase-r6/authoring/cottage.pzw`.
It still requires official export, a fresh test save, interaction/visual checks
and clean restart/reload. The r5 package, screenshots and runtime results below
remain the last verified playable artifact; they do not validate this follow-up.
Inspect table/wardrobe seams, chair facing, containers, bed, switches and all
window approaches as well as the revised garden before requesting creator review.

The clean worker checkout passed 72/72 tests. The canonical working directory
ran 72 tests with one failure in the pre-existing local edit to
`assets/buildings/cottage_rotations/cottage_270.tbx`: the ceiling layer is not
found where `test_all_variant_sources_keep_ceiling_furniture_and_room_counts`
expects it. That path is unchanged by this delivery; the tracked version passes
the same test. Preserve the local file and backup and investigate the editor
representation before altering it. Do not report the canonical suite as green.
Local evidence: `build/rural-showcase-r6/evidence/lead-checks.txt` and
`worker-source-checks.json` in the same directory.

## Build and export (r5 evidence)

From the repository, with the locally installed official tools/tiles:

```powershell
python -m tools.build_cottage --output build/rural-showcase-r5/authoring --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid" --cottage assets/buildings/rural_cottage_01.tbx --garden assets/gardens/rural_plot_01.json
```

Open the generated `cottage.pzw` in official WorldEd and run Generate Lots 8x8,
All Cells, at world origin 0,0. The export reports one building, three rooms,
three room rectangles and eight room objects. The existing cottage metadata
validator passes with 60 indoor squares; no metadata repair is required here.
Then package with:

```powershell
python -m tools.package_m0 --export build/rural-showcase-r5/authoring/export --output build/rural-showcase-r5/package --profile rural
```

Use a new output directory when repeating the build. Install only into the
separate local mod folder and start a new save when exported geometry changes.
Earlier fixtures and valuable saves are preserved.

## Visual defect found and repaired

The r1 build used an oversized white window variant. Replacing it with the
smaller divided-light variant in r2 exposed a second issue: the compact wall
palettes only defined the default window opening. These newer windows require
numbered opening variants. WorldEd exported the glass but omitted the wall
around it. Counting seven window objects did not detect this visual defect.

Revision r3 includes the matching official opening references in both wall
palettes. The export now contains `walls_exterior_house_07_120/121` and
`walls_interior_house_07_24/25`. The optional read-only rural probe also checks
that all seven window positions have their surrounding wall. r1/r2 are
diagnostic builds, not deliverables.

The r3 exterior inspection exposed missing foundation plants along the south
and east lot boundary. Moving them to the map's `0_Furniture2` layer in r4 did
not fix it: both new runtime planting checks failed. The building composite
replaces underlying map content at that edge. In r5, twelve exterior planting
tiles are therefore authored in the building's own `Furniture` grid; north/west
planting remains in the garden JSON. All adjacent window landings remain free.
The unsuccessful secondary-layer code change was removed. r3/r4 are retained
as diagnostic evidence only.

## Verification status

Fresh r5 save `2026-10-18_20-21-58` loads with Custom Occupation, no zombies and
a noon July start chosen through the normal sandbox menu. All **23/23** read-only
runtime probes pass: four wall collisions, entry/outdoor clearance, 60 ceiling
and indoor squares, three doors, seven windows, three switches, 32 deck squares,
five prop/boundary references, clear front approach, boundary collision, seven
free window landings, seven surrounding window walls and visible planting
at both the south/east foundation edges. The interior is visible
with the entrance closed; the repaired windows now have continuous wall above
and below them. Normal door opening and walking across the deck to the road pass.
The boundary planting is now also visually present in the fresh r5 save.
The game was closed normally, both optional QA scripts removed and the original
default mod selection restored byte-for-byte. All 16 installed files match the
clean package. A full Steam restart and Continue reload the same save with its
own rural mod selection. Planting, roof, props and normal walking persist; the
game is left paused beside the deck for the creator.

The reload console contains no QA markers or exceptions. It still reports
existing font-texture, fluid-container-name and Piano-recipe diagnostics, plus
the expected missing `RuralShowcase/objects.lua` warning: this bounded visual
fixture does not yet author map zones. This is not survival/zoning acceptance.

Earlier r1/r2 probes passed 20 checks, but those results did not establish visual
acceptance because of the window defect above.

The Python suite passed 72 tests with the existing local geodata dependencies
on `PYTHONPATH`. Agent setup, dashboard marker checks and `git diff --check`
also passed during development. These checks do not substitute for game QA.

Local evidence is retained under `build/rural-showcase-r5/evidence/`:
`console-qa.txt`, `console-clean-reload.txt`, `overview.jpg`,
`foundation-detail.jpg`, `indoor-closed-door.jpg`, `clean-reload.jpg` and
`deck-after-reload.jpg`. Screenshots are unedited captures of the running game.
The source diff adds a separate package profile, original TBX/JSON composition
and optional read-only probes; it does not add replacement gameplay systems.

## Reuse

The dwelling and garden are separate authored inputs to the existing exporter,
with twelve boundary plants kept in the dwelling composite for reliable export.
Deck furniture, service storage and planting groups can seed later plot variants.
Vary their position and density deliberately; copying this entire arrangement to
every house would recreate the repetition this showcase is intended to address.

## Creator playtest

The running game is paused. Press the top-right play triangle to resume.
After closing the game, use Continue or Load the sandbox save
`2026-10-18_20-21-58`. It has no zombies for this visual inspection. The separate
mod is already installed; the previous test mods and saves remain intact.
Walk the road, deck and garden and enter through the deck door. Normal PZ
cutaway hides nearby walls/roof while approaching or entering the house; the
overview was captured farther away with the whole gable roof visible.

## Limits

This first composition is reviewed at orientation 0; other rotations need
their own visual checks, especially for multi-tile objects. The generic interior
is still basic. Stock white pickets and conifers are approximations; a Swedish
red fence with light tops, fieldstone boundary, garage, chimney and richer
interiors remain separate additions. No external asset-mod dependency is needed
for this first proof. Multiplayer, survival balance and vehicle clearance are
not established by this plot inspection.

Visual follow-up should reduce the regular shrub spacing and repeated flower
colours, soften the large straight gravel areas, and enrich the entrance and
interior. These are visible limitations of the first composition, not verified
likeness to a real Swedish property. Creator visual acceptance remains open.
