# Getaboda local building candidates — 2026-10-18

## Acquisition and limits

The fresh Geotorget case view on 2026-10-18 shows **Behandlas** for both the
building-vector and orthophoto applications. Authentication works; data access
has not been granted. No duplicate applications were submitted.

A separate open source provides a useful local pilot:
[Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints),
release 2026-08-13, Sweden partition 120032302. The provider distributes building
polygons under [CDLA-Permissive-2.0](https://cdla.dev/permissive-2-0/). The source
license is retained locally. These are machine-detected candidate outlines with
variable accuracy, not surveyed walls or confirmed house identities. No imagery
was downloaded, no Google geometry was traced, and no household data was imported.

The 3.3 MB compressed partition contains 37,415 features. Local filtering found
13 candidates within the 750 m pilot; all 13 lie within the inner 250 m. Geometry
validation found no invalid features in the partition. The compressed source hash
is `9cc70630c9e0a7f151110e19acdf7d35d409ca21632fad821f47928e8f2035b5`.

The local source, license, index selection and backup are under ignored
`local-data/`; none of their raw geometry enters the repository or model output.
The catalog, selected raw bytes and subset have separate hashes. The original
EPSG:4326 coordinates remain intact; measurements use EPSG:3006 with explicit
longitude/latitude axis order.

## Persistent identities and uncertainty

`tools/building_registry.py` registers the frozen local source without networking.
Project UUIDs are allocated once. Release/partition/line aliases identify source
rows, not permanent real buildings. A source refresh requires explicit
reconciliation; rerunning the identical import preserves register and choices
byte-for-byte. The actual 13-record repeat passed, as did the synthetic tests.

Building use, facade/roof appearance, height, storeys, decks and gardens remain
unknown. Creator observations and game choices belong in separate fields/files.
The local review labels G01–G13 map to persistent project IDs. Ranking by size is
for review convenience, not proof that the four largest objects are homes.

**Creator selection, 2026-10-19:** begin the first Getaboda version with G01–G04
and correct details together. The existing local `choices.json` records this
decision against their persistent IDs, with the review labels and decision date.
Source geometry, registry status, building use and appearance remain unchanged;
selection is not verification that these candidates are homes. The fictional
rural showcase remains the immediate visual test.

## Fitting evidence and accepted grid decision

The largest four minimum rectangles measure approximately 10.9 × 17.1,
9.1 × 12.3, 7.7 × 11.6 and 6.1 × 9.3 m. Their polygon areas are approximately
166, 106, 89 and 57 m². The first outline occupies only 89% of its rectangle;
fitting it to a plain rectangle would lose meaningful shape and needs review.

The creator reviewed the local comparison and approved a **45-degree rotation**
of the game grid, preserving all distances at 1:1. For the four largest candidate
axes, mean adjustment to the game axes falls from about 36° to 9°. Source
coordinates remain unchanged. The 13 rotated source outlines span approximately
94 × 208 m, before scenery/access margins and game approximation.

The source comparison is a local planning view, not a finished playable map.
A generic 8 × 12 cottage variant now passes official export and 12/12 game
checks after restart/reload; see [sized cottage evidence](../COTTAGE_SIZE_TEST.md).
Next fit the first selected candidate and review the exact 4–5-building V1 list,
road access and source gaps. Matching a polygon does not verify facade color,
entry side, building use, actual private rooms or land-cover boundaries.

## Bounded layout experiment

`tools/world_grid.py` implements the approved transform and its inverse, without
rounding or changing source values. Synthetic compass, distance and round-trip
tests pass. A local proposal applies it to the frozen 13-outline sample and
centres the core in one 256-square runtime cell. All four larger game rectangles
fit; centre rounding displaces them by at most 0.696 m. This is a proposal, not
creator confirmation of the building list.

Only one segment of the existing corridor intersects this core. A separate local
diagnostic then inspected complete highway ways in the registered PBF, using
line/box intersection rather than requiring a vertex inside the selection.
It found one unclassified way in a 512 by 512 m area around the core; 265.843 m
intersects the 256-square core. No mapped driveways were found there. This is a
coverage gap, not evidence that driveways do not exist. All original node IDs,
longitude/latitude coordinates and relevant tags remain local and unchanged.
The source contained 66 ways with missing node locations across the whole
extract; their missing extents cannot be assigned confidently to this selection.
The diagnostic skips incomplete ways rather than bridging missing geometry.

This experiment is saved as `build/getaboda-ms-pilot/extract_village_roads.py`
and `local-data/getaboda/village-roads-diagnostic.json`. It is not yet a maintained
village importer or a completeness claim. Road widths, residential access and
land cover still need separate evidence or explicit design assumptions.
