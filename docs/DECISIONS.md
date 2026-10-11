# Accepted decisions — design grill (2026-10-11)

Summary from questions 1–28; accepted user comments override any overly broad wording in suggested answers.

| Topic | Accepted position |
|---|---|
| Product | Project Zomboid **map mod**; standalone engine deferred indefinitely |
| Test ground | Getaboda (roughly 4–5 buildings) is childhood location and automation experiment |
| Recognition | Accurate footprint/placement where legitimate geodata supports it; generic Swedish house exteriors/interiors now; detailed individual homes later |
| Override approach | Keep per-building overrides separately from generated defaults; reruns preserve corrections |
| Geodata | OSM plus legitimately usable Swedish datasets, with manual gap corrections and provenance |
| Scale | Getaboda 1:1. Later local settlements 1:1, compress suitable countryside road sections between them; preserve topology |
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
| Human-agent handoff | AI writes/tests; user conducts milestone game tests |
| Planning | Grill finished. Maintain MD canonical design/docs and simplified interactive human HTML projection |

**Priority rule:** hobby fun and working proof over exhaustive completeness, but avoid unnecessary traps by preserving source data and clean minimal interfaces. Do not create premature abstractions or gold-plate compatibility.

**Still must verify empirically:** exact Build 42 Stable tool chain; source geodata coverage and license for Getaboda; mod install/map generation process; usable tile resource rights; behavior of user edits on regenerate; multiplayer/save behavior later.
