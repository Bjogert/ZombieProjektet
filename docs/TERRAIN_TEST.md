# Small roadside terrain test

Date: 2026-10-18. TERRAIN-01 is a synthetic design sample around the existing
roadside cottage, not verified Getaboda land cover. The creator approved the
landscape direction on 2026-10-18: maintained plots with flowerbeds, freer
vegetation outside and vanilla gradual overgrowth. Detailed visual and milestone
acceptance remain separate. See [specification](specs/roadside-terrain.md).

## Implementation and repeatability

The optional `--terrain-seed 42` adds a 55 by 59 square patch in authoring cell
0,6. There are 101 narrow shoulder squares with stock grass-edge overlays and
117 grass/bush objects in small clusters. Existing road and staging-pad surfaces,
the complete driveway, cottage TBX, saved garden choice and access envelope stay
unchanged. Vegetation has an additional one-square margin around those areas.

Generation is coordinate/seed deterministic. Repeating the command produces
identical authoring bytes. Of the 108 existing TMX/PZW/PNG/TBX inputs, only
`road_0_6.tmx` changes. Omitting the option preserves the original fixture. The
manifest records algorithm version, seed, bounds and counts. All artwork is
referenced from the local official tiles; no tile images enter the repository.

```powershell
python -m tools.integration_source --source build/road-pipeline-r2/corridor.json --choices examples/roadside_choices.json --output build/roadside-terrain-r1 --terrain-seed 42 --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid"
```

Export `roads.pzw` using WorldEd 2026-09-16, Generate Lots 8x8, all cells, world
origin 0,0 and one thread. The [bounded metadata compatibility stage](INTEGRATION_TEST.md)
and normal package gate remain required for this fixture.

## Verification

- 57 Python tests pass with the cached optional geodata dependencies available.
- Tests cover repeatability, variation, invalid seeds, bounded edits, unchanged
  house/garden/roads, vegetation clearance and identical unaffected authoring files.
- Agent setup, overview marker and whitespace checks pass.
- Local evidence: `build/roadside-terrain-r1/evidence/`. Includes authoring hashes,
  test log, previous game screenshot and temporary read-only QA source.
- Official export completed with the same known split-room metadata defect. The
  compatibility stage changed only `0_7.lotheader`; normal packaging then passed.
- Package: `build/roadside-terrain-package-r1/ZombieProjektetRoadside.zip`, SHA-256
  `3d1e7887bab5c7ca9be8959dc0bcaed6d18256549da05b6e51b63b7d08ba951c`.
- Fresh Sandbox save `2026-10-18_10-02-44`, Steam 42.21.0 / `4a0e9546ec`:
  all 25 existing fixture probes pass. The added full-width driveway check finds
  172 adjacent edges with zero blocking collisions. This is character collision
  evidence, not a vehicle physics test.
- Manual checks: daylight with closed door, normal door opening, walking onto the
  deck and around the cottage, visible pitched roof from outside, visible grass
  clumps and bushes. The previous and new screenshots are local evidence files
  `before-terrain.png` and `terrain-exterior.png`; camera framing differs.
- The first exact-sprite check reported 101/218, retained as a failed diagnostic.
  All 101 grass-edge overlays matched. A save/reload diagnostic then observed
  102 authored grass objects replaced by `e_newgrass_1` variants and 15 authored
  bushes replaced by `f_bushes_1` variants. Local game resources identify these
  replacement paths. Do not require original sprite names for vanilla vegetation.
  Authoring placement is seeded; runtime appearance also depends on vanilla
  growth/season rules. This test does not establish behavior through all seasons.
- Temporary QA was removed. The save loads at its retained exterior position
  with the house, roof and garden visible, then exits normally. All 493 installed
  files match the package and the original default mod selection is restored.
  Evidence: `clean-reload.png`, `game-clean-reload-console.txt` and
  `final-verification.json`. No runtime exception or QA callback is observed.
  Existing stock font, fluid-name and recipe-icon warnings remain in the log.

Final self-review against the specification and engineering standards found no
remaining blocker for this bounded prototype. The source patch adds no dependency
or game mechanic. Broader decoration, trees and arbitrary footprint fitting were
deliberately deferred; detailed visual acceptance and vehicle driving remain open.

## Reuse and remaining gates

The useful pattern is to reserve road, house, garden and access geometry first,
then add seeded detail in the remaining space. Save the seed with the building
choices so regeneration retains the result. This implementation currently supports
the bounded rotation-0 synthetic fixture, not arbitrary real footprints.

For Getaboda, permitted source data must define actual roads/land cover and checked
building positions. Decorative vegetation remains an explicitly synthetic design
choice. The maintained-plot/wilder-outside direction is approved. Review material
changes to that direction and representative detail as real houses are fitted. Continuous vehicle clearance and the whole-corridor drive need
actual driving; pointwise collision probes do not substitute for it.
