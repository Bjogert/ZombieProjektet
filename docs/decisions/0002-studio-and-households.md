# ADR-0002 — Small studio workflow and fictional household briefs

Date: 2026-10-25. Status: creator-authorized direction; bounded implementation
and prototype, not approval of every example or a completed game feature.

## Request
The creator asked to put the studio workflow into the repository, improve role/
skill/instruction routing and the roadmap, and explore reusable fictional
inhabitants whose habits, household and location generate coherent interiors.
The world should remain interesting for the creator to discover while playing.

## Decision
Keep Project Zomboid, existing map/building tools, the current rural showcase,
source/override contracts and V1 scope. Add Art Director, interior/set-dressing
and Technical Artist responsibilities under the existing lead, with independent
QA and a small normal concurrency budget. Retain existing engineering skills;
add only art-direction and household-design workflows and dynamic parity checks.
Native Codex agent definitions provide a convenience, not running staff or new
permissions. Existing schedules, release and merge gates are unchanged.

Use original fictional person seeds combined with explicit household resources,
life events, environment and available space. Preferences and physical constraints
cause interior choices; names, gender, education and politics do not stand in for
crime, weapons, lack of reading or competence. These are game design recipes, not
claims about actual inhabitants or demographic statistics.

The first implementation is a separate offline brief generator with 20 fictional
seeds. It does not modify existing TBX/garden sources, game loot, item IDs, NPCs or
saves. Freeze generated choices, preserve manual edits, record versions and test
repeatability. AI creates/reviews reusable recipes; scripts perform repeated
selection. Future layout/loot consumers require separate evidence and balance gates.

## Consequences
Keep r6 export/game/reload first. A representative room with three variants and
one second compatible reuse is the next meaningful proof, not all-house generation.
Retain stable source geometry, existing local-data restrictions and later-area
spoiler preferences. Curate accessible actual showcase screenshots after rights/
privacy review; a local ignored file path alone is not remote evidence.

The 20 names/weights and example stories are provisional creative seeds. Habitat
compatibility and motif weights are not validated population probabilities. New
roles, skills, native-client loading and house quality each have separate checks.
No full token savings, complete autonomy or automatic per-house improvement is promised.
