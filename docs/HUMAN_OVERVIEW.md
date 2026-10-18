# ZombieProjektet — project overview

**Evidence reviewed (2026-10-18):** the roadside cottage, deck, flowerbeds and driveway pass 25/25 runtime probes, manual light/door/roof checks and clean save/reload in Build 42.21.0. A bounded compatibility stage corrects the official export's room metadata; packaging still rejects the original failure. Local road extraction reproduces the 5.09km corridor and identical authoring inputs. A small seeded vegetation/road-edge patch also passes game inspection and clean reload; all 172 driveway adjacencies are clear for characters. The suite has 72 passing tests with geodata dependencies available. This is a synthetic playable fixture; creator acceptance and the real Getaboda map remain separate. See [integration evidence](INTEGRATION_TEST.md), [terrain verification](TERRAIN_TEST.md) and the [road pipeline](ROAD_PIPELINE.md).

**New provisional Getaboda result:** one registered 8 by 12 candidate now has a playable generic house, deck, flowerbeds and assumed access to about 266 m of the registered village road. Official export and 17/17 runtime probes pass, including after full restart/reload; normal door use, walking to the road and the exterior roof were checked. The bounded landscape variant adds road edges and vegetation, passes 19/19 probes and loads cleanly without QA. Identity, likeness and the final V1 subset remain open. Better owned photos can refine appearance later; reversible work continues now. The creator finds this enlarged house barn-like, so residential proportions, entrances and plot character take priority over more scaled copies. The [Småland pattern study](research/smaland-houses-2026-10-18.md) proposes distinct croft, summer cottage and country house families; these are not yet new playable assets. See [candidate pilot evidence](CANDIDATE_PILOT_TEST.md).

## What are we building?
A recognizable Swedish world in Project Zomboid. Start with about 4–5 source-confirmed Getaboda buildings, nearby roads and nature, with Swedish 1990s styling and generic interiors where details are unavailable. Later, expand toward Ljungby and test multiplayer with friends.

## Why this world matters
The creator wants to reunite a former PZ group from Ljungby/Agunnaryd and surprise friends with familiar places. Approximately ten personally important homes across the expanding world receive extra exterior/interior care; the rest use plausible, varied Swedish templates. V1 still starts with roughly 4–5 Getaboda buildings. Getaboda remains open development with the creator.

Rural hunting firearms are planned as fictional gameplay loot, with frequency and balance still open. Tractors are desired; a Build 42 mod candidate has been found but has not been installed or tested with our game version or multiplayer. See the [specification](PROJECT_SPEC.md) for the evidence and remaining choices.

## How we work
The creator sets creative direction and important choices. The lead agent implements, tests, fixes and coordinates technical work. Specialist tasks cover world data, buildings/art and QA when useful and authorized. Conversation is in Swedish; project material is in English.

Getaboda and the worldbuilding tools are developed openly with the creator. Updates can show layouts, houses, gardens and screenshots, and explain how source data becomes a playable map. The lead handles routine work while the creator participates in design and important choices. Later areas retain surprise by default. Full developer evidence remains available, and bugs are always disclosed.

The lead assigns bounded work, checks the results and integrates changes. Separate stable-ID house, orientation and garden choices now produce a reproducible playable synthetic map. Independent code/source review found no blockers. The older style-only manifest's broader palette and fitting templates to real geometry remain future integration work. The mapping tools and game have one operator at a time.

## Next deliveries
1. Apply the accepted landscape direction: maintained residential plots with flowerbeds at game start, freer vegetation along roads and forest margins outside, then vanilla gradual overgrowth (approved 2026-10-18). The synthetic prototype and a provisional candidate with bounded vegetation/road edges are verified in-game. First improve the compact dwelling, entrance, window rhythm and one boundary/shrub treatment; then extend only the required building variants while identity and appearance are verified. Exact visual details and vehicle clearance remain separate checks.
2. Resume the continuous road drive when a supported sustained steering method is available. The bounded input diagnostic did not establish one; this remains a separate gate.
3. Review the 13 local building candidates and confirm the V1 subset. Validate one real building while the Lantmäteriet applications remain under review. The first provisional fit has game evidence; better photos will refine its appearance.
4. Add required building variants and provisional surroundings, then assemble the creator-confirmed Getaboda subset and run V1 installation, regeneration and game checks.

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
The source audit found 2025 aerial imagery catalog coverage at 16 cm pixel size and a municipal building download from Lantmäteriet. The refreshed Geotorget case view on 2026-10-18 shows both applications as Behandlas (under review). Authentication works; download approval is still pending. Raw geodata and imagery will initially be processed locally in Sweden; cloud/AI uploads await clarification of the conditions. OSM has roads but no building objects in the checked 750 m radius. A separate Microsoft open-footprint sample now provides 13 locally registered candidates with estimated dimensions. The creator approved a 45-degree grid rotation at 1:1. Residential identities, facade colors and the exact V1 subset remain unverified. The [automation workflow](GEODATA_WORKFLOW.md) preserves source facts, assumptions and individual corrections separately.

## Data feasibility pilot
The [2026-10-18 data feasibility test](research/getaboda-agunnaryd-pilot-2026-10-18.md) compared equal 750 m samples: the cached OSM source has 0 building areas in Getaboda and 190 in Agunnaryd, with no checked appearance/height tags in either sample. Three generic Agunnaryd building candidates were registered in a local experiment; repeating it preserved IDs and left missing appearance unknown. Getaboda remains the playable target. Heritage-site image records are promising leads, with rights and building matches still open. A later authenticated portal check shows both applications under review.

The [local Getaboda register](research/getaboda-building-register-2026-10-18.md) preserves source geometry, license, IDs and separate choices. A nearby-road diagnostic finds the main road but no mapped driveways; missing data stays explicit. The [8 by 12 cottage test](COTTAGE_SIZE_TEST.md) records the roof regression, repair and game evidence. This is still a generic component, not a finished real house.

## Municipality planning draft
A first geographic overview of the whole Ljungby municipality is available for creator review, using SCB's generalized boundary and locally processed OpenStreetMap roads, lakes and settlement points. It preserves actual distances and proposes Getaboda, nearby settlements and Ljungby as successive development anchors. This is a planning view, not a playable map or an approved whole-municipality delivery. The [source audit and scale proposal](research/ljungby-world-draft-2026-10-17.md) compares additional data channels and records the remaining choices.

The [road-first scale study](research/road-first-scale-study-2026-10-17.md) compares the installed vanilla map's approximately 20 × 16 km bounding extent with the municipality's 61 × 51 km extent, using one game square as approximately one metre. The creator approved a 1:1 Getaboda–Agunnaryd driving corridor. Its 5.09 km road geometry is installed as a separate test map. Vehicle start/motion and 52 sampled road positions passed game checks; continuous end-to-end driving remains open. See the [road test evidence](ROAD_TEST.md). Road widths are provisional. Most surroundings remain plain; only the bounded roadside cottage sample has added vegetation. Compression is deferred until driving evidence supports a decision.

## Established direction
- Modern source geography with Swedish 1990s atmosphere.
- Gable roofs with two slopes and vertical gable ends by default for Getaboda/Agunnaryd dwellings (creator correction, 2026-10-18). Single-pitch roofs remain separately chosen garage or supported modern/funkis exceptions.
- Decks/patios and gardens with flowerbeds as part of residential character, varied between houses. Start with maintained plots and wilder vegetation outside; use vanilla gradual overgrowth (approved 2026-10-18).
- Start at 1:1, including connecting roads; use the approved 45-degree Getaboda grid rotation. Reconsider countryside compression after driving and performance tests.
- Source-backed land cover with deterministic detail placement.
- Generic interiors by default; extra care for approximately ten selected homes across the expanding project. Review detailed private homes before publication.
- Free tools by default; GitHub packages first, Steam Workshop later.
- Development saves may need restarting; protect valuable existing saves.

## Feedback
The HTML companion lets you record a suggestion and your comment, then copy it or open a prefilled GitHub issue. Feedback stays in your browser until you send it. It does not automatically change project decisions or files.

Useful feedback: a desired atmosphere, a preferred example exterior, or observations from a requested playtest. Routine implementation choices remain with the agent.
