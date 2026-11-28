# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Check GitHub's current PR metadata and the first-line v1 certification."""

import json
import os
import subprocess
import sys


STATEMENT = "I certify under Stack Contributor Certification v1 that I may submit this contribution under the applicable repository licenses."
# The same v1 statement covers every live stack and the entry fields
# name, link, description, and tier. New categories do not get a new certification.
CATALOG_CATEGORIES = (
    "01-design-stack",
    "02-video-stack",
    "03-compute-stack",
    "04-agentic-stack",
)


def statement_for(category_id):
    if category_id not in CATALOG_CATEGORIES:
        raise ValueError("The v1 certification does not cover an unknown category.")
    return STATEMENT
QUERY = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      author { __typename ... on User { databaseId } }
      editor { __typename ... on User { databaseId } }
      lastEditedAt
      headRefOid
      body
    }
  }
}
"""


def check(pr, author_id, head):
    if not head or pr["headRefOid"] != head:
        raise ValueError("The pull request changed. Run the check for the current head.")
    author = {"__typename": "User", "databaseId": int(author_id)}
    if pr["author"] != author:
        raise ValueError("The certification requires the submitting GitHub user account.")
    editor = pr["editor"]
    if editor != author and (editor is not None or pr["lastEditedAt"] is not None):
        raise ValueError("The submitter must personally review the description, then clear and recheck the first-line box if accurate.")
    lines = pr["body"].split("\n", 1)
    if lines[0].removesuffix("\r") not in (
        "- [x] " + STATEMENT, "- [X] " + STATEMENT
    ):
        raise ValueError("Read the Stack v1 certification and check the first line if accurate.")


def main():
    owner, name = os.environ["GITHUB_REPOSITORY"].split("/")
    response = subprocess.check_output(
        ["gh", "api", "graphql", "--hostname", "github.com", "-f", "query=" + QUERY,
         "-f", "owner=" + owner, "-f", "name=" + name, "-F", "number=" + os.environ["PR_NUMBER"]]
    )
    result = json.loads(response)
    if not isinstance(result, dict) or result.get("errors"):
        raise ValueError("GitHub did not return complete certification metadata.")
    check(result["data"]["repository"]["pullRequest"], os.environ["PR_AUTHOR_ID"],
          os.environ["PR_HEAD_SHA"])


if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError, KeyError, OSError, subprocess.SubprocessError) as error:
        sys.exit(f"Certification check failed: {error}")
    print("Certification format and PR account metadata passed. Maintainer rights review is required.")
