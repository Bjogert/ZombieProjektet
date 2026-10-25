# Roadmap — Getaboda first, then a growing Swedish world

Updated 2026-10-25. **This is the only execution queue.** Rows are plans/evidence,
not running jobs. Product: PZ Build 42 Stable map mod, modern geography with Swedish
1990s styling, 1:1 including roads and the creator-approved 45-degree Getaboda grid.
Municipality coverage is a horizon, not the next delivery. Compression needs a new
creator decision backed by driving/performance evidence.

The creator authorizes the bounded [studio/household direction](decisions/0002-studio-and-households.md).
It does not replace the existing showcase, introduce an engine, increase V1 scope,
change release permissions or approve actual loot frequencies.

## Next delivery and current position

**First playable priority remains RURAL-SHOWCASE-01.** r5 has recorded official
export, 23/23 runtime probes, manual light/door/walk/roof checks and clean
restart/reload. The creator accepted the displayed visual direction; personal
playtesting/final milestone acceptance remain open. r6 source refinement is
integrated, but still needs fresh official export and game/reload proof. See
[RURAL_SHOWCASE_TEST](RURAL_SHOWCASE_TEST.md) and [the spec](specs/rural-showcase.md).
Do not rebuild the basic house, multiply r6 yet or treat the new design planner
as game content.

The last source handoff recorded 72/72 tests in a clean worker checkout and 71/72
in the local canonical checkout due to a pre-existing dirty `cottage_270.tbx`
ceiling-layer change. Preserve the file and backup; investigate the local diff
before declaring that checkout green. No cloud/documentation task can establish
that an uncommitted local change has been repaired.

Next game step: export `build/rural-showcase-r6/authoring/cottage.pzw` with official
WorldEd, validate/package the rural profile, inspect a fresh save and clean
restart/reload. Check furniture seams and interaction, seven windows, routes,
foundation planting, service/seating areas and roof. Keep r5 as the restore point.
The reviewed source assignment `rural_plot_polish` returned `3b8db3b`, integrated
as `05b9948`; its earlier review is not a review of this new studio change.

**Getaboda G01–G04 remain the selected starting batch (2026-10-19).** Selection is
not confirmation of identity, use, appearance or final fitting. Existing source
geometry, unknown properties, provenance and overrides remain separate.

## Prioritized execution queue

States: Ready = actionable within scope; Waiting = named dependency;
Source checked = limited source/automated evidence; Game evidence recorded =
specified artifact checks, not creator acceptance; Proposed later = not current work.
The lead is integration owner. A task blocked by local UI can coexist with one
small independent source task; this is not permission for uncontrolled parallelism.

| Order / ID | State / responsibility | Bounded result | Dependency / next action |
| --- | --- | --- | --- |
| 0 · BASELINE-RECONCILE-01 | Ready on local checkout; lead/QA | Understand the dirty `cottage_270.tbx` test regression without discarding edits | Preserve backup, inspect diff and rerun affected/full checks with exact results. Clean-branch results cannot clear a dirty checkout. |
| 1 · RURAL-SHOWCASE-01 | r5 game evidence; r6 awaiting game check; lead/buildings | Export and verify the already-authored complete rural dwelling/plot | Follow next step above. No more variants until access/roof/light/reload pass. |
| 2 · EVIDENCE-01 | Ready with local evidence; lead/QA | Curated accessible showcase screenshots and artifact index | Locate actual r5/r6 captures. Review rights/privacy; commit a small fictional-showcase selection or approved attachment, not all of ignored build/. Identify missing images explicitly. |
| 3 · STUDIO-01 | Source implementation in review; lead | Lean routing, role definitions, two focused skills, dynamic skill-parity checks and static overview | Check the full checkout and native agent discovery. No workers/schedules started by configuration. See STUDIO_WORKFLOW.md. |
| 4 · ART-01 | Ready for bounded assessment; Art Director/Technical Artist | One compact style brief and stock-resource audit for high-value Swedish details | Use actual showcase views. First candidates: faluröd panel, white corners/trim and white bargeboards; retain working roof tiles. New images/assets require game and rights proof. |
| 5 · HOUSEHOLD-01 | Offline prototype source checked; interior designer/QA | 20 fictional seeds plus deterministic, frozen design briefs | New tests cover design behavior only. Run full-checkout CI/client checks. No actual item IDs, layout, loot or claim of better in-game visuals. |
| 6 · ROOM-01 | Waiting for verified baseline and scoped design; interior/technical artist | One reusable room recipe, three coherent variants, then reuse in a second compatible room | Consume the brief through existing TBX/placement tools. Preserve access, all object parts and one correction. Official export/game/reload plus independent review and measured manual effort. |
| 7 · INTEGRATE-01 | Game evidence recorded; lead/buildings | Maintain cottage/garden/road synthetic fixture | Existing 25/25 probes, manual checks and clean reload after bounded metadata correction; defective original export still rejected. Recheck after shared changes. |
| 8 · DATA-ACCESS-01 | Waiting for verified access outcome; world/data | Smallest permitted source acquisition | Last authenticated check 2026-10-18: both Geotorget applications under review. Verify current outcome, do not assume approval or submit duplicates. Independent source work continues. |
| 9 · PIPELINE-01 | Technical evidence recorded; world/data | Reproduce registered corridor and authoring inputs | Existing 152 segments/108 authoring inputs repeat identically; preserve local processing, provenance and coverage limits. |
| 10 · TERRAIN-01 | Bounded game evidence; buildings/world | Maintain road-edge/vegetation pattern with clear access | Existing 172 clear character adjacencies and clean reload. Maintained plots/wilder edges/vanilla overgrowth accepted; exact visual details and vehicle clearance remain separate. |
| 11 · GETABODA-01 | Provisional register; verification pending; world/data | Verify selected G01–G04 and the small source subset | Microsoft snapshot supplies 13 candidates; OSM absence is not empty land. Preserve IDs, raw geometry and the approved rotation/scale. Identity/use/appearance still need evidence. |
| 12 · HOUSE-FIT-01 | Provisional game evidence; residential refinement; buildings/lead | One traceable real house using proven components | 8 x 12 sized cottage and candidate have recorded checks; candidate 17/17, landscape 19/19 with reload. Improve barn-like residential silhouette, not more scaled copies. Real likeness remains unverified. |
| 13 · GETABODA-ASSEMBLE-01 | Waiting; lead | V1 with about 4–5 source-confirmed buildings and surroundings | Verified subset, required fitting, roads and land cover. Only necessary variants; not a whole-town personality catalogue. |
| 14 · V1-QA-01 | Waiting; QA/lead | Fresh-install/regeneration/walk-drive/reload package and creator playtest | Assemble first, resolve technical failures, preserve one correction and attach evidence/known limits. |
| Conditional · DRIVE-INPUT-01 | Waiting for supported sustained control; QA/lead | Reliable accelerate/turn/brake/stop input | Earlier native key-tap and Escape attempts did not establish held input. One new testable diagnostic, not repeated tap loops. No teleportation-as-driving claim. |
| Conditional · ROAD-TEST-01 | Waiting for DRIVE-INPUT-01; QA/lead | Actual continuous 5.09 km run | Keep existing 52 road samples/66.47 m motion evidence, but neither proves the full drive. Check bends, boundaries, travel time and stutter. |
| Review · DESIGN-REVIEW-01 | Direction accepted; creator with lead | Representative visual choices and acceptance | Preserve 2026-10-18 landscape/gable decisions. 2026-10-25 prioritizes Swedish trim/material details. Exact assets, likeness and milestones remain separately reviewed. |
| Later · LOOT-01 | Proposed later; lead/QA | Small compatible household-to-container loot experiment | Requires ROOM-01 proof, inspected current-build APIs/item IDs, rarity/value budget and explicit balance review. No politics/gender/geography-to-crime shortcuts. Never rebuild the vanilla loot system by default. |

The new household prototype is preparation inside M2. ROOM-01 may simplify or stop
if it does not demonstrate practical reuse. A complete population model, biography
for every house and new loot system are **not** new V1 requirements.

## Dependency path

`BASELINE-RECONCILE-01 → RURAL-SHOWCASE-01 (r6 proof) → ROOM-01`

`EVIDENCE-01 + ART-01 + HOUSEHOLD-01 → ROOM-01 → optional LOOT-01 proposal`

`DATA-ACCESS-01 → GETABODA-01 → HOUSE-FIT-01 → GETABODA-ASSEMBLE-01 → V1-QA-01`

`INTEGRATE-01 + PIPELINE-01 + TERRAIN-01 → GETABODA-ASSEMBLE-01`

`DRIVE-INPUT-01 → ROAD-TEST-01` remains a separate path. It gates claiming the full
corridor tested/regional road expansion, not unrelated fixture or source work.
Local V1 driving still needs its own actual check. Permitted alternative data can
advance provisional fitting without claiming that the LM access gate passed.

## Test Version 1 — unchanged scope

V1 is M3: a local/private Getaboda proof of concept, not the municipality or a
complete survival campaign. Required:

1. Approximately 4–5 source-confirmed buildings with checked positions/footprints,
   stable IDs and provenance; G01–G04 are starting candidates, not verified facts.
2. Connected nearby roads/driveways at 1:1 and basic source-backed land cover;
   unknown measurements and invented details stay labelled.
3. At least one usable furnished house with entrance/collision/light/roof proof;
   others may be simpler but valid and traversable where intended.
4. Swedish 1990s character, representative exterior and varied appropriate plots;
   generic fictional interiors remain the default.
5. One manual correction survives regeneration, official export and game checks
   without changing source geometry or unrelated building choices.
6. Fresh install/spawn, local walk/drive, save/reload and recorded package/version
   evidence; technical QA precedes a short creator playtest request.

The 5.09 km corridor can accompany V1 after its own driving gate; otherwise it
remains experimental. Agunnaryd buildings, multiplayer, public release, custom
survival mechanics, a large Swedish tile catalogue and whole-municipality generation
remain outside V1. A synthetic showcase does not replace real Getaboda validation.

## Phases and exit gates

| Phase | Outcome | Exit / dependency |
| --- | --- | --- |
| M0 | Maintain proven house/road fixtures and exact tool chain; close QA gaps | Game proof and restoration path; continuous driving still open, creator acceptance separate |
| M1 | Traceable Getaboda sources, first building and agreed subset | Source/CRS/license/hash, local-processing compliance, verified facts vs assumptions |
| M2 | Reusable Swedish houses/plots/room recipes through existing tools | One working case then repeat use, deterministic choices/overrides and actual game evidence; household briefs alone are not completion |
| M3 | Getaboda / V1 | All six V1 checks, then recorded creator feedback |
| M4 | Stabilize/shareable test, independent installation and release preparation | Approved distribution, attribution/support claims; private multiplayer needs actual host/client checks |
| M5 | Nearby settlements, repeatable regional batches | Existing slice proven; creator selects next area; preserved choices and measured travel/performance/effort |
| M6 | Small Ljungby urban pilot | Selected district, denser scenes and suitable templates; measured capacity before wider city scope |
| M7 | Municipality coverage | Separate validated batches, source/gameplay/regression evidence and honest coverage ledger; no completion date promised |

## Evidence index and retained history

The detailed pre-update checkpoint remains in Git history at
[3f29483](https://github.com/Bjogert/ZombieProjektet/blob/3f2948315622100c6fd8bfd2a6f540defee841c4/docs/ROADMAP.md).
This current file alone owns task order/status. Existing test reports and sources
are not replaced by the new design prototype:

- [M0](BUILD42_SPIKE.md), [M0 report](test-reports/M0-BUILD42.md), [cottage](COTTAGE_TEST.md), [garden](GARDEN_TEST.md), [placements](PLACEMENT_TEST.md).
- [Integration](INTEGRATION_TEST.md), [terrain](TERRAIN_TEST.md), [road pipeline](ROAD_PIPELINE.md), [road drive](ROAD_TEST.md).
- [Sized cottage](COTTAGE_SIZE_TEST.md), [candidate pilot](CANDIDATE_PILOT_TEST.md), [rural showcase](RURAL_SHOWCASE_TEST.md).
- [Building register](research/getaboda-building-register-2026-10-18.md), [data feasibility](research/getaboda-agunnaryd-pilot-2026-10-18.md), [geodata workflow](GEODATA_WORKFLOW.md).
- [Residential revision](specs/residential-character.md), [environment library](design/ENVIRONMENT_LIBRARY.md), [Småland patterns](research/smaland-houses-2026-10-18.md).

Older task IDs remain valid: COTTAGE-01/02, TOOLS-01, REVIEW-01, OVERRIDE-01,
WORLD-DRAFT-01 and ROAD-SCALE-01 retain their recorded scope/evidence and separate
creator acceptance. The earlier model-policy/documentation review and source
review are historical completed assignments, not live workers or a review of this
revision. Last portal/source statements are dated records, not fresh access checks.

## Working rhythm, acceptance and boundaries

Read Git, current queue and actual live worker/resource state. Select one bounded
result, implement, run relevant checks, obtain official export/game proof when
needed, then review. Continue ready authorized work within an active session.
After one focused unsuccessful diagnostic, record a distinct next hypothesis and
resume condition; choose useful independent work rather than poll or hide a failed
gate. Local UI/data delays do not block all synthetic source work.

Keep one integration owner, disjoint writer worktrees and one editor/game operator.
The existing hourly heartbeat is a dated creation record; verify its current
scheduler state. This file starts no job and grants no merge/release/purchase access.
Report exact commands/output scope, implemented vs unverified behavior and a next
action. Screenshots in ignored folders require an accessible curated evidence path.
Use Swedish progress reports; project artifacts remain English. Later-area spoilers
stay out of routine updates, while defects/risks are always disclosed.

Do not infer whole-suite success from a subset or independent review from self-review.
Preserve versions/known-good artifacts and recheck affected fixtures after shared
changes or game updates. Stable sources, saved choices and user edits must survive
regeneration. Never use scope expansion to hide correctness, rights or performance
problems. GitHub issues may hold discussion by these IDs, not a second backlog.

Creator decisions still cover significant art/world/balance choices, actual
personal-home fidelity, new regions, purchases and distribution. Approximately ten
personally important homes and a friends' multiplayer reunion remain later priorities.
Rural hunting firearms are accepted fictional direction but frequency/ammunition/
balance still need design and playtests. Tractors remain an untested compatibility
candidate, not an installed dependency or V1 blocker; see PROJECT_SPEC.

Re-estimate from observed work after representative proof and data readiness. Do
not promise dates or declining per-house cost before measuring a second compatible
case. The studio overview is [here](STUDIO_OVERVIEW.html); it is static guidance,
not an agent launcher or an additional authority.
