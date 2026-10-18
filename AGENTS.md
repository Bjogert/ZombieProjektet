# ZombieProjektet — shared agent instructions

This is the canonical entry point for Codex and Claude Code. [CLAUDE.md](CLAUDE.md) points here; do not read these files recursively.

## Mission — settled
Build a **Project Zomboid Build 42 Stable map mod**. Getaboda (approximately 4–5 buildings) is the first real location and starting point for an expanding Swedish world. Use modern geodata with Swedish 1990s styling and the game's existing mechanics. The creator wants to discover the world while playing, participate in design and important decisions, and delegate routine development.

The personal goal is to reunite the creator's former PZ group from Ljungby/Agunnaryd with a surprise familiar world. Concentrate individual exterior/interior work on approximately ten creator-selected homes across the expanding project; use plausible varied templates elsewhere. This is a detail priority, not an additional V1 acceptance requirement. Getaboda remains open development with the creator.

Read [PROJECT_SPEC](docs/PROJECT_SPEC.md), [DECISIONS](docs/DECISIONS.md), [ROADMAP](docs/ROADMAP.md), [SCOPE](docs/SCOPE.md) and [ADR-0001](docs/decisions/0001-mod-or-game.md) as relevant. Do not reopen the mod-versus-standalone decision or the choice of Getaboda.

## Language and player experience
- Communicate with the user in **Swedish**. Write documentation, code, identifiers, comments, commit messages, PR text and authored UI text in **English**. Preserve proper place names, source identifiers and external tool names.
- Develop Getaboda and the worldbuilding tools openly with the creator. Show layouts, houses, gardens, screenshots, technical steps and tradeoffs as useful; Getaboda does not need spoiler protection. Explain how source data, templates, overrides, export and game testing connect, while handling routine implementation independently.
- Preserve surprises in later areas by default. Avoid exposing their exact interiors, placements, seeds, loot or discoveries unless requested. Use Getaboda or a representative test house for visual decisions. Follow the data-handling and publication rules in `docs/DATA_AND_RIGHTS.md`.
- Keep full evidence in developer documentation. Spoiler avoidance is a presentation preference, not repository secrecy. Never hide bugs, costs, failed checks or material limitations.

## Autonomy and decisions
Follow [AGENT_WORKFLOW](docs/AGENT_WORKFLOW.md). Independently implement, investigate, test and repair reversible changes within accepted scope. Do not ask the user to choose routine technical details or act as first-line QA. Bring consequential design, scope, cost and release decisions to the user with a concrete proposal, a recommendation and its tradeoff. Continue unrelated authorized work while awaiting an answer.

Use the current execution queue in [ROADMAP](docs/ROADMAP.md) to select the next bounded delivery. A ready task is planned work, not evidence that an agent is running or that a milestone passed.

Specialist roles and delegation rules are described in the workflow. Keep one integration owner. These instructions do not authorize unrestricted background execution, purchases, public releases or PR merges.

## Engineering principles
1. Choose the simplest complete, verifiable solution. Avoid speculative architecture and dependencies without a demonstrated need.
2. Preserve original coordinates, identifiers, licenses and verified properties. Record assumptions separately; never invent verified real building placements or footprints.
3. Keep generation deterministic. Store corrections separately by stable building ID; regeneration must preserve them and never overwrite source geometry.
4. Grow a small data-driven Swedish building library. Begin with permitted game resources and generic interiors; review detailed private interiors before publication.
5. Verify gameplay in the game. Python tests cannot prove map loading, collision, roof behavior or house entry. Record the exact version, tested artifact and evidence; distinguish agent tests from human acceptance.
6. Prefer free tools and lawful data. No purchases without approval. Follow [DATA_AND_RIGHTS](docs/DATA_AND_RIGHTS.md); do not commit proprietary game art or code.
7. Do not change the Steam installation or system-wide settings without approval. Ask before administrator actions or running unknown binaries. Necessary free development tools from trusted sources are already authorized by the project brief.

## Current delivery gate
Use [ROADMAP](docs/ROADMAP.md) for the next bounded delivery and dependencies. The [synthetic roadside integration](docs/INTEGRATION_TEST.md) has 25/25 runtime probes, manual light/door/roof checks and clean save/reload evidence after a bounded metadata compatibility step. Packaging still rejects the original defective export. [Local road extraction](docs/ROAD_PIPELINE.md) reproduces the registered corridor and authoring inputs. The [small terrain prototype](docs/TERRAIN_TEST.md) is verified in-game with clear character access and clean reload; the creator approved maintained residential plots with flowerbeds, wilder vegetation outside and vanilla gradual overgrowth on 2026-10-18. This approves direction, not every prototype detail. A frozen Microsoft open-footprint sample now supplies 13 local Getaboda candidates, with preserved IDs and source bytes. The creator approved a 45° grid rotation at 1:1; real-house verification and the exact V1 selection remain open. See `docs/research/getaboda-building-register-2026-10-18.md`. Creator acceptance and continuous driving remain separate gates. Do not turn a control or access blocker into an indefinite stop on independent work. No broad municipality exporter or completed milestone is implied by successful builds alone.

The [provisional candidate pilot](docs/CANDIDATE_PILOT_TEST.md) now connects one
8 by 12 candidate to the registered village road at 1:1, with a generic house,
garden and assumed access. Official export and 17/17 game probes pass, including
after full restart/reload. Its bounded landscape follow-on passes 19/19 probes
and clean reload, preserving candidate reservations and pedestrian access.
This advances fitting without confirming identity,
likeness or final selection. Better photos are not a blocker for reversible
prototype work; preserve unknown source properties and separate design choices.

The creator's latest visual feedback is that the enlarged pilot looks barn-like.
Prioritise [residential character](docs/specs/residential-character.md) before
scaling more copies. The [Småland pattern study](docs/research/smaland-houses-2026-10-18.md)
supports separate dwelling families and varied boundaries, shrubs and outbuildings.
It is research/design guidance, not a new game-tested asset or final approval.

## Working practice
- Use relevant project skills under `.agents/skills/` or `.claude/skills/`; keep mirrored skill files byte-identical.
- Read affected code and tests first. Work in small, verifiable steps. Record changed behavior, checks, unresolved concerns and the next action.
- Write specifications, decisions, reviews and handoffs in Markdown. Keep [HUMAN_OVERVIEW](docs/HUMAN_OVERVIEW.md) and the manually maintained [PROJECT_OVERVIEW.html](docs/PROJECT_OVERVIEW.html) consistent. `tools/render_dashboard.py` checks selected markers only; it does not generate HTML.
- HTML feedback buttons prepare suggestions; they do not approve decisions, submit issues or change files automatically.
- Run relevant checks: `python -m unittest discover -s tests -v`, `python tools/check_agent_setup.py`, `python tools/render_dashboard.py --check`, and `git diff --check`.

Out of scope for the first POC: a standalone engine, new zombie/survival systems, dynamic terrain, multiplayer, a complete Swedish asset catalog and automatic geographic compression.
