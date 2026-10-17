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

`tools.garden_source.garden_layers(template, origin)` translates the layout to a
house origin, validates bounds/overlap/access, and returns new terrain layers.
The cottage builder accepts `--garden assets/gardens/cottage_garden_01.json` and
keeps the source TBX unchanged. Omitting the option preserves the bare cottage.
See [the game test report](../../docs/GARDEN_TEST.md) for export and installation.

For Getaboda, first establish permitted source geometry and each house's actual
orientation/entrance. Then choose and adapt a garden layout as a separate design
layer. Flower colors, bed lengths, furniture and deck size can be edited here
without changing the house model or geographic source. Unknown real gardens must
remain labeled as design assumptions.

Translation is implemented and tested at two origins. Rotation, fitting arbitrary
house sizes/parcels and connecting stable-ID overrides to playable garden output
are not yet implemented. Do not automatically attach this identical garden to
every house. No proprietary tile artwork or real geodata is stored here.
