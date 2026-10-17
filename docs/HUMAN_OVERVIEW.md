# ZombieProjektet — project overview

**Status (2026-10-17):** the synthetic map has been tested in Project Zomboid Build 42.21.0. Lighting is fixed; wall collision and roof coverage/rendering pass agent checks. Creator acceptance remains open. The first reusable cottage is now a BuildingEd prototype; its game test is next. This is not yet the Getaboda map.

## What are we building?
A recognizable Swedish world in Project Zomboid. Start with about 4–5 source-confirmed Getaboda buildings, nearby roads and nature, with Swedish 1990s styling and generic interiors where details are unavailable. Later, expand toward Ljungby and test multiplayer with friends.

## How we work
The creator sets creative direction and important choices. The lead agent implements, tests, fixes and coordinates technical work. Specialist tasks cover world data, buildings/art and QA when useful and authorized. Conversation is in Swedish; project material is in English.

Routine updates and design previews preserve surprises. Full developer evidence remains available, and bugs are always disclosed. The creator should be able to enjoy playing without reviewing every room or implementation detail.

## Next deliveries
1. Creator playtest of the repaired test house; agent lighting, collision and roof checks have passed.
2. Refine and game-test the first reusable Swedish cottage, then review its representative exterior together.
3. Verify lawful Getaboda data and integrate the first real buildings.
4. Demonstrate that individual corrections survive regeneration.

Agents resolve technical issues before requesting milestone playtests. Creator playtests focus on feel and usability; acceptance is recorded only after actual feedback.

## Getaboda data research
The source audit found 2025 aerial imagery catalog coverage at 16 cm pixel size and a municipal building download from Lantmäteriet. The Geotorget account is active; the building application is being processed and the orthophoto application remains a draft. Raw geodata and imagery will initially be processed locally in Sweden; cloud/AI uploads await clarification of the conditions. OSM has roads but no building objects in the checked 750 m radius. Actual house dimensions and facade colors remain unverified. The [automation workflow](GEODATA_WORKFLOW.md) preserves source facts, assumptions and individual corrections separately.

## Established direction
- Modern source geography with Swedish 1990s atmosphere.
- Getaboda at local 1:1 scale; countryside distance compression later.
- Source-backed land cover with deterministic detail placement.
- Generic interiors; review detailed private homes before publication.
- Free tools by default; GitHub packages first, Steam Workshop later.
- Development saves may need restarting; protect valuable existing saves.

## Feedback
The HTML companion lets you record a suggestion and your comment, then copy it or open a prefilled GitHub issue. Feedback stays in your browser until you send it. It does not automatically change project decisions or files.

Useful feedback: a desired atmosphere, a preferred example exterior, or observations from a requested playtest. Routine implementation choices remain with the agent.
