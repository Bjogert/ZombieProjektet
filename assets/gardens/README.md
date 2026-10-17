# Reusable cottage garden

`cottage_garden_01.json` is an original fictional layout for the 6 x 10 cottage.
It adds a ground-level 4 x 6 wooden deck, two chairs, a table, three flowerbeds
(11 tiles) and three shrubs using stock game tile references.

Coordinates are relative to the house's northwest ground corner. Each `rect`
is `[x, y, width, height]`; negative values place objects west or north of the
house. `0_Floor` changes ground surfaces and `0_Furniture` places outdoor objects.
`clear_routes` reserves the entrance approach and a continuous one-tile ring
around the house, including its corners. Ground surfaces may occupy these routes;
decorative objects may not.

`tools.garden_source.garden_layers(template, origin, rotation=0)` places the layout
at a house origin, validates bounds/overlap/access, and returns new terrain layers.
Rotation is clockwise in map coordinates and accepts 0, 90, 180 or 270 degrees.
The origin remains the rotated house's northwest bounding corner. Directional
furniture declares `rotation_indices` in that order; other tiles remain aligned
to the world. Reserved routes rotate with the house.
The cottage builder accepts `--garden assets/gardens/cottage_garden_01.json` and
keeps the source TBX unchanged. Omitting the option preserves the bare cottage.
See [the game test report](../../docs/GARDEN_TEST.md) for export and installation.

For Getaboda, first establish permitted source geometry and each house's actual
orientation/entrance. Then choose and adapt a garden layout as a separate design
layer. Flower colors, bed lengths, furniture and deck size can be edited here
without changing the house model or geographic source. Unknown real gardens must
remain labeled as design assumptions.

Translation and quarter-turn rotation are implemented. The separate placement
builder connects saved stable-ID choices to authoring output; see
[the contract](../../docs/specs/building-placement-tools.md). Fitting arbitrary
house sizes/parcels remains unsupported. Do not automatically attach this
identical garden to every real house. No proprietary tile artwork or real
geodata is stored here.
