# Fictional households and reusable interiors

Status: **bounded offline design prototype**, 2026-10-25. Authorized direction:
use small choices to produce coherent, reusable Swedish/Småland-flavoured homes.
This is not a demographic model, survey of real residents or finished PZ integration.
The [environment catalogue](ENVIRONMENT_LIBRARY.md) and original game pipeline
remain authoritative for architecture and existing assets.

## Better than fixed stereotypes

Use three separable layers:

- **Person:** concrete interests, everyday habits and a short invented background.
- **Household:** residents, shared resources, household history and compromises.
- **Place:** available rooms/storage/garden, building type, local environment and
  scenario. Geographical context is not a claim about an individual's identity.

Names/pronouns, education or political labels must not imply possessions, lack of
books/food, criminality or competence. Name/pronouns/background are presentation
only in the prototype. Hunting and repair interests can motivate equipment;
actual space determines whether it fits. A town resident can hunt, and a rural
resident can read, cook or collect music. Crime/dangerous discoveries, if ever
approved, are rare explicit fictional scenario events, not demographic defaults.

The seed bank has 20 fictional starting characters: ten presented as men and ten
as women. Profiles are reusable recipes, not 20 unique NPCs repeatedly placed on
the map. Any supported combination of one to four residents can form a prototype
household; there are no gendered household roles or opposite-sex-only pairing
rules. Do not infer real identities from names, real building IDs or addresses.
Every applied biography remains explicitly fictional.

## What exists now

- `data/design/household_seeds.json`: original fictional seeds, 13 draft motifs,
  constraints and tunable relative weights. No game sprite/item IDs or external art.
- `data/design/household_example.json`: a synthetic countryside home with Nils and
  Birgitta, explicit spaces and a pinned reading motif. Not a real property.
- `tools/household_briefs.py`: validates inputs, chooses residents when requested,
  filters motifs for available space and performs weighted selection without
  replacement. Returns provenance, support reasons, omissions and unfilled slots.
- `tests/test_household_briefs.py`: deterministic/reuse/input-boundary tests. They
  do not prove visual quality, game placement, legal ownership of future assets,
  loot balance or multiplayer.

From the repository root:

```sh
python tools/household_briefs.py --request data/design/household_example.json --output build/household-preview/brief.json
python -m unittest discover -s tests -p 'test_household_briefs.py' -v
```

Supply either `resident_ids` or `resident_count`, never both. Automatic selection
is uniform among fictional seeds; it is **not** a measured population distribution.
Unknown fields/IDs, invalid counts and incompatible forced motifs fail clearly.
No input file, source geometry, TBX, original asset or game package is changed.

## Probability model and scope

For an eligible motif, the prototype weight is:

`base_weight + 2 * supporting_resident_count + context_bonus`

First reject motifs without a compatible declared space. Specialist motifs with
zero weight need an explicit compatible override; ordinary domestic motifs retain
a small baseline weight, so interest is not an absolute possessions checklist. Preserve validated
`theme_overrides`, then select remaining motifs without replacement up to the
requested limit. Candidate order and resident order are normalized. Every home
has its own SHA-256-derived random streams for residents and motifs; no Python
`hash()` or shared global RNG. Record generator/catalog versions, catalog hash,
building ID and seed. Reproducibility claims apply to pinned inputs/toolchain;
frozen outputs are the stronger long-term record.

Weights are design assumptions, not percentages measured in Småland. They control
prominence in an **interior brief**, not item spawn probability. A missing motif
means not selected for emphasis, never proof that the household owns none of it.
All residents' interests and habits remain in the brief even when shared-space
motifs cannot represent them. No profile forces wealth, starvation or weapons.

`resources`, `life_event` and personal habits are passed through for the designer;
the script does not yet calculate furniture condition, layout or possessions from
them. Do not describe these inputs as implemented placement rules.

## Shared households and history

Example: Nils' repairs/hunting interests plus Birgitta's gardening/reading/visits
can yield restrained tool storage, books and a usable coffee place, with garden
supplies when space exists. Shared rooms need a coherent negotiated style; private
interests should survive in a small corner or storage allocation. No person wins
by gender, name or being first in the input list.

A move to town changes space and compatible choices, not morality. A compact
apartment may retain outdoor clothing and a few tools but omit a workshop or
large garden. A shared modest-resource household can prefer repaired furniture
while retaining books and kitchen use. These are design examples, not actual PZ
results or claims about real Swedish households.

Initially the optional history is one or two invented sentences: who shares the
home, what routine explains a few visible objects, and one compatible life event
(established home, move, inheritance or renovation). No biographies at scale,
real-person profiling, unapproved sensitive stories or costly runtime AI calls.
Use AI to enrich and review reusable recipes; use scripts for repeatable batches.

## Frozen choices and corrections

The script creates a separate JSON brief. Repeating an identical output is a
no-op. A different existing output, including hand edits or a changed catalogue,
causes an error and is left unchanged. There is intentionally no `--force` flag.
`theme_overrides` are explicit request-level choices and must fit the spaces.

This is a conservative prototype safeguard, not a complete migration/merge
system for game saves. Before integration, store household/recipe choices in the
existing stable-building-ID choice layer; keep user corrections separate from
generated defaults. Preserve accepted residents, motif choices and asset versions
across catalogue upgrades. Review an explicit migration into a new output rather
than rerolling a built house. The broader integration remains a ROADMAP task.

## Placement and loot are separate gates

Future adapter: brief → room needs → compatible recipe → verified existing asset
references → valid placement → official export → actual game checks. Avoid making
a separate world generator. Reuse TBX/garden/placement and override tools.

Room recipes need footprint/orientation, complete multi-tile pieces, clearance,
window/door access, interaction points, room function, capacity and fallback.
Validate before claiming a room can be generated. Don't invent PZ sprite IDs.

Only after that proof should a narrowly scoped loot adapter be considered. It
must distinguish decorative props, storage/container type and randomized loot;
preserve vanilla room/container expectations; respect declared scenario/date,
food spoilage, rarity and a household/region value budget. Hunting intent may
justify a candidate, not guaranteed firearms or ammunition. Item IDs, API/hooks,
save behavior and spawn frequency require current-build inspection and tests.
The current change does not implement or authorize unbounded loot replacement.

## Promotion gate

Use the current fictional showcase and three small interior variants, then a
second compatible room/home. Show actual in-game differences at normal zoom,
validate access and reload, preserve one correction, and measure reuse/manual
repair effort. Only promote verified recipes. Keep later-area exact interiors and
loot out of routine creator updates. No whole-town population, new NPC simulation,
second editor or complete personality taxonomy is needed for this gate.
