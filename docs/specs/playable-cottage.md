# Playable representative cottage — COTTAGE-01

## Purpose and behavior

Turn the existing original `swedish_cottage_01.tbx` into a separate playable
fictional test map before any real Getaboda integration. Keep the tested M0 map
and existing saves intact. The stock exterior palette remains provisional.

The 6 x 10 cottage has generic furnishing, doors, windows, room light switches,
ceiling coverage and a pitched roof. A fresh game starts inside near its entrance.
`tools/build_cottage.py` prepares deterministic terrain plus a separate TBX lot;
the official WorldEd Generate Lots 8x8 command compiles game files. The existing
packager gains an explicit `cottage` profile with a distinct mod/map identity.

## Acceptance and verification

- Repeatable authoring output, unchanged input TBX, no artwork copied.
- Missing resources fail before source output is created; existing output is
  never silently replaced.
- Package has its own spawn/map metadata and Build 42 common map directory.
- Actual Build 42 load, entrance traversal, windows, lighting, wall collision,
  indoor classification and visible roof are recorded separately from Python tests.
- One representative exterior preview supports later creator design feedback.

The optional read-only runtime probe is kept outside distributable mod source.
Automated source/package tests cannot prove engine compatibility. Runtime evidence
and unresolved checks belong in `docs/COTTAGE_TEST.md`; creator acceptance remains
separate from agent checks.

## Boundaries

No real geodata, private interiors, custom game artwork, new game mechanics or
public release. Assets are tile-name references to permitted installed resources.
No automatic style-manifest-to-map integration is claimed by this slice.
