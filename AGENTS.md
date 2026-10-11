# Instructions for coding agents (Codex, Claude Code)

1. Read `docs/VISION.md`, `docs/SCOPE.md`, `docs/ROADMAP.md`, and `docs/decisions/0001-mod-or-game.md`.
2. Do not assume the engine has been chosen. Keep geographic data processing independent of engine.
3. Never copy Project Zomboid source code, textures, models, audio or game files here.
4. Do not extract protected Google Maps/Earth imagery or data.
5. Respect OSM ODbL, exact Lantmateriet dataset terms, mod asset licenses.
6. Make small testable changes; run `python -m unittest discover -s tests -v`.
7. Deterministic results for same seed/input; preserve source coordinates and stable IDs.
8. Mark adapters and game integrations as TODO until proven in-game.
9. Verify upstream API and version details rather than guessing.
10. Prioritize a playable, real-world-causal vertical slice over feature counts.
