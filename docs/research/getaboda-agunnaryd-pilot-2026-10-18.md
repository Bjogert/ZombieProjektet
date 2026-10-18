# Getaboda and Agunnaryd — first data feasibility test

Checked 2026-10-18. This is an executed source-coverage and local registration experiment, not a completed real-house reconstruction or an in-game test. It supplements the [reference workflow](exterior-reference-workflow-2026-10-18.md) and the [canonical execution queue](../ROADMAP.md).

## Recommendation from the results

Keep Getaboda as the first playable location and main exterior-research target. Use a small Agunnaryd comparison sample to exercise real-geometry registration while usable Getaboda building data is pending. The evidence supports Agunnaryd for a geometry experiment; it does not establish better ordinary-house photography or justify moving V1.

Start with one Getaboda house when permitted geometry and a usable reference can be matched, then expand to the agreed 4–5 buildings. Reference discovery can proceed now. A discovered image link is not yet a licensed, usable or correctly matched reference.

## Executed OSM comparison

The existing local Kronoberg extract was verified against its registered SHA-256 and processed locally. Both samples use the same 750 m radius around each named OSM place node. Building areas were assembled from ways/relations; valid geometry was tested by minimum distance in SWEREF 99 TM (EPSG:3006). No source coordinates or source image pixels were sent to the model.

| Measure | Getaboda | Agunnaryd |
| --- | ---: | ---: |
| Valid assembled building area features in sample | 0 | 190 |
| Additional building-tagged point features in sample | 0 | 0 |
| Areas with `building:levels` or `height` | 0 | 0 |
| Areas with `building:colour` or `building:material` | 0 | 0 |
| Areas with `roof:shape`, `roof:colour` or `roof:material` | 0 | 0 |
| Areas with `addr:housenumber` | 0 | 1 |

The 190 features comprise 187 generic `building=yes` areas, one church and two schools. They are not 190 verified homes. Zero features in Getaboda means missing coverage in this source/sample, not absence of real buildings. Missing appearance tags mean unknown properties; the appearance denominator is undefined for Getaboda, not a measured 0% completeness rate.

Source: [OpenStreetMap France Kronoberg extract](https://download.openstreetmap.fr/extracts/europe/sweden/kronoberg-latest.osm.pbf), snapshot `2026-10-17T01:27:19Z`, ODbL-1.0, attribution to [OpenStreetMap contributors](https://www.openstreetmap.org/copyright). SHA-256: `4d459da057e3c0132f879177947295dc4b208e9698460377f7a1c378aa0327c8`. The latest URL is mutable; reproduction requires the matching cached snapshot. This was not a new network download.

The area handler reported zero invalid building geometries in the extract. Unassembled/incomplete relations are not counted as valid footprints. Counts are source-feature counts, not a deduplicated cadastral inventory. These are equal-radius place samples, not matched residential streets or a sample-size claim about the entire municipality.

## Executed local registration experiment

Selected the three nearest generic `building=yes` areas to the Agunnaryd sample centre. Their residential use, addresses and association with a particular street are unverified. Each received an experimental UUID, a separate OSM provider alias and a reference to the locally stored footprint. No resident or ownership information was collected.

Results:

- Three source-feature candidates registered locally.
- All 27 appearance entries (nine per candidate) remain explicitly unknown: facade color/material, roof color/form/material, storeys, height, deck and garden.
- A repeated registration preserves the same IDs and record contents.
- An in-memory synthetic manual-choice probe survives repeat registration without changing source facts. The probe is not a real facade observation and is not persisted as one.
- A second run in separate processes reproduced both candidate extracts and the registry byte-for-byte.
- The source input hash remained unchanged.

These checks cover the same frozen source only. New/changed provider features, conflicts, splits/merges, full schema validation, production storage and integration with game generation are not implemented by the experiment. Experimental IDs are not yet authoritative project identities; preserve them if the records are later reviewed and adopted.

Local experiment artifacts, all excluded from Git under `build/`:

```text
build/exterior-pilot/audit_cached_osm.py
build/exterior-pilot/register_comparison_sample.py
build/exterior-pilot/coverage-summary.json
build/exterior-pilot/registration-summary.json
build/exterior-pilot/repeat-summary.json
build/exterior-pilot/getaboda-candidates.local.geojson
build/exterior-pilot/agunnaryd-candidates.local.geojson
build/exterior-pilot/comparison-registry.local.json
```

Run the two scripts from the canonical repository. They use the already installed local GIS dependencies under `build/municipality-draft/python-deps`; this is not a portable production importer. They currently emit a non-failing Shapely deprecation warning. Move durable source records into the planned backed-up local store before treating any experiment output as authoritative; disposable build output is not its final home.

## Exterior-reference discovery

Only public page text/metadata was inspected. No additional source imagery was viewed, downloaded or imported.

| Source lead | What the bounded search established | What remains open |
| --- | --- | --- |
| [Agunnaryds Hembygdsforening: Ekeboda, Smedjan, Getaboda](https://www.hembygd.se/agunnaryd/plats/334799) | Named Getaboda-related exterior-image candidates, including barn/smithy and an item titled Ekeboda 1940 | Rights holder/reuse terms, reliable capture dates and matching to the selected V1 buildings |
| [Ekeboda 1940 record](https://www.hembygd.se/agunnaryd/plats/334799/picture/2404585) | Title and place association in page metadata | The title alone does not independently verify the capture year or present-day appearance |
| [Getaboda villa lead](https://www.hembygd.se/agunnaryd/plats/334805) | A search-index lead for a villa record | Live extraction mostly returned the site shell; content and relevance are not verified |
| [Commons: Agunnaryd](https://commons.wikimedia.org/wiki/Category:Agunnaryd) | Four direct landscape/sign/bathing-place files and church/church-ruin subcategories | No ordinary residential street coverage established in this category |
| [Commons: Agunnaryd sign](https://commons.wikimedia.org/wiki/File:Agunnaryd_sign.JPG) | File metadata identifies Moralist, 2014-05-25 and CC BY-SA 4.0 | A licensed metadata example, not a house reference |

A bounded Commons site search for Getaboda returned no indexed result. This does not prove absence. Mapillary coverage was not refreshed; the earlier limited inspection still does not establish usable local facades. Heritage-site publication alone does not establish image reuse rights. No permission request or other message was sent.

## Access check

The connected Gmail search found the two Lantmateriet order receipts and account-registration mail, but no matching approval message. This is an email-only finding; Geotorget case status and delivery access were not rechecked, so access remains unconfirmed rather than newly declared pending or denied. Private correspondence and case identifiers are not included here. No duplicate application was made.

## What to automate next

1. Maintain one local source/observation register with persistent building identity, frozen source references and separate design overrides, following the existing record model.
2. Automate permitted vector import, metric checks, candidate matching, date/license metadata, missing-field reports and repeatability checks. Uncertain matches require review rather than silent acceptance.
3. Track image references through `discovered -> identified -> rights_verified -> usable_reference -> matched_building`. Search hits and thumbnails are not usable-coverage counts.
4. Use eligible photos or independent creator observations for appearance. Leave unavailable fields unknown; any generated Swedish variation is a design choice with a stable seed, not a claimed observation.
5. Prioritize individual exterior detail for the Getaboda pilot and selected landmarks. Reuse reviewed building parts for broad expansion instead of requiring exact data for every window, plant or deck.
6. Measure manual minutes, source/access failures and supported fields on the first real house before estimating larger-area automation. The short local OSM scan does not estimate total house-research time.

The result advances feasibility evidence for M1/GETABODA-01 while leaving that real-building gate open. The synthetic cottage/garden/road integration remains the next visible game delivery. No Agunnaryd settlement build, database server, cloud processing, paid API, public release or game-compatibility claim was introduced.
