# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Validate the curated catalog and contributor documents without fetching any URLs."""

import ipaddress
import json
import re
import sys
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def read(path):
    require(path.is_file() and not path.is_symlink(), f"expected regular file: {path}")
    require(path.stat().st_size <= 256_000, f"file exceeds 256 KB: {path}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def unique_keys(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, f"duplicate JSON field: {key}")
        obj[key] = value
    return obj


def fields(obj, names):
    require(isinstance(obj, dict) and set(obj) == set(names.split()), "expected fields: " + names)


def string(value):
    require(isinstance(value, str) and value.strip(), "expected nonempty text")


def sequence(items, check):
    require(isinstance(items, list) and items, "expected a nonempty list")
    for item in items:
        check(item)


def url(value):
    string(value)
    parsed = urlsplit(value)
    host = (parsed.hostname or "").rstrip(".").lower()
    try:
        ipaddress.ip_address(host)
        is_ip = True
    except ValueError:
        is_ip = False
    labels = host.split(".")
    hostname = (len(host) <= 253 and len(labels) >= 2 and all(
        1 <= len(label) <= 63 and re.fullmatch(r"[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?", label)
        for label in labels))
    # Browsers also interpret decimal, octal, hexadecimal and shortened numeric
    # hosts as IP addresses. A numeric final label is sufficient to reject them.
    numeric_end = re.fullmatch(r"(?:[0-9]+|0x[0-9a-f]*)", labels[-1]) is not None
    require(hostname and not is_ip and not numeric_end
            and not host.endswith((".localhost", ".local", ".internal", ".test"))
            and parsed.scheme == "https" and parsed.hostname and not parsed.username
            and not parsed.password and not re.search(r"[\s\\]", value), "expected a public HTTPS source link")


def day(value):
    string(value)
    reviewed = date.fromisoformat(value)
    require(reviewed.isoformat() == value, "expected YYYY-MM-DD")
    require(reviewed <= datetime.now(timezone.utc).date(), "review date cannot be in the future (UTC)")


def tool(obj):
    fields(obj, "name url access")
    string(obj["name"])
    url(obj["url"])
    string(obj["access"])


def workflow(obj, handle):
    require(isinstance(obj, dict), "expected workflow object")
    fields({k: v for k, v in obj.items() if k != "credits"},
           "author title purpose reviewed inputs tools steps output verification")
    require(obj["author"] == handle, "author must match the contributor folder")
    if "credits" in obj:
        def credit(item):
            fields(item, "handle contribution")
            require(isinstance(item["handle"], str) and len(item["handle"]) <= 39
                    and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item["handle"]),
                    "invalid credit handle")
            string(item["contribution"])
            require(len(item["contribution"]) <= 300 and
                    not any(unicodedata.category(c).startswith("C") for c in item["contribution"]),
                    "credit contribution must be a single line of at most 300 characters")
        sequence(obj["credits"], credit)
        handles = [item["handle"] for item in obj["credits"]]
        require(len(handles) == len(set(handles)) and handle in handles,
                "credits must include the author once and have unique handles")
    for key in ("title", "purpose", "output", "verification"):
        string(obj[key])
    day(obj["reviewed"])
    sequence(obj["inputs"], string)
    sequence(obj["steps"], string)
    sequence(obj["tools"], tool)


def curated(obj):
    fields(obj, "author reviewed source tools workflows")
    require(obj["author"] == "aunysillyme", "unexpected curated author")
    url(obj["source"])
    day(obj["reviewed"])
    for item in obj["tools"]:
        fields(item, "name url use")
        string(item["name"])
        url(item["url"])
        string(item["use"])
    for item in obj["workflows"]:
        fields(item, "name source steps")
        string(item["name"])
        url(item["source"])
        sequence(item["steps"], string)
    require(isinstance(obj["tools"], list) and obj["tools"] and isinstance(obj["workflows"], list)
            and obj["workflows"], "curated category needs tools and workflows")


def inventory(obj):
    fields(obj, "source reviewed entries")
    url(obj["source"])
    day(obj["reviewed"])
    def entry(item):
        fields(item, "name type route status cost_class model_id notes link")
        for field in ("name", "type", "route", "status", "cost_class", "notes"):
            string(item[field])
        require(isinstance(item["model_id"], str), "model ID must be a string")
        url(item["link"])
    sequence(obj["entries"], entry)


def category(path):
    require(path.is_dir() and re.fullmatch(r"[0-9]{2}-[a-z0-9-]+-stack", path.name), "invalid category")
    for entry in path.rglob("*"):
        require(not entry.is_symlink(), f"symlink: {entry}")
    obj = read(path / "stack.json")
    fields(obj, "id title status guide canonical inventory community")
    require(obj["id"] == path.name and obj["community"] == "community/", "category paths mismatch")
    string(obj["title"])
    require(obj["status"] in ("planned", "published"), "invalid category status")
    allowed = {"README.md", "stack.json", "community"}
    if obj["status"] == "published":
        if obj["guide"] is not None:
            url(obj["guide"])
        require(obj["canonical"] == "canonical.json", "published category requires canonical.json")
        curated(read(path / "canonical.json"))
        require((path / "canonical.md").is_file() and (path / "canonical.md").stat().st_size > 0, "missing canonical.md")
        allowed |= {"canonical.json", "canonical.md"}
    else:
        require(obj["guide"] is None and obj["canonical"] is None, "planned category cannot advertise a guide")
    if obj["inventory"] is not None:
        require(obj["inventory"] == "inventory.json", "unexpected inventory path")
        inventory(read(path / "inventory.json"))
        require((path / "inventory.md").is_file() and (path / "inventory.md").stat().st_size > 0, "missing inventory.md")
        allowed |= {"inventory.json", "inventory.md", "free", "freemium", "premium"}
        for tier in ("free", "freemium", "premium"):
            tier_dir = path / tier
            require(tier_dir.is_dir(), f"missing tier directory: {tier_dir}")
            require({p.name for p in tier_dir.iterdir()} == {f"{tier}.json", f"{tier}.md"}, f"unexpected tier files: {tier_dir}")
            tier_obj = read(tier_dir / f"{tier}.json")
            fields(tier_obj, "tier source reviewed entries")
            require(tier_obj["tier"] == tier and isinstance(tier_obj["entries"], list), f"invalid tier json: {tier_dir}")
            require((tier_dir / f"{tier}.md").is_file() and (tier_dir / f"{tier}.md").stat().st_size > 0, f"missing tier md: {tier_dir}")
    require({p.name for p in path.iterdir()} == allowed, f"unexpected or missing category files: {path}")
    for author in (path / "community").iterdir():
        if author.name == "README.md" and author.is_file():
            continue
        require(author.is_dir() and len(author.name) <= 39 and re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", author.name), f"invalid contributor handle: {author.name}")
        require(any(author.iterdir()), f"empty contributor directory: {author.name}")
        for item in author.iterdir():
            require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.json", item.name), f"invalid entry path: {item}")
            try:
                workflow(read(item), author.name)
            except (ValueError, TypeError, KeyError, OSError) as error:
                raise Invalid(f"{item}: {error}") from error


def category_names(root):
    names = read(root / "catalog.json")
    require(isinstance(names, list) and names, "catalog.json must list category names")
    reserved = {"scripts", "tests", "templates", "stacks", "licenses", "docs"}
    for name in names:
        require(isinstance(name, str) and re.fullmatch(r"[0-9]{2}-[a-z0-9-]+-stack", name)
                and name not in reserved, "invalid root category name")
    require(len(set(names)) == len(names), "duplicate root category")
    require({"01-design-stack", "02-video-stack"} <= set(names), "missing a required root category")
    return names


def validate(root):
    names = category_names(root)
    require(not (root / "stacks").exists() and not (root / "stacks").is_symlink(),
            "obsolete nested category directory")
    unexpected = [p.name for p in root.iterdir() if not p.is_symlink() and p.is_dir()
                  and (p / "stack.json").exists() and p.name not in names]
    require(not unexpected, "unregistered root categories: " + ", ".join(unexpected))
    categories = [root / name for name in names]
    for folder in categories:
        require(not folder.is_symlink(), f"symlink: {folder}")
        try:
            category(folder)
        except (ValueError, TypeError, KeyError, OSError) as error:
            raise Invalid(f"{folder}: {error}") from error
    return len(categories)


if __name__ == "__main__":
    try:
        print(f"Validated {validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd())} stack categories.")
    except (ValueError, OSError, TypeError, KeyError) as error:
        sys.exit(str(error))
