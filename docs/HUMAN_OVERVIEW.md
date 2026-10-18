# ZombieProjektet — project overview

**Evidence reviewed (2026-10-18):** the synthetic test house and furnished cottage have been agent-tested in Project Zomboid Build 42.21.0. A new four-house test map now rotates the cottage, wooden deck, outdoor furniture and three flowerbeds together. All 92 runtime checks and manual entry/exit checks passed. Saved house, orientation and optional garden choices survive regeneration; repeated official export produced an identical package. Creator acceptance and exterior approval remain open. This is not yet the Getaboda map.

## What are we building?
A recognizable Swedish world in Project Zomboid. Start with about 4–5 source-confirmed Getaboda buildings, nearby roads and nature, with Swedish 1990s styling and generic interiors where details are unavailable. Later, expand toward Ljungby and test multiplayer with friends.

## How we work
The creator sets creative direction and important choices. The lead agent implements, tests, fixes and coordinates technical work. Specialist tasks cover world data, buildings/art and QA when useful and authorized. Conversation is in Swedish; project material is in English.

Getaboda and the worldbuilding tools are developed openly with the creator. Updates can show layouts, houses, gardens and screenshots, and explain how source data becomes a playable map. The lead handles routine work while the creator participates in design and important choices. Later areas retain surprise by default. Full developer evidence remains available, and bugs are always disclosed.

The lead assigns bounded work, checks the results and integrates changes. Separate stable-ID house, orientation and garden choices now produce a reproducible playable synthetic map. Independent code/source review found no blockers. The older style-only manifest's broader palette and fitting templates to real geometry remain future integration work. The mapping tools and game have one operator at a time.

## Next deliveries
1. Make one focused attempt to resolve sustained vehicle steering and finish the continuous road test. Keep it open if the control method is still unavailable.
2. Connect one cottage, its deck/garden and road access in a separate synthetic playable fixture. This is the next visible build; it does not claim a real Getaboda house location.
3. Refresh the submitted data applications and validate the first permitted real building. While waiting, make the local road extraction reproducible and prototype a small road-edge/vegetation patch.
4. Fit one verified house, then assemble the agreed Getaboda subset and run V1 installation, regeneration and game checks.

The lead moves to ready independent work after a bounded diagnostic session without progress, while retaining the failed gate. Agents resolve technical issues before requesting milestone playtests; creator feedback focuses on feel, design and acceptance.

## Delivery roadmap
The [full roadmap](ROADMAP.md) contains dependencies, task owners, acceptance checks and blocker handling.

| Phase | Delivery |
| --- | --- |
| M0 | Maintain the technical foundation and close remaining QA gaps |
| M1 | Verify Getaboda sources, first building and the agreed small subset |
| M2 | Integrate roads, houses and gardens; adapt only the required templates |
| M3 | Test Version 1: roughly 4–5 real Getaboda buildings, nearby roads and basic nature |
| M4 | Stabilize the shareable test; independently reproduce installation; prepare approved distribution and later multiplayer |
| M5 | Extend to nearby settlements through the same measured, repeatable workflow |
| M6 | Build and measure a small Ljungby urban pilot |
| M7 | Expand municipality coverage in separately validated batches |

V1 is a local/private Getaboda POC. It requires at least one usable furnished house, verified basic surroundings and a manual correction that survives playable regeneration. The full 5.09 km road can accompany it once its own driving gate passes. Agunnaryd buildings, multiplayer and municipality-wide coverage are later work. Re-estimate timing after the first real house and data-access outcome; no calendar release date is promised now.

## Getaboda data research
The source audit found 2025 aerial imagery catalog coverage at 16 cm pixel size and a municipal building download from Lantmäteriet. At the last access check on 2026-10-17, the Geotorget account was active and both building and orthophoto applications had been received; decisions were pending. Refresh that status when starting data acquisition. Raw geodata and imagery will initially be processed locally in Sweden; cloud/AI uploads await clarification of the conditions. OSM has roads but no building objects in the checked 750 m radius. Actual house dimensions and facade colors remain unverified. The [automation workflow](GEODATA_WORKFLOW.md) preserves source facts, assumptions and individual corrections separately.

## Municipality planning draft
A first geographic overview of the whole Ljungby municipality is available for creator review, using SCB's generalized boundary and locally processed OpenStreetMap roads, lakes and settlement points. It preserves actual distances and proposes Getaboda, nearby settlements and Ljungby as successive development anchors. This is a planning view, not a playable map or an approved whole-municipality delivery. The [source audit and scale proposal](research/ljungby-world-draft-2026-10-17.md) compares additional data channels and records the remaining choices.

The [road-first scale study](research/road-first-scale-study-2026-10-17.md) compares the installed vanilla map's approximately 20 × 16 km bounding extent with the municipality's 61 × 51 km extent, using one game square as approximately one metre. The creator approved a 1:1 Getaboda–Agunnaryd driving corridor. Its 5.09 km road geometry is installed as a separate test map. Vehicle start/motion and 52 sampled road positions passed game checks; continuous end-to-end driving remains open. See the [road test evidence](ROAD_TEST.md). Road widths are provisional, and surrounding terrain is plain. Compression is deferred until driving evidence supports a decision.

## Established direction
- Modern source geography with Swedish 1990s atmosphere.
- Decks/patios and gardens with flowerbeds as part of residential character, varied between houses.
- Start at 1:1, including connecting roads; reconsider countryside compression after driving and performance tests.
- Source-backed land cover with deterministic detail placement.
- Generic interiors; review detailed private homes before publication.
- Free tools by default; GitHub packages first, Steam Workshop later.
- Development saves may need restarting; protect valuable existing saves.

## Feedback
The HTML companion lets you record a suggestion and your comment, then copy it or open a prefilled GitHub issue. Feedback stays in your browser until you send it. It does not automatically change project decisions or files.

Useful feedback: a desired atmosphere, a preferred example exterior, or observations from a requested playtest. Routine implementation choices remain with the agent.
