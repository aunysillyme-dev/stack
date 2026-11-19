# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Offline tests for the PR certification check and the contributor-facing form."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("certification", ROOT / "scripts/check_certification.py")
certification = importlib.util.module_from_spec(spec)
spec.loader.exec_module(certification)


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.author = {"__typename": "User", "databaseId": 12}
        self.line = "- [x] " + certification.STATEMENT
        self.head = "a" * 40
        self.pr = dict(author=self.author, editor=None, lastEditedAt=None,
                       headRefOid=self.head, body=self.line + "\n\nSources and credit.")

    def check(self, **changes):
        certification.check({**self.pr, **changes}, "12", self.head)

    def test_original_and_submitter_edits(self):
        self.check()
        self.check(body=self.pr["body"].replace("[x]", "[X]").replace("\n", "\r\n"),
                   lastEditedAt="2026-01-01T00:00:00Z", editor=self.author)

    def test_only_a_checked_first_line_counts(self):
        for body in ("", self.line.replace("[x]", "[ ]"), "Example\n" + self.line,
                     "<!--\n" + self.line + "\n-->", "> " + self.line, "```\n" + self.line + "\n```",
                     self.line + " (maybe)", self.line.replace("v1", "v2"),
                     "- [x] I agree to the Contributor License Agreement in CLA.md"):
            with self.subTest(body=body), self.assertRaises(ValueError):
                self.check(body=body)

    def test_account_edits_and_current_head(self):
        for changes in ({"author": None}, {"author": {"__typename": "Bot"}},
                        {"author": {"__typename": "User", "databaseId": 23}},
                        {"editor": {"__typename": "User", "databaseId": 23}},
                        {"editor": {"__typename": "Bot"}, "lastEditedAt": "date"},
                        {"editor": None, "lastEditedAt": "date"}, {"headRefOid": "stale"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.check(**changes)
        with self.assertRaises(ValueError):
            certification.check(self.pr, "", self.head)
        with self.assertRaises(ValueError):
            certification.check(self.pr, "12", "")

    def test_template_matches_policy_and_checker(self):
        first_line = (ROOT / ".github/pull_request_template.md").read_text().splitlines()[0]
        self.assertEqual(first_line, self.line.replace("[x]", "[ ]"))
        self.assertIn("> " + certification.STATEMENT,
                      (ROOT / "CONTRIBUTOR-CERTIFICATION.md").read_text().splitlines())

    def test_api_response_and_failures(self):
        env = {"GITHUB_REPOSITORY": "example/project", "PR_NUMBER": "12",
               "PR_HEAD_SHA": self.head, "PR_AUTHOR_ID": "12"}
        payload = {"data": {"repository": {"pullRequest": self.pr}}}
        with patch.dict(os.environ, env), patch("subprocess.check_output") as api:
            api.return_value = json.dumps(payload).encode()
            certification.main()
            args = api.call_args.args[0]
            self.assertEqual(args[:5], ["gh", "api", "graphql", "--hostname", "github.com"])
            self.assertIn("number=12", args)
            self.assertIn("owner=example", args)
            self.assertIn("name=project", args)
            api.return_value = json.dumps(dict(payload, errors=[{"message": "partial"}])).encode()
            with self.assertRaises(ValueError):
                certification.main()
            api.return_value = b"null"
            with self.assertRaises(ValueError):
                certification.main()
            api.side_effect = subprocess.CalledProcessError(1, ["gh"])
            with self.assertRaises(subprocess.CalledProcessError):
                certification.main()
