# Getaboda source audit and automation workflow

**Checked:** 2026-10-17. **Status:** source discovery and proposed workflow. No real building footprints, orthophoto pixels or laser points have been imported into the game. The cottage remains a fictional prototype. This research does not close creator acceptance of M0 or start a broad GIS implementation.

## Actual findings

The [machine-readable audit](research/getaboda-source-audit-2026-10-17.json) preserves queries, selected public catalog metadata, response hashes and limitations. External source facts retain their stated licenses; MIT does not replace them.

| Check | Result | Meaning and limitation |
| --- | --- | --- |
| OpenStreetMap place | Hamlet node `7465414578`, latitude `56.7325969`, longitude `14.0837009` | Source-backed search center, not a particular house, verified address or final game origin. |
| OSM within 750 m | Zero objects tagged `building`; two highway ways | OSM cannot supply the pilot's buildings. Way `58601063` is tagged `surface=gravel`; this is a database observation, not a field survey. |
| Lantmäteriet buildings | `byggnader/0781`, Ljungby municipality, GeoPackage in EPSG:3006 | A suitable municipal download exists. Individual footprints, dimensions and completeness remain uninspected. The search also returns Älmhult because catalog bounding boxes overlap. |
| Lantmäteriet orthophoto | `orto-e2-2025/o62875_4425_25_mr25`, acquisition **2025-07-01**, **0.16 m** pixels | Aerial coverage at the search center. An adjacent tile also intersects the study window. The 2023 catalog has imagery here too. Pixel size is not positional accuracy. |
| Lantmäteriet laser data | `dsm-skoglig-copc/25a021-62875_4425_25`, acquisition interval **2025-03-22–2025-04-02**, COPC | Point-cloud coverage at the search center. Actual roof-height suitability is unverified. |
| Lantmäteriet terrain | `dtm-cog/628_44`, **1 m** ground grid | Terrain data exists. Ground elevation does not measure roof height. |
| Mapillary viewer | No green image sequences visible in the inspected view at the OSM point, zoom 17 | No usable facade image verified. This limited visual check does not establish absence of imagery across the wider area. |

Only the first five results of each imagery/height search were inspected, not every acquisition year. Catalog updates differ from acquisition/survey dates. Public catalog availability does not grant access to the underlying products.

No house length, width, facade color, roof material or exact height has been verified. The creator's Google Maps screenshot communicates the intended area; it is not a traced geometry source.

## Recommended free sources

| Need | Source and access | Automation and limits |
| --- | --- | --- |
| Building location and outline | [Lantmäteriet Byggnad Nedladdning, vektor](https://geotorget.lantmateriet.se/geodataprodukter/byggnad-nedladdning-vektor-api?page=%C3%85tkomst-och-leverans.html&version=2025.02&view=dokumentation): free, Geotorget account and purpose review | STAC discovery and GeoPackage selection. Check whether geometry represents walls or another building outline before deriving facade dimensions. |
| Roofs and surroundings | [Lantmäteriet Ortofoto Nedladdning](https://geotorget.lantmateriet.se/geodataprodukter/ortofoto-nedladdning-api?page=Kvalitetsbeskrivning.html&version=2025.02&view=dokumentation): free, account and purpose review | STAC and COG image windows. Shadows, trees and color processing affect interpretation. Roof appearance does not establish facade color. |
| Roads, width and surface | [NVDB](https://www.nvdb.se/sv/kund/) open data, [Lastkajen](https://www.trafikverket.se/lastkajen) registration/terms | Download packages or [Datautbytesportal API](https://www.nvdb.se/sv/kund/hamta-aktuella-data/), whose listed products include road width. Check local attributes and coverage. Drawn line thickness is not road width. |
| Labels and fallback geography | [OpenStreetMap](https://www.openstreetmap.org/copyright), ODbL 1.0; [Geofabrik Sweden](https://download.geofabrik.de/europe/sweden.html) | Small cached Overpass discovery queries; local PBF extraction for expansion. Preserve attribution and assess derived-database obligations. Coverage varies; no raster tile harvesting. |
| Forest, open land and wetlands | [Naturvårdsverket NMD](https://www.naturvardsverket.se/verktyg-och-tjanster/kartor-och-karttjanster/nationella-marktackedata/ladda-ner-nationella-marktackedata/), CC0 | Clip the 10 m base raster; map classes to deterministic vegetation rules. Check local release and coverage mask: NMD2023 production is progressive. It does not locate individual trees or garden edges. |
| Ground and possible roof heights | [Lantmäteriet height catalog](https://api.lantmateriet.se/stac-hojd/v1), free products ordered through Geotorget | Ground COG plus suitable laser points. Separate terrain, eaves, ridge and vegetation. Sparse or obscured points may leave heights unknown. Flat gameplay terrain remains initial scope. |
| Facade color and materials | Creator-owned exterior photos, or verified [Mapillary images](https://help.mapillary.com/hc/en-us/articles/115001770409-CC-BY-SA-license-for-open-data) | Suggest broad labels with source image ID, date and confidence. Mapillary uses CC BY-SA with contributor attribution; API access has separate setup/terms. Local usable coverage is unverified. Exact paint codes cannot reliably be recovered from ordinary photos. |

NMD resolution and CC0 are documented in the [NMD2023 v2.1 description](https://geodata.naturvardsverket.se/nedladdning/marktacke/NMD2023/Basskikt_v2_x/NMD2023_Produktbeskrivning_Basskikt_NMD2023_v2_x.pdf), printed pages 9, 14 and 32. Keep the downloaded release's class table; do not mix NMD2018 and NMD2023 codes.

## Access and rights

[Geotorget delivery guidance](https://www.lantmateriet.se/sv/geotorget-produktstod/om-tillhandahallandet/) distinguishes free pricing from unrestricted access. Buildings and orthophotos need an account, stated purpose/geographic selection and review. No account or application was submitted during this audit.

The [HVD terms containing personal data](https://www.lantmateriet.se/globalassets/geodata/geodataprodukter/anvandningsvillkor_for_vardefulla_datamangder_pu.pdf), version 1.1, 2025-03-04, specify CC BY 4.0 and approved-purpose/data-handling conditions. Credit the product, ©Lantmäteriet, license and modifications. Check processing/storage conditions before cloud use or public uploads; a license label alone is insufficient.

[Laserdata Skog terms](https://www.lantmateriet.se/globalassets/geodata/geodataprodukter/anvandningsvillkor-for-laserdata-nedladdning-skog.pdf), version 1.0, 2026-05-20, specify CC BY 4.0 and personal-data responsibilities. Its catalog says `license=other`; retain both the catalog value and actual terms.

Priority access requests: **Byggnad Nedladdning, vektor** and **Ortofoto Nedladdning**. Describe the actual purpose: a geographically based Project Zomboid hobby map, initially Getaboda in Ljungby municipality, generic interiors, and intended later distribution of a game adaptation. Describe intended local/cloud/AI processing accurately. Request only necessary attributes; residents, ownership and security information are unnecessary. Laser and road products can follow when needed. The creator handles account details and approves any submitted declarations.

## Repeatable workflow

1. **Define the area.** Locate the intended cluster in permitted data using the OSM point, match it to the creator's reference, and save an AOI polygon plus buffer. The exploratory 750 m radius is not the final playable boundary.
2. **Freeze inputs.** Use documented APIs, cache responses and download approved products. Record dataset/item IDs, acquisition/retrieval dates, license/terms, authorized scope, source URLs, hashes and tool versions. Keep credentials outside Git. Use explicit refreshes, bounded retries and provider rate limits; normal builds consume frozen local files.
3. **Normalize.** Preserve raw files in ignored `build/geodata/` or another approved local cache. Use metric GeoPackage geometry in SWEREF 99 TM, EPSG:3006, retaining source CRS and axis order. Height products also carry RH2000, e.g. EPSG:5845. GeoJSON interchange remains longitude/latitude and is projected before measuring. Validate geometry, duplicates and permitted extent.
4. **Identify buildings.** Preserve provider IDs and assign persistent project IDs with provider aliases. Do not derive identity from mutable geometry. Match buildings to imagery, distinguish houses/outbuildings and leave ambiguous matches unresolved. Keep original geometry separate from game adaptations.
5. **Measure and enrich.** Derive area, orientation and approximate dimensions in meters with named methods. A minimum rotated rectangle estimates a simple house's size; it is not an exact wall schedule for an irregular house. Estimate roof/eaves heights only if points support them. Attach permitted photo evidence to appearance observations; unknown values stay null.
6. **Apply corrections and templates.** Suggested precedence: reviewed correction → supported source property → documented deterministic fallback. Corrections have a stable building ID, reason and evidence; generation never overwrites them. Conflicting new source data creates a review item. Use the approved Swedish style library for missing detail.
7. **Adapt to PZ.** Preserve source scale/orientation and record snapping, resizing and rotations separately. Verify the approved local 1:1 intent against the practical tile grid. Report overlap, clearance and shape distortion; arbitrary geographic rotations may require adaptation to editor walls.
8. **Review and test.** Show one representative exterior for creator review. The agent checks data quality and tests doors, windows, daylight, lighting, walls and roofs in the exact game version. Expand after the pilot regenerates consistently and corrections survive.

QGIS is a suitable first visual inspection/clipping tool, with Python/GDAL introduced for repeated operations. This is a proposed workflow, not a claim that these processing tools are installed. `tools/building_styles.py` currently implements deterministic style selection only, not acquisition, measurement, overrides or map export.

## Minimum building record

| Group | Contents |
| --- | --- |
| Identity | Persistent project ID, provider/dataset/feature IDs, source revision/hash |
| Geometry | Original reference/CRS, normalized geometry, separate game transform |
| Measurement | Value, unit, method, evidence, date and uncertainty; null if unavailable |
| Appearance | Facade/trim/roof colors and materials, roof shape; evidence/date per known property |
| Evidence | `source_reported`, `derived`, `observed`, `assumed` or `design_override`, confidence and rationale |
| Generation | Template version, fixed seed, generator version and override revision |
| Rights | Product/source, attribution, license/terms, access scope and publication review state |

Image-based suggestions remain inferences until reviewed. Use supported broad labels such as red timber; do not invent NCS/RAL codes. Present-day observations and the chosen 1990s interpretation remain separate properties.

## First pilot and acceptance

Start with one real building after access, then about 4–5 buildings in the agreed cluster.

- Match a footprint to permitted evidence and create a traceable measurement record.
- Leave unknown appearance values unknown or explicitly assumed; a Swedish-looking template is not source verification.
- Frozen inputs produce identical generated content on two runs; run timestamps are recorded separately.
- A facade correction survives regeneration and leaves unrelated buildings stable.
- Changed/deleted provider features raise reconciliation items rather than silently dropping corrections.
- Include attribution with distributable output. Exclude credentials and source archives unless redistribution is cleared.
- Record geometry QA separately from game QA. Creator review covers representative style and play feel.

Next: obtain access to the two priority Geotorget products, inspect the Getaboda subset and measure one source-backed house. Cottage refinement and game testing can proceed independently.
