# Roadmap — evidence-based small milestones

**Chosen:** Project Zomboid Build 42 Stable map mod. **Not building:** standalone game.

## Current execution queue (2026-10-17)

This queue refines the milestones below. `Ready` means the task has no known external prerequisite; it does not mean it is running. The lead records assignments and evidence when work begins or finishes. No worker agents or recurring jobs are started by this file.

| Task | State | Role and delivery | Completion evidence |
| --- | --- | --- | --- |
| COTTAGE-01 | Ready; next main delivery | Buildings/art, with the lead operating shared tools: furnish and export the existing fictional cottage into a separate synthetic test map | New package loads in the recorded Build 42 version; usable entrance, windows, lighting, wall collision and roof checks; logs and one representative exterior preview |
| OVERRIDE-01 | Ready; independent code task | World/data: preserve a manually chosen building style across manifest regeneration using synthetic fixtures | Two identical runs; input reordering preserves results; changing one building leaves others stable; invalid style and unmatched IDs reported; source geometry and override input unchanged |
| REVIEW-01 | Waiting for the relevant implementation | QA: review COTTAGE-01 and OVERRIDE-01 against their actual evidence | Findings resolved or explicitly retained; automated, editor and in-game claims distinguished; creator acceptance stays separate |
| GETABODA-01 | Waiting for access decisions and permitted handling | World/data plus lead: obtain the approved local subset and measure one traceable building | Source IDs/CRS/terms retained; unknown appearance left unknown; handling and publication conditions checked before sharing derived output |

**COTTAGE-01 boundary:** start from `assets/buildings/swedish_cottage_01.tbx` and its README. Keep the known-good M0 test fixture and valuable saves intact. Use permitted stock resources and generic interiors. Record any export/manual steps; an editor screenshot alone does not pass the game checks. This work does not require real map data.

**OVERRIDE-01 boundary:** extend `tools/building_styles.py`, `tests/test_building_styles.py` and synthetic example inputs. Use stable fixture IDs and a separate override file with manual values taking precedence over generated style defaults. Start with style selection only; no geometry edits, GIS downloads, game exporter, UI or automatic real-world identity matching. Passing this task proves the manifest behavior; persistence in a regenerated playable map remains a later M3 check.

**While waiting:** prioritize the cottage and synthetic override task. The two Geotorget applications are being processed; no new application is needed. The creator can review a representative exterior without seeing real Getaboda interiors or future discoveries. M0 creator acceptance and independent reproduction remain open.

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
