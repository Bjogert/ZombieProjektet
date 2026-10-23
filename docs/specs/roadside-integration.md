# INTEGRATE-01 — synthetic cottage beside the road prototype

## Value and boundary
Join the tested cottage/garden and road exporter in one separate playable test.
The cottage and driveway are fictional placements, not source-confirmed Getaboda.
Use the existing locally normalized road input without changing its coordinates.

## Smallest implementation
- Reuse placement validation, the unrotated cottage and its optional garden.
- Place one stable-ID cottage 25 squares east and 25 south of the starting pad.
  Support the saved garden choice; reject other rotations for this bounded fixture.
- Add a three-square gravel driveway from the pad to the garden's reserved entrance.
  Preserve road/pad surfaces and garden floors; reject house/garden-road overlap,
  obstructed access, out-of-cell placement and unsupported choices before writing.
- Generate a separate authoring folder and officially export through WorldEd.
  Package under `ZombieProjektetRoadside` / `RoadsideTest`, with its own indoor spawn.
  Retain existing fixtures and saves. Do not ship QA scripts or proprietary assets.

## Acceptance and verification
Status on 2026-10-18: the initial official export failed shared building metadata.
The bounded compatibility step below now produces a package with 25/25 runtime
probes, manual interaction/roof checks and clean save/reload evidence. Packaging
still rejects the original defective export. See [integration evidence](../INTEGRATION_TEST.md).
Creator acceptance remains separate; the pre-gate diagnostic ZIP stays diagnostic.

Automated: correct cottage and driveway alignment on a synthetic metric road;
continuous walkable ground connection; no overwritten road/garden surfaces;
stable-ID garden correction survives repeat generation; unchanged inputs;
colliding placement, unsupported rotation and missing exports fail closed;
separate deterministic package with correct spawn and map-scoped vehicle setup.
The cottage's exported header must contain three ground-floor rooms covering 60
squares, one building containing all three room IDs and eight room metadata objects.
Reject truncated headers and the observed split/missing-metadata regression.

Game: record exact version and artifact; fresh spawn; daylight/light switch,
doorway, walls and roof; walk house–deck–driveway–road; save/reload; screenshots.
Change the saved garden choice, regenerate/export and check the resulting game
artifact. Preserve automated, export, game and creator acceptance as separate gates.

No real-house fitting, automatic parcel layout, scenery pass, full-route driving
claim, multiplayer, tractor dependency or public release is included. The existing
road-driving gate remains open. Raw geodata stays local under DATA_AND_RIGHTS.md.

## Bounded exporter compatibility step
The identical rotation-0 TBX exports correctly at (120,120) in authoring cell
(0,0): one building, three rooms, eight room objects. At the roadside location,
the official exporter produces correct room rectangles and physical tiles but
splits membership and loses room objects. Retain both original exports.

Implement a separate staging command for this single synthetic cottage only:
- Require identical TBX bytes, one ground-floor 6x10 lot, zero world origin,
  the expected integration manifest and complete official export files.
- Require three uniquely matching room names/floors/translated rectangles,
  a valid reference and exactly the observed split-building/zero-object failure.
- Preserve target room order/IDs, rectangles, tile table, level bounds and zombie
  suffix. Translate only the reference room objects and map reference membership
  onto the existing target IDs. Reject unsupported geometry, levels or counts.
- Write a fresh staging directory with a hash-based provenance record. Preserve
  every other export byte and both inputs. Refuse existing output directories.
- Keep the packaging gate. Prove malformed/mismatched input rejection,
  deterministic output and unchanged physical exports with synthetic tests.
- Verify shared building identity, lighting, roof, entry and save/reload in-game.

This is a documented compatibility transformation of official output, not a new
map exporter or a general repair tool. Remove/revisit it when the pinned official
tool is fixed; do not silently apply it to unrelated buildings or versions.
