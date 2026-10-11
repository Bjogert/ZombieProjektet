# Roadmap: evidence-gated milestones

## Gate 0: Choose first delivery path
Decide between a Project Zomboid map mod or an original Godot vertical slice. Record the decision in an ADR.

## Gate 1: Verify geographic data pipeline
- Process a small, legally usable OSM extract into normalized road, water, building data.
- Compare rural building coverage against permitted Swedish geodata.
- Preserve source IDs and coordinates and generate deterministic style assignments.

## Gate 2A: Mod spike
- Build a Build 42 test map with legal and compatible tooling.
- Render a Swedish red wooden wall with white corner boards.
- Test player access, collisions, interiors and saving in-game.

## Gate 2B: Standalone game spike
- Fixed orthographic 3D camera, player, house, zombie.
- Door/window interactions, sound, line of sight, inventory and save/load.
- Verify one realistic cause-effect chain through playtesting.

## Gate 3: Evaluate
Compare implementation effort, performance, playability, asset rights and maintenance.

## Gate 4: Expand only verified systems
Ljungby region, Swedish architecture, carefully controlled geographic compression, later Swedish items, vehicles and clothes.

Completion requires reproducible in-engine/in-game proof, not plausible generated source code.
