---
name: household-design
description: Use for ZombieProjektet fictional residents, household briefs, reusable room recipes or related tests. Not for real-person profiling, automatic NPCs or unapproved loot changes.
---
# Coherent fictional homes

Read AGENTS.md, the ROADMAP task and docs/design/HOUSEHOLD_DESIGN.md. Reuse the
existing planner and fixtures; do not invent a second world-generation pipeline.

1. Separate person interests/habits, shared household resources/history and actual
   available rooms/storage/garden. Label inhabitants and interiors fictional.
2. Use a stable building ID, pinned seed/catalog and saved choices. Names/pronouns
   are presentation only; no politics, education or locality-to-crime shortcut.
3. Generate a bounded brief with tools/household_briefs.py. Inspect exclusions and
   unfilled slots. This produces design motifs, not PZ placements or item IDs.
   Preserve each resident's interests and explicit compatible overrides.
4. For a placement task, choose one room/group recipe and inspected asset refs.
   Check complete multi-tile furniture, access, orientation, capacity and fallback.
   Preserve source geometry and human edits. No silent catalogue-upgrade rerolls.
5. Keep decorative props, container type and randomized loot separate. Actual
   loot integration needs its own inspected API, rarity/budget and game tests.
6. Test deterministic output, order independence, constrained spaces, mixed
   households, invalid inputs and existing-output protection. Run actual game
   checks through the lead before calling a room recipe playable.

Return changed files, exact tests, fixture/artifact identity, limitations and
next action. No per-house online AI, hidden paid dependency or full population
simulation. Measure second-use effort before claiming generation gets cheaper.
