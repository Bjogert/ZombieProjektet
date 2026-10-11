---
name: tdd
description: Implement non-trivial ZombieProjektet Python, Lua, C# or gameplay logic through small observable red-green-refactor cycles. Use for features, parsing, geography transforms and bug fixes that can be tested.
---

# Behavior-first TDD (adapted from Matt Pocock)

1. Read the approved behavior and existing tests. Pick the highest practical **public seam**; ask only if a high-impact seam decision is unresolved.
2. Write one test with an independently known expected result, run it and observe the **correct** failure (red).
3. Make the smallest complete change; re-run that test (green). Repeat for the next meaningful behavior, then tidy code only while green.
4. Prefer data fixtures and deterministic seeds. Test geographic identity, building counts, stable ordering, roads/water topology and missing data as relevant.
5. Avoid tautological expected values, private-method tests, needless mocks and snapshots that simply bless the implementation.
6. Run the relevant tests and then the repo's complete automated suite before finishing. Report exact commands/results.
7. A passing Python test does NOT prove an in-game feature. For Project Zomboid or Godot behavior, record the required manual game/engine test and mark it UNVERIFIED until actually run.

Source: mattpocock/skills tdd, adapted for this project.
