# Roadmap — evidence-based small milestones

**Chosen:** Project Zomboid Build 42 Stable map mod. **Not building:** standalone game.

## Current execution queue (2026-10-17)

This queue refines the milestones below. `Ready` means the task has no known external prerequisite; it does not mean it is running. The lead records assignments and evidence when work begins or finishes. No worker agents or recurring jobs are started by this file.

| Task | State | Role and delivery | Completion evidence |
| --- | --- | --- | --- |
| COTTAGE-01 | Agent checks passed; creator review open | Furnished fictional cottage in its own synthetic test package | Official WorldEd export, 11 runtime probes, entrance/window/light interaction and exterior roof checks pass in 42.21.0; [COTTAGE_TEST](COTTAGE_TEST.md) |
| OVERRIDE-01 | Implemented, tested and reviewed | Separate manual style overrides by stable synthetic building ID | Integrated as `b24eedd`; repeatability, reordered input, unrelated buildings and unchanged inputs verified; invalid values/IDs fail before output. [Contract](specs/building-style-overrides.md) |
| REVIEW-01 | Code and saved-evidence review passed | Independent read-only review of both changes | No blocking findings; M0 TMX output remains byte-identical. Logs, screenshots, package hash, source copy and installed-file parity reviewed. This is not independent game reproduction; creator acceptance stays open |
| GETABODA-01 | Waiting for access decisions and permitted handling | World/data plus lead: obtain the approved local subset and measure one traceable building | Source IDs/CRS/terms retained; unknown appearance left unknown; handling and publication conditions checked before sharing derived output |

**COTTAGE-01 boundary:** start from `assets/buildings/swedish_cottage_01.tbx` and its README. Keep the known-good M0 test fixture and valuable saves intact. Use permitted stock resources and generic interiors. Record any export/manual steps; an editor screenshot alone does not pass the game checks. This work does not require real map data.

**OVERRIDE-01 boundary:** extend `tools/building_styles.py`, `tests/test_building_styles.py` and synthetic example inputs. Use stable fixture IDs and a separate override file with manual values taking precedence over generated style defaults. Start with style selection only; no geometry edits, GIS downloads, game exporter, UI or automatic real-world identity matching. Passing this task proves the manifest behavior; persistence in a regenerated playable map remains a later M3 check.

**While waiting:** the cottage and synthetic override deliveries have passed agent checks. The next creator involvement is a representative exterior review and optional short playtest. The two Geotorget applications are being processed; no new application is needed. Real Getaboda interiors and future discoveries need not be exposed. M0 creator acceptance and independent reproduction remain open.

## M0 — Prove a custom Build 42 map really loads (IN PROGRESS)
See [BUILD42_SPIKE.md](BUILD42_SPIKE.md).

As of 2026-10-17, world selection, indoor spawn, doorway traversal, closed-door daylight and the light switch have been agent-tested in 42.21.0. All four wall collision probes pass in the running game. All 80 room squares have an upper floor and are classified indoors; the roof renders outdoors. Creator acceptance and independent reproduction remain open. The first reusable cottage is now a furnished, separately playable early M2 prototype with agent game checks passed; design review remains. Real geography has not yet been verified.

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
