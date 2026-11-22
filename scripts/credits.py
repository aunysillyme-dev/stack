# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Render credits offline; check a proposed README against a trusted base."""
import html
import importlib.util
import os
from pathlib import Path
import re
import sys

SPEC = importlib.util.spec_from_file_location("validator", Path(__file__).with_name("validate.py"))
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
START = b"<!-- credits:start -->\n"
END = b"<!-- credits:end -->"


def escape(value):
    # Escape Markdown punctuation and HTML before placing untrusted text in a list.
    text = html.escape(re.sub(r"([\\`*_{}\[\]()#+\-.!|~])", r"\\\1", value), quote=False)
    return text.replace("@", "&#64;").replace(":", "&#58;")


def render(root):
    validator.validate(root)
    lines = ["<!-- credits:start -->", "## Credits", "",
             "- [@aunysillyme](https://github.com/aunysillyme): Curated the [Video tools and workflows](02-video-stack/canonical.json), including the production pipeline and creative techniques.",
             "- [@aunysillyme](https://github.com/aunysillyme): Curated the [Design tools and workflows](01-design-stack/canonical.json) and the [design resource inventory](01-design-stack/inventory.json)."]
    paths = (path for name in validator.category_names(root)
             for path in (root / name / "community").glob("*/*.json"))
    for path in sorted(paths):
        obj = validator.read(path)
        for credit in obj.get("credits", [{"handle": obj["author"], "contribution": "Submitted " + obj["title"]}]):
            handle = credit["handle"]
            link = path.relative_to(root).as_posix()
            lines.append(f'- [@{handle}](https://github.com/{handle}): {escape(credit["contribution"])} ([workflow]({link})).')
    lines.append("<!-- credits:end -->")
    return "\n".join(lines).encode("utf-8")


def replace(base, block):
    if base.count(START) != 1 or base.count(END) != 1:
        raise ValueError("README needs exactly one pair of credit markers")
    before, rest = base.split(START)
    _, after = rest.split(END)
    return before + block + after


def confirmed_handles(body, number):
    if not re.fullmatch(r"[1-9][0-9]*", number):
        return set()
    pattern = (r"^Credit confirmation @([a-z0-9-]+) "
               r"https://github\.com/aunysillyme-dev/stack/pull/" + number + r"#issuecomment-[1-9][0-9]*[ \t]*$")
    visible = re.sub(r"<!--[\s\S]*?(?:-->|$)", "", body)
    return set(re.findall(pattern, visible.replace("\r\n", "\n"), re.MULTILINE))


def check_changed(base, root, data, outside, author, confirmed):
    # The scope check independently validates this NUL-delimited diff and both rename paths.
    tokens = data.split(b"\0")
    if tokens[-1] != b"":
        raise ValueError("unterminated changed-file list")
    tokens.pop()
    categories = set(validator.category_names(root))
    while tokens:
        status = tokens.pop(0).decode("ascii")
        count = 2 if re.fullmatch(r"[RC][0-9]{1,3}", status) else 1
        if len(tokens) < count:
            raise ValueError("incomplete changed-file list")
        paths, tokens = tokens[:count], tokens[count:]
        path = os.fsdecode(paths[-1])
        parts = path.split("/")
        if not (len(parts) == 4 and parts[0] in categories and parts[1] == "community"
                and parts[3].endswith(".json")):
            continue
        if status == "D":
            if outside:
                raise ValueError("Retire the workflow in place or request a maintainer removal review.")
            continue
        obj = validator.read(root / path)
        if not obj.get("credits"):
            raise ValueError(f"changed community workflow needs specific credits: {path}")
        previous = base / os.fsdecode(paths[0])
        if outside:
            prior = validator.read(previous).get("credits", []) if previous.is_file() else []
            old = {item["handle"]: item["contribution"] for item in prior}
            new = {item["handle"]: item["contribution"] for item in obj["credits"]}
            if old.keys() - new.keys():
                raise ValueError("Removing a prior byline requires maintainer review.")
            if any(old[h] != new[h] for h in old if h != author):
                raise ValueError("Editing another author's credit requires a maintainer PR.")
            if (new.keys() - old.keys() - {author}) - confirmed:
                raise ValueError("Link each newly credited coauthor's confirmation on this PR.")


def readme_bytes(root):
    path = root / "README.md"
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 2_000_000:
        raise ValueError("README must be a regular text file within 2 MB")
    return path.read_bytes()


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--write":
        root = Path.cwd()
        readme = root / "README.md"
        readme.write_bytes(replace(readme_bytes(root), render(root)))
    elif len(sys.argv) == 4 and sys.argv[1] == "--check":
        base, proposed = map(Path, sys.argv[2:])
        author = os.environ.get("PR_AUTHOR", "").lower()
        maintainers = Path(__file__).with_name("maintainers.txt").read_text().splitlines()
        outside = author not in maintainers
        source = base if outside else proposed
        expected = replace(readme_bytes(source), render(proposed))
        if readme_bytes(proposed) != expected:
            raise ValueError("README differs from trusted base outside credits or generated credits are stale")
        confirmed = confirmed_handles(os.environ.get("PR_BODY", ""), os.environ.get("PR_NUMBER", ""))
        check_changed(base, proposed, sys.stdin.buffer.read(), outside, author, confirmed)
    else:
        raise ValueError("use --write, or --check TRUSTED_BASE PROPOSED with a NUL-delimited diff on stdin")
    print("Credits are up to date.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError) as error:
        sys.exit(str(error))
