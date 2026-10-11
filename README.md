# ZombieProjektet - project skeleton

A Swedish survival-world project inspired by the *design goals* of realistic survival games.

**Status:** research and technical spikes. No game or working Project Zomboid mod is included.
**Decision pending:** extend Project Zomboid as a mod, or build an original standalone game.

## Why this repository exists

We want the player to ask: "What would I do in real life?" and have a consistent simulation reward reasonable decisions. The long-term world concept is based on Ljungby, Ryssby, Kanna, Agunnaryd and rural Smaland, with house locations preserved where feasible and large empty distances selectively shortened.

The starter contains:
- Vision, scope boundaries, phased milestones, engineering decision record, data-policy notes.
- Independent world-data preparation experiment: converts OSM-like GeoJSON building features into a reproducible *style manifest*. This is NOT a map compiler and does NOT generate in-game tiles.
- Placeholder directories for the two mutually exclusive delivery tracks.
- Agent instructions for Codex/Claude Code, automated Python tests.

## Quick start (Python 3.10+; no third-party packages)

```shell
python -m unittest discover -s tests -v
python tools/building_styles.py --input data/sample/buildings.geojson --output build/building-styles.json
```

Check `docs/ROADMAP.md` and `docs/decisions/0001-mod-or-game.md` before adding engine-specific code.

## Legal boundaries

No Project Zomboid game files, copyrighted graphics, trademarks, or code are included. This repository does not claim official affiliation. Review third-party tool and geographic-data licenses before redistribution.

## Ownership and licensing

All newly written code here is presented as an initial private-project draft; choose a license after checking each contributor's rights. Do not automatically apply a permissive license to copied tools or third-party assets.
