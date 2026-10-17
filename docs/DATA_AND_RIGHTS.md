# Geodata, imagery, rights and private information

## Sources and provenance

- **OpenStreetMap/Geofabrik:** retain ODbL attribution and assess derived-database obligations before distribution. Coverage is not guaranteed. Use cached queries or extracts, not raster tile harvesting.
- **Lantmäteriet:** use products whose specific terms permit the intended access, storage, processing and distribution. Free pricing, public catalog metadata and download authorization are separate facts. Buildings and orthophotos currently require Geotorget access and purpose review. Retain approved scope and terms; check processing/storage conditions before cloud use or public uploads.
- **Naturvårdsverket NMD:** current product documentation specifies CC0. Record the release, local coverage and class definitions; credit the source for traceability.
- **Trafikverket NVDB:** use official delivery services and record the product's license and attributes at download. Viewer access does not establish reuse rights for every background layer.
- **Street-level photos:** use creator-owned photos or explicitly licensed imagery for exterior observations. Preserve author, image ID, date and license. Mapillary image licensing and API access terms are separate. An uncertain visual inference is not a verified fact.
- **Google Maps/Earth and other map imagery:** never scrape, trace or republish without explicit permission/license. A supplied reference screenshot is not automatically a permitted source for imported geometry or textures.
- **Project Zomboid:** do not copy proprietary code, graphics, audio or data into the repository or redistribute them. Refer to the player's local installation where permitted.
- **Workshop/mod resources:** check permissions, dependencies and redistribution terms before import.

Every imported dataset or building needs provenance, version/date and relevant terms. Preserve original coordinates separately from game adaptations. Distinguish source-reported, derived, observed, assumed and design-selected properties. Unknown values stay null; synthetic details must never be presented as verified real-world facts.

The dated [Getaboda source audit and workflow](GEODATA_WORKFLOW.md) links official documentation and records coverage checks. It is a discovery report, not authorization to download restricted products or release the mod.

## Initial processing boundary (creator decision, 2026-10-17)

Store and process raw geodata and source imagery locally on the creator's computer in Sweden, within the EU/EEA. Do not upload those inputs to cloud storage or AI services until the applicable terms and access decision have been clarified. This includes attaching source imagery or exposing raw geometry in model-visible tool output. Agents may develop local processing code without receiving the restricted inputs; review permitted derived outputs separately before sharing. Keep applicant identifiers, account details and private correspondence outside the repository.

## Private homes and contributions

Detailed replicas of private homes, real floor plans and information that could expose private residential details require review before public release. Generic interiors are the default. Do not import residents, ownership or security-system information. Review contributions through GitHub before integrating them into the main branch.

## Project licenses

Original project code and documentation use MIT where the project holds the rights. **New graphical assets need an explicit license before public distribution**; choosing a permissive art license remains a separate decision when original assets are ready. ODbL, CC BY, CC BY-SA and other third-party terms are not replaced by MIT. Include source-specific attribution with distributable outputs.

This is the project's working checklist; product terms and applicable access decisions remain authoritative.
