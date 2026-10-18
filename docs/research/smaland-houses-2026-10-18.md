# Småland houses and residential plots

Research date: 2026-10-18. Scope: reusable, original residential patterns for
Getaboda and the later Swedish map. This is a qualitative source review, not a
frequency survey or an identification of individual Getaboda properties.

## Why the current house reads as a barn

The creator describes the candidate pilot as barn-like. The technical fixture
proves export, collision, daylight and regeneration, but does not have accepted
residential character. Its enlarged red-brown volume, dominant uninterrupted
roof, sparse stock windows and weak entrance emphasis are plausible contributors.
That is a design diagnosis, not a historical claim.

Code inspection explains part of the result: `cottage_variant.generate` enlarges
the same rectangle while retaining seven windows and one exterior door. The
roof changes for coverage, while there is no entrance projection, chimney or
alternative architectural family. A larger valid footprint therefore does not
automatically produce a convincing larger home. Fix the visual grammar before
scaling this template into every candidate.

## Evidence and its limits

The linked pages were read as text. Their photographs are further visual
references, not downloaded textures or traced models. No raw geodata or source
imagery was uploaded or added to the repository. Broad web searches also found
rental listings, social posts and irrelevant archaeological reports; those are
not used to establish these patterns.

| Source | Supported finding | Scope / limitation |
| --- | --- | --- |
| [Kulturparken Småland: building conservation](https://www.kulturparkensmaland.se/byggnadsantikvarier/) | Regional variety includes simple cottages, two-storey parstugor and larger farmhouses; red board-and-batten is one of several wall treatments. Roof materials and ancillary building functions vary. | A regional overview, not proof that every house is red or that a footprint is residential. |
| [Länsstyrelsen: Ljungby municipality](https://www.lansstyrelsen.se/kronoberg/samhalle/kulturmiljo/kulturmiljoprogram/ljungby-kommun.html), Hörda/Klövaryd | One-and-a-half-storey houses, open or glazed verandas, red or pale facades and generally white joinery. | Specific cultural landscapes, not a Getaboda property record. |
| Same source, Ivla | Red wooden houses, gabled tile roofs, one chimney and distinctive upper half-moon windows. | The half-moon window is a local variant, not a universal cottage feature. |
| Same source, Lammakulla/Angshult and landscape sections | Symmetrical houses and white joinery; stone walls also define agricultural and woodland boundaries. | Do not turn every stone wall into a garden enclosure or copy field boundaries from this narrative. |
| [Länsstyrelsen: Alvesta municipality](https://www.lansstyrelsen.se/kronoberg/samhalle/kulturmiljo/kulturmiljoprogram/alvesta-kommun.html), Härlöv/Piggaboda | Verandas, simple and paired cottage forms, separate historic utility buildings and substantial stone-wall landscapes. | Neighbouring regional examples, with conservation selection bias. |
| [Kulturparken Småland: museum park](https://www.kulturparkensmaland.se/museiparken/), Fiskaretorpet | A relocated Angelstad example of a low dwelling combined with taller loft sections; the type occurred in southwest Småland. | A historic special case, not the default 1990s house. It shows why a single box cannot represent all regional forms. |
| [Länsstyrelsen: Stensjö by](https://www.lansstyrelsen.se/kalmar/besoksmal/kulturmiljoer/stensjo-by.html) | Gardens combine food growing, fruit trees and ornamental plants; lanes, boundaries and flowering verges contribute to the setting. | A deliberately preserved older village in eastern Småland. Use as a historical layer, not an unchanged model of 1990s Getaboda. |
| [Stockholms läns museum: summer houses and sport cottages](https://stockholmslansmuseum.se/byggnadswebben/arkitekturstilar/byggnadsguide/fritidshus-och-sportstugor/) | Summer houses include both rustic and simpler modern forms; panel, colours and trim vary. The account describes small cottages and later modular construction. | Comparative Swedish typology from a different region. It does not establish local prevalence. |
| [Stockholms läns museum: 1960s–1970s small houses](https://stockholmslansmuseum.se/byggnadswebben/arkitekturstilar/byggnadsguide/egnahem-smahus-och-villor/1960-1970-tal/) | Brick/wood combinations, differing window arrangements and later material choices distinguish modern homes from older cottages. | Comparative period evidence; do not label these houses as uniquely Småland. |

The creator additionally requests stone boundaries, garages, shrubs and red
fences with white tops. These are direct design inputs and local observations.
The exact red/white fence treatment and the frequency of garages have not been
established by this source sample. Preserve both as selectable design variants;
do not invent a percentage or a source-confirmed Getaboda attribution.

## Three architectural families to develop

These are proposed game profiles. Dimensions below are authored test sizes, not
measured regional averages. A torp is also a historical tenure/use category; the
profile name describes an inspired visual family, not a real property's history.

| Profile | House pattern | Plot pattern | First technical target |
| --- | --- | --- | --- |
| `croft_cottage` | Compact rectangular body, visible masonry/plinth base, gable roof, grouped or regularly spaced windows with light trim, a clear small porch or sheltered entrance; optional chimney. | Partial stone boundary or timber fence, gate-to-door gravel walk, shrub clusters, flowerbeds near the entrance, modest separate shed. | A fictional 6 by 9 cottage. Improve entrance, trim and window rhythm before adding complex roofs. |
| `summer_cottage` | Low compact body, simpler roof and window grouping, small side extension or sheltered deck where appropriate. Red/light trim and brown/darker trim are alternatives. | Open lawn, retained trees/rock where supported, a side deck, less formal hedge or fence, optional small annex. | A separate low cottage profile; a proposed 6 by 8 variant needs explicit support because the current resizer starts at length 9. |
| `country_house` | Larger body with a deliberate facade hierarchy; consider one-and-a-half/two storeys and a central veranda or entrance projection, not a uniformly enlarged cottage. | Entrance route, separate garage/utility area, hedge or fence segments, fruit/ornamental tree groups and a usable lawn. | Revisit the 9 by 12 candidate only after a representative residential facade passes review. Extra storeys and roofs need their own implementation and QA. |

Keep older houses, later extensions and postwar homes in the same 1990s setting.
Do not impose gingerbread trim, tile-red roofs, spröjs or a chimney on every type.
Existing regional variety is more useful than a village of identical red cottages.

## Reusable plot grammar

Design a plot as related parts: road-facing boundary and opening; approach and
entrance; main house and usable outdoor sitting area; side service route and
small building; maintained lawn and planted groups; transition to wilder edges.

- Offer stone wall, red fence with white tops, hedge, mixed partial boundary and
  open frontage as alternatives. Avoid enclosing every plot with every option.
- Align the gate and walk with the entrance. Leave paths, doors, garage approaches
  and access to outbuildings clear. Boundary objects must not cross source roads
  or reserved neighbours.
- Use bushes in groups, corners or a short hedge; place flowerbeds around chosen
  entrances or seating areas instead of repeating the same outline everywhere.
- A garage is a service destination with access and a subordinate roof/volume.
  It is not just a decorative box on the lawn. A shed or woodshed can serve the
  smaller profile. Exact real outbuilding positions remain unknown until sourced.
- Preserve maintained residential space at game start. Use vanilla progression
  for later overgrowth, following the existing creator decision.

Possible lilac, rose, currant and apple-like details are design candidates, not
verified vegetation species at any Getaboda house. Available PZ sprites may only
support generic visual approximations; label those honestly.

## Implementation order

1. Retain the current tested pilot as a technical baseline. Make a separate
   compact residential revision and compare it from the road and both visible
   sides at normal play zoom, with the roof visible and cut away.
2. Check existing local assets for light window/door trim, suitable panel/roof
   combinations, a plinth, entrance roof and stock stone/fence/hedge pieces.
   Do not promise a specific sprite or chimney until export and game checks pass.
3. Build one readable entrance/window/trim improvement, then one boundary and
   shrub treatment. Make the selected generic profile and plot choices persistent
   under the existing stable-ID choice system when the playable prototype exists.
4. Add the remaining family only when a candidate needs it. Use compatible
   combinations rather than independently randomising every architectural part.

Do not change a registered footprint to make the house prettier. An extension,
height assumption or approximation is a separate reversible design choice. A
material footprint change still needs creator review. The existing palette
manifest is not a playable architectural catalogue; do not claim that naming
these profiles adds them to the game.

The [residential character specification](../specs/residential-character.md)
defines the next bounded implementation and its game checks.
