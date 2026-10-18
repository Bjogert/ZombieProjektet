# Environment and building library — working draft

Created 2026-10-18 from the creator's proposed countryside, rural village,
planned neighbourhood and town-centre mood boards. This is an initial design
catalogue, not a new generator, an approved complete art direction or a list of
finished game assets. The creator accepted this library direction on 2026-10-18;
the immediate playable delivery is the fictional rural showcase, without a
Getaboda-likeness requirement. Individual variants still need visual review.

## One library, overlapping environments

An environment describes the relationship between buildings, plots, streets and
landscape. A building family describes architecture. Keep them independent: an
older croft can survive inside a town, and a later brick house can stand on a
country road. Use local evidence and explicit creator choices before generic
defaults. An environment tag must never rewrite a verified roof or footprint.

The setting retains modern geography with a Swedish 1990s atmosphere. It mixes
older buildings with later additions; it is not a reconstruction of a surveyed
1990s streetscape. Maintain gardens at game start and let vanilla progression
handle subsequent overgrowth. The existing rural gable-roof decision still applies.

The four boards below are design proposals, not measured distributions. No
percentage quotas or automatic zoning boundaries have been chosen.

| Environment ID | Spatial character | Building mix to explore | Ground, boundaries and everyday details |
| --- | --- | --- | --- |
| `countryside` | Buildings separated by gardens, fields or woodland; irregular approaches and useful service space | Croft, summer cottage, country house and occasional later detached home; barns and sheds are distinct utility buildings | Gravel access, open lawns, partial stone boundaries, shrub groups, flowerbeds, deck, wood storage and outbuilding access; wilder vegetation beyond maintained space |
| `rural_village` | A recognisable street or road with varied setbacks, plot sizes and building ages; Agunnaryd/Kånna are creator reference areas | Older timber houses alongside later detached houses; small shops, workshops or public buildings only where supported or explicitly authored | Hedged or fenced frontages, gates, drives, gardens and garages; bus stop or shared place where appropriate; pavement presence depends on the particular street |
| `planned_neighbourhood` | More regular plot widths, setbacks and street relationships; neighbourhoods need not form a perfect grid | Postwar brick/timber detached houses, selected row houses and occasional older retained homes | Front gardens, driveways, subordinate garages/carports, clipped hedges, rear patios, pedestrian connections and shared play/green areas |
| `town_centre` | Shorter gaps and stronger street frontage, with courtyards and service access behind | Low-rise apartments, shops with housing above, older timber houses and later brick/plaster buildings | Pavements, shopfronts, cycle parking, benches, street planting, bins and loading/service areas; a retained older house may keep a small garden |

Commercial strips, industrial yards, farms, schools, recreation and woodland
will need their own functional treatments as the map reaches them. They do not
need to be forced into a residential family or built before Getaboda is ready.

## Building families

IDs are stable design vocabulary. The families below describe the intended range, not a completed catalogue.
The new `rural_cottage_01` and `rural_plot_01` sources implement one compact
countryside combination using the existing pipeline. See the
[rural showcase specification](../specs/rural-showcase.md),
[game evidence](../RURAL_SHOWCASE_TEST.md) and
[plot source notes](../../assets/gardens/RURAL_PLOT.md). Other families remain
proposals; this single combination does not establish their implementation.

| Family ID | Recognition features | Useful variation | Context relationship |
| --- | --- | --- | --- |
| `croft_cottage` | Compact timber dwelling, gable roof with vertical ends, readable entrance, light opening trim, modest plinth | Porch, window rhythm, restrained colour choices, chimney when supported | Rural default candidate; an older retained house can occur in village or town contexts |
| `summer_cottage` | Low compact timber body, gable roof, simple windows, useful outdoor sitting area | Open deck, modest extension, red/light or brown/darker treatment | Countryside and village candidates; not automatically assigned from a small footprint |
| `country_house` | More substantial dwelling, deliberate facade rhythm and veranda/entrance emphasis, gable roof | One-and-a-half or two storeys, porch form, pale or red timber facade | Countryside and village candidates, with retained examples possible in later neighbourhoods |
| `postwar_detached` | Lower brick/timber dwelling, regular openings and an entrance/garage relationship | Brick tone, timber panels, gable pitch, one or one-and-a-half storeys | Planned neighbourhood candidate, also possible on village and rural plots |
| `modernist_detached` | Deliberate modernist composition and window arrangement | Plaster/brick, roof form and setbacks chosen for the individual case | Later Ljungby exception supported by references; not a random substitute for Agunnaryd gable-roof homes |
| `terraced_house` | Repeated attached units with individual doors and coherent roof/facade rhythm | Short groups, entrance planting, rear patios and shared parking arrangements | Planned neighbourhood or town-edge candidate; placement needs a suitable actual group |
| `low_rise_apartments` | Shared entrances, repeated window stacks and usable common grounds | Brick/plaster, balconies, stairwell treatment and storey count | Town or neighbourhood candidate, not restricted to the centre |
| `mixed_use_townhouse` | Ground-floor shop/service frontage with upper rooms or apartments | Older timber or later brick/plaster treatment, courtyard entry, awning | Town-centre candidate; a modest variant can serve a village centre |

Keep `garage`, `shed`, `barn`, `workshop`, `small_shop` and civic buildings as
separate functional families. Their doors, scale, access and room usage differ
from dwellings. A red facade alone must not select a barn, a dwelling or a loot
profile. Schools, churches, petrol stations and other landmarks get dedicated
work when needed, rather than stretching a cottage into their footprint.

For a dwelling, describe the complete compatible combination: proportions,
storeys, roof, facade, windows, entrance and optional additions. Do not shuffle
every component independently. Approved variants can share components without
producing structurally or visually contradictory houses.

## Plot and detail kits

A kit is a reusable relationship between objects and clear routes, not a fixed
stamp copied onto every property. These are proposed additions except for the
explicitly listed existing cottage-garden elements.

| Kit ID | Contents and placement intent | Access to preserve |
| --- | --- | --- |
| `domestic_garden` | Lawn, grouped shrubs, flowerbeds near an entrance or seating area; optional fruit tree or vegetable patch | Gate-to-door route, windows and a useful route around the house |
| `outdoor_living` | Deck/patio, chairs and table; optional clothesline, grill or small storage after asset review | Door swing, seating access and a route from the house |
| `rural_boundary` | Partial stone wall, red fence with light tops, hedge or open frontage; choose a coherent subset | Gates, roadside sight lines, driveways and neighbouring reservations |
| `garage_service` | Garage/shed, drive, wood storage or small service area | Vehicle approach, garage opening and pedestrian separation |
| `village_street` | Appropriate road edge, individual entrances, occasional shared bus-stop or meeting-place detail | Continuous pedestrian and vehicle movement |
| `neighbourhood_street` | Pavement/path where appropriate, hedges, drive crossings, shared planting and play space | Accessible entrances and uninterrupted pedestrian connections |
| `town_frontage` | Shopfront, awning, cycle rack, bench, planting and bins used selectively | Shop doors, pavement movement and delivery/service entry |
| `working_yard` | Workshop/farm storage, equipment and utilitarian ground treatment | Loading/turning space; machinery requires separate compatibility checks |

Use restrained variation in orientation, compatible finishes, bed shapes and
object combinations. Some plots should have open frontage, others a boundary;
not every house needs a deck, garage, flowerbed, flagpole and woodpile together.
Wear and maintenance can vary without making the whole starting world abandoned.
Storage and room function should support vanilla gameplay, with loot balancing
kept separate from real households or imagined personal possessions.

## What an entry records

Start with this versioned Markdown catalogue and the existing local building
register. A new database or automatic classifier is not needed for this draft.
Move approved entries into machine-readable generation settings only when a
playable consumer exists; extend the current pipeline instead of making a second
world implementation.

| Field | Meaning |
| --- | --- |
| `family_id` / `kit_id` | Stable reusable design identifier, independent of address |
| `context_tags` | Several compatible environment contexts, not exclusive zones |
| `era_notes` | Relevant architectural layers and compatibility with the 1990s atmosphere |
| `form_rules` | Body, storeys, roof, openings and compatible additions |
| `material_options` | Named candidate finishes; distinguish existing tile references from unimplemented art |
| `variation_rules` | Compatible combinations and limits; deterministic selection when implemented |
| `placement_rules` | Entrance/road relationship, required space, reservations and clear routes |
| `reference_records` | Source URL/ID, date, licence/permission and what the reference actually supports |
| `design_status` | Proposed, under review or creator accepted; record which aspect was accepted |
| `implementation_status` | Not implemented, authored, exported or game-tested, with exact artifact evidence |
| `rights_status` | Game reference, permitted dependency, authorised adapted content or original art pending distribution decision |

Individual houses keep their source geometry and stable source ID in the existing
register. A separate saved choice can eventually select a family and kits, with
its assumptions and seed; it must survive regeneration. An address is an optional
human lookup label, not the primary key or evidence for appearance. Unknown roof,
colour, function and interior remain unknown until supported; a design choice
does not silently become a source fact.

Existing integration points:

- [House styles](../../config/house_styles.json) currently name palette choices;
  they do not define these architectural families or prove those finishes playable.
- [Style overrides](../specs/building-style-overrides.md) preserve manifest choices.
- [Placement tools](../specs/building-placement-tools.md) connect saved synthetic
  house/orientation/garden choices to playable authoring.
- [Building register evidence](../research/getaboda-building-register-2026-10-18.md)
  records the separate local source and choice workflow.
- [Garden template](../../assets/gardens/README.md) already separates layout from
  the house, with clear routes and directional placement.

Do not pass the vocabulary in this document to existing CLIs as if their input
contracts had changed. Environment selection and arbitrary kit composition are
not implemented by this design catalogue.

## Reuse and adaptation order

1. **Use existing game references first.** The tested cottage/garden already use
   stock walls, windows, doors, roof pieces, furniture, a wooden deck, shrubs and
   flowers. New arrangements and architectural proportions can make these feel
   local before any new sprite is needed. Current evidence applies only to the
   tested arrangements and Build 42.21.0.
2. **Audit stock candidates for each missing detail.** Check actual appearance,
   size, orientation, collision and interactions. Stone boundaries, the exact
   red/white fence, garage doors, street furniture and signage still need this
   audit; a concept picture does not establish sprite availability.
3. **Evaluate a small number of mods for specific gaps.** Record author, Workshop
   ID or source URL, version, dependencies, permissions and exact tested game
   build. Prefer declared dependencies or a Workshop collection when appropriate;
   do not bundle other authors' assets by default. Multiplayer remains untested
   until our later multiplayer checks.
4. **Create or adapt only the high-value missing pieces.** Candidates include
   distinctive fence parts, facade/entrance details and period-appropriate local
   signage. Adaptation requires the relevant permissions. Original graphical
   assets still need a distribution licence decision before public release.

The Indie Stone's [Modding Policy](https://projectzomboid.com/blog/modding-policy/),
read 2026-10-18, requires permission for third-party material, including content
from other mods (§1.1.2 and §4). Public and unlisted modpacks need the relevant
permissions (§7); the policy also points to Workshop collections as an
alternative. Download availability alone is not permission to copy, recolour or
redistribute an author's work. Follow [project data and rights rules](../DATA_AND_RIGHTS.md).
No new mod is installed, copied or selected as a dependency by this draft.

## Reference and mood-board method

Keep three kinds of evidence visibly separate:

- **Observed references:** creator-owned or appropriately licensed exterior
  images, with date, source and supported observations. Keep source imagery local
  under the existing processing boundary.
- **Original concepts:** proposed combinations for discussing character. The
  first four-panel board is AI-generated from text only, with no source imagery
  or geodata supplied. It is not a record of real houses, period proof, a texture
  pack or a promise of game fidelity. The preview and prompt remain in the hub's
  ignored `outputs/` folder, outside the game package.
- **Game evidence:** screenshots of the exported asset in the target build,
  including normal play zoom and functional checks. These demonstrate the
  actual result rather than a concept renderer's appearance.

The [Småland house research](../research/smaland-houses-2026-10-18.md) supplies
regional and comparative starting points. Ljungby municipality's
[cultural-environment overview](https://www.ljungby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/kulturhistoriska-byggnader-kulturmiljoer),
read 2026-10-18, describes a low-rise town with varied housing: older panel
architecture alongside later brick and plaster buildings and substantial
development in the second half of the twentieth century. This supports exploring
mixed periods; it does not verify a particular street or the proposed four-way
classification. The linked 2019 municipal programme is a further reference lead,
not a document fully reviewed in this slice.

## Next playable slice

Apply the library to the existing [residential character revision](../specs/residential-character.md):
one fictional compact gable-roof dwelling, a readable entrance and one maintained
garden/boundary treatment. Compare the mood with actual front/side game views.
Verify roof, light, doors, windows, collisions, access and clean reload. Record
technical evidence and creator visual acceptance separately.

Then reuse the proven parts for the required Getaboda houses, adding one family
or kit at a time. Build and test complete small places — house, approach, garden
and road relationship — rather than finishing every municipal house before
discovering that the surrounding layouts or performance do not work. Wider
village, neighbourhood and town pilots stay in the existing roadmap phases.
