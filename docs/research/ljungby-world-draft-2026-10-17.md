# Ljungby municipality — world draft 01

Status: **geographic planning draft for creator review**, 2026-10-17. The creator requested a view of the eventual whole municipality and research into sources beyond Lantmäteriet. This does not approve an immediate municipality-wide build, a compression factor or a release date. Getaboda remains the first real playable location.

## What the draft proves

The overview combines SCB's generalized municipality boundary for code `0781` with locally downloaded OpenStreetMap roads, water and settlement points. Positions and geographic distances are retained. The generalized boundary spans approximately **61.4 km east–west and 51.1 km north–south** in SWEREF 99 TM. These are bounding extents, not driving distances or a rectangular playable area.

The map contains 1,445 road features, 109 generalized water polygons, 164 river features and 14 settlement points before label selection. Segments are not unique roads; these counts do not measure completeness. Only major road classes and water polygons of at least 0.15 km² are shown. Neutral land fill does not represent forest, farmland or verified land cover. Buildings and gardens are absent.

Numbered places are a **design proposal**, not a route or artificial road: 1 Getaboda; 2 nearby Agunnaryd/Södra Ljunga; 3 Ljungby. Other settlements illustrate later municipal expansion. Their ordering, final playable boundary, travel times and countryside compression remain open.

## Sources and acquisition routes

| Source | Useful contribution | Access and rights verified on this date | Limitations / next action |
| --- | --- | --- | --- |
| [SCB digital boundaries](https://www.scb.se/hitta-statistik/regional-statistik-och-kartor/regionala-indelningar/digitala-granser/) | Municipality extent and planning overview | Free download, **CC0**, SWEREF 99 TM shapefile | SCB explicitly says these simplified boundaries are for thematic maps and unsuitable for precise analysis. Do not use them for house placement or exact clipping. |
| [OpenStreetMap](https://www.openstreetmap.org/copyright), [OSM France regional extracts](https://download.openstreetmap.fr/extracts/europe/sweden/) and [Geofabrik](https://download.geofabrik.de/europe/sweden.html) | Roads, water, settlement points and whatever buildings are mapped | **ODbL**; attribution required and database obligations must remain attached. Kronoberg extract downloaded locally without an account. | Coverage varies. The earlier Getaboda audit found no building objects in its checked 750 m radius. Regional downloads make repeatable local work less dependent on public query servers. |
| [Trafikverket / NVDB](https://www.nvdb.se/sv/kund/hamta-aktuella-data/) | Road class, width, road names, road numbers and traffic-network attributes | Official page lists 12 current datasets in the Open API. Download requires a registered account; historical data is on Lastkajen. | Record exact product terms at acquisition. The account and a local sample have not been obtained here. Road width is more useful for game generation than tracing a viewer screenshot. |
| [Naturvårdsverket NMD](https://www.naturvardsverket.se/verktyg-och-tjanster/kartor-och-karttjanster/nationella-marktackedata/ladda-ner-nationella-marktackedata/) | Forest, open land, wetland and water classification; tree-species and other additional layers | Open data; the existing project audit records CC0 in product documentation. Current portal lists NMD2018 and NMD2023, with distinct 0.x and 2.x base versions. | Pin the selected version, class definitions, resolution and tile. No raster imported for this draft. Land classification does not supply individual garden layouts. |
| [SMHI hydrology / SVAR](https://www.smhi.se/data/sjoar-och-vattendrag/hydrografi) | Catchment context and hydrological reference | Some catchments are open WFS datasets. **The page explicitly restricts the listed lake/river geometries to viewing, because their Lantmäteriet base is not open data.** | Do not assume all SMHI water geometry is freely reusable. Use verified open water data or a separately authorized product. No SMHI geometries imported. |
| [Ljungby municipal geodata](https://www.ljungby.se/bygga-bo-och-miljo/lantmateri-och-kartor/kartor-och-geodata) | Locally maintained base map; possible high-quality reference | The published service sells DWG/DXF base-map extracts; no blanket open-data offer is stated on that page. | Not the default free pipeline. No purchase or contact made. The [municipal comprehensive plan](https://www.ljungby.se/trafik-och-samhallsplanering/samhallsplanering/oversiktsplan-och-detaljplaner/oversiktsplan) is useful context, but planned developments are not existing-world evidence. |
| [Riksantikvarieämbetet K-samsök](https://www.raa.se/museer/digital-omstallning-pa-museiomradet/k-samsok-en-digital-dataformedlingstjanst-for-kulturarv/att-anvanda-data-fran-k-samsok/) | Historical building and streetscape references, helpful for 1990s styling | API metadata is CC0; individual resources/images can have separate conditions | Check each image's license, date and location. No claim of Getaboda photographic coverage yet. |
| Creator-owned exterior photographs | Facade colors, roofs, decks, gardens and flowerbeds | Record ownership/permission and image date | Most direct way to resolve small local details. Observations, uncertain inferences and chosen fictional 1990s styling must remain separate. |

Lantmäteriet remains valuable for buildings and aerial context. Alternative sources let us develop and verify the overview workflow while access is pending; they do not guarantee replacement of every missing building or appearance attribute.

## Local workflow proposal

1. **Register:** dataset URL, source ID, snapshot, CRS, license, permitted processing, coverage and hash. Keep raw files locally outside Git.
2. **Normalize:** work in SWEREF 99 TM for metric dimensions, preserving original geometry and identifiers. Keep each source's rights attached; a combined project is not automatically MIT-licensed geodata.
3. **Validate:** measure coverage, gaps and disagreements. Never interpret missing OSM buildings as empty land. Mark unknown colors and dimensions as unknown.
4. **Separate design:** store game projection, template, orientation, exterior palette, deck and garden choices as stable-ID overrides. Source facts survive regeneration unchanged.
5. **Export a small slice:** connect the verified Getaboda buildings to the already tested cottage/garden workflow. Local corrections should not require rebuilding all municipality content.
6. **Game QA:** verify each playable slice's roads, entrances, collision, roofs and performance in the game before expansion. Map previews do not pass gameplay gates.

This is a proposed workflow, not a newly implemented municipality importer. The existing template only supports one rectangular cottage and optional garden; adapting real footprints is still needed.

## Scale recommendation for creator review

Keep the source map geographically correct and preserve local 1:1 dimensions in built-up areas. Treat any later countryside compression as a separate, reversible game transform with continuity checks for roads, waterways and settlement boundaries. Compare a real driving corridor with one compressed prototype before choosing a ratio. Do not apply uniform scale reduction to houses or gardens.

A whole-municipality 1:1 build preserves distances but creates a much larger content, storage, iteration and travel-time burden. Selective compression can shorten travel but risks visible discontinuities and distorted relationships. No performance, export-time or storage claim for municipality scale has been measured.

## Draft provenance and review

- SCB archive: `shape_svenska_260225.zip`, nested `Kommun_Sweref99TM.zip`, feature `KnKod=0781`; SHA-256 `26a7030a23648ad25a69acee16f08974148eafd076bfa8dd76013060693f51f4`.
- OSM download: `https://download.openstreetmap.fr/extracts/europe/sweden/kronoberg-latest.osm.pbf`; replication timestamp `2026-10-17T01:27:19Z`; SHA-256 `4d459da057e3c0132f879177947295dc4b208e9698460377f7a1c378aa0327c8`.
- Visual QA exposed incomplete cross-county lake relations in the regional extract. Complete OSM relations `7130` (Bolmen), `7131` (Vidöstern) and `3805462` (Unnen) were fetched individually from the OSM API on 2026-10-17 and processed locally. URLs and hashes are in the local `provenance.json`. The corrected final image includes these lakes; this demonstrates why completeness checks must precede generation.
- Derived overview: projected locally, display simplification of 45 m for roads, 55 m for rivers and 65 m for water outlines; coordinates rounded for display. Original inputs retained separately. These tolerances are inappropriate for house-level work.
- Getaboda point: OSM node `7465414578`; a place label, not the address of an individual house or final game origin.
- Local scratch tools, raw inputs and metadata: ignored `build/municipality-draft/`. No restricted imagery, personal application information or raw geometry was placed in model-visible output or committed.
- Artifact location: `C:/Users/rober/Documents/ChatGPT/ZombieProjektet/outputs/ljungby-world-draft.png` and `.svg`. The accompanying HTML experiment is not a validated deliverable: browser policy rejected local-file preview, so the delivered image is rendered offline.
- Public Overpass queries returned HTTP errors. A regional PBF extract supplied the actual displayed OSM geometry. Neither an unsuccessful query nor a catalogue page is counted as successful source acquisition.
- Validation: final PNG visually reviewed after lake repair; source features projected in EPSG:3006; source counts and geographic extent recorded. Project agent-setup and overview consistency checks and `git diff --check` passed. No game-code changes or game-test claims are made by this research delivery.
- Creator review remains open. This draft does not change the first-playable-version scope or approve whole-municipality production.
