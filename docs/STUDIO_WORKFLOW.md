# Reusable-world production workflow

Added 2026-10-25 at the creator's request. This is an extension of
[AGENT_WORKFLOW](AGENT_WORKFLOW.md), not a second queue or an autonomous service.
Product scope and release permissions are unchanged. Start from the existing
rural showcase, not a new engine or another M0 house.

## One small production loop

**Lead brief → art/household intent → reusable room/plot recipe → technical
validation → official export → game QA → independent review → library promotion.**

Review architecture, openings and room needs together before locking the shell.
Do not place an entire town of empty shells before discovering they cannot be
furnished. A typical delivery is one room or one high-value exterior detail,
reused once in a second compatible case before expansion.

| Stage | Accountable responsibility | Minimum output |
| --- | --- | --- |
| Select | Lead | One existing ROADMAP ID, outcome, base, files, checks and stop condition |
| Direct | Art Director | Short brief, allowed references, current/proposed status, normal-zoom acceptance criteria |
| Motivate | Interior / household designer | Fictional daily-life needs, shared/personal space priorities; no assertions about actual residents |
| Compose | Interior / environment worker | Reusable furniture/prop groups, routes, required space, fallback and allowed variation |
| Validate | Technical Artist | Existing verified references, full object parts/orientations, rights and compatible authoring output |
| Exercise | Lead as game/editor operator | Exact export/package, fresh-save and clean-reload checks, day/dusk/night comparisons when relevant |
| Review | Independent QA | Diff, access, determinism, actual image evidence, regressions and unverified behavior |
| Promote | Lead | Versioned tested entry, evidence link and explicit status; creator acceptance recorded separately |

Use responsibilities sequentially when that is simpler. Normally the lead works
with one worker and one independent reviewer, not every role at once. No recursive
subagent spawning. Use small briefs and reuse accepted rules rather than asking
an LLM to redesign every room each time. Work distribution cannot guarantee token
savings; measure effort and redo work for representative deliveries.

## Keep the instructions inexpensive and executable

AGENTS.md is the short routing entrypoint. ROADMAP owns task order/status.
AGENT_ROLES owns ownership and handoff contracts. This file owns production gates;
HOUSEHOLD_DESIGN owns the fictional-profile contract. Existing environment/asset
catalogues own appearance and references. Do not copy all five into every prompt.

Load `art-direction` for a visual delivery and `household-design` for household
variation. Keep the eight existing engineering skills. The updated setup checker
discovers new skill directories on either client and still enforces the original
minimum. No new skill is needed per person, room, house type or department.

Custom-agent TOML is an optional runtime convenience, not a second set of design
rules. The files point back to the briefs and inherit model/permissions. Test
agent discovery in the actual client before claiming the roles are loaded.
The two-child cap is a project setting, not proof that workers are running.

## Reuse ladder and library entry

**Asset reference → object group → room recipe → house family → plot kit.**

For the current slice, use small JSON/Markdown files and existing TBX/garden tools,
not a database, new editor or general constraint engine. A recipe must record:
stable ID/version, draft/authored/game-tested status, required room/space,
orientations, verified asset references, placement/interaction clearances,
capacity limits, supported substitutions, rights and test evidence. Do not label
an alias game-ready merely because its spelling resembles a sprite name.

Selection precedence: verified source constraints → explicit building choices
and overrides → compatible generated defaults. Incompatible overrides produce a
clear error for review, not an ignored correction. Never mutate source geometry.
Frozen household choices remain separate from source facts and library defaults.
A library upgrade affects new/unfrozen content only until an explicit migration
is reviewed. Keep original sources and a restore path.

## First art scope

Inspect stock assets first. The first original Swedish detail budget is a small
family of faluröd panel/white corners and trim plus white roof-edge/bargeboard
parts, keeping working PZ roof tiles and proportions. Do not replace every texture.
A new detail must visibly improve the actual play view, not only a concept board.
Keep gable ends, maintained gardens, wilder edges and the existing environmental
mix. No all-red Ljungby, automatic pavement on country lanes, or uniform house kit.

## Fictional household scope

The 20 seeds and `tools/household_briefs.py` are an **offline design prototype**.
They produce motifs and briefs only, not NPCs, furniture coordinates, item IDs,
container assignments, a new loot system or a playable map. Habits, resources
and life events are explicit designer inputs, not implemented placement effects.
[HOUSEHOLD_DESIGN](design/HOUSEHOLD_DESIGN.md) defines the future integration gate.

AI authors and reviews a small reusable library. A deterministic script supplies
variation. An LLM may compose a short build-time fictional explanation from a
frozen brief, but no online generation, per-house API requirement or player-facing
biography is introduced. Neither story nor probabilities describe real residents.

## Evidence and screenshots

For changed visuals collect actual game images of the tested artifact, preferably
one exterior and one interior at normal play zoom, plus matched day/dusk/night
views when testing light/materials. Record game/tool versions, package hash,
view/settings, checks, attribution and whether the image is a concept or game
capture. Never use an AI render as proof of PZ quality.

A path under ignored `build/` is not accessible evidence in GitHub. For the
fictional showcase only, curate a small non-sensitive, rights-checked set under
`docs/evidence/<delivery-id>/` with an index and captions, or an explicitly
approved accessible attachment. This is a review record, not permission to ship
game art as an asset pack. Do not loosen `.gitignore` wholesale, commit source
imagery/geodata, private interior references or later-area spoilers. Record a
missing picture as unavailable. No existing screenshots were fetched or inspected
in the 2026-10-25 workflow update.

## Acceptance before scaling

Keep r5 as the baseline until r6 passes official export/game/reload checks. Then
use the same house for three small interior variants. Pass criteria:

1. Doors/windows, routes, seating/storage interactions and complete multi-tile
   objects remain usable; roof/light/save-reload have actual evidence.
2. Same pinned inputs reproduce the brief; changing another building does not
   reroll this one; a deliberate correction survives regeneration.
3. The variants differ in recognisable activity and arrangement, not just colour
   or random clutter. A second compatible room reuses the recipe with recorded
   manual work rather than a rewrite.
4. No extra valuable loot is granted by a stereotype. Actual loot work is gated
   separately with vanilla/container integration, rarity caps and gameplay tests.
5. Report repair/reuse effort, manual interventions, rejected placements and
   measured performance where relevant. Do not promise a percentage improvement
   before comparison evidence exists.

Stop widening the library if export breaks, access regresses or extra detail is
invisible at normal zoom. Repair one fixture or keep the vanilla resource; do not
turn a disappointing art experiment into an engine rewrite.

## Runtime references and limits

Official OpenAI documentation checked 2026-10-25:
[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[skills](https://learn.chatgpt.com/docs/build-skills),
[subagents and TOML schema](https://learn.chatgpt.com/docs/agent-configuration/subagents).
The project adds native agent definitions and a concurrency setting, not custom
permissions or installed plugins. Names/descriptions are loaded before full skill
instructions. Local client support, authentication and live execution must still
be checked. Existing model selection and authorized heartbeat policy remain in
AGENT_WORKFLOW; this change starts no worker and modifies no schedule.
