"""Offline tests for generated credits and the trusted-base boundary."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("credits", ROOT / "scripts/credits.py")
credits = importlib.util.module_from_spec(spec)
spec.loader.exec_module(credits)


class CreditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name) / "base"
        self.proposed = Path(self.tmp.name) / "proposed"
        shutil.copytree(ROOT, self.base, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        shutil.copytree(self.base, self.proposed)
        self.path = self.proposed / "design/community/alice/work.json"
        self.path.parent.mkdir()
        self.obj = json.loads((ROOT / "templates/workflow.json").read_text())
        self.obj["author"] = "alice"
        self.obj["reviewed"] = "2020-01-01"
        self.obj["credits"] = [{"handle": "alice", "contribution": "Wrote the lighting workflow"}]
        self.save()
        self.diff = b"A\0design/community/alice/work.json\0M\0README.md\0"

    def save(self):
        self.path.write_text(json.dumps(self.obj), encoding="utf-8")

    def update_readme(self):
        readme = self.proposed / "README.md"
        readme.write_bytes(credits.replace(readme.read_bytes(), credits.render(self.proposed)))

    def check(self, body=""):
        return subprocess.run([sys.executable, "-I", str(ROOT / "scripts/credits.py"), "--check",
                               str(self.base), str(self.proposed)], input=self.diff,
                              env=dict(os.environ, PR_AUTHOR="alice", PR_BODY=body, PR_NUMBER="42"), capture_output=True)

    def test_new_submitter_and_shared_credit(self):
        self.obj["credits"].append({"handle": "bob", "contribution": "Tested the final export"})
        self.save()
        self.update_readme()
        text = (self.proposed / "README.md").read_text()
        self.assertIn("[@alice](https://github.com/alice): Wrote the lighting workflow", text)
        self.assertIn("[@bob](https://github.com/bob): Tested the final export", text)
        self.assertNotEqual(self.check().returncode, 0)
        self.assertNotEqual(self.check("Credit confirmation @bob https://github.com/aunysillyme-dev/stack/pull/9#issuecomment-1").returncode, 0)
        self.assertEqual(self.check("Credit confirmation @bob https://github.com/aunysillyme-dev/stack/pull/42#issuecomment-1").returncode, 0)

    def test_old_record_valid_but_changed_record_needs_credit(self):
        del self.obj["credits"]
        self.save()
        credits.validator.validate(self.proposed)
        self.update_readme()
        self.assertIn("Submitted", (self.proposed / "README.md").read_text())
        self.assertNotEqual(self.check().returncode, 0)

    def test_injection_is_plain_text(self):
        self.obj["credits"][0]["contribution"] = 'Made ![image](https://evil.example/a) <img src=x> & [link](https://evil.example) @person'
        self.save()
        self.update_readme()
        result = (self.proposed / "README.md").read_text()
        self.assertIn(r'\!\[image\]\(https&#58;//evil\.example/a\)', result)
        self.assertIn('&lt;img src=x&gt;', result)
        self.assertNotIn('<img', result)
        self.assertIn('&#64;person', result)
        self.assertNotIn('https://evil', result)
        self.assertEqual(self.check().returncode, 0)

    def test_tampering_outside_or_inside_block_fails(self):
        self.update_readme()
        readme = self.proposed / "README.md"
        original = readme.read_bytes()
        for changed in (original.replace(b'# Stack', b'# Altered'),
                        original.replace(b'Wrote the lighting workflow', b'Invented work')):
            readme.write_bytes(changed)
            self.assertNotEqual(self.check().returncode, 0)

    def test_existing_credit_requires_owner_review_for_removal(self):
        previous = self.base / self.path.relative_to(self.proposed)
        previous.parent.mkdir(parents=True, exist_ok=True)
        original = dict(self.obj, credits=self.obj["credits"] + [{"handle": "bob", "contribution": "Checked exports"}])
        previous.write_text(json.dumps(original))
        self.diff = b"M\0design/community/alice/work.json\0"
        self.update_readme()
        self.assertNotEqual(self.check().returncode, 0)
        self.path.unlink()
        self.path.parent.rmdir()
        self.diff = b"D\0design/community/alice/work.json\0"
        self.update_readme()
        self.assertNotEqual(self.check().returncode, 0)

    def test_other_authors_description_cannot_be_rewritten(self):
        previous = self.base / self.path.relative_to(self.proposed)
        previous.parent.mkdir(parents=True, exist_ok=True)
        self.obj["credits"].append({"handle": "bob", "contribution": "Checked exports"})
        previous.write_text(json.dumps(self.obj))
        self.obj["credits"][-1]["contribution"] = "Approved everything"
        self.save()
        self.update_readme()
        self.assertNotEqual(self.check().returncode, 0)

    def test_root_registry_and_links(self):
        self.update_readme()
        self.assertIn("(design/community/alice/work.json)", (self.proposed / "README.md").read_text())
        for bad in (["design", "video", "../outside"], ["design", "video", "scripts"],
                    ["design"], ["design", "video", "video"]):
            (self.proposed / "catalog.json").write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                credits.validator.validate(self.proposed)
        (self.proposed / "catalog.json").write_text('["design","video"]')
        (self.proposed / "stacks").mkdir()
        with self.assertRaises(ValueError):
            credits.validator.validate(self.proposed)

    def test_credit_validation(self):
        for items in ([{"handle": "bob", "contribution": "Helped"}],
                      [{"handle": "alice", "contribution": "a\nb"}],
                      [{"handle": "alice", "contribution": "a"}, {"handle": "alice", "contribution": "b"}]):
            self.obj["credits"] = items
            self.save()
            with self.assertRaises(ValueError):
                credits.validator.validate(self.proposed)

    def test_scope_still_restricts_paths(self):
        script = ROOT / "scripts/check_contribution.py"
        for diff, ok in ((b'M\0README.md\0', True),
                         (b'M\0design/community/bob/work.json\0', False),
                         (b'A\0README.md\0', False),
                         (b'M\0scripts/credits.py\0', False)):
            result = subprocess.run([sys.executable, '-I', str(script), str(self.base)], input=diff,
                                    env=dict(os.environ, PR_AUTHOR='alice'), capture_output=True)
            self.assertEqual(result.returncode == 0, ok)


if __name__ == '__main__':
    unittest.main()
