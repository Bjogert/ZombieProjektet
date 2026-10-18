# Roadmap — Getaboda first, then a growing Swedish world

Updated 2026-10-18. This is the canonical execution queue and delivery plan. The creator owns design, scale, major scope and release decisions; the lead owns implementation, integration and technical QA. Conversation is Swedish; project material is English.

**Product:** a Project Zomboid Build 42 Stable map mod. **Scale:** 1:1, including connecting roads. The eventual municipality is a planning horizon, not the next build. Compression requires new evidence and a new creator decision.

## Next delivery and current position

The cottage, deck and garden now connect to the road prototype in a separate synthetic fixture. A bounded metadata compatibility step resolved the official export defect: 25/25 runtime probes, manual light/door/roof checks and clean save/reload pass. Packaging still rejects the defective original export. See [integration evidence](INTEGRATION_TEST.md). The maintained local extraction command reproduces the road and authoring inputs. A small seeded road-edge/vegetation patch now has [game and clean-reload evidence](TERRAIN_TEST.md), including all 172 driveway adjacencies clear for characters. The creator approved **maintained residential plots with flowerbeds, wilder vegetation outside, and vanilla gradual overgrowth** on 2026-10-18. Next is **the first permitted real building and applying this direction to its surroundings**. The open-source building pilot now supplies 13 locally registered candidate outlines; creator-approved 45° grid rotation keeps 1:1 scale. Real-house verification, final selection and vehicle driving remain separate gates.

The unfinished continuous road drive remains a separate technical gate. Give its control problem one focused diagnostic attempt with a new, testable hypothesis; do not repeat unsuccessful input methods while other work is ready. Do not count teleportation as a driving pass.

| Existing result | Evidence | Still open |
| --- | --- | --- |
| Minimal house loads; daylight, switch, walls and roof checked in 42.21.0 | [M0](BUILD42_SPIKE.md), [report](test-reports/M0-BUILD42.md) | Creator acceptance and independent game reproduction |
| Furnished cottage, deck, seating and flowerbeds; four orientations | [Cottage](COTTAGE_TEST.md), [garden](GARDEN_TEST.md), [placements](PLACEMENT_TEST.md) | Creator visual review; library has one rectangular cottage and one optional garden |
| Stable-ID house/orientation/garden choices survive playable regeneration | [Placements](PLACEMENT_TEST.md), [style contract](specs/building-style-overrides.md) | Broader style palette and real-footprint fitting are not connected |
| Cottage/garden/driveway joined to road; seeded small terrain patch, 25/25 fixture probes, 172 clear driveway edges and clean reload; suite now has 68 tests | [Roadside integration](INTEGRATION_TEST.md), [terrain](TERRAIN_TEST.md), [road pipeline](ROAD_PIPELINE.md) | Bounded metadata compatibility stage required; creator review and continuous driving open |
| Separate 5.09 km OSM road prototype; 37 automated tests; 52 runtime road samples across 25 cells | [Road test](ROAD_TEST.md) | Continuous driving, handling through bends and populated-map performance; observed vehicle motion was only 66.47 m |
| Municipality overview, source audit and 1:1 scale decision | [World draft](research/ljungby-world-draft-2026-10-17.md), [scale study](research/road-first-scale-study-2026-10-17.md) | Whole-municipality production is not approved or performance-tested |
| Building/orthophoto applications submitted; alternative sources documented | [Geodata workflow](GEODATA_WORKFLOW.md) | Authenticated portal check on 2026-10-18 shows both applications under review; download approval pending |
| Local source-coverage comparison: 0 Getaboda and 190 Agunnaryd OSM building areas in equal 750 m samples; three Agunnaryd candidates registered reproducibly | [Data feasibility test](research/getaboda-agunnaryd-pilot-2026-10-18.md) | Appearance and residential identity remain unverified. A later Microsoft sample provides 13 Getaboda candidates; both portal applications are under review. No real-house gate passed. |

Existing task IDs remain valid: COTTAGE-01, COTTAGE-02, TOOLS-01 and REVIEW-01 have the technical evidence above and open creator review; OVERRIDE-01 is implemented and reviewed; WORLD-DRAFT-01 remains a planning draft; ROAD-SCALE-01 has an accepted 1:1 pilot. Evidence is not creator approval.

## Test Version 1 — explicit scope

**V1 is the existing Getaboda proof of concept (M3), delivered first as a local/private test package.** It is not the full municipality or a finished survival campaign.

Required:

1. Approximately 4–5 source-confirmed Getaboda buildings, with checked positions/footprints, stable IDs and provenance. Confirm the exact building list with the creator after source review.
2. Connected nearby roads and driveways at 1:1, plus basic source-backed forest/open land/water where present. Unknown measurements and invented details stay labelled assumptions.
3. At least one usable, furnished house with verified entrance, collision, daylight/lighting and roof behavior. Other buildings may be simpler but must be valid and traversable where intended.
4. Swedish 1990s presentation, including a reviewed representative exterior and varied decks/gardens with flowerbeds where appropriate. Generic interiors remain the default.
5. One manual correction survives regeneration, a fresh official export, packaging and an in-game check. Preserve original source data and unrelated building choices.
6. A fresh-save install, save/reload and local walk/drive test pass on a recorded game version. The creator receives a short playtest request, screenshots, instructions and known limitations after agent QA.

The full 5.09 km corridor can accompany V1 once its own driving gate passes; it does not require building Agunnaryd. It stays a separate experimental package if unfinished. Multiplayer, public release, custom survival systems, a large tile catalog and municipality-wide generation are not V1 requirements. A synthetic fixture cannot substitute for source-confirmed Getaboda.

## Phases and exit gates

M0–M4 retain their historical meanings; M5–M7 describe later expansion. Preparation can overlap when dependencies allow. A phase does not finish merely because code or screenshots exist.

| Phase | Outcome and main steps | Exit evidence | Creator involvement / dependency |
| --- | --- | --- | --- |
| **M0 — Technical foundation** | Maintain known-good house, cottage and road fixtures. Resolve control/QA limitations; pin versions; verify clean packages and protect saves. | Recorded game checks, repeatable build/export steps and explicit failures. House checks passed; continuous road driving remains open. | Creator acceptance remains separate. Use proven fixtures for bounded work while closing remaining checks. |
| **M1 — Traceable Getaboda data** | Refresh access; register permitted datasets; select the small area; normalize metric geometry; reconcile roads/buildings/land cover; record gaps and stable identity. Prove one real building first. | Source/CRS/license/hash records; checked first building and agreed building list; local processing; no invented precise footprints. | Data access and handling terms. Creator confirms selection and can supply owned exterior references. |
| **M2 — Reusable Swedish building tools** | Combine cottage/garden with roads; fit the first verified footprint; connect saved choices to playable output; add only Getaboda's required house/outbuilding variants; improve road edges and landscaping. | Integrated fixture, then one real house; usable access, roof and collision; deterministic variation and separate overrides. | Synthetic inputs are usable now. Real fitting depends on M1; creator reviews representative exterior/landscaping. |
| **M3 — Getaboda / Test Version 1** | Assemble 4–5 buildings, roads and basic surroundings; regenerate after an individual correction; run installation, walk/drive, save/reload and visual QA; fix defects. | All V1 requirements above have evidence, followed by recorded creator feedback. | M1 data and sufficient M2 tools. Technical defects remain the lead's responsibility. |
| **M4 — Shareable test and release preparation** | Stabilize V1 after feedback; independently reproduce installation; document package/rights/version support; test private multiplayer separately if selected; prepare GitHub distribution, then Workshop later. | Reproducible package/install; supported compatibility claims; attribution and known issues. Multiplayer requires an actual host/client test. | Creator approves distribution and public release. Singleplayer need not wait for multiplayer. |
| **M5 — Nearby settlements and repeatable expansion** | Select the next bounded area toward Agunnaryd/Södra Ljunga; extend roads, nature and necessary building types; automate demonstrated repeated steps; test regional streaming/travel. | A second area built through the same workflow, preserved overrides, documented manual steps and measured travel/performance. | Getaboda slice and repeatable pipeline; creator selects expansion order and consequential design choices. |
| **M6 — Ljungby pilot** | Select a small urban district; handle denser streets, varied footprints and larger buildings; measure performance and effort before wider city coverage. | Playable district, dense-scene measurements, required urban templates and a reviewed expansion estimate. | Regional workflow proven; creator selects district/scope. Do not build the whole town in one delivery. |
| **M7 — Municipality coverage** | Expand in validated geographic batches; audit road/water continuity and coverage; address gaps; package and maintain supported versions. | Each batch has source, gameplay and regression evidence; a coverage ledger distinguishes complete, simplified and missing areas. | Long-term horizon, gated by capacity and creator priorities. Full coverage and completion date are not promised. |

## Dependency path

`DATA-ACCESS-01 → GETABODA-01 → HOUSE-FIT-01 → GETABODA-ASSEMBLE-01 → V1-QA-01`

`INTEGRATE-01 → HOUSE-FIT-01`; `PIPELINE-01 → GETABODA-ASSEMBLE-01`; `TERRAIN-01 → GETABODA-ASSEMBLE-01`.

`DRIVE-INPUT-01 → ROAD-TEST-01` is a separate validation path. It gates declaring the full corridor tested and regional road expansion, not unrelated building-tool work. Local V1 driving still requires its own actual check.

## Prioritized execution queue

States: **Ready** = no known blocker; **Waiting** = named dependency; **Technical evidence recorded** = specified checks passed, not creator acceptance; **Proposed later** = planning only. Rows are plans, not running agents/background jobs. The lead owns integration throughout.

| Order / ID | State and owner role | Deliverable | Dependency / next action |
| --- | --- | --- | --- |
| 1 · DRIVE-INPUT-01 | Diagnostic attempted; waiting for supported sustained control; QA/lead | Reliable sustained input and steering for an actual driving check | Native API exposes key taps and the new Escape trial did not work. No held accelerate/steer/stop path verified. Retain the gate; do not repeat tap loops. |
| 2 · INTEGRATE-01 | Technical evidence recorded; lead/buildings | Cottage, deck/garden and road access in one synthetic playable fixture | 25/25 runtime probes, manual light/door/roof checks and clean save/reload pass after the bounded metadata stage. Original export remains rejected. Creator acceptance separate; see INTEGRATION_TEST.md. |
| 3 · DATA-ACCESS-01 | Waiting for access outcome; world/data | Current access outcome and smallest permitted acquisition plan | Fresh authenticated Geotorget check on 2026-10-18 shows both applications as Behandlas. A separate Microsoft open-footprint pilot supplies 13 local candidates; see research/getaboda-building-register-2026-10-18.md. No duplicate applications; continue ready work. |
| 4 · PIPELINE-01 | Technical evidence recorded; world/data/lead | Reproduce the corridor from registered local source through maintained code | Bounded local command reproduces all 152 segments and 108 authoring inputs. Repeat output identical; source coverage/access limits documented in ROAD_PIPELINE.md. |
| 5 · TERRAIN-01 | Technical evidence recorded for bounded prototype; buildings/world | Small road-edge/vegetation patch with clear cottage access | Seeded authoring, official export, visible runtime plants/edges, 25/25 fixture probes, 172 clear character adjacencies and clean reload. Vanilla replaces vegetation sprite names. Landscape direction approved on 2026-10-18; detailed visual acceptance and actual vehicle clearance remain open. Real land cover waits for permitted data. |
| 6 · GETABODA-01 | In progress; world/data | One verified building, then the agreed building/road/land-cover subset | Microsoft 2026-08-13 provides 13 locally registered candidate outlines. Repeated import preserves IDs/choices. Creator approved 45° grid rotation; review candidate identity, fitting and the exact V1 list. LM remains pending. |
| 7 · HOUSE-FIT-01 | In progress; buildings/lead | One traceable real house in the game | Generic 8 x 12 variant passed official export, exterior inspection and 12/12 probes after full restart/reload. A roof gap found in r1 was repaired in r2; see [sized cottage evidence](COTTAGE_SIZE_TEST.md). Real candidate placement follows. Review material footprint approximations with the creator. |
| 8 · GETABODA-ASSEMBLE-01 | Waiting; lead | V1 candidate with the agreed buildings and surroundings | Verified subset, HOUSE-FIT-01, PIPELINE-01 and terrain/land-cover integration. Add only required variants. |
| 9 · V1-QA-01 | Waiting; QA/lead | Reproducible, locally installable Getaboda package and creator playtest | GETABODA-ASSEMBLE-01; resolve technical failures before requesting acceptance. |
| Conditional · ROAD-TEST-01 | Waiting for reliable control; QA/lead | Continuous 5.09 km road run | DRIVE-INPUT-01. Keep [existing evidence](ROAD_TEST.md); resume when control is available. |
| Review · DESIGN-REVIEW-01 | Landscape direction accepted 2026-10-18; creator with lead | Exterior, garden and road-edge direction | Maintained residential plots with flowerbeds, freer road-edge/forest-margin vegetation outside, then vanilla gradual overgrowth. Apply within agreed scope without reopening this choice. Exterior likeness, exact detail and milestone acceptance remain separate reviews. |

### Near-term acceptance checks and boundaries

**DRIVE-INPUT-01**
- Demonstrate repeated accelerate, turn, brake and stop actions in the actual game through supported tools; record method/version and position/heading evidence.
- Use ordinary vehicle physics. Teleporting or directly setting position/orientation is not a steering test.
- If unsuccessful, record the blocker, hypothesis and condition to resume. No indefinite input experiments or general automation framework.

**INTEGRATE-01**
- Fresh map contains one explicitly fictional cottage, its saved orientation/garden choice, a clear driveway and connection to the road.
- Walk between road, garden and house; verify entrance, collision, lighting and roof after integration. Preserve existing separate fixtures/saves.
- Change one placement choice, regenerate/export and verify it without altering source geometry. Capture game screenshots. No verified-real-location claim.

**DATA-ACCESS-01 / GETABODA-01**
- Record access outcome, permitted use and local storage. No raw geodata/source imagery enters cloud/model output under the current handling decision.
- Retain source IDs, snapshot, CRS, license and hashes; validate one building against its source and record unknown appearance separately.
- Confirm the bounded building list/coverage before assembly. No new paid service, duplicate application or interpretation of missing OSM buildings as empty land.

**PIPELINE-01**
- Reproduce corridor/provenance from the same registered local snapshot with a documented command; preserve raw input bytes.
- Test connectivity, projection, missing attributes, access/direction handling and unsupported crossings with synthetic fixtures; report uncertain source completeness.
- Keep official export explicit and package validation mandatory. No all-Sweden importer, hidden cloud transfer or replacement for the official exporter.

**TERRAIN-01**
- Produce one deterministic playable patch with softened road edges, grass/vegetation and unobstructed driveway/door access using permitted assets.
- Inspect vehicle/character clearance and the actual game view; record the seed and distinguish synthetic styling from source-backed land cover.
- Show representative before/after images for design review. No whole-corridor decoration before the small pattern works.

**HOUSE-FIT-01 / GETABODA-ASSEMBLE-01**
- Preserve source footprint, stable ID and provenance separately from grid approximation; document fitting limits instead of forcing every house into the current rectangle.
- Prove the first house's access, interior and roof before adapting the remaining buildings. Unverified decks/gardens remain varied design choices.
- Assemble source-backed roads/land cover, clear access and only required variants; inspect seams in-game. No detailed private interiors without review.

**ROAD-TEST-01 / V1-QA-01**
- Road gate: drive the whole route without teleports; check surfaces, bends and cell boundaries; record elapsed time and loading/stutter observations. Investigate stalls rather than hiding them behind average FPS.
- V1 gate: fresh install/spawn, required house checks, local walk/drive and save/reload; record version, artifact hash, logs, screenshots and defects. Demonstrate one surviving correction in the regenerated playable artifact.
- Remove QA helpers, verify installed/package parity and provide known limits plus a short creator playtest. No public release, multiplayer claim or save-compatibility guarantee from singleplayer checks.

## Working rhythm and blocker policy

1. At the start of an active development session, inspect Git and this queue; select one bounded result and its evidence. Keep one active integration task and at most one secondary ready task.
2. Implement, test, officially export where needed, verify in-game and review. Each delivery should leave a playable improvement or necessary reproducible tool result, not only another planning document.
3. For a blocker, record failure, evidence, next distinct hypothesis and exit condition. After one focused diagnostic session without progress, choose the next ready independent task. Keep the failed gate open; do not transfer technical acceptance to the creator.
4. Data delays block real-data integration only. Synthetic integration, reproducible extraction and small terrain prototypes continue. Pending visual/release approval does not stop unrelated reversible work.
5. At each delivery, update this queue, evidence and the human overview. Report changes, actual passes, open checks and next action. Send Swedish updates and game screenshots at meaningful points during active work.
6. Delegate specialist roles when explicitly authorized and useful, with bounded ownership, separate worktrees for concurrent writers and one operator for shared game/editor resources. A role label does not mean an agent is running. This plan creates no schedule or unattended execution.

## Creator decisions and planning horizon

The creator clarified the personal goal on 2026-10-18: a surprise reunion for a former PZ group from Ljungby/Agunnaryd. Approximately ten selected homes across the expanding world deserve extra exterior/interior care; ordinary houses use plausible templates. Select those homes and their recognition details with the creator as the relevant areas enter scope. The V1 building count and next integration delivery remain unchanged.

Rural hunting firearms are accepted fictional gameplay direction, with loot frequency and balance still to be designed. Tractors are desired conditional content; [initial research](PROJECT_SPEC.md#tractor-feasibility-check) found a mod candidate, not a validated dependency. Schedule a bounded vehicle test before adoption. Private multiplayer remains the eventual friends-play goal and requires the M4 host/client evidence before claiming readiness.

| When | Creator decision | Independent work that continues |
| --- | --- | --- |
| Representative previews | Exterior palette, recognizable likeness, garden/road-edge character | Reversible prototypes, geometry validation and QA |
| Verified source subset | Which 4–5 buildings define V1; material footprint approximations | Tool tests and supported fixture improvements |
| V1 passes agent QA | Playtest feedback/acceptance and next bounded area | Defect fixes and packaging preparation |
| Before distribution | Private/public release scope, then any Workshop publication | Local tests and release preparation |
| Measured regional/urban pilots | Expansion order, travel feel/performance, any reconsideration of 1:1 | Source preservation and measured prototypes |

Do not assign a calendar release date from task count. Re-estimate V1 after the first real house works and the data-access outcome is known, using observed effort and remaining blockers. Later-phase dates stay unset until their representative pilot exists. Listing future options does not authorize purchases, new regions or new design commitments.

## Completion and regression rules

- Distinguish implementation, automated checks, official export, game verification, creator acceptance and release approval. Do not collapse these into one done marker.
- Run relevant tests and required project checks for game/source changes. Documentation updates need link/status/overview and whitespace checks, not a new gameplay claim.
- Preserve tested artifacts/versions. Recheck affected fixtures after shared building/road/export changes; a game update requires compatibility checks before claiming support.
- Do not expand coverage to hide correctness, performance or rights issues. Keep a small known-good fixture and restore path.
- GitHub issues may hold approved discussions using these IDs; this file remains the ordered queue. Do not create a second unsynchronized backlog or auto-close parent issues.
