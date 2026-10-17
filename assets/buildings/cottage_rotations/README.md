# Reviewed orientation sources

These original rectangular cottage layouts extend `../swedish_cottage_01.tbx`
without replacing the earlier tested fixture. Angles are clockwise in map
coordinates: 0 has its entrance west, 90 north, 180 east and 270 south.

The starting source now includes explicit W/N/E/S entries for every furniture
group. The former single tile from a two-tile living-room table is replaced by a
complete one-tile wooden table (stock indices 2/3). All other furniture types,
room sizes, openings and roof dimensions retain the original design.

## Authoring workflow

1. Complete the starting file's directional tile references using the installed
   official BuildingEd furniture catalog. Do not copy artwork into this folder.
2. Open the source in BuildingEd. Use **Building > Rotate Right**, then **Save
   As** a distinct angle file. Repeat for the other orientations. These variants
   were authored with the installed official 2026-09-16 tools.
3. Rotation removes user-painted tile layers. Restore the four white corner
   posts in the ground-floor `WallTrim` and all 60 ceiling squares in the upper
   `Floor` layer. TBX tile grids are `(width+1) x (height+1)`; the extra east and
   south edges have no ceiling tiles. Corner tiles remain selected by their
   world-facing corner rather than by the pre-rotation sprite orientation.
4. Run `python -m unittest tests.test_placement_source -v`, re-export the
   separate four-house fixture with official WorldEd, then test a fresh game
   save. Inspect furniture facing, entrance traversal, switches, roofs and access.

The generator selects these saved sources by template and angle; it does not
rotate arbitrary TBX files. Editing one file does not automatically update the
other three. Regenerate and recheck all variants after changing the base design.
The previous cottage source is retained for reproducing older test evidence.

The inspected upstream [PZW writer](https://github.com/timbaker/pzworlded/blob/4da5e78969dfeb27d913305fe5b7ea28eecad2c8/src/editor/worldwriter.cpp#L242-L260)
has no lot rotation property. [BuildingEd rotation](https://github.com/timbaker/tiled/blob/9ef277c19e10e9798a2a041302615e35434ace15/src/tiled/BuildingEditor/buildingeditorwindow.cpp#L2189-L2236)
clears painted layers; the installed editor also displayed that warning. These
source references explain the workflow, not a claim that upstream and installed
binary commits are identical.

No raw geographic data, proprietary art or editor/game code is included.
