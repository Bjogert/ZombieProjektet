# Local road pipeline — PIPELINE-01

The maintained `tools/road_extract.py` replaces the ignored extraction experiment
for the current bounded corridor. It performs no network requests and prints no
raw geometry. Source files, registry coordinates and derived geometry remain
local under [DATA_AND_RIGHTS](DATA_AND_RIGHTS.md).

## Input contract and execution

Use a frozen local OSM PBF and JSON registry with `dataset_id`, `url`, `snapshot`,
`sha256`, `license` (`ODbL-1.0`), `attribution`, two ordered `place_node_ids`,
`bounds_epsg3006` (west/south/east/north, at most 30km per axis) and `max_snap_m`
(at most 200m). The current ignored registry is `build/road-source/registry.json`.
The expected hash must come from the registered acquisition, not silently refresh
to match whichever file happens to exist. The public latest URL is mutable.

Optional dependencies are pinned in `requirements-geodata.txt`. This machine
already has the tested versions in the following local dependency directory:

```powershell
$env:PYTHONPATH = 'C:/PZModding/ZombieProjektet/build/municipality-draft/python-deps'
python -m tools.road_extract --source build/municipality-draft/raw/kronoberg.osm.pbf --registry build/road-source/registry.json --output build/road-pipeline-r2
```

Use a fresh output directory. `corridor.json` feeds the existing road or roadside
generator. `provenance.json` records the registry, input/output hashes, library
versions, way IDs, length, snap distances and exclusions. Neither file belongs in
public output by default. Official WorldEd export and mandatory packaging checks
remain separate commands; extraction does not install a mod.

## Routing and explicit limitations

The command projects longitude/latitude to SWEREF 99 TM using `always_xy=True`.
It routes by length over shared OSM node IDs and preserves ordered segment and
way identity. It applies way-level motorcar/motor_vehicle/vehicle/access
precedence, explicit one-way direction, and implied roundabout/motorway direction.
Conditional/directional access it cannot interpret is excluded. Bridges, tunnels,
nonzero layers and fords require separate support and are excluded.

Entire incomplete ways are excluded; no shortcut joins across a missing node.
The result reports incomplete ways with known points near the selection and
those outside its known bounds. Missing access tags remain uncertainty. Node
barriers and turn-restriction relations are **not evaluated**: this is a bounded
map prototype selector, not legal navigation or verified public access. Coverage
gaps can hide a shorter/different route. Review those limits before expanding to
a new region. Widths remain provisional 5m/7m design values; source tags are
preserved separately. Missing surface is explicit and falls back to the existing
provisional asphalt treatment in the map generator.

## Local reproduction on 2026-10-18

Same registered OSM France Kronoberg snapshot as [ROAD_TEST](ROAD_TEST.md):
`2026-10-17T01:27:19Z`, SHA-256
`4d459da057e3c0132f879177947295dc4b208e9698460377f7a1c378aa0327c8`.
No new source download or cloud upload was used.

- **152 ordered segments, 5,087.54654m**: coordinates, IDs, widths, surfaces and
  endpoints exactly match the previous corridor; same four source ways.
- Repeated extraction produces byte-identical corridor/provenance files.
- Regenerating the integrated cottage/garden map produces **108 byte-identical
  official authoring inputs** (TMX/PZW/PNG/TBX) compared with the earlier fixture.
  Manifest provenance changes as expected; the map geometry does not change.
- The selection excludes 12 ways for access and 45 unsupported crossings. It
  records one incomplete way near the selection and 65 outside known selection
  bounds. None is partially used. All 152 selected segments lack explicit access
  tags; all have surface tags. These are source limitations, not surveyed facts.
- Synthetic tests cover projection/axis order, immutable input, repeated output,
  checksum and registration failures, connectivity, equal-length ordering,
  direction/access precedence, crossings, missing attributes/locations and bounds.

Evidence: ignored `build/road-pipeline-r2/`, `build/road-pipeline-r2-repeat/`,
`build/road-pipeline-r1/verification.json` and `build/roadside-pipeline-r1/`.
The raw source is unchanged. The 5.09km continuous-driving gate remains open.
