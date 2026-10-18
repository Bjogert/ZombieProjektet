# Provisional Getaboda candidate pilot

Date: 2026-10-18. This slice connects one local Microsoft footprint candidate
to the registered village road in the approved 45-degree, 1:1 grid. The creator
asked development to continue while better owned photos are pending. Candidate
identity, residential use, exact appearance and the final V1 subset remain open.
See the [bounded specification](specs/candidate-house-pilot.md).

## Authoring and provenance

`python -m tools.candidate_source` reads a frozen register, a derived local layout
and a separate stable-ID garden choice. It checks source hashes, registered
identities, supported rectangular dimensions, overlap and road geometry before
writing a fresh authoring directory. Existing output is refused. Original source
geometry and choices are never rewritten; the local receipt records input hashes
and design assumptions. Only aggregate counts reach stdout.

The selected candidate fits the supported 8 by 12 rectangle. One official
authoring cell contains the cottage, 1,332 road squares and 64 access squares.
The nearby registered road segment is about 266 m long. Width is provisionally
5 m and missing surface information uses a gravel fallback. The access route is
an assumed two-square pedestrian connection, not a surveyed driveway or verified
vehicle entrance. Other candidate rectangles are reserved as obstacles.

The stock cottage, generic rooms, west entrance, deck, flowerbeds and plain grass
outside are provisional design choices. No Google screenshot was traced or
imported. No real interior, facade or garden is claimed as verified.

Local inputs: `local-data/getaboda/candidate-pilot-layout.json`,
`candidate-pilot-choices.json`, the frozen `microsoft-2026-08-13/` register and
the existing nearby-road diagnostic. Two authoring runs were byte-identical and
all six checked input files, including the register's original choices, were
unchanged. The command deliberately consumes the reviewed local layout; it does
not itself classify buildings, derive the geographic projection or acquire data.

## Export, package and game evidence

- 71 Python tests pass with the cached geodata dependencies available. New tests
  cover repeatability, preserved choices/source bytes, connected unobstructed
  access, optional garden output and rejection of unsupported inputs.
- WorldEd 2026-09-16, Generate Lots 8x8, world origin 0,0, one thread: export
  succeeds. The normal metadata gate sees one building, three rooms, 96 indoor
  squares and eight room objects. No metadata compatibility edit was needed.
- Local authoring: `build/getaboda-candidate-r2/authoring/`. Evidence is in the
  adjacent `evidence/` directory. Export spans four runtime cells and twelve
  binary files.
- The first complete package did not appear in world selection. Its empty
  `common/` directory lacked `common/media/maps/`, which Build 42's MapGroups
  requires before examining the version directory. The existing M0 report and
  template tests already document this requirement; the ad-hoc packager missed
  it. Corrected package r3 explicitly retains the directory in the ZIP. World
  and spawn selection then work. Preserve this requirement in future packaging.
- Corrected local artifact:
  `build/getaboda-candidate-r2/package-r3/ZombieProjektetCandidatePilot.zip`.
  SHA-256: `b3421ef4e9ebdbd53abf89c8638f3160b8d80285d2317600dc8d4ef5f28221f8`.
  Separate mod ID `ZombieProjektetCandidatePilot`; map `GetabodaCandidatePilot`.
  Includes Microsoft CDLA-Permissive-2.0 and OSM attribution. QA is excluded.
- Fresh Sandbox save `2026-10-18_14-13-14`, zero zombies, Steam Build 42.21.0 /
  `4a0e9546ec`: 17/17 read-only runtime probes pass, including four walls,
  clear entry/deck, 96 ceilings/roof slopes/indoor squares, shared building
  identity, three doors, seven windows, three switches, 24 exterior deck floors
  and eleven flower tiles. All 94 adjacent access edges are clear.
- Manual checks: visible interior with the entrance closed, normal door opening,
  walking onto the deck and all the way to the road junction and back, and a
  complete pitched roof viewed from outside. The nearby automatic cutaway hides
  walls/roof as usual; moving farther away restores the exterior. No teleport,
  climate override or movement script was used.
- Normal window-close saved the world and exited the game. Full process restart
  and loading the same save retained the exterior position and passed 17/17
  probes again. Evidence: `console-first.txt`, `console-reload.txt`,
  `interior-closed-door.png`, `walk-road-junction.png`, `exterior-roof.png`,
  `reload-selection.png`, `reloaded-exterior.png`.

The read-only QA helper was removed and the original default mod selection
restored. A second full process restart loads the same save with only packaged
content, retaining the exterior and character position. All 17 installed files
match the ZIP, with the required empty discovery directory present. No QA callback
or exception appears in the clean log, which records normal save and exit. Stock
font, fluid-name and recipe-icon warnings remain. Evidence: `clean-reload.png`,
`console-clean.txt` and `package-parity.json`. Creator acceptance is separate.

## Review and next work

Sequential self-review against the specification and engineering standards found
no remaining authoring blocker. The source hash is a binding to the previously
validated register, not independent verification of the real building. Official
export and local packaging remain explicit steps; this is not a village exporter.

Next: reuse the tested bounded vegetation/road-edge pattern at this placement,
then add only variants required by the remaining candidates. Better photos can
correct appearance later through stable-ID choices. Keep raw geodata and build
receipts local. Final V1 selection, real-house verification, source-backed land
cover, actual vehicle driving and creator acceptance remain separate gates.
