---
name: handoff
description: Prepare a concise cross-agent ZombieProjektet handoff when switching between Codex and Claude Code or ending a significant work session.
---

# Cross-agent handoff (adapted from Matt Pocock)

1. Read git status, current branch, relevant issues/specs/ADRs and test results. Never claim an unrun test passed.
2. Update `docs/HANDOFF.md` **only when explicitly asked or when a meaningful active task is being handed to another agent**. Avoid rewriting this file for trivial tasks.
3. Keep it concise: goal, active branch/issue, what changed (links), confirmed decisions, commands and test results, blockers, next smallest action and any manual in-game verification.
4. Never duplicate full specs or commit diffs. Link to them. Never store secrets or personal paths.
5. Tell the receiving agent to read `AGENTS.md`, the active issue/spec and this handoff before continuing. It should verify git status, not trust stale handoff notes.

Source: mattpocock/skills handoff, adapted for project-based agent switching.
