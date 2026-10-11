---
name: code-review
description: Review ZombieProjektet changes or a PR against its requirements and engineering standards, including correctness, scope creep, licensing, performance and missing tests.
---

# Review against spec AND standards (adapted from Matt Pocock and Ponytail)

1. Establish a diff baseline (PR base, merge-base or stated commit); include impacted callers/config/tests, not only edited lines.
2. **Spec axis:** Did the change deliver the stated behavior and acceptance checks? Any undocumented behavior or speculative expansion?
3. **Standards axis:** Check simplicity, correctness, error handling, security, deterministic map/data behavior, test quality, game-engine boundaries and provenance/rights.
4. Run available tests/static checks. Distinguish confirmed failures from unverified suspicions; use file/line references.
5. Sort findings by impact: must fix, should fix, optional. Suggest the smallest complete fix, including what can be deleted.
6. Report separately what was tested, what could not be verified in-game and whether the change is safe to merge.
7. No requirement for parallel subagents; use them if available, otherwise perform the two independent reviews sequentially.

Source: mattpocock/skills code-review and DietrichGebert/ponytail, adapted.
