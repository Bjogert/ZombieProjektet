# Reusable studio assignments

Use these briefs with [AGENT_WORKFLOW](AGENT_WORKFLOW.md). The lead selects work
from [ROADMAP](ROADMAP.md), fills in its task ID, bounded outcome, base commit,
worktree, owned files and acceptance evidence, then dispatches the brief through
the available subagent tools. These are reusable instructions, not running jobs.

## Shared assignment contract

- Read the assigned checkout's `AGENTS.md` and the relevant specification first.
- Use English in project materials; the lead communicates with the creator in Swedish.
- Work only within the assigned outcome and files. Inspect local changes first.
  Concurrent writers require separate worktrees; never reset another worker's work.
- Keep raw geodata, source imagery, private correspondence and credentials out of
  prompts and model-visible output. Use synthetic fixtures for data-tool development.
  Follow `docs/DATA_AND_RIGHTS.md`; source permission is separate from tool access.
- Leave game/editor control, mod installation, shared integration documents and
  release actions to the lead unless explicitly reassigned. Do not send mail,
  create accounts, accept terms, purchase, publish or merge under a task brief.
- Report a blocker with its evidence and the smallest next action. Do not invent
  source facts or turn a successful unit test into a gameplay claim.
- Return: task ID; outcome; changed files/commit (or read-only findings); checks
  actually run; evidence paths; unverified behavior; next action. Do not spawn
  further agents unless the lead's assignment explicitly requests it.

## Lead / integration

Own prioritization, creator decisions, assignments, shared documentation, exports,
mod installation and game testing. Keep one primary delivery and at most one
independent secondary task. Normally use one worker plus one independent reviewer;
add a third specialist only for a clearly independent result.

Before dispatch, record the outcome, writer ownership and resource owner. Review
the returned diff and evidence, integrate sequentially, run the relevant checks
and close the assignment. Report implementation, automated checks, game checks
and creator acceptance separately. If there is no useful parallel task, work alone.

## World / data

**Typical input:** a permitted source specification, provenance schema, synthetic
fixture and existing import/override code. Use the project's current source and
rights decisions; never assume a new application has been approved.

**Own:** explicitly assigned importer, registry or synthetic-test files in the
assigned worktree; read-only research when requested.

**Deliver:** the smallest repeatable processing change or source-readiness report.
Preserve original IDs, coordinates and input hashes; distinguish source-reported,
derived, assumed and design-selected values. Unknown appearance stays unknown.
Prove that regeneration preserves overrides and fails clearly on invalid input.

**Exclude:** mailbox/portal access unless specifically delegated, raw-source output,
new applications, unreviewed licenses, real-house identity claims and public uploads.

## Buildings / art

**Typical input:** the approved environment library, relevant building/garden
sources, a bounded visual brief and existing build tools. Start with the current
fictional rural showcase before multiplying a new layout.

**Own:** explicitly assigned TBX, garden JSON or generator/test files in the
assigned worktree. Keep per-building corrections separate from generated defaults.

**Deliver:** reusable sources with plausible Swedish residential character and
clear door/window access. Retain the agreed two-slope gable roofs, maintained
gardens and wilder edges. Use permitted local game resources by reference.
Check dimensions, clear routes and deterministic output; identify which visual
questions need the lead's official export and fresh in-game screenshots.

**Exclude:** changing the overall art direction, assuming Getaboda likeness,
copying proprietary art, controlling BuildingEd/WorldEd or installing a test mod.

## QA / review

**Typical input:** a specific diff/base, acceptance criteria, exact artifact and
test evidence. The reviewer is independent of the implementation author.

**Own:** read-only inspection and isolated checks; no implementation edits.

**Deliver:** findings ordered by impact, with file/line or evidence references,
reproduction and the smallest repair. Check source boundaries, clear routes,
override preservation, package identity and unsupported claims as relevant.
Distinguish a verified pass, a reproducible failure and a check not performed.

**Exclude:** changing the implementation, approving design for the creator,
declaring gameplay success from source inspection, or driving the game/editor.
Return a concrete game-test checklist for the lead when runtime proof is needed.

## Dispatch state and evidence

ROADMAP is the only task queue. A live assignment may be noted under its existing
task ID with worker ID, mode (read-only/writer), base/worktree and owned paths.
Use **Running** only after dispatch and a current tool status confirms it.
On return, replace that with **Review ready**, **Integrated** or a named blocker;
an ended session cannot retain a live-running claim. A committed note records
history, not a live monitor. A role brief alone proves no agent is active.

During an active session the lead moves to the next ready approved task. This
setup creates no recurring job or guarantee of work after the turn ends.
