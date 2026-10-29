---
name: household-design
description: Use for ZombieProjektet fictional residents, household briefs, reusable room recipes or related tests. Not for real-person profiling, automatic NPCs or unapproved loot changes.
---
# Coherent fictional homes

Read AGENTS.md, the ROADMAP task and docs/design/HOUSEHOLD_DESIGN.md, including
its accepted everyday-home strategy and biography-hidden promotion gate. Reuse
the existing planner and fixtures; do not invent a second world-generation pipeline.

1. Start from a believable everyday household, not a mandatory dramatic story.
   Treat character seeds as starting points. Separate person interests/habits,
   shared resources/history and actual rooms/storage/garden. Label all residents
   and histories fictional; no political, demographic or locality-to-crime shortcut.
2. Write a short intent with a few feasible visible cues. Plan shared rooms and
   personal areas, not added inventories or averaged personalities. Keep ordinary
   domestic functions; unusual details need a reason and a small emphasis budget.
3. Use a stable building ID, pinned seed/catalog and saved choices. Generate a
   bounded brief with tools/household_briefs.py; inspect exclusions/unfilled slots.
   It selects design motifs only. Shared-life compromise, physical placement,
   realized stories and post-outbreak effects are not implemented by that script.
4. For placement, filter physical constraints before weighting compatible activity
   groups. Use inspected references, complete multi-tile pieces, clearances,
   orientations, capacity and fallback. Preserve explicit compatible overrides,
   source geometry and human edits. Do not invent assets for a story.
5. Distinguish the pre-outbreak household from later scenario effects, and props
   from containers and randomized loot. Inspect vanilla behavior before proposing
   an adapter; no duplicate looting/damage or unapproved spawn changes. A clue
   suggests a possible find, not a guaranteed reward. Freeze choices at build time.
6. Ground any final narrative in actual saved placements. Record intended versus
   realized cues; omit objects that were not built. Propose one reusable addition
   when the library is insufficient, not a bespoke unsupported exception.
7. Test determinism, input order, constrained spaces, mixed households, invalid
   inputs and edit preservation. Route actual game/reload checks through the lead.
   For ROOM-01 compare three briefs on the same shell, asset pool and approximate
   loot budget. Let independent QA inspect game views before the biographies.
   Show coherent visible differences, not just colours/clutter; reuse once more.

Return changed files, exact tests, fixture/artifact identity, cue mapping,
limitations and next action. No runtime LLM, hidden paid dependency or full
population simulation. Build-time AI helps author/review recipes; scripts repeat
validated choices. Measure second-use effort before claiming generation gets
cheaper. More biographies are not a remedy for indistinguishable rooms.
