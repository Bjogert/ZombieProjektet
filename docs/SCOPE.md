# Scope — Getaboda proof of concept

Updated 2026-10-18. The [specification](PROJECT_SPEC.md) defines acceptance; the [roadmap](ROADMAP.md) defines phases, ordered work and blockers.

## Test Version 1 / M3 — accepted POC outcome

A separate Swedish world in Project Zomboid Build 42 Stable with:

1. Approximately 4–5 source-confirmed Getaboda buildings, nearby roads and basic forest/open land/water where present, from permitted data checked against its sources.
2. Simple playable Swedish houses from a small data-driven library. At least one house has a working entrance and minimal interior; decks/patios and gardens with flowerbeds contribute to the agreed residential character.
3. Verified classification where data exists; otherwise explicit assumptions that can be corrected in data or QGIS. Unknown real appearance is not a measured fact.
4. Stable building identity and reproducible generation. Individual corrections survive regeneration, official export and a playable-artifact check.
5. Documented installation and actual game verification, followed by creator feedback. Use a local/private test package first.

Use 1:1 geography, including connecting roads. Preserve source coordinates and record grid approximations separately. Generic interiors remain the default.

## Intermediate deliveries

M0 proved the technical route with a minimal house; cottage/garden/placement fixtures now have separate evidence. The 5.09 km Getaboda–Agunnaryd road experiment remains a separate prototype until continuous driving is verified. A synthetic cottage beside that road is a useful integration test, not a verified real house placement.

These prototypes support V1 without requiring Agunnaryd buildings or a municipality-wide build. Manual official export steps remain acceptable while the repeatable workflow matures.

## Later work — not required for V1

- Additional Swedish house/outbuilding types, original tiles and carefully reviewed individual details.
- Private multiplayer using the game's existing systems, then approved GitHub/Workshop distribution.
- Bounded nearby settlements, a Ljungby district pilot and eventually municipality coverage after capacity and performance are measured.
- Broader automation of demonstrated repeated work; no custom editor during the POC.
- Optional elevation presentation and new Swedish game items remain separate later scope decisions.
- Save compatibility where actually verified. Development resets are acceptable; valuable saves remain protected.
- Any countryside compression only after evidence and a new creator decision. It is not an assumed later requirement.

## Outside current scope

A standalone engine/Godot implementation, new zombie systems, custom networking, AI NPCs, exhaustive historical reconstruction, precise private interiors for every home, all of Småland in the first version, costly GIS infrastructure or an unapproved public release.
