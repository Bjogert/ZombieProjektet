# ZombieProjektet — Småland in Project Zomboid

A hobby project building a recognizable Swedish world as a **Project Zomboid Build 42 Stable map mod**. The first real test area is **Getaboda between Agunnaryd and Södra Ljunga**, approximately 4–5 buildings, with later expansion toward Ljungby.

Use lawful source data for actual building locations, roads and land cover. Generate ordinary buildings and details from a small Swedish template library, with separate stable-ID overrides that survive regeneration. Aim for Swedish 1990s atmosphere and a world the creator can enjoy discovering.

## Current state (2026-10-17)
A synthetic test map has been exported with the official mapping tools and tested in **42.21.0**. World selection, indoor spawn, doorway traversal, closed-door daylight and the light switch work. Runtime collision probes pass on all four walls; the roof covers all 80 room squares and renders outdoors. Human acceptance remains open. See the [M0 report](docs/test-reports/M0-BUILD42.md) for evidence and limits.

The first [reusable cottage](assets/buildings/README.md) is furnished, exported and agent-tested in a separate playable map. Entrance traversal, a window, a light switch, indoor daylight, wall collision and roof coverage/rendering pass; see [COTTAGE_TEST](docs/COTTAGE_TEST.md). A separate [garden template](assets/gardens/README.md) now adds a wooden deck, outdoor furniture and three flowerbeds, with game checks recorded in [GARDEN_TEST](docs/GARDEN_TEST.md). Its stock exterior palette and landscaping still await creator review.

Real Getaboda geometry has **not** been imported or verified. The deterministic GeoJSON style manifest now preserves separate manual style overrides by stable ID, with automated regression checks. Connecting those choices to regenerated playable maps remains future work.

## Start here
- Creator: [project overview](docs/PROJECT_OVERVIEW.html), with local feedback controls; it does not automatically submit anything to GitHub.
- Agents: [AGENTS.md](AGENTS.md), [workflow](docs/AGENT_WORKFLOW.md), [specification](docs/PROJECT_SPEC.md), [decisions](docs/DECISIONS.md) and [roadmap](docs/ROADMAP.md).
- Integration: [Build 42 test plan](docs/BUILD42_SPIKE.md).
- World data: [Getaboda source audit and automation workflow](docs/GEODATA_WORKFLOW.md), including verified 2025 imagery catalog coverage and remaining access/appearance gaps.

Conversation with the creator is in Swedish. Project documentation, code, identifiers and authored UI are in English. Getaboda and the worldbuilding tools are developed openly with the creator; later areas retain surprise by default. Developer evidence remains available for inspection.

## Local checks (Python 3.10+, standard library)
```sh
python -m unittest discover -s tests -v
python tools/check_agent_setup.py
python tools/render_dashboard.py --check
git diff --check
python tools/building_styles.py --input data/sample/buildings.geojson --output build/building-styles.json
python tools/building_styles.py --input data/sample/buildings.geojson --overrides data/sample/building-style-overrides.json --output build/building-styles-corrected.json
```

Keep `docs/HUMAN_OVERVIEW.md` and the manually maintained `docs/PROJECT_OVERVIEW.html` consistent. The dashboard check validates selected markers; it does not render or fully compare the documents.

The [style override contract](docs/specs/building-style-overrides.md) preserves manual style choices by stable ID while leaving source geometry unchanged. Its automated tests prove manifest behavior; playable map regeneration is a later integration step.

## Rights
Distribute only original material and permitted data. Original code uses [MIT](LICENSE); external data, resources and art retain their own terms. See [DATA_AND_RIGHTS](docs/DATA_AND_RIGHTS.md). This project is not affiliated with The Indie Stone.
