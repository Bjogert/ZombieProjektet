# ZombieProjektet — agent entrypoint (Codex and Claude Code)

This is the canonical shared instruction file. Claude Code: also read [CLAUDE.md](CLAUDE.md), which points back here. Read it once, not recursively.

## Project
Make believable Swedish survival gameplay: "what would I do in reality?" should usually work. Read [docs/VISION.md](docs/VISION.md) and [docs/SCOPE.md](docs/SCOPE.md) for boundaries. The Project Zomboid mod versus standalone-game decision is still OPEN; see [docs/decisions/0001-mod-or-game.md](docs/decisions/0001-mod-or-game.md). Do not silently select an engine.

## Working agreement
- First inspect affected code, existing tests, [GLOSSARY.md](GLOSSARY.md), and relevant ADRs. Ground API and license claims in primary sources.
- For uncertain architecture or game design, use `grill-with-docs`. For accepted work, use `to-spec` then `to-tickets` when breakdown is warranted. One independently verifiable vertical slice at a time.
- For behavioral logic, use `tdd` with a public test seam; for defects, `diagnosing-bugs`; before shipping, `code-review`. For context switching, `handoff`.
- Always apply the **ponytail principle**: understand scope, reuse built-ins and existing code, choose the smallest complete solution. Do not trade away validation, security, gameplay correctness, or tests to save code.
- Follow [docs/AGENT_WORKFLOW.md](docs/AGENT_WORKFLOW.md) for skills, invocation, git and review conventions.
- Run `python -m unittest discover -s tests -v` for Python changes and report what actually ran. In-game claims require an in-game test, not just a passing unit test.
- Preserve deterministic map processing, stable IDs and original geodata provenance. Follow [docs/DATA_AND_RIGHTS.md](docs/DATA_AND_RIGHTS.md); do not import proprietary Project Zomboid game assets or Google map imagery.
- Finish with changed behavior, evidence, untested items, and meaningful risks. Do not claim success without verification.

## Skills
Selected skills live under `.agents/skills/` (Codex) and identical copies in `.claude/skills/` (Claude Code). Read a matching `SKILL.md` only when its task applies. If your runtime doesn't discover these automatically, open its file explicitly. Keep mirrored skill content identical.
