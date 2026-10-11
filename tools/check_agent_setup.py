#!/usr/bin/env python3
"""Check two-agent skill parity and core instruction pointers (stdlib only)."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("grill-with-docs", "to-spec", "to-tickets", "tdd", "diagnosing-bugs", "code-review", "handoff", "ponytail")


def verify():
    errors = []
    for name in SKILLS:
        a = ROOT / ".agents" / "skills" / name / "SKILL.md"
        c = ROOT / ".claude" / "skills" / name / "SKILL.md"
        if not a.is_file() or not c.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        if a.read_bytes() != c.read_bytes():
            errors.append(f"Skill drift: {name}")
        content = a.read_text(encoding="utf-8")
        if not content.startswith("---\nname: " + name + "\n") or "\ndescription:" not in content:
            errors.append(f"Invalid skill frontmatter: {name}")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    if "CLAUDE.md" not in agents or "AGENTS.md" not in claude:
        errors.append("Agent entrypoints must reference each other")
    if not (ROOT / "docs" / "AGENT_WORKFLOW.md").is_file():
        errors.append("Missing shared workflow")
    return errors


if __name__ == "__main__":
    problems = verify()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print(f"OK: {len(SKILLS)} mirrored skills and agent entrypoints")
