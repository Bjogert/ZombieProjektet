# ZombieProjektet — Småland in Project Zomboid

A hobby project building a recognizable Swedish world as a **Project Zomboid Build 42 Stable map mod**. The first real test area is **Getaboda between Agunnaryd and Södra Ljunga**, approximately 4–5 buildings, with later expansion toward Ljungby.

Use lawful source data for actual building locations, roads and land cover. Generate ordinary buildings and details from a small Swedish template library, with separate stable-ID overrides that survive regeneration. Aim for Swedish 1990s atmosphere and a world the creator can enjoy discovering.

## Current state (2026-10-17)
A synthetic test map has been exported with the official mapping tools and smoke-tested in **42.21.0**. World selection, loading, indoor spawn and walking out/in were verified. Closed-door darkness, direct wall collision, roof behavior and human acceptance remain open. See the [M0 report](docs/test-reports/M0-BUILD42.md) for evidence and limitations.

Real Getaboda geometry has **not** been imported or verified. The deterministic GeoJSON style manifest is a separate data experiment, not a playable Getaboda map. A reusable Swedish cottage remains the next visual prototype after closing the technical test-house gaps.

## Start here
- Creator: [project overview](docs/PROJECT_OVERVIEW.html), with local feedback controls; it does not automatically submit anything to GitHub.
- Agents: [AGENTS.md](AGENTS.md), [workflow](docs/AGENT_WORKFLOW.md), [specification](docs/PROJECT_SPEC.md), [decisions](docs/DECISIONS.md) and [roadmap](docs/ROADMAP.md).
- Integration: [Build 42 test plan](docs/BUILD42_SPIKE.md).

Conversation with the creator is in Swedish. Project documentation, code, identifiers and authored UI are in English. Routine updates preserve surprises; developer evidence remains available for inspection.

## Local checks (Python 3.10+, standard library)
```sh
python -m unittest discover -s tests -v
python tools/check_agent_setup.py
python tools/render_dashboard.py --check
git diff --check
python tools/building_styles.py --input data/sample/buildings.geojson --output build/building-styles.json
```

Keep `docs/HUMAN_OVERVIEW.md` and the manually maintained `docs/PROJECT_OVERVIEW.html` consistent. The dashboard check validates selected markers; it does not render or fully compare the documents.

## Rights
Distribute only original material and permitted data. Original code uses [MIT](LICENSE); external data, resources and art retain their own terms. See [DATA_AND_RIGHTS](docs/DATA_AND_RIGHTS.md). This project is not affiliated with The Indie Stone.
