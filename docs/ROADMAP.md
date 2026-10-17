# Roadmap — evidence-based small milestones

**Chosen:** Project Zomboid Build 42 Stable map mod. **Not building:** standalone game.

## Current execution queue (2026-10-17)

This queue refines the milestones below. `Ready` means the task has no known external prerequisite; it does not mean it is running. The lead records assignments and evidence when work begins or finishes. No worker agents or recurring jobs are started by this file.

| Task | State | Role and delivery | Completion evidence |
| --- | --- | --- | --- |
| WORLD-DRAFT-01 | Geographic draft prepared; creator review open | Municipality overview and alternative-source audit requested by the creator | SCB boundary and local OSM extract, geographic scale retained; [research and open scale choices](research/ljungby-world-draft-2026-10-17.md). This does not expand the next playable milestone to the whole municipality |
| ROAD-SCALE-01 | Scale study complete; 1:1 driving pilot approved | Compare installed vanilla-map extent with the municipality and preview the mapped road network | [Road-first study](research/road-first-scale-study-2026-10-17.md): local game metadata, same-scale road preview, missing attributes recorded. The creator selected 1:1; compression remains deferred |
| ROAD-TEST-01 | Playable prototype installed; continuous driving QA open | Lead: 5.09 km Getaboda–Agunnaryd corridor in a separate map | 37 tests, official export, vehicle start/motion, 52 road-floor probes across 25 runtime cells and game screenshots. Reliable steering and a continuous end-to-end trip remain open; [ROAD_TEST](ROAD_TEST.md) |
| TOOLS-01 | Agent checks passed; creator review open | Four cottage orientations, rotated gardens and stable per-building choices in a separate synthetic map | 32 automated tests, 92 runtime probes, manual entry/exit in all four orientations and byte-identical repeated WorldEd export/package; [PLACEMENT_TEST](PLACEMENT_TEST.md) |
| COTTAGE-01 | Agent checks passed; creator review open | Furnished fictional cottage in its own synthetic test package | Official WorldEd export, 11 runtime probes, entrance/window/light interaction and exterior roof checks pass in 42.21.0; [COTTAGE_TEST](COTTAGE_TEST.md) |
| COTTAGE-02 | Agent checks passed; creator review open | Wooden deck, seating and three flowerbeds in a separate fictional cottage test | Deterministic relative-coordinate layout, official export, 7 garden and 11 cottage runtime probes, manual walking and screenshots in 42.21.0; [GARDEN_TEST](GARDEN_TEST.md) |
| OVERRIDE-01 | Implemented, tested and reviewed | Separate manual style overrides by stable synthetic building ID | Integrated as `b24eedd`; repeatability, reordered input, unrelated buildings and unchanged inputs verified; invalid values/IDs fail before output. [Contract](specs/building-style-overrides.md) |
| REVIEW-01 | Code and saved-evidence review passed | Independent read-only review of both changes | No blocking findings; M0 TMX output remains byte-identical. Logs, screenshots, package hash, source copy and installed-file parity reviewed. This is not independent game reproduction; creator acceptance stays open |
| GETABODA-01 | Waiting for access decisions and permitted handling | World/data plus lead: obtain the approved local subset and measure one traceable building | Source IDs/CRS/terms retained; unknown appearance left unknown; handling and publication conditions checked before sharing derived output |

**COTTAGE-01 boundary:** start from `assets/buildings/swedish_cottage_01.tbx` and its README. Keep the known-good M0 test fixture and valuable saves intact. Use permitted stock resources and generic interiors. Record any export/manual steps; an editor screenshot alone does not pass the game checks. This work does not require real map data.

**COTTAGE-02 boundary:** the creator requested decks/patios and gardens with flowerbeds as part of the Swedish feel. Start with a small generic outdoor setting for the fictional test cottage using permitted stock resources. Keep routes and usable openings clear; vary later templates instead of attaching an identical garden to every house. These are design choices, not observations of real Getaboda properties. Deliver actual in-game screenshots; do not present the current bare test lawn as completed landscaping.

**OVERRIDE-01 boundary:** extend `tools/building_styles.py`, `tests/test_building_styles.py` and synthetic example inputs. Use stable fixture IDs and a separate override file with manual values taking precedence over generated style defaults. Start with style selection only; no geometry edits, GIS downloads, game exporter, UI or automatic real-world identity matching. Passing this task proves the manifest behavior; persistence in a regenerated playable map remains a later M3 check.

**While waiting:** the cottage, deck/flowerbed garden and synthetic override deliveries have passed agent checks. TOOLS-01 now preserves separate per-ID house, quarter-turn and optional garden choices in actual PZW/TMX output, with a reproducible game-tested four-house package. Review the new in-game screenshots with the creator. Adapting templates to verified Getaboda geometry and connecting the broader style palette remain future work; only one rectangular cottage and garden are supported. Develop Getaboda and the tools openly, including layouts and technical explanations; preserve surprises in later areas. The two Geotorget applications are being processed; no new application is needed. M0 creator acceptance and independent game reproduction remain open.

## M0 — Prove a custom Build 42 map really loads (IN PROGRESS)
See [BUILD42_SPIKE.md](BUILD42_SPIKE.md).

As of 2026-10-17, world selection, indoor spawn, doorway traversal, closed-door daylight and the light switch have been agent-tested in 42.21.0. All four wall collision probes pass in the running game. All 80 room squares have an upper floor and are classified indoors; the roof renders outdoors. Creator acceptance and independent reproduction remain open. The first reusable cottage is now a furnished, separately playable early M2 prototype with agent game checks passed; design review remains. Real building geometry has not yet been verified. The separate road prototype is tracked in ROAD-TEST-01.

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
- Begin settlements around Agunnaryd/Södra Ljunga at the approved 1:1 scale. Reconsider compression only after driving evidence and a new creator decision.

## Completion rules
A milestone is not done until its acceptance evidence is documented. Python unit tests support data-stage claims but **cannot** prove working in-game maps. Keep source geodata independent from world projection and game assets. Do not commit copyrighted proprietary content.
