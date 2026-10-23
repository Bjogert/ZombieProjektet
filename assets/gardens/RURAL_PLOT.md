# Rural plot 01

Original fictional layout authored for `docs/specs/rural-showcase.md`. It is not
a real address or a reconstruction from source imagery. The dwelling source is
`assets/buildings/rural_cottage_01.tbx` (6 x 10 squares).

All tile names reference the player's local vanilla resources. No game artwork
is included. The local official 2026-09-16 tiles were inspected before choosing
the pale yellow clapboard, matching gable caps, white-framed windows, timber deck,
picket fence, planting, barbecue, seats, wood stack, bin and storage references.
The stock conifers are a visual woodland approximation, not a Swedish species
classification. The white pickets do not implement the proposed red/white fence
or a fieldstone wall.

`rural_plot_01.json` stores local offsets from the house's northwest square.
Each patch is labelled by purpose. The existing garden assembler rejects overlaps
with the dwelling, same-layer duplicates and objects on reserved routes. Window
landings and the two-square entrance approach are reserved individually; there
is deliberately no empty ring around the house. Flowerbeds touch blank sections
of the facade.

Twelve foundation plants at the south/east edge live in the TBX's exterior
`Furniture` tile grid. WorldEd's building lot replaces underlying map content
at that boundary, including plants on a second furniture layer. North/west beds
remain in the garden JSON. Treat the TBX and garden as a paired composition;
keep the window landings free when editing either. r3/r4 exposed this boundary
problem and are diagnostic builds, not distributable showcase artifacts.

The r5 composition was reviewed in-game at orientation 0. The source refinement
below still needs fresh official export and game inspection. Other orientations,
particularly multi-tile props, need individual visual verification before use.
This is a reusable source template, not an automatic assignment of this garden
to all real-world buildings.

Build with `python -m tools.build_cottage`, passing the rural TBX and JSON to
`--cottage` and `--garden`. Use the existing official WorldEd Generate Lots 8x8
workflow at world origin 0,0 and `tools.package_m0 --profile rural`. The output
uses its own `ZombieProjektetRural` mod and `RuralShowcase` map. Always start a new
save when changing the exported map.

The white divided-light windows require the numbered `WestWindowN` and
`NorthWindowN` opening references in both wall palettes. A palette with only
`WestWindow` / `NorthWindow` exports the window object but can omit its surrounding
wall. The showcase therefore includes the official matching opening references;
visual checks must inspect the wall below and above each window, not only count
window objects. Earlier r1/r2 builds are diagnostics and must not be distributed.

## Source refinement — 2026-10-23

This bounded follow-up keeps the approved r5 dwelling, roof, openings and deck.
It is source work for RURAL-SHOWCASE-01; the r5 runtime results do not validate
these new placements.

- Replace the 15 x 4 rear gravel yard with a 4 x 4 service pad at `(8,12)`,
  a small rear garden entrance and a narrower rear path with a grass shoulder.
  Gravel within the plot falls from 114 to 70 squares, excluding the lane.
- Give the existing garden seats an eight-square paving area at `(2..4,14..16)`
  with one omitted corner. Lawn and a small planting group separate it from
  service storage. The 32-square timber deck remains intact.
- Group narrow and round shrubs asymmetrically, with paired flower colours
  instead of a repeating three-colour border. An entrance planter at `(-1,5)`
  leaves both entrance rows clear. All twelve south/east foundation plants
  remain in the TBX, with their original occupied squares and free window gaps.
- Complete the existing two-square dining table and add a second dining chair,
  armchair, bookcase, wardrobe, bedside cabinet and houseplant. Move the bed
  north one square so the south bedroom window's inside landing `(2,9)` is free.

Coordinates below are local to the house's northwest square, at orientation 0.
The wood stack now occupies `(10,14)` / `(10,15)` (`camping_01_26/27`), and the
crates occupy `(11,14)` / `(11,15)`. The bin remains at `(10,13)` and the bird bath
at `(4,19)`. Update the lead-owned wood-stack runtime probe from `(7,9)` to
`(10,14)` before testing this revision.

The table is the complete official W entry: `furniture_tables_low_01_001` at
`(3,3)` and `_000` at `(3,4)`. Chairs are at `(2,3)` and `(4,4)`. The wardrobe is
also a complete W entry: `furniture_storage_01_057` at `(0,8)` and `_056` at
`(0,9)`; `_056` alone is not the full wardrobe. The bed occupies `(2,7..8)`, with
the cabinet at `(3,7)`. The armchair, bookcase and plant occupy `(0,5)`, `(0,0)`
and `(1,0)` respectively. References and furniture groups were checked against
the installed official 2026-09-16 Tiles and `BuildingFurniture.txt`; no artwork
or tool definitions are copied into the repository.

Source checks pass for all four garden rotations, deterministic assembly,
169 local tile references, valid complete furniture entries and no overlapping
interior furniture squares. A conservative four-neighbour walkability check
using room boundaries and the three doorway edges reaches all 43 unoccupied
interior squares and all seven inside window landings. The 6 x 10 room geometry,
60-square ceiling, gable roof, wall palettes, three doors, seven windows and
three switches are unchanged. These checks cannot establish engine collision
or interaction behavior.

The existing 72-test suite passes with the installed GIS dependencies on
`PYTHONPATH`; agent setup, dashboard markers and whitespace checks also pass.
Two runs of `tools.build_cottage` produce byte-identical authoring files and
preserve the supplied TBX. Neither authoring build is a compiled game export.

Fresh manual QA must inspect the table and wardrobe seams, chair facing,
container access, bed access, switches, the two-wide entrance, every window
from both sides, foundation planting, the new service pad and the separate
garden seats. Inspect the full gable roof from outside, then restart and reload
the fresh save without optional QA. Rotated visuals and survival zoning remain
outside this source-only result.
