# Claude Code — ZombieProjektet

**Läs [AGENTS.md](AGENTS.md) först.** Den är gemensam källa för Codex och Claude Code. Läs inte om dessa två filer i en loop.

Project Zomboid **Build 42 Stable-kartmod** är beslutad. Ingen fristående motor utreds eller byggs nu.

Läs [docs/PROJECT_SPEC.md](docs/PROJECT_SPEC.md), [docs/ROADMAP.md](docs/ROADMAP.md) och den aktuella [Build 42-spiken](docs/BUILD42_SPIKE.md) före arbetet. Projekt-skills finns i `.claude/skills/<name>/SKILL.md`; Codex har motsvarande filer i `.agents/skills/`.

Skriv agentplaner och reviews i Markdown. Håll den förenklade HTML-vyn uppdaterad genom `docs/HUMAN_OVERVIEW.md` och `python tools/render_dashboard.py`. Utge aldrig unit tests för faktiska speltester. Installera inte externa agenter, hooks eller pluginpaket utan godkännande.
