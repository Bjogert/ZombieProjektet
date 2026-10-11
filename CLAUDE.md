# Claude Code entrypoint

**Read [AGENTS.md](AGENTS.md) first.** It is the single source of project rules for both Claude Code and Codex. AGENTS.md also points here for entrypoint discovery; do **not** recursively reread it.

Use project-local skills from `.claude/skills/<name>/SKILL.md` when their task applies. The authoritative workflow and skill selection is [docs/AGENT_WORKFLOW.md](docs/AGENT_WORKFLOW.md). Codex uses mirrored copies in `.agents/skills/`.

Do not silently install external plugins, enable hooks, or change the pending mod-versus-standalone decision. State what you tested and what you did not.
