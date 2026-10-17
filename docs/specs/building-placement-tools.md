# Stable building choices and four cottage orientations

## Value and boundary

TOOLS-01 prepares the reusable authoring path for Getaboda while access to real
data is pending. A separate synthetic map must show four usable cottage
orientations with matching decks and gardens. These placements are invented test
coordinates, never representations of real properties.

The creator approved autonomous implementation and game QA of this bounded tool
workflow. Significant visual direction, geography and release decisions remain
with the creator.

## Contract

- A synthetic placement JSON lists stable building IDs and integer cell origins.
  A separate JSON maps those IDs to house template, clockwise rotation
  (`0`, `90`, `180`, `270`) and optional garden template choices.
- Inputs are immutable. Missing choices use explicit fixture defaults. Unknown
  IDs, fields, templates, rotations, duplicate IDs, out-of-cell or overlapping
  placements fail before output is created. Reordering inputs does not change
  generated source. Adding another building preserves existing choices.
- The generator selects reviewed TBX variants; it does not implement a general
  TBX rotator. WorldEd PZW lots have no rotation attribute in the inspected
  source. BuildingEd rotation drops hand-painted tiles, so restored ceiling and
  corner trim are required in every saved variant. Furniture needs all four
  orientation entries. Keep the earlier cottage and garden fixtures intact.
- Garden coordinates and reserved access routes rotate about the house's
  bounding rectangle. Directional garden furniture uses explicit tile variants.
- Output contains deterministic TMX/PZW, copied TBX sources, a resolved choice
  manifest and zombie-density image for official Generate Lots 8x8. A dedicated
  mod identity keeps earlier fixtures and saves separate.

## Acceptance and evidence

Automated checks prove four known coordinate transforms, directional chair/table
selection, unchanged inputs, stable-ID override persistence in regenerated PZW
and garden layers, deterministic repeat builds and invalid/overlapping placement
rejection. Validate 60 ceiling squares and complete furniture directions in each
TBX; this alone does not establish gameplay.

Official WorldEd must export the four-house fixture. In the installed game,
record the exact version, package hash and a fresh test save. Check all four
houses for rooms, roof coverage, walls, doors/windows, light switches and garden
access; manually traverse each entrance and inspect roofs and directional
furniture. Capture in-game screenshots. Keep creator acceptance separate.

## Exclusions and dependencies

Only the rectangular synthetic cottage is supported initially. No arbitrary
angles, automatic house fitting, GIS processing, real-house color inference,
multiplayer, new assets or public release. Official installed editors and local
stock tile references are required; no proprietary artwork or editor code is
redistributed. The older style-only GeoJSON manifest remains a separate design
experiment; its full palette is not claimed as playable.
