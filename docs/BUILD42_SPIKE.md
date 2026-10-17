# M0 test plan — first playable separate Build 42 map

**State: EXPORTED / NOT VERIFIED IN GAME (2026-10-17).** Official 8x8 export and local mod package exist. Gameplay acceptance remains open; see [evidence](test-reports/M0-BUILD42.md) and [playtest instructions](PLAYTEST_M0.html).

## Goal
Using legally permitted, currently compatible mapping tools, ship the smallest separate Swedish-world test map loading on **Project Zomboid Build 42 Stable**. At least one building should have a working entrance, basic inside space, correct player collision, and a documented spawn point.

## Preconditions
- The human tester has an installed Project Zomboid Build 42 **Stable** version. Capture exact build string.
- Verify official/community tool version and authoritative modding documentation. Do **not** assume Build 41 file format and older WorldEd examples work unchanged.
- Confirm source/tool licenses before adding anything to the repository; test with placeholder/fabricated terrain instead of Getaboda real data.
- No paid dependencies.

## Minimal experiment
1. Record game build and the specific mapping tool/version, downloads and setup, with links in the test log.
2. Make a 1-cell or similarly minimal separate world map with ground, a simple building, interior space, a door, a small road and player starting location, following tool-chain requirements confirmed in step 1.
3. Export/import using the actual Build 42 tool path, manually if necessary. Keep a fully reproducible procedure and only original/redistributable files in Git.
4. Have the human install/enable the map and start a **new save**. Verify the world selection, spawn, terrain, doorway, wall collision, entering/leaving interior, game log and errors.
5. Record pass/fail for each acceptance criterion in `docs/test-reports/M0-BUILD42.md`; attach screenshots or describe paths; never claim success without human test.
6. Package source project and documented reproduction steps. If blocked, stop and write `BLOCKED` with minimal repro and one recommended next action.

## Acceptance checklist
- [ ] Exact build and verified compatible mapping tools documented.
- [ ] Test level/map can be reproduced by a second developer.
- [ ] Map appears as **separate selectable/playable** world.
- [ ] Character spawns where expected.
- [ ] Ground and test road render.
- [ ] Door, wall collision, and entering/leaving the house work.
- [ ] No unexplained critical game loading errors.
- [ ] Licensing/reuse of all files verified.
- [ ] Human game test logs/screenshots linked.

## Agent work ticket
**Title:** M0: verify minimal Build 42 custom map integration
**Do only:** source verification, toolchain experiment, minimal map, repro instructions, evidence capture.
**Do not:** write general OSM importer, procedurally generate all Getaboda, build full house tileset, optimize multi-region compression, claim game test via Python alone.
**Deliver:** small verified mod/test data, exact install instructions and report; when game test requires user, provide a short checklist and wait for actual result.

## Human playtest (draft, update after actual toolchain is known)
1. Enable the test mod in Build 42 Stable.
2. Start a **new game** with the test map.
3. Check that the test house and road render and you can walk into the house.
4. Return a screenshot of the world and the relevant game log if it fails.

No Project Zomboid files are included in the repository.
