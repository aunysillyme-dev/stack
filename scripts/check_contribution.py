# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Check a NUL-delimited git diff --name-status against the PR author's scope."""

import json
import os
from pathlib import Path
import re
import sys


# Keep this list in the trusted base branch and aligned with repository ownership.
MAINTAINERS = set(Path(__file__).with_name("maintainers.txt").read_text().splitlines())
HANDLE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
WORKFLOW = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\.json\Z")


def check(root, author, data):
    if not author.isascii():
        raise ValueError("invalid PR author")
    author = author.lower()
    if len(author) > 39 or not HANDLE.fullmatch(author):
        raise ValueError("invalid PR author")
    if data and not data.endswith(b"\0"):
        raise ValueError("unterminated changed-file list")
    tokens = data[:-1].split(b"\0") if data else []
    # The workflow passes the trusted base checkout, including its category catalog.
    catalog = root / "catalog.json"
    if catalog.is_symlink() or not catalog.is_file():
        raise ValueError("missing or unsafe category catalog")
    categories = json.loads(catalog.read_text())

    def allowed(path):
        parts = path.split("/")
        return (len(parts) == 4 and parts[0] in categories
                and parts[1] == "community" and parts[2] == author
                and WORKFLOW.fullmatch(parts[3]) is not None)

    added_folders = set()
    deleted_folders = set()
    while tokens:
        status = tokens.pop(0).decode("ascii")
        if re.fullmatch(r"[RC][0-9]{1,3}", status):
            count = 2
        elif status in ("A", "D", "M", "T"):
            count = 1
        else:
            raise ValueError("unexpected diff status")
        if len(tokens) < count:
            raise ValueError("incomplete changed-file list")
        paths = [os.fsdecode(token) for token in tokens[:count]]
        del tokens[:count]
        if any(not path for path in paths):
            raise ValueError("empty changed path")
        if author not in MAINTAINERS:
            if not all(allowed(path) or (status == "M" and path == "README.md") for path in paths):
                raise ValueError("change outside the PR author's community folder")
            if count == 2 and paths[0].rsplit("/", 1)[0] != paths[1].rsplit("/", 1)[0]:
                raise ValueError("cross-folder rename or copy")
            if status == "A":
                added_folders.add(paths[0].rsplit("/", 1)[0])
            elif status == "D":
                deleted_folders.add(paths[0].rsplit("/", 1)[0])
    # Git may report a heavily edited rename as a deletion plus an addition.
    if added_folders and deleted_folders and len(added_folders | deleted_folders) > 1:
        raise ValueError("additions and deletions across folders are not allowed in one PR")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("expected trusted repository path")
        check(Path(sys.argv[1]), os.environ.get("PR_AUTHOR", ""), sys.stdin.buffer.read())
        print("Contribution scope accepted.")
    except (ValueError, OSError, UnicodeError) as error:
        sys.exit(f"Contribution scope rejected: {error}")
