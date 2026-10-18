# ZombieProjektet — implementation specification v1 (updated 2026-10-18)

**Authority:** this specification, `DECISIONS.md`, `ROADMAP.md`, then relevant ADRs. `HUMAN_OVERVIEW.md` is a concise display companion, not an independent authority.

## Product
Project Zomboid **Build 42 Stable** mod. A standalone Swedish world expanding from Getaboda toward Agunnaryd, Södra Ljunga and Ljungby, initially singleplayer and later small private multiplayer. The users are the hobby creator and friends from the region. Their real-world recognition and ability to play outweigh exact reconstruction, historical research, or engine innovation.

## Active showcase priority (2026-10-18)

The creator accepts the environment-library direction and requests a complete
fictional rural dwelling and plot before further real-house fitting. Getaboda
likeness is no longer required for this immediate test. Show the house, deck,
foundation flowerbeds, garden and everyday props together in the actual game.
The [rural showcase](specs/rural-showcase.md) overrides earlier next-delivery
wording; geographic inputs and historical V1 plans remain preserved separately.

## Personal purpose and detail priorities (2026-10-18)
The creator wants to reunite a former PZ group from Ljungby/Agunnaryd and surprise friends with familiar places. Private multiplayer is an eventual product goal, with actual host/client testing before claiming readiness. Getaboda and the tools remain open development with the creator; later-area discovery preferences still apply.

- Concentrate individual exterior and interior work on approximately ten creator-selected homes across the expanding world. Use creator input to identify the rooms and details that matter for recognition. The list and fidelity of each home remain to be chosen; these ten homes are not all required for V1.
- Other buildings use plausible, varied Swedish templates and invented interiors. Research known geometry and useful exterior character, but do not pursue exact room layouts for ordinary homes. Keep verified source facts distinct from design choices; store individual changes through stable-ID overrides.
- Rural hunting weapons are accepted gameplay direction: include hunting firearms in selected rural residential/farm loot rather than assuming a dense gun-shop network. Placement is fictional game content, never a record of real residents' possessions. Frequency, ammunition and balance remain to be designed and playtested; no loot changes are implemented by this decision.
- Tractors are desired rural content, subject to suitable assets and version compatibility. A mod dependency and working agricultural implements are not yet selected. They do not gate V1.

The creator's recollection of a hunting shop near the E4 at Lagan is an unverified research lead; no business identity or location has been confirmed.

### Tractor feasibility check
On 2026-10-18, a search of the installed game's script/Lua definitions and media filenames found no tractor definition. This is a bounded inspection, not a complete vehicle audit. The original [Agrotsar Farming Company](https://pz.ibrrus.ru/mods/agrotsar) documents a tractor and agricultural attachments for Build 41. A separate [Workshop port](https://steamcommunity.com/sharedfiles/filedetails/?id=3587117139) by Beathoven is labelled B42.20 and requires Tsar's Common Library B42. Treat it as a research candidate: distribution status, permissions, compatibility with our recorded 42.21.0 baseline, spawning, driving, save/reload and host/client behavior remain unverified. Nothing was installed or adopted. Assess driving separately from implement mechanics before making a dependency decision.

## First proof of concept — acceptance
1. A separate, loadable Swedish map is tested in a recorded Build 42 Stable game version.
2. Approximately 4–5 actual Getaboda buildings, access roads and basic land cover are present, with source data checked for accuracy and rights. Never invent precise Getaboda coordinates or building footprints.
3. One building at minimum has a usable entrance, collision and minimal interior; the player can move through it in-game. Remaining buildings may use simpler valid game content.
4. Buildings have stable identifiers, source coordinates and data provenance. Classification and generated choices are deterministic and distinguish observed facts from assumptions.
5. A human correction to an individual building survives rerunning the generation process. This is demonstrated in an automated test and in a regenerated game artifact where possible.
6. Installation/export steps (including any manual WorldEd/TileZed step) are documented and reproducible; game test evidence is recorded.

The first **technical gate M0** is deliberately narrower: prove a minimal custom playable Build 42 map with one usable house and record its exact tool chain before building a broad exporter.

The proof of concept above is **Test Version 1 (M3)** in the [roadmap](ROADMAP.md). Deliver it first as a local/private test package. The separate 5.09 km road experiment may accompany it after its own driving gate passes; it does not require Agunnaryd buildings, multiplayer or whole-municipality coverage. A synthetic integration fixture is an intermediate engineering test, not a substitute for source-confirmed Getaboda.

## Layer boundaries (implement only when needed)
1. **Ingest:** OpenStreetMap plus permissible Lantmäteriet/other datasets; respect licenses, source identity, time, geometry and coordinate system. Reject missing/ambiguous critical coverage for the POC until manually checked.
2. **Normalize:** shared feature schema for buildings, roads, vegetation/landuse, water; preserve original source geometry immutable. Use geodata confidence/provenance. Separate stable internal IDs from potentially changing OSM IDs through a documented mapping.
3. **Classify:** begin with a handful of extensible building categories (house/cottage, barn, shed, garage, other). Map known source tags; default to explicit 'unknown/assumed' rather than pretend the type is verified.
4. **Style + interior:** compact JSON definitions of building type, exterior variants and rule-driven basic interiors. Apply deterministic seed derived from stable building IDs. Include 1990s-consistent selections. Residential variants should include decks/patios and gardens with flowerbeds, with variation between houses and clear entrance routes. Record invented garden details as design choices, not verified real-property features. The creator approved maintained residential plots with flowerbeds at game start, freer vegetation along road edges and forest margins outside the plots, and vanilla gradual overgrowth afterward (2026-10-18). Preserve clear access; do not add a custom growth system.
5. **Overrides:** optional separate JSON keyed by immutable internal building ID for user-chosen type, facade, geometry correction, roof, doors, later floor plan. Explicit precedence: permitted observed source -> reproducible generated defaults -> approved manual overrides. Keep layer details documented and validate overrides; overriding original source geometry is forbidden.
6. **Gameplay projection:** transform normalized source coordinates into grid/world cells, with minimal quantization offset saved separately. Start at 1:1, including connecting roads, as approved on 2026-10-17. Preserve the original source geometry. Reconsider countryside compression only after driving/performance evidence and a new creator decision; no compression implementation is currently required.
7. **Build 42 exporter:** only implement against observed correct, legally usable Build 42 tools/format, with current game smoke-test evidence; tolerate manual import/export steps in initial phase.
8. **Packaging:** reproducible mod bundle for GitHub Releases; Steam Workshop later after validation.

## Community and user interface
- Data-file contributions through reviewed GitHub PRs; public code permissive, original art separately licensed, external materials kept under their own terms.
- QGIS can be used as a temporary UI for selecting buildings/editing exported attributes/overrides; no custom editor during POC.
- Agents work in English Markdown and communicate with the creator in Swedish. `HUMAN_OVERVIEW.md` accompanies a manually maintained static HTML view with locally interactive choice buttons and feedback; HTML has no credentials/backend and does not write to GitHub on its own. The dashboard script validates selected markers only.
- Agents implement and test independently within accepted scope; the creator retains creative direction and consequential decisions. Develop Getaboda and the supporting worldbuilding tools openly with the creator through layouts, screenshots and useful technical explanations. Preserve discovery in later areas by default; full developer evidence remains available. See `AGENT_WORKFLOW.md`.
- Creator tests in the real game and returns screenshots/logs. New games are acceptable during development. Once publicly distributed, prefer stable coordinates but never guarantee backward save compatibility until verified.

## Deliberately deferred
Detailed reconstruction of the selected personal homes beyond V1's minimum, automatic large-scale distance compression, terrain elevation simulation, heavy geodata inference, bespoke editor, custom survival mechanics, standalone engine, multiplayer in first POC, any costs without permission. Exact interiors for every home are outside scope; selected personal interiors remain an accepted later priority.

## Review gate
Each milestone must list versioned source data, command/test outputs, files produced, in-game manual steps, screenshot/log proof, unverified requirements, and rights checks. Do not equate plausible source code with a playable mod.
