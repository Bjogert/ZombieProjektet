# Accepted decisions — design grill (2026-10-11)

Summary from questions 1–28; accepted user comments override any overly broad wording in suggested answers.

| Topic | Accepted position |
|---|---|
| Product | Project Zomboid **map mod**; standalone engine deferred indefinitely |
| Test ground | Getaboda (roughly 4–5 buildings) is childhood location and automation experiment |
| Recognition | Accurate footprint/placement where legitimate geodata supports it; generic Swedish house exteriors/interiors now; detailed individual homes later |
| Override approach | Keep per-building overrides separately from generated defaults; reruns preserve corrections |
| Geodata | OSM plus legitimately usable Swedish datasets, with manual gap corrections and provenance |
| Scale (updated 2026-10-17) | Start at 1:1, including the Getaboda–Agunnaryd road trial. Preserve source coordinates. Reconsider countryside compression only after driving and performance tests; this supersedes the earlier assumption that connecting countryside would be compressed |
| Game target | Build 42 Stable; record tested exact version in every integration test |
| World | Separate Swedish world, expandable toward Ljungby |
| Assets | Small original Swedish tile library supplementing permitted use of built-in game resources; no copied proprietary art |
| Interiors | Minimal rule-based playable interior, evolving via library and individual edits |
| Extensibility | Open data-file-based (e.g. JSON) building library; other contributors can add types/buildings |
| Unknown building type | Best-effort automatic categorization with manual map/QGIS selection; record uncertainties |
| Automation | Stepwise automated processing + temporary manual export/import allowed; automate later only after evidence |
| First POC success | Getaboda's 4–5 houses, nearby roads/landscape, enter one house, rerun preserving corrections |
| Grid | Original geo coordinates preserved; quantization/play adjustments tracked separately |
| Save compatibility | Aim to avoid moving released areas, but experimental resets/rebuilds acceptable; don't build migration machinery |
| Multiplayer | Singleplayer first; private friends multiplayer later using game's systems |
| Nature | Forest/farmland/water aligned to permitted geodata; deterministic vegetation |
| Elevation | Flat gameplay terrain now; future height source retained if legitimate/useful |
| Time period | Modern cartographic shapes, **1990s in-world styling**, without historical reconstruction |
| Distribution | GitHub release zip when playable, later Steam Workshop |
| Licenses | Permissive own code/library where rights allow; independent licenses for external data/art |
| Real-home privacy | Generic interiors default; carefully review detailed private interiors before publishing |
| Costs | Free/open default; explicit approval before purchases |
| Human-agent handoff | AI implements, tests and resolves routine QA; creator playtests milestones for feel and acceptance |
| Planning | Grill finished. Maintain MD canonical design/docs and simplified interactive human HTML projection |
| Language (2026-10-17) | Swedish conversation; English documentation, code, identifiers and authored UI; preserve proper names |
| Autonomy (2026-10-17) | Agent proceeds within agreed scope; creator participates in design and consequential decisions |
| Discovery (2026-10-17, clarified) | Develop Getaboda and the worldbuilding tools openly with the creator, including layouts, screenshots and technical explanations. Preserve surprises in later areas by default; full evidence remains available |
| Residential outdoor character (2026-10-17) | Include decks/patios and gardens with flowerbeds in the Swedish residential library. Vary them by house; synthetic garden design is not verified information about a real property |
| Progress previews (2026-10-17) | Include screenshots and short Swedish updates at meaningful milestones during active work. Getaboda and the tools can be shown in detail; preserve discoveries in later areas |
| Initial geodata processing (2026-10-17) | Raw geodata and source imagery stay and are processed locally in Sweden (EU/EEA); cloud/AI upload waits until conditions and access scope are clarified |

**Priority rule:** hobby fun and working proof over exhaustive completeness, but avoid unnecessary traps by preserving source data and clean minimal interfaces. Do not create premature abstractions or gold-plate compatibility.

**Evidence update (2026-10-17):** the official tools produced a map smoke-tested in Build 42.21.0. See [the M0 report](test-reports/M0-BUILD42.md) for demonstrated behavior and remaining checks. M0 acceptance is pending. Getaboda data coverage/rights, override persistence in a playable artifact, and later multiplayer/save behavior still require verification.
