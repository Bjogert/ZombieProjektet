# Road-first scale study

2026-10-17. The creator proposed starting with roads to judge world size and whether compression is necessary. This study measures the installed vanilla map and previews the mapped municipality road network. It does not select a compression ratio or claim an exported road mod.

## Installed-game comparison

Read-only inventory of `C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid/media/maps/Muldraugh, KY` found **4,065 runtime `.lotheader` cells**, x=0..77 and y=0..62. Other ordinary spawn-region folders contain no runtime lotheaders; challenge maps were excluded. Installed version: **42.21.0**, Steam build `25485521`, consistent with the prior game-test evidence.

Using the project's verified Build 42 runtime cell size of **256 squares** and the explicit comparison convention **one square ≈ one metre**:

| Measure | Installed PZ map | Ljungby municipality |
| --- | --- | --- |
| Bounding width × height | 19.968 × 16.128 km | Approximately 61.4 × 51.1 km |
| Bounding rectangle | 322.0 km² | Approximately 3,138 km² |
| Covered area proxy | 266.4 km² in supplied whole runtime cells | Approximately 2,049 km² in SCB's generalized boundary |

The dimensions differ by about **3.1× in each direction**. The covered-area proxies differ by about **7.7×**. These are planning comparisons, not exact authored or playable areas: PZ whole-cell coverage includes water, wilderness and edge padding; SCB uses a generalized municipality boundary. Neither figure measures building density. No claim is made that vanilla-map size is the engine's maximum supported size.

The [developer's July 2026 Build 42 article](https://projectzomboid.com/blog/news/2026/07/42-20-the-big-glow-up/) says the map's surface area doubled from Build 41. This is why older, unversioned online area estimates should not replace measurement of the installed version. The absolute dimensions above come from local file inventory, not that article.

## Road-network preview

Reused the locally cached OSM France Kronoberg PBF and SCB boundary from [world draft 01](ljungby-world-draft-2026-10-17.md). No additional raw geodata was sent to a cloud service. All valid mapped highway ways intersecting the generalized municipality were considered, with three display groups:

| Group | OSM ways intersecting the municipality | Sum of clipped way lengths |
| --- | --- | --- |
| Vehicle-road classes, including links, residential and service roads | 5,809 | 2,743.8 km |
| Tracks | 1,781 | 1,095.8 km |
| Other highway ways, including paths | 1,784 | 329.0 km |

These are sums of mapped geometries, not unique route kilometres: divided carriageways, access roads and paths are distinct features. OSM coverage is not proven complete. Tracks are not automatically suitable or permitted for motor vehicles. The coarse municipal boundary is suitable for this overview, not exact road-end clipping for game generation.

The county extract also contains **78 highway ways with unusable line geometry**, skipped before local inclusion could be established. They may be outside this municipality; their exclusion is recorded rather than treated as evidence of complete extraction. Before a playable corridor is generated, audit completeness and road continuity in its source buffer.

Of the 5,809 road-class ways, **5,684 (97.8%) lack an explicit `width` tag**, 4,859 lack `lanes`, and 3,343 lack `surface`. Missing attributes must be supplemented from a permitted source such as NVDB or marked as provisional design defaults. They are not verified measurements.

## Recommended bounded road test

1. Keep the whole mapped network in true metric coordinates as the planning reference. Preserve source IDs, elevations/layer tags for crossings, access attributes and original data independently of generated terrain.
2. Export a small, connected **1:1 driving corridor** around Getaboda first, then extend toward Agunnaryd and Ljungby. Use flat placeholder ground, simple road surfaces, a vehicle and test-only spawn setup. Do not add detailed houses, gardens, zombies or decorative forest to the first scale experiment.
3. Record actual driving time, route length, loading/stutter, export duration, output size and cell-boundary traversal. Keep building density/performance testing as a later, separate gate: an empty road map cannot prove performance of a populated municipality.
4. Extend road-only coverage after exporter and game checks pass. Decide whether rural travel needs shortening from measured playtests. Preserve local house/lot/street dimensions; uniform 1:3 scaling is not an approved solution.

Important edge cases: bridges must not become false junctions or road-through-water shortcuts; disconnected source ways must be reported; unknown road width stays an assumption; generated borders must not leave driving gaps. Use a new test mod/save and leave existing valuable saves intact.

This proposal is a reversible scale experiment, not a decision to build the entire municipality before Getaboda or a change to the first playable milestone. No full-world exporter, compression algorithm or game package was implemented in this turn.

## Evidence

- Ignored local study scripts: `build/municipality-draft/measure_game_extent.py` and `road_extent_study.py`.
- Aggregate metadata: `pz-extent.json` and `road-network-stats.json` in the same directory. Source provenance remains in `provenance.json`.
- Reviewed image: `C:/Users/rober/Documents/ChatGPT/ZombieProjektet/outputs/ljungby-road-scale-study.png`. Geographic road projection is EPSG:3006; the PZ rectangle is drawn at the same metric scale using measured dimensions. It is not copied game art or a traced vanilla-map outline.
- Final image visually inspected. Geometry failures and missing attributes reported. No game tests were run for this research-only delivery.
