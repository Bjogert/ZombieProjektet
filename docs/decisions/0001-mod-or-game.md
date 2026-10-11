# ADR-0001: Project Zomboid mod or standalone game?

**Status: UNDECIDED**

## Option A: Build a mod
Pros: existing gameplay systems, deep survival mechanics and community. Cons: upstream compatibility, mod API limits and third-party licensing.

## Option B: Standalone game
Pros: control over engine, architecture, art and simulation. Cons: substantial new work in animation, AI, physics, inventory, save system, user experience and content.

## Evidence needed
Compare short working slices for both approaches:
1. Time to first realistic interaction: break window -> noise -> zombie response.
2. Time to turn an OSM building footprint into a recognizable Swedish house.
3. Iteration speed, debugging, save compatibility, licenses and practical performance.

Do not copy proprietary game assets or source into standalone game.
