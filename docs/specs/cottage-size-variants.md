# Cottage dimensions needed for the Getaboda pilot

The source candidate measurements exceed the current 6 by 10 metre cottage.
Prepare a bounded rectangular variant builder using the existing authored tile
references. Keep generic interiors; dimensions are a game adaptation of estimated
outlines, not proof of real rooms or wall positions.

Support integer widths 6–12 and lengths 9–18, west entrance, three rooms and the
existing stock pitched-roof vocabulary. Resize room/floor/ceiling grids and move
doors, windows, switches and furniture coherently. Preserve the source TBX. The
fixed garden stays limited to the original 6 by 10 cottage until adapted.

First representative variant: 8 by 12 squares. It approximates the third-largest
source rectangle, about 7.7 by 11.6 metres. No exact private interior is inferred.

Acceptance: deterministic output; full room and ceiling coverage; all openings on
valid boundaries; furniture inside its intended room; invalid sizes fail before
writing. Official export must yield one building, three rooms, eight room objects
and the requested indoor area. Record an actual game test separately from source
tests. Existing cottage authoring and metadata validation defaults remain intact.

Roof regression found in the first 8 by 12 game test: a `PeakNS` roof has only
three sloped squares on each side. Increasing its width left a flat central
strip and missing gable infill. Width six keeps the tested steep peak. Wider
variants now use stock 30-degree slopes: paired slopes for even widths and the
supported odd-width ridge primitive for odd widths. No slope exceeds six
squares. The shallow red-brown wooden gable uses stock barn references; this is
a prototype palette, not verified Getaboda appearance. Source tests verify
complete non-overlapping coverage and supported primitive dimensions.

No arbitrary angles, extra floors, template stretching of roof tile art, new
mechanics or game-readiness claim from XML alone. Getaboda uses the creator-approved
45-degree world-grid rotation; geographic source coordinates remain unchanged.
