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

This first composition is authored and reviewed at orientation 0. Other
orientations, particularly multi-tile props, need individual visual verification
before use. This is a reusable source template, not an automatic assignment of
this garden to all real-world buildings.

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
