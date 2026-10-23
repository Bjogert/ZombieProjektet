# PIPELINE-01 — reproducible local road extraction

Replace the ignored one-off corridor experiment with a maintained command. Read
a frozen local OSM PBF and a local source registry; emit the existing metric
corridor contract plus provenance into a fresh ignored output directory. No
network access, raw geometry in console output, source mutation or automatic
WorldEd export. This is one selected corridor, not a municipality importer.

The registry records dataset ID, URL, snapshot, expected SHA-256, ODbL license,
attribution, two exact OSM place-node IDs, a bounded EPSG:3006 selection rectangle
and maximum endpoint snap distance. Real coordinates remain local. Use cached
osmium 4.3.1 and pyproj 3.8.0; keep these optional geodata dependencies separate.

Select ordinary driveable highway classes and shared-node connectivity. Apply
motorcar/motor_vehicle/vehicle/access precedence, explicit and roundabout-implied
direction, and reject ambiguous conditional/directional values. Exclude bridges,
tunnels, nonzero layers and fords pending separate support. Missing access is an
explicit uncertainty, not verified public access. Missing surface uses the
existing provisional asphalt choice; all widths remain provisional (5m gravel,
7m otherwise), with original source tags retained separately.

Route deterministically by metric length with stable ID tie ordering. Bound
endpoint snaps, reject disconnected endpoints, exclude entire ways with missing
locations and report those coverage gaps (including any near the selection), preserve
way/node identity, and never infer connections at geometric crossings without a
shared OSM node. Serialize original projected endpoints with no compression.

Acceptance: synthetic tests for direction, access precedence, connectivity,
missing attributes, crossings, projection axis order, immutable inputs and
failure before output. Re-extract the registered snapshot locally, repeat for
byte equality, and compare ordered geometry/way IDs/distance with the existing
5.09km corridor. Document actual differences; do not quietly replace a different
route. Official export, packaging and driving gates remain separate.
