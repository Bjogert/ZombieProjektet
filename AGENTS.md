# ZombieProjektet — shared agent entrypoint

Canonical entrypoint for Codex and Claude Code; [CLAUDE.md](CLAUDE.md) points here.
Read this once, then only the instructions relevant to the assigned task.

## Mission and authority
Build a **Project Zomboid Build 42 Stable map mod**, not a standalone engine.
The first real-world delivery remains approximately 4–5 Getaboda buildings;
later areas can grow toward Agunnaryd, Södra Ljunga and Ljungby. Retain the game's
mechanics, modern geography and Swedish 1990s atmosphere. The creator should
be able to enjoy discovering the world, not supervise every chair placement.
Approximately ten creator-selected homes across the eventual world deserve
extra recognition work; they are not ten additional V1 requirements.

Use [PROJECT_SPEC](docs/PROJECT_SPEC.md) and [DECISIONS](docs/DECISIONS.md) for
product decisions; [ROADMAP](docs/ROADMAP.md) is the **only execution queue**.
The creator's 2026-10-25 studio/household request is recorded in
[ADR-0002](docs/decisions/0002-studio-and-households.md). It authorizes bounded
workflow and fictional-design work, not a new engine, loot rebalance or wider V1.
Do not reopen settled scope, Getaboda, 1:1 roads, or the approved 45-degree grid
rotation. Preserve original geodata and stable IDs separately from game fitting.

## Read by task, not by department
| Task | Read next |
| --- | --- |
| Any delivery | Current ROADMAP item; [working agreement](docs/AGENT_WORKFLOW.md) |
| Dispatch or review | [Role briefs](docs/AGENT_ROLES.md); actual diff and acceptance criteria |
| House, material, light, garden or interior | [Studio production](docs/STUDIO_WORKFLOW.md); relevant environment-library entry; `art-direction` skill |
| Fictional inhabitants or variation | [Household design](docs/design/HOUSEHOLD_DESIGN.md); `household-design` skill |
| Data, images, assets or publishing | [DATA_AND_RIGHTS](docs/DATA_AND_RIGHTS.md) |
| Implementation, failure or handoff | Relevant existing skill only; affected code/tests |

## Durable operating rules
- Speak **Swedish** with the creator. Author project docs, code, identifiers,
  commits, PRs and UI in **English**, preserving proper names. Show Getaboda and
  the tools openly. Preserve later-area interiors, loot, seeds and discoveries
  in routine updates unless requested. Never hide defects, costs or limitations.
- The creator owns consequential design/scope/cost/release decisions. The lead
  independently implements, tests and repairs reversible work within scope.
  Continue useful ready work rather than asking permission for routine steps.
- Use one integration owner and one primary deliverable. Normally use at most
  one worker and one independent reviewer; combine responsibilities for small
  tasks. No recursive recruitment. Roles are not always-running employees.
  Concurrent writers use separate worktrees and disjoint owned files. Only the
  designated operator controls the game/editor, installs test mods or packages.
- Preserve the creator's lead-model choice and use actually available worker
  models under AGENT_WORKFLOW. Project agent files deliberately do not pin a
  model or change permissions. Read-only review is an instruction, not a separate
  sandbox. Do not claim activity without current tool evidence.
- The hourly `zombieprojektet-studio` heartbeat was recorded on 2026-10-23.
  Verify live scheduler/worker state before describing it as active. These files
  create no job and do not authorize new schedules, purchases, external messages,
  accounts, accepted terms, public releases or PR merges.
- Never reset another writer's changes or valuable saves. No Steam/system-wide
  changes, administrator actions or unknown binaries without approval. Necessary
  free trusted development tools remain authorized under the existing brief.
- Respect local-processing boundaries: no raw geodata, source imagery, private
  correspondence or credentials in prompts/model-visible output. Use synthetic
  fixtures for tool development. Source access is not redistribution permission.
- Keep geometry, source facts, fictional household choices, asset references and
  actual game loot separate. Invented inhabitants are **not** claims about real
  addresses. No demographic/political shortcuts for criminality, possessions or
  competence. Use concrete interests, habits, space and explicit scenario rules.
- Prefer existing tested components. Improve high-value Swedish details first:
  faluröd panel, white corners/window trim and white bargeboards, retaining usable
  stock roof tiles. Preserve gable roofs with two slopes and vertical ends,
  maintained gardens and wilder edges; vanilla handles later overgrowth.
- Keep generation deterministic, choices versioned and corrections separately
  keyed by stable building ID. Never silently reroll accepted houses on library
  updates. No global replacement of vanilla sprite IDs or unverified item IDs.

## Evidence before expansion
The r5 rural showcase is the last recorded game-verified baseline. r6 source
work needs official export and fresh game/reload checks; see ROADMAP and
[RURAL_SHOWCASE_TEST](docs/RURAL_SHOWCASE_TEST.md). Do not rebuild M0 from scratch,
multiply an unverified layout, or call the household planner an in-game generator.
The dirty local `cottage_270.tbx` regression remains a local reconciliation task;
this checkout cannot prove it has been repaired. Preserve its backup and edits.

Separate: authored → automated checks → official export → game verification →
creator acceptance → release approval. Python and HTML cannot prove gameplay.
Capture exact build, artifact/hash, representative game screenshots and remaining
checks. Record absent images as absent, not as inspected. Independent QA must be
an actual separate review; self-review is labelled self-review.

## Checks and handoff
Keep `.agents/skills/` and `.claude/skills/` byte-identical. Retain existing skills;
add new ones only for repeated workflows. Run applicable tests and report exact
scope, not a fabricated whole-suite pass:

- `python -m unittest discover -s tests -v`
- `python tools/check_agent_setup.py`
- `python tools/render_dashboard.py --check`
- `git diff --check`

Update the single ROADMAP queue and affected evidence, with a short handoff:
base/head, owned files, actual tests, game artifact, blockers and next action.
[Studio overview](docs/STUDIO_OVERVIEW.html) is a static guide, not a live agent
monitor. Existing HTML feedback does not approve decisions or write to GitHub.
