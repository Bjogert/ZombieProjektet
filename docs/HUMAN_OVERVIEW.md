# ZombieProjektet — project overview

**Status (2026-10-17):** the synthetic test house and furnished cottage have been agent-tested in Project Zomboid Build 42.21.0. A new four-house test map now rotates the cottage, wooden deck, outdoor furniture and three flowerbeds together. All 92 runtime checks and manual entry/exit checks passed. Saved house, orientation and optional garden choices survive regeneration; repeated official export produced an identical package. Creator acceptance and exterior approval remain open. This is not yet the Getaboda map.

## What are we building?
A recognizable Swedish world in Project Zomboid. Start with about 4–5 source-confirmed Getaboda buildings, nearby roads and nature, with Swedish 1990s styling and generic interiors where details are unavailable. Later, expand toward Ljungby and test multiplayer with friends.

## How we work
The creator sets creative direction and important choices. The lead agent implements, tests, fixes and coordinates technical work. Specialist tasks cover world data, buildings/art and QA when useful and authorized. Conversation is in Swedish; project material is in English.

Getaboda and the worldbuilding tools are developed openly with the creator. Updates can show layouts, houses, gardens and screenshots, and explain how source data becomes a playable map. The lead handles routine work while the creator participates in design and important choices. Later areas retain surprise by default. Full developer evidence remains available, and bugs are always disclosed.

The lead assigns bounded work, checks the results and integrates changes. Separate stable-ID house, orientation and garden choices now produce a reproducible playable synthetic map. Independent code/source review found no blockers. The older style-only manifest's broader palette and fitting templates to real geometry remain future integration work. The mapping tools and game have one operator at a time.

## Next deliveries
1. Creator playtest of the repaired test house; agent lighting, collision and roof checks have passed.
2. Review the cottage, deck, seating and flowerbeds in the new in-game screenshots. Four orientations are game-tested; the current library supports one rectangular cottage and one optional garden. See [PLACEMENT_TEST](PLACEMENT_TEST.md).
3. Verify lawful Getaboda data and integrate the first real buildings.
4. Adapt the tested placement workflow to verified house geometry and extend the visual library after creator review. Broader facade colors are not yet playable.

Agents resolve technical issues before requesting milestone playtests. Creator playtests focus on feel and usability; acceptance is recorded only after actual feedback.

## Getaboda data research
The source audit found 2025 aerial imagery catalog coverage at 16 cm pixel size and a municipal building download from Lantmäteriet. The Geotorget account is active; both building and orthophoto applications have been received and are being processed. Access decisions are pending. Raw geodata and imagery will initially be processed locally in Sweden; cloud/AI uploads await clarification of the conditions. OSM has roads but no building objects in the checked 750 m radius. Actual house dimensions and facade colors remain unverified. The [automation workflow](GEODATA_WORKFLOW.md) preserves source facts, assumptions and individual corrections separately.

## Established direction
- Modern source geography with Swedish 1990s atmosphere.
- Decks/patios and gardens with flowerbeds as part of residential character, varied between houses.
- Getaboda at local 1:1 scale; countryside distance compression later.
- Source-backed land cover with deterministic detail placement.
- Generic interiors; review detailed private homes before publication.
- Free tools by default; GitHub packages first, Steam Workshop later.
- Development saves may need restarting; protect valuable existing saves.

## Feedback
The HTML companion lets you record a suggestion and your comment, then copy it or open a prefilled GitHub issue. Feedback stays in your browser until you send it. It does not automatically change project decisions or files.

Useful feedback: a desired atmosphere, a preferred example exterior, or observations from a requested playtest. Routine implementation choices remain with the agent.
