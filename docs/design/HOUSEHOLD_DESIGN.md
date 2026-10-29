# Fictional households and reusable interiors

**Strategy accepted by the creator, 2026-10-25, after the household discussion.**
Implementation remains a **bounded offline design-brief prototype**. Acceptance
of this strategy does not mean its layout, story or loot effects exist in code.
This document is the canonical household-design contract; ROADMAP remains the
only execution queue. The [environment catalogue](ENVIRONMENT_LIBRARY.md) and
existing game pipeline govern architecture, assets and export.

## Creative default: everyday homes, occasional discoveries

Build believable Swedish/Småland everyday homes first. A few places may contain
unusual, poignant or dark discoveries, but not every house needs an obvious
scripted story. Ordinary homes provide the contrast that makes exceptions matter.
No numerical exception frequency or new loot balance has been approved.

The goal is **a few understandable choices producing a coherent lived-in home**,
not a psychological simulator or a large collection of biographies. Meaningful
variation must be visible in the game without reading the household card. Keep
ordinary furniture and domestic functions between the distinctive details.
Preserve later-area discoveries for the creator; use the showcase/Getaboda for
open design and quality reviews.

## Person, household and place

Use three separable layers:

- **Person:** concrete interests, everyday habits and a short invented background.
- **Household:** who shares the home, shared resources, tenure/history and practical
  compromises. This, not an isolated person, is the unit of furnishing.
- **Place:** actual rooms, storage, garden, building type and local context.
  Geography constrains available opportunities; it does not determine morality.

Names/pronouns, education or political labels must not imply criminality,
possessions, lack of reading/food or competence. A character can be unpleasant,
contradictory or unusual; use explicit fictional activities/history to motivate
visible traces rather than demographic shortcuts. A hunter can live in town; a
rural resident can enjoy books, cooking and music. Rare crime-related discoveries,
if later approved, are explicit fictional scenario events, not group defaults.
Never infer actual residents or possessions from real addresses or footprints.

The bank of 20 fictional seeds (ten presented as men and ten as women) is a
creative starting interface, not 20 fixed NPCs to stamp repeatedly onto the map.
Core interests may anchor an archetype while secondary interests, habits and
household circumstances vary through reviewed choices. Such variation is a
future design capability, not functionality already provided by the prototype.
Any supported combination of one to four residents can form a prototype household;
there are no gendered household jobs or opposite-sex-only pairing rules.

## Shared life, not added inventories

Do not concatenate each resident's possessions or average all their preferences
into a uniformly mediocre style. Plan shared rooms and small personal areas.
Who lived there first, inherited furniture, space, resources and recent changes
can explain compromises without simulating a relationship.

Design example: Nils likes repairs and hunting; Birgitta likes gardening, reading
and visits. Their shared home might have a usable coffee table, a reading corner
and compact equipment storage. If she already owned the home, its existing
furniture may remain while he uses a storage-room work area. Moving to a smaller
town home removes the full workshop, not his interests. A tidy kitchen and a
cluttered hobby room can coexist; neither resident must dominate every room.
These are fictional design examples, not observed residents or game-tested rooms.

## Generate related arrangements, not independent object lists

Start with required domestic functions and valid circulation. Reject options
that cannot fit or function before weighting the remaining compatible choices.
Then select coherent activity groups: a repair in progress, a reading corner,
a sewing surface or equipment prepared for a trip. Each reusable group should
have supported sizes, orientations, clearance, capacity and a fallback.

Do not roll separately for every prop and hope they tell a story. A full-size
workbench blocking a door is invalid, not merely unlikely. A smaller tool-storage
group can preserve the same interest. Never silently ignore an explicit correction
or invent a sprite to make an attractive idea fit.

Limit distinctive emphasis: for example one primary activity, an optional
secondary interest and a small keepsake. This is a starting art guideline, not
a new implemented parameter or a demand to fill three slots in every home.
Avoid representing every trait with another object. Allow modest, explainable
contradictions, such as inherited furniture or an unusually cared-for hobby amid
otherwise practical surroundings. Do not add arbitrary eccentricity everywhere.

## A short intent before furnishing; evidence afterwards

Use an optional short house card: household composition, daily activity, a few
habits, available resources/space and one relevant life event. A few sentences
are enough. It is an internal furnishing brief, not required player-facing text
or a reason to generate long biographies for every building.

Before furnishing, ask: **which two or three feasible visual cues could make this
routine/history legible?** Scale that cue budget down for tiny rooms. If the
library cannot express an idea, use a compatible fallback or propose a bounded
reusable addition; do not fabricate a bespoke unsupported placement.

After placement, any final descriptive narrative must be grounded in the saved
layout and verified objects. Separate intended cues from realized cues. Remove
claims about a piano, balcony or cabinet that did not get built. An abandoned
intent is not evidence of environmental storytelling.

## Before the outbreak versus when the player arrives

Keep the pre-outbreak household and its possible possessions separate from later
scenario effects: departure, damage, elapsed time or prior scavenging. The house
can suggest tools without guaranteeing that valuable tools remain. Decorative
props, container purpose and randomized loot are distinct decisions.

This is a design boundary, not authorization to implement a second catastrophe
or loot generator. Inspect current vanilla systems first; any future adapter must
avoid applying damage, looting or spawn rules twice. Until compatible integration
is separately verified, keep existing scenario/loot behavior unchanged. No such
post-outbreak adapter exists in this prototype.

## AI authors the library; scripts perform repeatable generation

AI can propose household briefs, explain a few visible details, design reusable
groups and review coherence at build time. It may help a particular house, but
should choose tested recipes first. A genuinely new requirement becomes one
bounded library experiment, not an unsupported exception in every house.

Deterministic scripts handle compatible selection, repeated placement and checks.
No runtime LLM requirement, paid per-house service, new NPC simulation or permanent
agent department is introduced. Reuse gets cheaper only when a tested component
works again; measure actual manual effort rather than claiming that AI learns
faster automatically. More names or longer biographies cannot compensate for an
inadequate room/group library.

Here, dynamic means adapting choices **while building the world**, not rerolling
occupied homes during play. Freeze accepted household/recipe choices, versions
and overrides. Changing the library must not silently redecorate an existing home.

## What exists now — separate from the accepted target

- `data/design/household_seeds.json`: 20 original fictional seeds, 13 draft motifs,
  space constraints and relative weights. No game sprite/item IDs or external art.
- `data/design/household_example.json`: a synthetic countryside home with Nils and
  Birgitta, explicit spaces and a pinned reading motif. Not a real property.
- `tools/household_briefs.py`: validates requests, optionally selects residents,
  filters motifs for declared spaces and selects weighted motifs without replacement.
  It returns provenance, support reasons, omissions and unfilled slots.
- `tests/test_household_briefs.py`: tests the design planner's behavior, not actual
  furniture placement, visible storytelling, game loot, balance or multiplayer.

From the repository root:

```sh
python tools/household_briefs.py --request data/design/household_example.json --output build/household-preview/brief.json
python -m unittest discover -s tests -p 'test_household_briefs.py' -v
```

Supply either `resident_ids` or `resident_count`, never both. Automatic resident
selection is uniform among fictional seeds, not a measured population distribution.
Unknown fields/IDs, invalid counts and incompatible forced motifs fail clearly.
No source geometry, TBX, original asset or game package is changed.

For a motif with a compatible declared space, the existing prototype weight is:

`base_weight + 2 * supporting_resident_count + context_bonus`

Specialist motifs with zero weight need an explicit compatible override. Ordinary
domestic motifs retain a small baseline weight, so interests are not an exhaustive
possessions checklist. Preserve validated `theme_overrides`, then choose remaining
motifs without replacement up to the limit. A missing motif means not selected
for emphasis, never proof that the household owns none of it.

Candidate and resident order are normalized. Each building has separate
SHA-256-derived random streams for residents and motifs, not Python `hash()` or
a shared global RNG. Record generator/catalog versions, catalog hash, building ID
and seed. Reproducibility applies to pinned inputs/toolchain; saved outputs are
the stronger long-term record. Weights are design assumptions, not percentages
measured in Småland and not item-spawn probabilities.

All residents' interests and habits remain in the brief. `resources`, `life_event`
and habits are passed through for a designer; the script does not derive layout,
furniture condition or possessions from them. Shared-room compromise, varied
archetypes, realized narrative and post-outbreak effects are not implemented.
The strategy documentation update changes neither code nor the existing seed bank.

## Frozen choices and corrections

The planner creates a separate JSON brief. An identical rerun is a no-op. Any
differing existing output, including manual edits or a changed catalogue, causes
an error and is left unchanged. There is no `--force` flag. Request-level
`theme_overrides` must be compatible with the declared spaces.

This is a conservative prototype safeguard, not a complete migration/merge
system for saves. Before integration, store choices through the existing stable
building-ID choice layer, separately from source facts and manual corrections.
Preserve accepted residents, motifs and asset versions across catalogue upgrades.
Review an explicit migration into a new output instead of silently rerolling.

## Placement and loot are separate gates

Future adapter: brief → room needs → compatible recipe → verified asset references
→ valid placement → official export → actual game checks. Use the existing
TBX/garden/placement and override tools, not a separate world generator.

A room/group recipe needs footprint/orientation, complete multi-tile pieces,
clearance, window/door access, interaction points, domestic function, capacity and
fallback. Validate these before claiming a room is generated. Do not invent IDs.

Only after room proof should a narrow loot adapter be considered. Preserve vanilla
room/container expectations and declared scenario/date, food spoilage, rarity and
household/region value budgets. Hunting intent may motivate a candidate, not
guarantee firearms or ammunition. Current-build APIs/item IDs, save behavior and
spawn frequencies need separate inspection, tests and balance approval.

## Promotion gate — judge the room without its biography

Use one reusable room in the existing fictional showcase with three different
household briefs, then demonstrate reuse in a second compatible room/home.
Hold the shell, available asset pool, approximate loot budget and comparison
lighting/zoom constant. Do not modify loot just to make a variant look distinctive.

Ask an independent reviewer to inspect actual in-game views **before** reading
the briefs. Record what different routines or activities the rooms suggest and
which visible cues caused that impression; exact names or traits need not be
guessed. Then compare those observations with the intended and realized cues.
The pass condition is distinguishable, coherent everyday use without biographies,
not only different colours, extra clutter, caricatures or guaranteed rewards.

Also verify routes, doors/windows, complete furniture, interactions and clean
reload; preserve one deliberate correction through regeneration. Record manual
repairs and second-use effort. If the visible variation is weak, improve the room
recipes instead of expanding the personality bank. No arbitrary success percentage
is set before this small test. Promote only game-verified recipes; creator
acceptance remains a separate recorded step.

## Ownership and handoff

| Responsibility | Required action |
| --- | --- |
| Interior / household designer | Own the short intent, shared-life compromises, compatible groups and intended-to-realized cue mapping. |
| Art Director | Maintain everyday plausibility and restrained exceptions; assess visible coherence at normal play zoom. |
| Technical Artist | Validate actual asset/group contracts, clearance, export and reuse; reject unsupported placements. |
| QA / review | Own the biography-hidden comparison, repeatability/correction checks and clear separation of design, game evidence and loot claims. |
| Lead / integration | Include this document in relevant task briefs; preserve ROADMAP order, versioned choices and integration gates. |

See [role briefs](../AGENT_ROLES.md). Apply this contract under existing ART-01,
HOUSEHOLD-01 and ROOM-01. LOOT-01 remains later and separately gated. Do not create
a second backlog, extra skill per character or a new V1 requirement. This agreement
records creative strategy, not evidence that agents have loaded it or begun work.
