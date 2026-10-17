# Roadmap — evidence-based small milestones

**Chosen:** Project Zomboid Build 42 Stable map mod. **Not building:** standalone game.

## M0 — Prove a custom Build 42 map really loads (IN PROGRESS)
See [BUILD42_SPIKE.md](BUILD42_SPIKE.md).

As of 2026-10-17, world selection, indoor spawn, doorway traversal, closed-door daylight and the light switch have been agent-tested in 42.21.0. All four wall collision probes pass in the running game. All 80 room squares have an upper floor and are classified indoors; the roof renders outdoors. Creator acceptance and independent reproduction remain open. The first reusable cottage is now an early M2 BuildingEd prototype; game integration, furnishing and design review remain. Real geography has not yet been verified.

- Identify the exact installed Build 42 Stable version and supported official/community mapping toolchain using current primary sources and local proof.
- Create minimal separate test map, a usable door and one simple building.
- Launch game, select/spawn on map, walk into house, check collision and errors.
- Save proof: tool versions, commands/manual steps, logs/screenshots, paths and limitations.
- If blocked: smallest reproduction, precise blocker, then choose an alternative. Do not invent a working exporter.

## M1 — Source-backed Getaboda data
- Retrieve permissible real source geometries for Getaboda (without guessing coordinates); inspect all expected houses and roads against available data.
- Preserve source CRS, IDs, license/provenance and normalized projections.
- Add tests for repeatability, invalid/missing geometries and attribution.
- Establish small manually correctable data file and compare run to baseline.

## M2 — Swedish style/interior library
- Expand deterministic style manifest into a minimal typed Swedish exterior/interior template library.
- Add one simple custom original red wall/white-corner asset only after its usage pipeline is verified; reuse permitted game resources meanwhile.
- Implement a simple playable rule-based interior, validated via game.
- Add individual override keyed by building ID with regression test showing it survives regeneration.

## M3 — Getaboda POC
- Combine 4–5 source-confirmed buildings, nearby roads and land cover in separate Swedish map.
- Confirm Getaboda local 1:1 within grid constraints.
- Prove load/entry/collision in current Build 42, rerun/override persistence, reproducible mod package and setup instructions.

## M4 — Small public test
- Generate zip for GitHub Releases; test installation and errors with friends.
- Later confirm Steam Workshop rules, multiplayer and save file behavior.
- Begin settlements around Agunnaryd/Södra Ljunga; implement constrained rural-distance compression only with continuity tests.

## Completion rules
A milestone is not done until its acceptance evidence is documented. Python unit tests support data-stage claims but **cannot** prove working in-game maps. Keep source geodata independent from world projection and game assets. Do not commit copyrighted proprietary content.
