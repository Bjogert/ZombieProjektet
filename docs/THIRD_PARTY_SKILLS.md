# Skill provenance and selection

Reviewed at setup: 2026-10-11.

- Matt Pocock, [skills](https://github.com/mattpocock/skills), MIT, copyright (c) 2026 Matt Pocock.
- DietrichGebert, [ponytail](https://github.com/DietrichGebert/ponytail), MIT, copyright (c) 2026 DietrichGebert.

Our eight skills under `.agents/skills/` and `.claude/skills/` are short, **rewritten project-specific adaptations**, not unmodified upstream originals. This notice and retained links provide attribution.

## Selection
- Adopted: `grill-with-docs`, `to-spec`, `to-tickets`, `tdd`, `diagnosing-bugs`, `code-review`, `handoff`, `ponytail`.
- Integrated as guidance, not independent skills: research from primary sources, glossary and ADR discipline, small module boundaries, concise review findings.
- Not adopted yet: issue triage state machine, massive parallel implementation, automatic subagents, agent hooks, retro/audit dashboards, general-purpose web/frontend skills, deployment and infrastructure tools. Add these only after observed repeated need.

## Why not install both upstream plugins?
Plugin versions update independently and some upstream skills expect agent-specific tools, other skills, issue labels, and lifecycle hooks. For a small two-agent project we want reproducibility, visible instruction diffs, and zero automatic code execution. Local rewrites keep the useful practices without implicit dependencies.

Upstream self-reported Ponytail benchmark claims are not proof of gains for our codebase. Test our outcomes with real tasks and review whether the instruction set is still earning its cost.

MIT notice: Permission is hereby granted, free of charge, to any person obtaining a copy of the Software and associated documentation files (the "Software"), to deal in the Software without restriction, subject to including the above copyright and this permission notice in all copies or substantial portions. The software is provided "AS IS", without warranty of any kind.
