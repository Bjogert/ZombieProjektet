---
name: ponytail
description: Prefer the smallest complete and safe ZombieProjektet code change; actively prevent AI-generated slop, unnecessary abstractions, duplicate systems and dependency bloat during implementation, refactoring and review.
---

# Ponytail - adapted for ZombieProjektet

Read the code and inputs the change reaches **before** deciding what to build. Be economical in solutions, not in investigation.

Take the first option that fully solves the task:
1. Does it need to exist? Skip speculative features.
2. Already implemented here? Reuse it.
3. Standard library, game engine or platform feature? Prefer it.
4. Existing installed dependency? Use it rather than adding another.
5. Otherwise write the smallest readable implementation.

Avoid redundant wrappers, helper layers, APIs, options, config files and comments that explain obvious code. Remove dead or duplicative code. A changed shared contract requires checking callers, docs and fixtures. For non-trivial branching/parsing/state logic, leave a focused test or reproducible assertion.

Never sacrifice source validation, error handling, data safety, security, accessibility or genuinely required gameplay behavior to save lines. Domain correctness matters more than minimal character count. Don't compress clear code into clever one-liners.

Finish by noting what you deliberately skipped, what was not verified and remaining risk. Use `shortcut: <limit>; reconsider when <condition>` only for an intentional, documented shortcut.

Adapted from DietrichGebert/ponytail (MIT); attribution in `docs/THIRD_PARTY_SKILLS.md`. No background hooks or automatic external plugin updates.
