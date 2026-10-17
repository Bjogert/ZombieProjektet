# ZombieProjektet — implementation specification v1 (2026-10-11)

**Authority:** this specification, `DECISIONS.md`, `ROADMAP.md`, then relevant ADRs. `HUMAN_OVERVIEW.md` is a concise display companion, not an independent authority.

## Product
Project Zomboid **Build 42 Stable** mod. A standalone Swedish world expanding from Getaboda toward Agunnaryd, Södra Ljunga and Ljungby, initially singleplayer and later small private multiplayer. The users are the hobby creator and friends from the region. Their real-world recognition and ability to play outweigh exact reconstruction, historical research, or engine innovation.

## First proof of concept — acceptance
1. A separate, loadable Swedish map is tested in a recorded Build 42 Stable game version.
2. Approximately 4–5 actual Getaboda buildings, access roads and basic land cover are present, with source data checked for accuracy and rights. Never invent precise Getaboda coordinates or building footprints.
3. One building at minimum has a usable entrance, collision and minimal interior; the player can move through it in-game. Remaining buildings may use simpler valid game content.
4. Buildings have stable identifiers, source coordinates and data provenance. Classification and generated choices are deterministic and distinguish observed facts from assumptions.
5. A human correction to an individual building survives rerunning the generation process. This is demonstrated in an automated test and in a regenerated game artifact where possible.
6. Installation/export steps (including any manual WorldEd/TileZed step) are documented and reproducible; game test evidence is recorded.

The first **technical gate M0** is deliberately narrower: prove a minimal custom playable Build 42 map with one usable house and record its exact tool chain before building a broad exporter.

## Layer boundaries (implement only when needed)
1. **Ingest:** OpenStreetMap plus permissible Lantmäteriet/other datasets; respect licenses, source identity, time, geometry and coordinate system. Reject missing/ambiguous critical coverage for the POC until manually checked.
2. **Normalize:** shared feature schema for buildings, roads, vegetation/landuse, water; preserve original source geometry immutable. Use geodata confidence/provenance. Separate stable internal IDs from potentially changing OSM IDs through a documented mapping.
3. **Classify:** begin with a handful of extensible building categories (house/cottage, barn, shed, garage, other). Map known source tags; default to explicit 'unknown/assumed' rather than pretend the type is verified.
4. **Style + interior:** compact JSON definitions of building type, exterior variants and rule-driven basic interiors. Apply deterministic seed derived from stable building IDs. Include 1990s-consistent selections. Residential variants should include decks/patios and gardens with flowerbeds, with variation between houses and clear entrance routes. Record invented garden details as design choices, not verified real-property features.
5. **Overrides:** optional separate JSON keyed by immutable internal building ID for user-chosen type, facade, geometry correction, roof, doors, later floor plan. Explicit precedence: permitted observed source -> reproducible generated defaults -> approved manual overrides. Keep layer details documented and validate overrides; overriding original source geometry is forbidden.
6. **Gameplay projection:** transform normalized source coordinates into grid/world cells, with minimal quantization offset saved separately. Getaboda locally 1:1. In later phases compress empty transport segments between geographically true built-up regions without breaking networks; out of scope for M0/first POC.
7. **Build 42 exporter:** only implement against observed correct, legally usable Build 42 tools/format, with current game smoke-test evidence; tolerate manual import/export steps in initial phase.
8. **Packaging:** reproducible mod bundle for GitHub Releases; Steam Workshop later after validation.

## Community and user interface
- Data-file contributions through reviewed GitHub PRs; public code permissive, original art separately licensed, external materials kept under their own terms.
- QGIS can be used as a temporary UI for selecting buildings/editing exported attributes/overrides; no custom editor during POC.
- Agents work in English Markdown and communicate with the creator in Swedish. `HUMAN_OVERVIEW.md` accompanies a manually maintained static HTML view with locally interactive choice buttons and feedback; HTML has no credentials/backend and does not write to GitHub on its own. The dashboard script validates selected markers only.
- Agents implement and test independently within accepted scope; the creator retains creative direction and consequential decisions. Develop Getaboda and the supporting worldbuilding tools openly with the creator through layouts, screenshots and useful technical explanations. Preserve discovery in later areas by default; full developer evidence remains available. See `AGENT_WORKFLOW.md`.
- Creator tests in the real game and returns screenshots/logs. New games are acceptable during development. Once publicly distributed, prefer stable coordinates but never guarantee backward save compatibility until verified.

## Deliberately deferred
Precise real-house interiors, automatic large-scale distance compression, terrain elevation simulation, heavy geodata inference, bespoke editor, custom survival mechanics, standalone engine, multiplayer in first POC, any costs without permission.

## Review gate
Each milestone must list versioned source data, command/test outputs, files produced, in-game manual steps, screenshot/log proof, unverified requirements, and rights checks. Do not equate plausible source code with a playable mod.
