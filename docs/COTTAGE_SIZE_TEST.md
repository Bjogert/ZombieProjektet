# Sized cottage verification — 2026-10-18

## Purpose and boundary

Adapt the original three-room cottage to the approximate dimensions needed by
the local Getaboda candidates. `tools/cottage_variant.py` produces deterministic
6–12 by 9–18 square sources with a west entrance, generic rooms and stock tile
references. It preserves the authored 6 by 10 source. The fixed garden still
rejects other house sizes. No private layout or real exterior is inferred.

Only the representative **8 by 12** variant has the game evidence below. Other
dimensions pass source checks; their game appearance is not yet verified.

## Failure and correction

Revision r1 exported successfully and passed 11 runtime probes, including all
96 indoor/ceiling squares. Exterior inspection nevertheless found a central
roof gap: the original steep roof covers only three squares on each side.
Metadata and ceiling tests alone did not detect this visual failure.

Revision r2 uses supported 30-degree stock roof primitives for wider cottages.
Even widths use two opposing slopes; odd widths use the supported ridge type.
A regression test rejects unsupported spans and verifies full, non-overlapping
coverage for every supported width. All 72 referenced roof mappings in r2 match
the installed official BuildingEd tile configuration. The original cottage's
steep roof remains unchanged. The wider gable uses red-brown barn wood references;
its palette is provisional and is not evidence of Getaboda appearance.

## Artifact and reproduction

- Official tools: 2026-09-16 distribution, WorldEd Generate Lots 8x8, origin 0,0,
  one thread. One building, three rooms, three room rectangles, eight objects.
- PZ: 42.21.0, `4a0e9546ec`, Steam, windowed 1280 by 720.
- ZIP: `build/cottage-size-r2/package/ZombieProjektetCottage.zip`.
- SHA-256: `6b93c02a6d4cfb3ae94397bf5acfc0e010b6d75405ddca8a2a398295ebad6c28`.
- Fresh Sandbox save: `2026-10-18_12-03-33`, Custom Occupation, no zombies,
  July 9 at 9 AM. Separate from the earlier failed test and valuable saves.

```powershell
python -m tools.cottage_variant --width 8 --height 12 --output build/cottage-size-r2/source/cottage_8x12.tbx
python -m tools.build_cottage --output build/cottage-size-r2/authoring --tiles C:/PZModding/Tools/Official-2026-09-16/Tiles/2x --game "C:/Program Files (x86)/Steam/steamapps/common/ProjectZomboid" --cottage build/cottage-size-r2/source/cottage_8x12.tbx
```

After official export, call `validate_cottage_metadata(header, expected_area=96)`
before packaging. Paths refuse existing output; use a fresh directory for a repeat.
The source generation itself does not perform or prove official export.

## Game evidence

The fresh r2 test passes 11 read-only runtime checks: collision against each of
four walls, clear entry/path, 96 indoor squares, 96 ceiling squares, three doors,
seven windows and three light switches. Daylight is visible with the door closed.
The entrance opens normally and the character walks through it and around the
house. The full exterior view shows continuous roof slopes and a closed gable.

Temporary local QA files are excluded from the ZIP. One weather-only helper
disables fog during exterior inspection; this is an explicit test condition,
not a shipping gameplay feature. It does not change map geometry or position.
The original installed cottage and default mod selection were backed up first.

Evidence is local under `build/cottage-size-r2/evidence/`: `worlded-export.png`,
`closed-door.png`, `exterior.png`, `console-first.txt` and `tests.txt`.
The failed r1 roof screenshot and logs remain under `build/cottage-size-r1/evidence/`.

After a full game restart, explicitly loading the same save passes **12/12**
read-only checks. The added probe finds a stock slope sprite on every one of the
96 roof squares. The exterior remains present after reload; `reload.png` and
`console-reload.txt` record this check. Both sessions shut down normally
(`GameThread exited`). Nine startup ERROR lines (six distinct messages)
concern stock font/container/recipe resources and are identical in r1 and r2; they
are retained in the logs rather than called a clean global error count.

After testing, the temporary installed variant was archived under
`build/cottage-size-r2/evidence/test-installed`. The original cottage installation
and default mod selection were restored and compared byte-for-byte with the
pre-test backup. No saved world was deleted. Reinstall r2 before loading its
diagnostic save; it shares the cottage test map identity with the original fixture.

## Remaining gates

Real candidate identity, exact V1 selection, footprint approximation, house
orientation, driveway evidence, exterior likeness and creator acceptance remain
open. This validates a reusable synthetic building component, not Getaboda V1.
Garden resizing and additional roof/palette variants are separate work when needed.
