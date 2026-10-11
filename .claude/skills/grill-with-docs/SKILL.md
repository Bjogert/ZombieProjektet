---
name: grill-with-docs
description: Clarify an ambiguous ZombieProjektet feature, engine decision or architecture proposal before implementation. Use for consequential design decisions, scope conflicts or when asked to challenge a plan.
---

# Grill with docs (adapted from Matt Pocock)

1. Read the relevant code, `docs/VISION.md`, `docs/SCOPE.md`, `GLOSSARY.md` and existing ADRs first. Never ask for facts available in the repository.
2. Identify the one **next consequential decision** that blocks progress. Ask one concrete question at a time, with your recommended default, alternatives and real consequences. Do not interrogate for trivial choices.
3. Distinguish confirmed user decisions from agent guesses. Never quietly decide between the Project Zomboid mod and standalone game tracks.
4. Stress-test acceptance criteria against an edge case (missing OSM building, disconnected road, wrong house style, game-version mismatch, missing asset permissions).
5. Record **settled** vocabulary in `GLOSSARY.md` and consequential decisions in `docs/decisions/` as ADRs with context, choice, rejected alternatives and reversal criteria.
6. Stop when the next practical experiment is clear. Provide its success/failure check.

Inspired by mattpocock/skills: grill-with-docs, grilling and domain-modeling. MIT attribution in `docs/THIRD_PARTY_SKILLS.md`.
