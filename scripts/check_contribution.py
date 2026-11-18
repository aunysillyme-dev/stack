"""Check a NUL-delimited git diff --name-status against the PR author's scope."""

import os
from pathlib import Path
import re
import sys


# Keep this list in the trusted base branch and aligned with repository ownership.
MAINTAINERS = {"aunysillyme"}
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
    categories = {p.name for p in (root / "stacks").iterdir()
                  if p.is_dir() and not p.is_symlink() and (p / "stack.json").is_file()}

    def allowed(path):
        parts = path.split("/")
        return (len(parts) == 5 and parts[0] == "stacks" and parts[1] in categories
                and parts[2] == "community" and parts[3] == author
                and WORKFLOW.fullmatch(parts[4]) is not None)

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
            if not all(allowed(path) for path in paths):
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
