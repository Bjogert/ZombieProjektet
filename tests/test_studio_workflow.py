"""Test skill discovery with synthetic repositories; no agent activity claimed."""
from pathlib import Path
import tempfile
import unittest

from tools.check_agent_setup import SKILLS, skill_names, verify


class SkillDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'docs').mkdir()
        (self.root/'docs/AGENT_WORKFLOW.md').write_text('Synthetic workflow', encoding='utf-8')
        (self.root/'AGENTS.md').write_text('See CLAUDE.md', encoding='utf-8')
        (self.root/'CLAUDE.md').write_text('See AGENTS.md', encoding='utf-8')
        for skill in SKILLS:
            self.add_skill(skill)

    def add_skill(self, name):
        for client in ('.agents','.claude'):
            path = self.root/client/'skills'/name/'SKILL.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f'---\nname: {name}\ndescription: Synthetic fixture\n---\n', encoding='utf-8')

    def test_existing_contract_still_passes(self):
        self.assertEqual(verify(self.root), [])

    def test_new_skill_is_discovered(self):
        self.add_skill('art-direction')
        self.assertIn('art-direction', skill_names(self.root))
        self.assertEqual(verify(self.root), [])

    def test_new_skill_drift_is_caught(self):
        self.add_skill('art-direction')
        (self.root/'.claude/skills/art-direction/SKILL.md').write_text('different', encoding='utf-8')
        self.assertIn('Skill drift: art-direction', verify(self.root))

    def test_one_sided_new_skill_is_caught(self):
        self.add_skill('household-design')
        (self.root/'.agents/skills/household-design/SKILL.md').unlink()
        self.assertIn('Missing skill: household-design', verify(self.root))

    def test_required_skill_cannot_silently_disappear(self):
        for client in ('.agents','.claude'):
            (self.root/client/'skills/tdd/SKILL.md').unlink()
        self.assertIn('Missing skill: tdd', verify(self.root))

    def test_frontmatter_is_checked_for_new_skill(self):
        self.add_skill('new-skill')
        for client in ('.agents','.claude'):
            (self.root/client/'skills/new-skill/SKILL.md').write_text('No header', encoding='utf-8')
        self.assertIn('Invalid skill frontmatter: new-skill', verify(self.root))

    def test_missing_entrypoint_reports_instead_of_crashing(self):
        (self.root/'AGENTS.md').unlink()
        self.assertTrue(any('Unreadable entrypoint AGENTS.md' in e for e in verify(self.root)))

    def test_missing_workflow_is_caught(self):
        (self.root/'docs/AGENT_WORKFLOW.md').unlink()
        self.assertIn('Missing shared workflow', verify(self.root))

try:
    import tomllib
except ImportError:
    tomllib = None


@unittest.skipIf(tomllib is None, 'Native TOML syntax check needs Python 3.11+; CI uses 3.12')
class NativeAgentDefinitionTests(unittest.TestCase):
    def test_native_definitions_have_only_supported_required_fields(self):
        root = Path(__file__).resolve().parents[1]
        definitions = sorted((root/'.codex/agents').glob('*.toml'))
        self.assertEqual(len(definitions), 4)
        names = set()
        for path in definitions:
            data = tomllib.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(set(data), {'name','description','developer_instructions'})
            self.assertEqual(data['name'], path.stem)
            self.assertNotIn(data['name'], names)
            names.add(data['name'])
            self.assertIn('AGENTS.md', data['developer_instructions'])
            self.assertIn('docs/AGENT_ROLES.md', data['developer_instructions'])

    def test_project_config_caps_children_without_model_or_permission_changes(self):
        root = Path(__file__).resolve().parents[1]
        config = tomllib.loads((root/'.codex/config.toml').read_text(encoding='utf-8'))
        self.assertEqual(config, {'agents':{'max_concurrent_threads_per_session':2}})

    def test_new_skill_mirrors_are_identical(self):
        root = Path(__file__).resolve().parents[1]
        for name in ('art-direction','household-design'):
            a = (root/'.agents/skills'/name/'SKILL.md').read_bytes()
            b = (root/'.claude/skills'/name/'SKILL.md').read_bytes()
            self.assertEqual(a,b)
            self.assertTrue(a.startswith(f'---\nname: {name}\n'.encode()))


if __name__ == '__main__':
    unittest.main()
