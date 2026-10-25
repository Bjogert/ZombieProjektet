#!/usr/bin/env python3
"""Check every mirrored skill plus the retained required entrypoints (stdlib)."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
# Retain the original minimum; discovering additions must not allow silent removal.
SKILLS = ('grill-with-docs', 'to-spec', 'to-tickets', 'tdd', 'diagnosing-bugs',
          'code-review', 'handoff', 'ponytail')


def skill_names(root=None):
    root = ROOT if root is None else Path(root)
    names = set(SKILLS)
    for client in ('.agents', '.claude'):
        directory = root / client / 'skills'
        if directory.is_dir():
            names.update(path.name for path in directory.iterdir() if path.is_dir())
    return sorted(names)


def verify(root=None):
    root = ROOT if root is None else Path(root)
    errors = []
    for name in skill_names(root):
        a = root / '.agents' / 'skills' / name / 'SKILL.md'
        c = root / '.claude' / 'skills' / name / 'SKILL.md'
        if not a.is_file() or not c.is_file():
            errors.append(f'Missing skill: {name}')
            continue
        try:
            if a.read_bytes() != c.read_bytes():
                errors.append(f'Skill drift: {name}')
            content = a.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'Unreadable skill {name}: {exc}')
            continue
        if not content.startswith('---\nname: ' + name + '\n') or '\ndescription:' not in content:
            errors.append(f'Invalid skill frontmatter: {name}')
    texts = {}
    for filename in ('AGENTS.md', 'CLAUDE.md'):
        try:
            texts[filename] = (root / filename).read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'Unreadable entrypoint {filename}: {exc}')
    if len(texts) == 2 and ('CLAUDE.md' not in texts['AGENTS.md'] or 'AGENTS.md' not in texts['CLAUDE.md']):
        errors.append('Agent entrypoints must reference each other')
    if not (root / 'docs' / 'AGENT_WORKFLOW.md').is_file():
        errors.append('Missing shared workflow')
    return errors


if __name__ == '__main__':
    problems = verify()
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        sys.exit(1)
    print(f'OK: {len(skill_names())} mirrored skills and agent entrypoints')
