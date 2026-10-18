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
Status on 2026-10-18: generation and initial game diagnostics implemented; game
acceptance **failed** because official export split the three cottage rooms into
three buildings and emitted zero room metadata objects. Packaging now rejects
that output. See [integration evidence](../INTEGRATION_TEST.md). Do not bypass the
gate or treat the pre-gate diagnostic ZIP as a playtest release.

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
