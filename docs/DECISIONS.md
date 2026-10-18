# Accepted decisions — design grill (2026-10-11)

Summary from questions 1–28; accepted user comments override any overly broad wording in suggested answers.

| Topic | Accepted position |
|---|---|
| Product | Project Zomboid **map mod**; standalone engine deferred indefinitely |
| Test ground | Getaboda (roughly 4–5 buildings) is childhood location and automation experiment |
| Recognition | Accurate footprint/placement where legitimate geodata supports it; generic Swedish house exteriors/interiors now; detailed individual homes later |
| Personal purpose (2026-10-18) | Reunite the creator's former PZ group from Ljungby/Agunnaryd with a surprise familiar world; eventual private multiplayer remains a tested later goal |
| Detail priority (2026-10-18) | Approximately ten creator-selected homes across the expanding project receive extra exterior/interior care. Plausible varied templates cover the remainder. The exact list and recognition details remain open; V1 still requires roughly 4–5 Getaboda buildings, not all ten homes |
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
| Landscape at game start (2026-10-18) | Maintained residential plots with flowerbeds; freer vegetation along road edges and forest margins outside the plots. Use vanilla PZ gradual overgrowth afterward. This approves the design direction, not exact prototype density, real-property accuracy or milestone acceptance |
| Rural hunting loot (2026-10-18) | Include hunting firearms in selected rural homes/farms as fictional gameplay placement, never as real household ownership data. Frequency, ammunition and balance remain open for design/playtesting; no loot implementation is implied |
| Agricultural vehicles (2026-10-18) | Tractors are desired if a suitable compatible option exists. Evaluate available assets/mods before selecting a dependency; agricultural implements, Build 42 compatibility and multiplayer are separate checks. Not a V1 blocker |
| Progress previews (2026-10-17) | Include screenshots and short Swedish updates at meaningful milestones during active work. Getaboda and the tools can be shown in detail; preserve discoveries in later areas |
| Initial geodata processing (2026-10-17) | Raw geodata and source imagery stay and are processed locally in Sweden (EU/EEA); cloud/AI upload waits until conditions and access scope are clarified |

**Priority rule:** hobby fun and working proof over exhaustive completeness, but avoid unnecessary traps by preserving source data and clean minimal interfaces. Do not create premature abstractions or gold-plate compatibility.

**Evidence reviewed (2026-10-18):** the official tools produced house/cottage/garden fixtures with recorded checks in Build 42.21.0. See [the M0 report](test-reports/M0-BUILD42.md) and [placement evidence](PLACEMENT_TEST.md); creator acceptance remains open. Saved house/orientation/garden choices survive synthetic playable regeneration; the broader style palette and real-building integration remain unverified. The separate [road prototype](ROAD_TEST.md) has sampled runtime loading and short vehicle-motion evidence, but no continuous route drive. Real building coverage/rights and later multiplayer/save compatibility remain open. The [roadmap](ROADMAP.md) preserves these distinctions and defines Test Version 1 as the Getaboda POC.
