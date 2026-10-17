# Swedish cottage prototypes

`swedish_cottage_01.tbx` is an original, reusable BuildingEd source model: a
6 × 10 tile cottage with red-brown timber walls, light corner posts, stock windows,
a slate-coloured pitched roof and generic rooms. It represents no real property.
The stock palette is provisional, not an approved final Swedish facade.

Open it directly in the official 2026-09-16 BuildingEd with the matching Tiles
directory configured. It was loaded and visually inspected there on 2026-10-17.
Use the upper floor for the exterior preview; hide the grid and object shapes.
The ground floor contains doors, windows, three light switches and generic
living, sleeping, kitchen and bathroom furniture. The upper floor includes a
full ceiling under the roof.

This source has been exported as a separate WorldEd lot and **agent-tested in
Build 42.21.0** using the `ZombieProjektetCottage` test mod. It is not included in
M0's installed package. The [runtime report](../../docs/COTTAGE_TEST.md) records
the exact package, reproduction steps, interaction checks and remaining limits.
Creator acceptance and exterior design approval remain open.

The separate [garden template](../gardens/README.md) adds a wooden deck, outdoor
furniture and flowerbeds around this unchanged house. Its own package and game
checks are recorded in [GARDEN_TEST](../../docs/GARDEN_TEST.md).

The newer [four-orientation library](cottage_rotations/README.md) adds fully
assembled directional furniture and restored ceiling/trim layers for native
BuildingEd quarter-turns. It leaves this earlier source unchanged. Stable-ID
house and garden choices now generate a separate four-house playable fixture;
see [PLACEMENT_TEST](../../docs/PLACEMENT_TEST.md) for game evidence and limits.

The file contains original layout data and stock tile names, with no copied
textures or game code. Tile references resolve from the user's permitted game
mapping resources; the referenced artwork remains The Indie Stone's property.
