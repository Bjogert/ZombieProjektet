# ZombieProjektet — shared agent instructions

This is the canonical entry point for Codex and Claude Code. [CLAUDE.md](CLAUDE.md) points here; do not read these files recursively.

## Mission — settled
Build a **Project Zomboid Build 42 Stable map mod**. Getaboda (approximately 4–5 buildings) is the first real location and starting point for an expanding Swedish world. Use modern geodata with Swedish 1990s styling and the game's existing mechanics. The creator wants to discover the world while playing, participate in design and important decisions, and delegate routine development.

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
Finish [BUILD42_SPIKE](docs/BUILD42_SPIKE.md) before a broad geodata pipeline. Its report records current evidence and remaining checks. M0 is not complete merely because a package builds or a smoke test passes. A reusable Swedish cottage is the next visual prototype, followed by source-backed Getaboda integration.

## Working practice
- Use relevant project skills under `.agents/skills/` or `.claude/skills/`; keep mirrored skill files byte-identical.
- Read affected code and tests first. Work in small, verifiable steps. Record changed behavior, checks, unresolved concerns and the next action.
- Write specifications, decisions, reviews and handoffs in Markdown. Keep [HUMAN_OVERVIEW](docs/HUMAN_OVERVIEW.md) and the manually maintained [PROJECT_OVERVIEW.html](docs/PROJECT_OVERVIEW.html) consistent. `tools/render_dashboard.py` checks selected markers only; it does not generate HTML.
- HTML feedback buttons prepare suggestions; they do not approve decisions, submit issues or change files automatically.
- Run relevant checks: `python -m unittest discover -s tests -v`, `python tools/check_agent_setup.py`, `python tools/render_dashboard.py --check`, and `git diff --check`.

Out of scope for the first POC: a standalone engine, new zombie/survival systems, dynamic terrain, multiplayer, a complete Swedish asset catalog and automatic geographic compression.
