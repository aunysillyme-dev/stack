# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Offline regression tests for contribution scope and catalog validation."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SourceTests(unittest.TestCase):
    def test_hostname_urls(self):
        for value in ("https://example.org/", "https://docs.example.org/path"):
            with self.subTest(value=value):
                validator.url(value)

    def test_ip_and_numeric_addresses_are_rejected(self):
        for value in ("https://8.8.8.8/", "https://[2606:4700:4700::1111]/",
                      "https://2130706433/", "https://127.1/", "https://0177.0.0.1/",
                      "https://0x7f000001/", "https://0x7f.0.0.1/"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validator.url(value)

    def test_review_date(self):
        today = datetime.now(timezone.utc).date()
        validator.day(today.isoformat())
        validator.day((today - timedelta(days=1)).isoformat())
        with self.assertRaises(ValueError):
            validator.day((today + timedelta(days=1)).isoformat())


class ScopeTests(unittest.TestCase):
    def check_scope(self, author, entries, expected):
        env = dict(os.environ, PR_AUTHOR=author)
        result = subprocess.run(
            [sys.executable, "-I", str(ROOT / "scripts/check_contribution.py"), str(ROOT)],
            input=b"\0".join(part.encode() for part in entries) + b"\0",
            env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode == 0, expected, result.stderr.decode())

    def test_valid_contributions_and_maintainer(self):
        self.check_scope("Alice", ["A", "01-design-stack/community/alice/my-workflow.json"], True)
        self.check_scope("alice", ["M", "02-video-stack/community/alice/a.json"], True)
        self.check_scope("aunysillyme", ["M", "02-video-stack/canonical.json"], True)
        self.check_scope("alice", ["R100", "01-design-stack/community/alice/a.json",
                                   "01-design-stack/community/alice/b.json"], True)
        self.check_scope("alice", ["A", "03-compute-stack/community/alice/job.json"], True)
        self.check_scope("alice", ["A", "04-agentic-stack/community/alice/job.json"], True)

    def test_root_categories_only(self):
        for path in ("stacks/02-video-stack/community/alice/work.json", "templates/community/alice/work.json",
                     "scripts/community/alice/work.json", "catalog.json", "/02-video-stack/community/alice/work.json",
                     "02-video-stack/community/../alice/work.json", "02-video-stack//community/alice/work.json"):
            self.check_scope("alice", ["A", path], False)

    def test_invalid_authors_and_paths(self):
        for author, path in (("", "01-design-stack/community/alice/a.json"),
                             ("alice/../bob", "01-design-stack/community/bob/a.json"),
                             ("K", "01-design-stack/community/k/a.json"),
                             ("alice", "01-design-stack/community/bob/a.json"),
                             ("alice", "02-video-stack/canonical.json"),
                             ("alice", ".github/workflows/checks.yml"),
                             ("alice", "fake/community/alice/a.json"),
                             ("alice", "01-design-stack/community/alice/nested/a.json")):
            with self.subTest(author=author, path=path):
                self.check_scope(author, ["M", path], False)

    def test_cross_folder_rename_rejected_in_both_directions(self):
        own = "01-design-stack/community/alice/a.json"
        other = "01-design-stack/community/bob/a.json"
        self.check_scope("alice", ["R100", other, own], False)
        self.check_scope("alice", ["R100", own, other], False)
        self.check_scope("alice", ["R100", own, "02-video-stack/community/alice/a.json"], False)
        self.check_scope("alice", ["D", own, "A", "02-video-stack/community/alice/a.json"], False)
        self.check_scope("alice", ["D", own, "A", "01-design-stack/community/alice/b.json"], True)

    def test_malformed_diff_is_rejected(self):
        for entries in (["R100", "01-design-stack/community/alice/a.json"],
                        ["U", "01-design-stack/community/alice/a.json"],
                        ["M", ""]):
            with self.subTest(entries=entries):
                self.check_scope("alice", entries, False)


class PublishedStackTests(unittest.TestCase):
    def test_video_and_design_are_published_and_valid(self):
        self.assertEqual(validator.validate(ROOT), 4)
        for name in ("01-design-stack", "02-video-stack", "03-compute-stack", "04-agentic-stack"):
            meta = json.loads((ROOT / name / "stack.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["status"], "published")
            self.assertEqual(meta["canonical"], "canonical.json")
            self.assertEqual(meta["inventory"], "inventory.json")

    def test_original_entries_are_kept(self):
        pairs = (
            ("01-design-stack", "original-design-names.json", "original-design-links.json", "name", "link"),
            ("02-video-stack", "original-video-names.json", "original-video-links.json", "name", "link"),
        )
        for folder, names_file, links_file, name_key, link_key in pairs:
            entries = json.loads((ROOT / folder / "inventory.json").read_text(encoding="utf-8"))["entries"]
            current_names = {entry[name_key] for entry in entries}
            current_links = {entry[link_key] for entry in entries}
            original_names = json.loads((ROOT / "tests/fixtures" / names_file).read_text(encoding="utf-8"))
            original_links = json.loads((ROOT / "tests/fixtures" / links_file).read_text(encoding="utf-8"))
            self.assertTrue(set(original_names) <= current_names)
            self.assertTrue(set(original_links) <= current_links)
            self.assertEqual(len(original_names), len(set(original_names)))

    def test_new_stacks_use_the_public_entry_fields(self):
        self.assertEqual(validator.ENTRY_FIELDS, ("name", "link", "description", "tier"))
        for name in ("03-compute-stack", "04-agentic-stack"):
            inventory = json.loads((ROOT / name / "inventory.json").read_text(encoding="utf-8"))
            canonical = json.loads((ROOT / name / "canonical.json").read_text(encoding="utf-8"))
            self.assertTrue(inventory["entries"])
            self.assertTrue(canonical["tools"])
            self.assertTrue(canonical["workflows"])
            for entry in inventory["entries"]:
                self.assertIn(entry["cost_class"], validator.PUBLIC_TIERS)
                self.assertNotIn("\n", entry["notes"])
                validator.url(entry["link"])
            links = [entry["link"] for entry in inventory["entries"]]
            self.assertEqual(len(links), len(set(links)))

    def test_design_canonical_and_inventory_policies(self):
        canonical = json.loads((ROOT / "01-design-stack/canonical.json").read_text(encoding="utf-8"))
        inventory = json.loads((ROOT / "01-design-stack/inventory.json").read_text(encoding="utf-8"))
        tool_urls = [item["url"] for item in canonical["tools"]]
        self.assertEqual(len(tool_urls), len(set(tool_urls)))
        self.assertTrue(canonical["workflows"])

        links = [entry["link"] for entry in inventory["entries"]]
        self.assertEqual(len(links), len(set(links)))
        cost_classes = [entry["cost_class"] for entry in inventory["entries"]]
        self.assertTrue(set(cost_classes) <= {"free", "freemium", "paid"})
        seen_paid = False
        for cost_class in cost_classes:
            if cost_class == "paid":
                seen_paid = True
            else:
                self.assertFalse(seen_paid, "non-paid entry cannot appear after paid entries")

        def normalize(value):
            return value.rstrip("/").lower()

        paid_links = {normalize(e["link"]) for e in inventory["entries"] if e["cost_class"] == "paid"}
        for tool in canonical["tools"]:
            self.assertNotIn(normalize(tool["url"]), paid_links)

    def test_published_guide_nullable_but_must_be_https_when_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            stack_path = root / "01-design-stack/stack.json"
            meta = json.loads(stack_path.read_text(encoding="utf-8"))
            meta["guide"] = None
            stack_path.write_text(json.dumps(meta), encoding="utf-8")
            validator.category(root / "01-design-stack")

            meta["guide"] = "http://example.com"
            stack_path.write_text(json.dumps(meta), encoding="utf-8")
            with self.assertRaises(ValueError):
                validator.category(root / "01-design-stack")

    def test_tier_and_markdown_sync_is_current(self):
        result = subprocess.run(
            [sys.executable, "-I", str(ROOT / "scripts/sync_tiers.py"), "--check", str(ROOT)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
