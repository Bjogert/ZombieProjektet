---
name: diagnosing-bugs
description: Diagnose failing ZombieProjektet tests, broken generated maps, missing houses, engine crashes, incorrect game behavior or performance regressions using reproducible evidence.
---

# Diagnose before patching (adapted from Matt Pocock)

1. Identify the user's **exact symptom**, expected behavior, changed versions/configuration and any relevant logs (redact secrets).
2. Build the tightest repeatable failure signal: one test, input fixture, export comparison, game log or captured manual reproduction.
3. Reproduce first. If the game or data is unavailable, say what cannot be tested and request the minimum evidence; do not declare a speculative fix verified.
4. Minimize the reproducer. Inspect all callers and input transformations touched by a potential root cause.
5. List a few falsifiable hypotheses only after reproducing; test the strongest. Prefer fixing the root cause once.
6. Add a regression test where feasible. Re-run the failure signal plus relevant suite.
7. Report observed root cause, changed behavior, evidence and any in-game checks still needed.

Source: mattpocock/skills diagnosing-bugs, adapted for this project.
