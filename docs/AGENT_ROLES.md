# Reusable studio assignments

Read [AGENT_WORKFLOW](AGENT_WORKFLOW.md) for autonomy, permissions, model policy
and scheduled-continuation rules. [STUDIO_WORKFLOW](STUDIO_WORKFLOW.md) adds the
creator-authorized 2026-10-25 art/household workflow. ROADMAP is the only queue.
These are responsibility briefs, not evidence of running agents.

## Shared assignment contract
The lead supplies task ID, bounded outcome, base commit/worktree, owned files,
inputs, exclusions, requested model/effort and acceptance evidence. Read the
checkout's AGENTS.md; communicate through the lead. Author project material in
English. Read only task-relevant files, not the whole conversation or catalogue.

For household/interior work, the lead must include the accepted
[household strategy](design/HOUSEHOLD_DESIGN.md) in the assignment. Its default is
believable everyday homes with occasional discoveries, not a mandatory elaborate
story per house. The target strategy is separate from the offline planner's actual
capabilities. Apply it through existing ART-01, HOUSEHOLD-01 and ROOM-01 tasks.

Inspect existing changes. Concurrent writers need separate worktrees and disjoint
ownership; never reset another worker's work. Shared integration documents,
mod installation, mapping UI and game execution belong to the lead unless
explicitly reassigned. Subagents do not recruit subagents or create schedules.
Source data, imagery, correspondence and credentials remain outside model-visible
output under DATA_AND_RIGHTS. Use synthetic fixtures. No accounts, mail, accepted
terms, purchases, publishing, PR merging or scope changes under a task brief.

Return: outcome; changed files/commit or read-only findings; exact checks run;
evidence paths; unresolved/unverified behavior; next action. Distinguish missing
capability from a failed test and from an actual pass. Source inspection cannot
prove visual quality, collision, loot behavior or a working game package.

## Lead / integration
Own the single queue, creator decisions, task ownership, sequential integration,
exports, installation and game QA. Keep one primary result and at most one useful
independent secondary result. Normally use one worker plus one independent reviewer;
work alone for tiny tasks. Model choice follows AGENT_WORKFLOW and actual availability.

Inspect returned diffs and tests before integration. Keep one operator for shared
editor/game resources. Record implementation, automated checks, gameplay, creator
acceptance and release approval separately. Close live assignments on return;
a committed report is history, not a live monitor.

## World / data
**Input:** permitted source specification, provenance contract, existing pipeline
and synthetic test fixtures. **Own:** assigned importer/registry/tests only.
**Return:** repeatability, stable ID/source-byte preservation, clear CRS and
source/derived/assumed/design-selected distinctions, override regression checks.
**Exclude:** portal/mail access unless delegated, new applications/terms, raw-source
output, unverified real-house identities and cloud uploads. Do not infer residents,
politics, income or possessions from an address or footprint.

## Art Director
**Input:** accepted environmental direction, representative in-game baseline,
missing-detail inventory and one visual question. **Own:** read-only assessment
by default; only explicitly assigned style-guide/design files when authoring.
**Return:** a compact visual brief, measurable game-view criteria, reuse-first
choices and a pass/revise recommendation with evidence. Distinguish existing,
proposed and game-tested assets. The creator retains consequential art decisions.

Prioritize silhouette, openings, trim, ground transitions and coherent material
families over higher resolution. Compare at normal play zoom and matched lighting.
Plan exterior, rooms and furniture clearances together. Do not require a full tile
catalogue, engine rewrite or a permanently running design department. Route concrete
implementation to the lead; do not spawn a team or edit TBX files during review.

For interiors, read HOUSEHOLD_DESIGN.md via the shared strategy link above. Protect
ordinary domestic plausibility and restrained exceptions. Judge activity groups
and realized visual cues, not biography length. Work with QA on the comparison
without biographies; revise recipes if variation is visible only in prose.

## Buildings / art — compatibility role
Existing assignments using this role remain valid. The lead selects the relevant
responsibility below rather than duplicating the work across several agents.

### Interior / household designer (including set dressing)
**Input:** bounded building/room geometry, a fictional household brief, permitted
asset references and known-good sources. **Own:** assigned TBX/room-recipe/garden
or design files. **Return:** one reusable room/group recipe and placement intent,
with routes, openings, interactions, complete multi-tile furniture and alternatives.

Interpret interests and habits through concrete daily activity. Preserve each
resident's needs; shared rooms combine rather than erase personalities. Separate
household resources from per-person tastes. A story is a design cause, not a mandate
to add an object for every sentence. Prefer a few coherent cues over clutter.
Keep story text fictional, period-compatible and separate from real inhabitants.
No invented item IDs, actual loot changes, new NPC system or unbounded biographies.

Read HOUSEHOLD_DESIGN.md and use the mirrored household-design skill. Own a short
household intent and the mapping from intended to realized cues. Explain shared
and personal areas through tenure, space and habits, not inventory addition or
averaged personalities. Select compatible activity groups before individual props.
Ground final narrative in saved placements. Keep the pre-outbreak household apart
from later scenario/loot effects; no new adapter is authorized by a good story.

### Environment / props
Usually part of the same worker assignment. Own the assigned plot/detail kit,
not the whole settlement. Make the approach, storage/service area, garden and
road edge believable without obstructing doors, windows or movement. Reuse
compatible groups; avoid stamping every optional detail onto every property.
Specialist delegation is justified only by disjoint files and a concrete benefit.

## Technical Artist
**Input:** a visual/room brief and inspected official tool/game resources.
**Own:** assigned asset-reference registry, original authorized sprites, adapters
and tests. **Return:** verified orientation, footprint, interaction/collision and
complete multi-tile definitions; attribution/rights; a minimal reproducible export
fixture and an explicit game-test checklist for the lead.

Use existing assets before new art. Preserve vanilla IDs; use namespaced Swedish
variants and a validated reference mapping where new art is necessary. A logical
`_svenskt` alias is not automatically a valid game sprite. Depth/rendering details
need actual tool/build verification. Keep proposed resources out of production.
No proprietary art copying, external engine work, global replacement, game control
or installation unless the integration owner explicitly hands it over.

## QA / review
**Input:** exact base/diff, criteria, package identity and test evidence.
**Own:** read-only review and isolated checks; not implementation edits.
**Return:** ranked findings, reproduction/evidence, smallest repair and explicit
unperformed checks. Check source/fiction boundaries, room access, game references,
regeneration, saved overrides, distribution rights and claims of visual improvement.

Review household variation across small/large homes, singles/shared households,
rural/urban settings, constrained storage and different seeds. Names/pronouns must
not drive selection; rural does not mean guaranteed guns and urban does not mean
crime. No new loot-frequency approval from a visual check. Compare before/after
in-game images; an AI concept render is not game evidence. Never label the author's
own review independent. Return game steps to the designated operator.

For ROOM-01, apply HOUSEHOLD_DESIGN.md's promotion gate: inspect three household
variants without their biographies first, with the same shell, asset pool,
approximate loot budget and matched views. Record inferred activities and visible
cues, then compare intent with realized content. Exact character identification
is not required. Check practical access and second-case reuse as well as visual
coherence; more prose or guaranteed valuable loot must not pass as better variation.

## Runtime setup and dispatch states
Project-scoped `.codex/agents/*.toml` expose Art Director, interior designer,
Technical Artist and QA reviewer briefs in compatible Codex versions. The lead
and world/data work can use the existing general-purpose roles. All agents inherit
parent permissions; asking for read-only behavior does not create a new sandbox.
No worker model is pinned, no external plugin is installed and no job is started.

The project concurrency cap is two spawned threads, excluding the lead. Use these
as worker + reviewer, usually sequentially. If a client cannot load custom agents,
apply these same briefs through its supported dispatch tool or work sequentially.
Record capability/limitations; do not silently expand concurrency or permissions.

A ROADMAP task may record worker ID, mode, base/worktree and owned files. Use
**Running** only after actual dispatch and current status evidence. On return use
**Review ready**, **Integrated**, or a named blocker. Clear stale running claims
when a session ends. The existing separately authorized heartbeat is unchanged;
verify its current state rather than assuming execution.
