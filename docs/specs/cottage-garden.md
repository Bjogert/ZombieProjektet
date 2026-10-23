# Cottage deck and garden — COTTAGE-02

Add a ground-level wooden deck, a small seating group and flowerbeds to the
fictional cottage. Keep the entrance, windows and a route around the house clear.
Use original layout data referencing permitted stock tiles. No real geodata or
proprietary images are included.

Store the outdoor layout in `assets/gardens/cottage_garden_01.json`, with tile
rectangles relative to the house's northwest ground corner. Generate independent
terrain layers and combine them with the existing cottage terrain before official
WorldEd export. The TBX house stays unchanged. The same layout must translate to
a second origin without changing its relative arrangement or its input file.

Validate coordinates, tile references, duplicate layer placement, house overlap,
map bounds and reserved walking routes before producing output. A reserved route
allows ground surfaces but no decorative objects. Invalid placement must fail
without writing a partial map.

Automated tests cover deterministic translation, clear routes, intact house source
and rejected invalid layouts. Game verification separately covers new-save load,
wooden deck floors classified outdoors, seating collision, clear approach/walking,
flowerbed appearance and unchanged house entry. Save screenshots and exact package
identity. Preserve the previous cottage artifact and all existing saves.

This slice supports translation and editing relative layout data. Rotation,
automatic fitting to arbitrary parcels, stable-ID garden overrides, seasonal
growth and gardening gameplay are future work, not claimed capabilities. The
existing style-override manifest remains a separate experiment.
