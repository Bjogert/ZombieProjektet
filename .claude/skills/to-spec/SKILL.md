---
name: to-spec
description: Turn a settled ZombieProjektet conversation, request or design into a compact, testable feature specification. Use when asked to write a spec, plan a non-trivial change or capture accepted requirements.
---

# Spec from known context (adapted from Matt Pocock)

1. Read relevant code and `docs/VISION.md`, `docs/SCOPE.md`, `GLOSSARY.md` and relevant ADRs.
2. Synthesize the **smallest complete user-visible behavior**; do not invent unrequested subsystems or reopen settled decisions.
3. Write a short spec under `docs/specs/<slug>.md` with:
   - Problem and player/developer value
   - Intended behavior, supported inputs and outputs
   - Key implementation choices and known external dependencies
   - Acceptance criteria including at least one negative/edge case
   - Verification (automated tests vs manual in-game tests)
   - Out of scope, unknowns and licensing/data risks
4. Choose one testable public seam where possible. Separate proven tool capability from hypothetical integration.
5. Request approval before creating GitHub Issues or changing core scope. If the user already clearly authorized publication, proceed without an extra confirmation.

No exhaustive user-story lists for small features. Source: mattpocock/skills to-spec, adapted for this repo.
