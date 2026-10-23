# Exterior reference research — Getaboda

Checked 2026-10-18. This supplements [the geodata workflow](../GEODATA_WORKFLOW.md) and follows [data and rights rules](../DATA_AND_RIGHTS.md). It records source discovery and a bounded research method, not verified building measurements or a new implementation milestone. The execution queue remains in [ROADMAP](../ROADMAP.md).

Follow-up: the [Getaboda/Agunnaryd feasibility test](getaboda-agunnaryd-pilot-2026-10-18.md) now records an executed local OSM comparison, a three-candidate registration experiment, reference discovery and an email-only access check. Its experiment does not implement the production register proposed below.

## Findings

- Searches in the available plugin directory for `Google Maps` and `Street View` returned no matching integration. This is a discovery result, not proof that no integration exists elsewhere. No plugin was installed and no Maps API was configured.
- The creator supplied five Street View screenshots for discussion. Their visible capture label says June 2026; this does not establish a historical appearance. They remain conversation attachments, not imported geometry, textures or an appearance database. No images were copied into the repository or redistributed.
- Google permits viewing its products, but its [Geo Guidelines](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) explicitly restrict creating data from Street View imagery and using applications to analyze/extract information from it. The [Maps end-user terms](https://www.google.com/intl/en-US/help/terms_maps/) also restrict copying and bulk downloads. Do not build a Street View scraping or image-to-building importer. A browser or plugin does not grant additional reuse rights.
- The existing 2026-10-17 Mapillary inspection found no visible sequences in one limited view. No new coverage inspection was performed here; usable Getaboda facade coverage remains unverified.
- [Lansstyrelsen's Ljungby cultural environment program](https://www.lansstyrelsen.se/kronoberg/samhalle/kulturmiljo/kulturmiljoprogram/ljungby-kommun.html) is useful regional reading, but the inspected page had no `Getaboda` match. It does not verify the identity, age, dimensions or materials of the pictured houses, or grant a blanket image-reuse license.

## Viewing versus collecting facts

The creator clarified that the immediate question is occasional browser inspection of exterior details, not a municipality-wide Street View automation. Browser operation, permitted viewing, recording new structured information and copying imagery are distinct questions.

The Maps end-user terms allow viewing; ordinary permitted viewing is not presented as requiring a separate application. Google's Street View restrictions on creating data are broader than bulk scraping, however, and the inspected guidance provides no small-sample/manual-observation exception for a building register. We cannot confirm that transferring Street View observations into our production records is allowed merely because a person or agent clicks through a few views. The guidelines also say they do not grant exceptions to disallowed uses. Do not promise that buying API access or submitting a generic permission request will resolve this.

This is a documented uncertainty about our proposed use, not a conclusion that merely looking at a house is forbidden. No new Street View session, image capture or building-attribute collection was performed in this audit. Model inspection of source imagery is also cloud/AI processing even when the browser runs locally; the existing processing boundary still applies. Creator-supplied screenshots in the conversation are not permission to retrieve and upload additional source imagery.

## Source selection

| Source | Useful contribution | Condition / remaining uncertainty |
| --- | --- | --- |
| Creator-owned exterior photos and first-hand observations | Visible facade, roof, porch and garden reference for the first few houses | Record author, date and project-use permission; retain the current local-processing boundary. An unknown dimension or hidden facade stays unknown. |
| Approved Lantmateriet building and orthophoto products | Traceable footprint, location and aerial context | Existing applications are not new evidence of access. Check the granted product and terms before acquisition; aerial views do not establish facade colors. |
| Mapillary | Candidate street-level references and capture metadata | Verify coverage and each image's license; use approved interfaces and separate API credentials/terms. No scraping fallback. |
| Wikimedia Commons | Potential landmarks and regional architectural references | Verify each file's license, author and relevance. No Getaboda house coverage has been established. |
| Cultural environment descriptions | Regional building and landscape context | Keep regional descriptions separate from evidence about a particular building; image rights need separate checking. |

[Mapillary's image-license guidance](https://help.mapillary.com/hc/en-us/articles/115001770409-CC-BY-SA-license-for-open-data) links ordinary contributed imagery to CC BY-SA 4.0. Contributor attribution and ShareAlike requirements for shared adaptations need review. Its [service terms](https://www.mapillary.com/terms) separately govern API use, developer application registration, scraping and downloaded-image display. The [official API demo](https://github.com/mapillary/api-demo/blob/main/README.md) documents metadata discovery; its sample token is not our production credential. No quota or availability is promised.

[Commons reuse guidance](https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia) requires checking individual file terms. The [MediaWiki imageinfo API](https://www.mediawiki.org/wiki/API:Imageinfo) can expose licensing metadata for review; missing metadata is not permission.

## What is realistic to collect

The following priorities are engineering recommendations, not verified data about the pictured houses. Provider coverage, access and actual fields must be checked on the first permitted sample.

| Information | Practical source and method | Realistic result / limitation |
| --- | --- | --- |
| Building position and footprint | Approved building vectors; checked OSM features where present | Strong basis for scale and orientation after geometry/source QA. A footprint does not establish facade color, interior layout or an exact wall schedule. |
| Address or local building label | Creator identification or a permitted address source; explicit matching | Useful for search. Address access is separate from building access, and a nearby address point is not a verified building association. Missing addresses do not block a record. |
| Roads, driveways and landscape context | Registered road vectors and permitted orthophotos/land-cover products | Useful geometry and broad land use; completeness, capture date, obscured access and surface assumptions need review. |
| Broad facade/trim/roof color and apparent material | Creator-owned or explicitly licensed exterior photos, or independent first-hand notes | Usually practical when visible; store lighting/occlusion uncertainty. Exact paint codes cannot be recovered reliably from ordinary imagery. |
| Roof form, approximate height and storeys | Visible exterior views; suitable laser points and ground reference if available | Estimates with method and uncertainty. Laser coverage/density may not resolve small roof features; a terrain model alone does not give roof height. |
| Veranda, deck, visible entrances and windows | Permitted ground-level reference; aerial context for larger visible features | Partial exterior evidence. No visible deck is not evidence that none exists; hidden elevations stay unknown. |
| Garden character, boundary walls and large trees | Permitted references and creator knowledge | Representative layout and character are attainable. Individual plants, seasonal appearance and covered areas are incomplete and change over time. |
| Historical 1990s appearance | Dated, permitted archival material or explicit creator knowledge | Patchy evidence. Store current observations and the 1990s design interpretation separately; no exact historical reconstruction promise. |
| Interiors and hidden details | Generic authored layouts within current scope | Not a collection requirement. Do not pursue private floor plans, resident information or security details. |

The official [Geotorget catalog](https://geotorget.lantmateriet.se/geodataprodukter) describes [building vectors](https://geotorget.lantmateriet.se/geodataprodukter/byggnad-nedladdning-vektor-api) as building areas with purpose/name where available, and [address vectors](https://geotorget.lantmateriet.se/geodataprodukter/belagenhetsadress-nedladdning-vektor-api) as a separate product. It describes [orthophotos](https://geotorget.lantmateriet.se/geodataprodukter/ortofoto-nedladdning-api) as aerial images scaled in the ground plane and [Laserdata Skog](https://geotorget.lantmateriet.se/geodataprodukter/laserdata-nedladdning-skog-api) as classified points. These descriptions do not establish access for this account, parcel coverage or all desired attributes. The individual product pages returned only application-shell text through the research reader; a complete product-schema inspection remains part of the acquisition pilot.

## Local building register recommendation

Use the existing minimum building record in [GEODATA_WORKFLOW](../GEODATA_WORKFLOW.md), with small structured JSON records for the first 4–5 houses and linked local GeoPackage geometry when approved data is acquired. This is a proposed implementation approach; no registry importer, database or user interface was created during this audit.

| Record | Essential contents and behavior |
| --- | --- |
| Building identity | Immutable project ID; provider-ID aliases; optional site/group ID; address labels with evidence and match status. A house and outbuilding remain distinct even if they share an address. |
| Source | Source ID, author/provider, URL or local-file reference, capture date, retrieval date, revision/hash, license and applicable processing/distribution conditions. Unknown dates stay unknown. |
| Observation | Building ID, property, value/unit, source ID, method, viewed side, visibility, confidence and review state. Keep conflicting observations instead of silently overwriting them. |
| Selected interpretation | Reference to the observation(s) currently used, reviewer and rationale. A rough visual estimate remains an estimate after review. |
| Design choice | Template, palette, rotation and garden selection by building ID, with rationale and revision. Separate deliberate 1990s adaptation from contemporary observations. |
| Game adaptation / QA | Reference to source geometry, grid adjustment and game dimensions, generator version/seed, artifact evidence and test state. Do not overwrite the original footprint. |

An address is a searchable label, not a primary key. Several buildings can share it; a building can lack an address; labels can change. Do not create IDs from coordinates, current geometry or an address string. Allocate a project ID once and preserve it through corrections and source refreshes. Ambiguous matches stay unresolved, and split/merged source objects require reconciliation.

For an unknown property, store `null` plus a reason such as `not_visible`, `no_source` or `conflicting_evidence`. Keep `source_reported`, `derived`, `observed`, `assumed` and `design_override` distinct. Do not turn an empty field into a randomly selected real-world fact.

Keep authoritative records and references in a local directory excluded from Git, with local versioned backups; they must not exist only inside disposable generated output. Commit only schemas, tools and synthetic examples until publication of actual inputs/records is cleared. Geometry belongs in its own referenced layer instead of being copied into every observation. No server or cloud database is needed for the pilot.

[GeoPackage](https://www.ogc.org/standards/geopackage/) is itself a standardized SQLite container for spatial and other tabular data. Use it for the planned local geometry workflow. Add observation tables or a rebuildable SQLite search index when repeated cross-house queries and history comparisons justify it; keep a single authoritative store per record type and preserve IDs through migration. Do not independently edit conflicting JSON and database copies. Increased multi-writer demand would need a separate concurrency design; adding SQLite alone does not solve that.

Existing seams are [`building_styles.py`](../../tools/building_styles.py) (stable feature IDs and separate style overrides) and [`placement_source.py`](../../tools/placement_source.py) (synthetic fixture IDs and separate house/rotation/garden choices). An eventual adapter must preserve provider IDs as aliases and pass the canonical project identity consistently to these tools. Neither currently consumes the proposed real-building register. The style manifest contains `source_geometry`, so a manifest generated from restricted real data remains inside the same local processing boundary.

## One-house research pilot

1. Obtain one permitted building footprint and retain its provider identity. Do not match a screenshot to a house by guessing from a miniature map.
2. Discover a usable exterior reference. Record source URL/ID, author, capture date, license, allowed processing and attribution before importing anything.
3. Review only visible exterior features under the applicable processing permission. Record broad facade/trim/roof color, apparent material, roof shape, visible openings and porch/deck separately. Preserve uncertainty and occlusion; ordinary images do not yield exact paint codes or reliable dimensions.
4. Separate current observations from the creator's chosen 1990s interpretation. A contemporary detail is not automatically part of the game design, and its absence in an old image is not proof of absence today.
5. Match the evidence to an original PZ building template. Keep source geometry, grid approximations and design overrides separate; use generic interiors.
6. Show the creator an in-game exterior and a short list of uncertain design choices. Verify access, collision, roof and lighting; preserve accepted corrections on regeneration.
7. Repeat the proven steps for the remaining selected houses. Automate metadata intake, missing-field checks and source/override reconciliation first; add image analysis only where both provider terms and the project's processing decision permit it.

Evaluate feasibility on one permitted real house before collecting all five: record time spent per source/house, which properties are supported, missing/occluded properties, rights/access blockers and manual correction effort. If required geometry or appearance evidence is unavailable, report the gap and continue the existing synthetic integration work. A synthetic record can test software behavior but cannot count as completed real-house research. These measurements support a realistic expansion estimate; do not promise an automatic appearance inventory for the municipality.

## Agent responsibilities

- **World/data research:** discover permitted sources, check provenance and associate evidence with a stable building identity. Report coverage gaps explicitly.
- **Buildings/art:** translate reviewed observations into original PZ building parts and propose reversible variations.
- **QA/review:** check supported versus assumed claims, template fit and actual game behavior.
- **Lead:** keep the single integration queue, reconcile findings and bring exterior/design choices to the creator.

One read-only source-research agent was used for this audit. These roles do not create persistent agents or background jobs. No household identities, ownership, private interiors or security information are needed.

## Next action

Continue the roadmap's cottage/garden/road integration while checking a usable reference and permitted geometry for the first real house. Creator-owned photos are a practical optional contribution, not a prerequisite for independent tool work. This audit did not refresh Geotorget access, acquire source images, verify new real building facts or run the game.
