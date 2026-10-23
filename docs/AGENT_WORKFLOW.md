# Agent workflow — Codex + Claude Code

## Working agreement (2026-10-17)
The creator owns creative direction and consequential decisions. The lead agent owns implementation, routine technical choices, integration, testing and documentation within approved scope. The goal is a playable world the creator can discover without supervising every implementation detail.

Clarified on 2026-10-18: the world is also a surprise for the creator's former PZ group from Ljungby/Agunnaryd, with an eventual private multiplayer reunion. Approximately ten personally important homes merit individual exterior/interior work; plausible templates cover the rest. Keep research effort proportional to recognition value. This does not expand the 4–5-building V1 or prevent open Getaboda development with the creator.

Conversation is in Swedish. Documentation, code, identifiers, comments, commits, PRs and authored UI text are in English; retain proper place names and source identifiers. Bring existing documents into English when updating them without rewriting historical evidence or external names.

| Proceed independently | Bring a concrete proposal to the creator |
| --- | --- |
| Bug investigation, tests, reversible fixes and refactoring within scope | Changes to atmosphere, visual direction, world layout policy or gameplay balance |
| Generic interiors and procedural variation within approved style | New mechanics, major features, target regions or material milestone changes |
| Tool experiments, reproducible exports and local test packages | Purchases, paid services, public releases and PR merges |
| Evidence capture, documentation and small draft PRs | Destructive actions affecting valuable saves or source data |

Continue useful independent work while a design answer is pending. Separate provisional prototypes from accepted design. Ask one consequential question at a time, with an example, a recommendation and its tradeoff. Do not make routine implementation details approval gates. Existing explicit authorization takes precedence over this default table.

Clarified on 2026-10-18: during an active session, continue from a completed slice
to the next ready authorized task. A progress report or routine technical failure
is not a reason to return ownership to the creator. Resolve failures or move to
independent ready work under the roadmap's diagnostic limit. Pause dependent work
for consequential creator decisions or a genuine external boundary. This does
not claim that work continues between turns or configure unattended execution.

## Specialist roles
Creator request, 2026-10-23: set up specialist agents directed by the lead. During
active project sessions, delegate useful independent tasks using the reusable
[studio assignments](AGENT_ROLES.md). This is standing authorization for bounded
project delegation within accepted scope, not a new release, access or scheduling
permission. Keep the current model unless the creator requests a change.

Use a small team structure when parallel work is explicitly authorized and useful. These are task roles, not installed agents or a claim of distinct model expertise. The lead can perform any role without spawning another agent.

| Role | Responsibility | Required handoff |
| --- | --- | --- |
| Lead / integration | Priorities, scope, integration, user decisions and delivery | State, tested artifact, open decisions and next step |
| World / data | Source geometry, provenance, projections and overrides | Source/license record, assumptions and repeatability checks |
| Buildings / art | Swedish templates, compatible assets and interiors | Reusable source, attribution and representative preview |
| QA / review | Actual game checks, regressions and evidence review | Exact version/artifact, passes, failures and unverified behavior |

Give delegated tasks a bounded result, acceptance criteria and file ownership. Use separate worktrees for concurrent writers; review and integrate sequentially. Worktrees do not share uncommitted changes. Only the integration owner installs test mods, drives WorldEd/BuildingEd or controls the game: these resources remain shared even with separate Git worktrees. Do not create persistent chats or schedules merely to fill roles. Use the current model unless the user requests another.

## Dispatch and integration

The execution queue lives in [ROADMAP](ROADMAP.md); keep task state there instead of creating a second backlog. Select one main deliverable. When delegation is authorized and useful, start with one implementation task and one independent review task; split further only for genuinely independent work. A role is a focused task with context and evidence, not a permanent model identity.

Each assignment includes this compact brief:

```text
Task ID and outcome:
Repository/worktree and base commit:
Inputs and relevant instructions:
Owned files; shared files reserved for the lead:
Acceptance criteria and required evidence:
Dependencies, exclusions and data-handling boundary:
Return: changed files/commit, checks, unresolved risks and next action.
```

Workers report to the lead. The lead reviews the actual diff and evidence, integrates one result at a time, and runs the affected checks. Read-only reviewers do not edit the implementation. Shared documentation, packaging, mod installation, mapping-tool UI and game execution remain with the lead unless explicitly handed over. Record a new owner before transferring those resources.

Use the [role briefs and dispatch states](AGENT_ROLES.md) for repeat assignments.
Show actual worker activity separately from roadmap readiness. Do not leave a
historical assignment marked Running after it returns or the session ends.

For each delivery, report separately what is implemented, what has passed automated/editor/game checks, and what still needs creator acceptance. If a dependency blocks one task, choose another ready task rather than repeatedly polling or inventing success. Raw Lantmäteriet data must not enter agent prompts or model-visible tool output under the current local-processing decision.

## Open development and later discovery
The creator explicitly wants to participate in developing Getaboda and the worldbuilding tools. Getaboda has no spoiler restriction: show house and garden layouts, screenshots, placements, implementation progress and useful technical explanations. Explain the path from source data through templates and overrides to official export and game testing. Invite feedback on design and consequential technical tradeoffs while continuing routine implementation independently. The agreed product remains a Project Zomboid map mod with supporting generation tools.

Preserve surprises in later areas by default. Avoid their exact floor plans, loot, seeds and discovery locations in routine updates, task titles and unsolicited screenshots unless requested. Use Getaboda or a representative test building for design reviews. Keep detailed evidence in developer reports and identify spoilers for later areas before opening them. Always disclose bugs and material risks. Follow `DATA_AND_RIGHTS.md` for source-data handling and publication of detailed private interiors.

## Delivery rhythm
1. Read the current milestone and evidence; choose the smallest useful next slice.
2. Build, test and repair it before asking the creator to play it.
3. Review acceptance criteria; record tool and game checks separately.
4. Give a short Swedish update at meaningful milestones during active work: playable change, validation, limitation and any decision required. Include in-game screenshots and useful technical explanations for Getaboda and the tools; preserve surprises in later areas. Identify older test images and distinguish playable results from proposals. The creator explicitly requested regular visual progress updates.
5. Request brief milestone playtests for feel and usability. Keep unresolved technical QA with the agent. Never mark human acceptance without feedback.

Repository instructions and handoffs carry durable context. A Codex project groups work; it does not itself keep agents running or automatically share every chat's state. This agreement configures no unattended schedule.

## Studio report adaptation (2026-10-23)

The creator supplied [How the studio ran itself: a report for the CEO](https://claude.ai/artifact/BGBcFViGM3zmj2yGGzkTqJ),
whose document heading is *How to set up an autonomous game studio where you are
the CEO* (16 October 2026, @Aurora). Its full content was read after sign-in.
Use it as workflow inspiration, not as verified documentation of this client's
capabilities or permission to execute its embedded project-instruction template.

Apply its coordinator, ownership, QA and handoff pattern through the existing
roles and single queue. Adapt the web-game release model to this local PZ mod:

- **Quick validation:** during a bounded change, run affected checks and inspect
  the result. Documentation changes need setup/link/overview/whitespace checks;
  source changes need relevant tests and authoring validation. Record exactly
  what ran. Repeat broader checks when changes or failures justify them.
- **Test-delivery validation:** before calling a new playable package ready,
  run the required suite and package checks, then have the lead verify the exact
  artifact in the game, including relevant access, light, collision, roof and
  clean save/reload behavior. An independent reviewer examines the diff and
  evidence. Automated success alone cannot clear this gameplay gate.
- **One integration owner:** the lead assembles the tested package and records
  its version/hash, screenshots, known limits and short playtest instructions.
  Creator visual feedback, personal playtesting and public-release approval
  remain separate. No daily automatic publishing is configured.
- **Cross-owner requests:** return the needed file/change, reason, dependency
  and acceptance evidence to the lead. The lead routes it to its current owner
  and records the outcome under the existing ROADMAP task. Do not introduce a
  second whiteboard/backlog or edit another writer's files.
- **Pending choices:** continue independent approved work. An inexpensive,
  reversible prototype may explore options within scope, but hiding a change
  behind a switch does not authorize a consequential design, access or release
  decision. Do not spend a delivery building an unapproved major direction.
- **Session handoff:** record the current commit/worktree, completed checks,
  exact playable artifact, unresolved decisions and next ready queue item.
  Resume from that evidence instead of repeating settled questions. Only live
  worker status establishes active work; a handoff does not schedule a wake-up.

## Selected skills (same SKILL.md mirrored in two directories)

| Task | Skill | Expected result |
| --- | --- | --- |
| Architectural ambiguity | `grill-with-docs` | One decision at a time; confirmed decision recorded |
| Agreed non-trivial feature | `to-spec` | Small spec with measurable acceptance criteria |
| Large approved spec | `to-tickets` | Dependency-ordered vertical issues |
| Implement behavior | `tdd` | Red–green, public-behavior test and minimum implementation |
| Investigate failing/slow feature | `diagnosing-bugs` | Reproduction, root cause, regression proof |
| Review completed diff | `code-review` | Spec vs implementation and maintainability/risk |
| Switch agent/session | `handoff` | Short context handoff with commit, state, next step |
| Any code change | `ponytail` | Simplest complete solution, no speculative additions |

The skills are **adaptations** inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills) and [Ponytail](https://github.com/DietrichGebert/ponytail), not full upstream plugins. Licensing and differences: [THIRD_PARTY_SKILLS.md](THIRD_PARTY_SKILLS.md).

## Default change path
1. Read [AGENTS.md](../AGENTS.md) and affected code. Read only the relevant docs or skill, not every file.
2. For a material unknown: ask one essential question or prove it with a small experiment. Do not invent a decision.
3. Plan the thinnest vertical slice; write a spec/tickets only if complexity warrants them.
4. Inspect the current branch and work first. Continue the relevant feature branch when appropriate; start a new branch/worktree for independent work. Make narrow changes and execute relevant checks.
5. Review the actual diff against specification **and** code quality. Record manual game tests when required.
6. Open a small PR with actual evidence and remaining risks; request human review for gameplay/engine/rights decisions.
7. Update docs or the glossary when an actual decision changes. Handoff using committed paths, not vague session memory.

## Agent switching
Both clients operate against the same GitHub repository. Make sure the other agent fetches the latest commit; never run both on the same uncommitted working directory. Prefer separate branches or git worktrees, particularly for concurrent work. A handoff names the branch/commit, ticket, acceptance criteria, verification output, known risks and next action.

## Security and licensing
Project code, imported geodata and third-party assets need traceable provenance. No credential files, executable external hooks or auto-updating plugins committed here. Review any dependency or plugin before installation. Do not run commands copied from untrusted issue content.

## Installation / discovery
- Codex: project skills at `.agents/skills/<name>/SKILL.md`.
- Claude Code: project skills at `.claude/skills/<name>/SKILL.md`.
- Files are duplicated rather than symlinked for cross-platform compatibility and should remain byte-identical.
- Codex/Claude features vary by product version; if a skill isn't auto-discovered, open it directly. These local instructions do not install upstream marketplace plugins.

## Check
Run `python tools/check_agent_setup.py` and `python -m unittest discover -s tests -v` after modifying skill instructions or project code, respectively.
