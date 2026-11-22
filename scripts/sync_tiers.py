# SPDX-FileCopyrightText: Auny LLC and contributors
# SPDX-License-Identifier: MIT
"""Generate and verify Markdown companions and free/freemium/premium splits for each stack."""

import json
import sys
from pathlib import Path

TIER_ORDER = ("free", "freemium", "premium")

TIER_DESCRIPTIONS = {
    "free": "Free and open-access tools and resources.",
    "freemium": "Tools and platforms with a free tier alongside paid upgrades.",
    "premium": "Paid, subscription, metered API, or paywalled resources.",
}


def tier_for(cost_class: str) -> str:
    value = cost_class.strip().lower()
    if value == "free":
        return "free"
    if value == "freemium":
        return "freemium"
    if value in ("paid", "subscription", "metered"):
        return "premium"
    raise ValueError(f"Unsupported cost_class: {cost_class}")


def render_canonical_md(title: str, canonical: dict) -> str:
    lines = [
        f"# {title} stack: core tools and workflows",
        "",
        f"Curated by @{canonical['author']} · Reviewed {canonical['reviewed']}",
        "",
        f"Source: {canonical['source']}",
        "",
        f"## Core tools ({len(canonical['tools'])})",
        "",
    ]
    for tool in canonical["tools"]:
        lines.append(f"- **[{tool['name']}]({tool['url']}):** {tool['use']}")
    lines.extend(["", f"## Workflows ({len(canonical['workflows'])})", ""])
    for wf in canonical["workflows"]:
        lines.append(f"### {wf['name']}")
        lines.append("")
        lines.append(f"Source: {wf['source']}")
        lines.append("")
        for idx, step in enumerate(wf["steps"], 1):
            lines.append(f"{idx}. {step}")
        lines.append("")
    return "\n".join(lines)


def render_entries_md(heading: str, intro: str, source: str, reviewed: str, entries: list[dict], stack_name: str) -> str:
    lines = [
        f"# {heading}",
        "",
        intro,
        "",
        f"Reviewed {reviewed} · {len(entries)} entries · Source: {source}",
        "",
    ]
    if not entries:
        lines.extend([
            f"No entries in `{stack_name}/inventory.json` are currently classified in this tier.",
            "",
            f"Check [{stack_name}/canonical.md](../canonical.md) for core tools and [{stack_name}/inventory.md](../inventory.md) for all recorded entries.",
            "",
        ])
        return "\n".join(lines)

    for entry in entries:
        model_note = f" (`{entry['model_id']}`)" if entry.get("model_id") else ""
        lines.append(
            f"- **[{entry['name']}]({entry['link']})**{model_note} — "
            f"{entry['route']} · {entry['type']} · {entry['status']} (`{entry['cost_class']}`): {entry['notes']}"
        )
    lines.append("")
    return "\n".join(lines)


def expected_outputs(root: Path) -> dict[Path, str]:
    names = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    outputs: dict[Path, str] = {}
    for name in names:
        folder = root / name
        meta = json.loads((folder / "stack.json").read_text(encoding="utf-8"))
        title = meta["title"]

        if meta.get("canonical"):
            canonical = json.loads((folder / meta["canonical"]).read_text(encoding="utf-8"))
            outputs[folder / "canonical.md"] = render_canonical_md(title, canonical)

        if meta.get("inventory"):
            inv = json.loads((folder / meta["inventory"]).read_text(encoding="utf-8"))
            entries = inv["entries"]
            # Notice no em dashes in rendered markdown
            inv_lines = [
                f"# {title} stack: full inventory",
                "",
                f"Plain-text index of all {len(entries)} recorded resources in `{name}/inventory.json`.",
                "",
                f"Reviewed {inv['reviewed']} · Source: {inv['source']}",
                "",
                "- [Free resources](free/free.md)",
                "- [Freemium resources](freemium/freemium.md)",
                "- [Premium / paid resources](premium/premium.md)",
                "",
                "| Name | Category / Route | Type | Status | Cost class | Notes |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
            for entry in entries:
                safe_name = entry["name"].replace("|", "\\|")
                safe_route = entry["route"].replace("|", "\\|")
                safe_type = entry["type"].replace("|", "\\|")
                safe_status = entry["status"].replace("|", "\\|")
                safe_notes = entry["notes"].replace("|", "\\|")
                inv_lines.append(
                    f"| [{safe_name}]({entry['link']}) | {safe_route} | {safe_type} | {safe_status} | `{entry['cost_class']}` | {safe_notes} |"
                )
            inv_lines.append("")
            outputs[folder / "inventory.md"] = "\n".join(inv_lines)

            buckets = {tier: [] for tier in TIER_ORDER}
            for entry in entries:
                buckets[tier_for(entry["cost_class"])].append(entry)

            for tier in TIER_ORDER:
                tier_entries = buckets[tier]
                tier_obj = {
                    "tier": tier,
                    "source": inv["source"],
                    "reviewed": inv["reviewed"],
                    "entries": tier_entries,
                }
                outputs[folder / tier / f"{tier}.json"] = json.dumps(tier_obj, indent=2) + "\n"

                md_lines = [
                    f"# {title} stack: {tier} resources",
                    "",
                    TIER_DESCRIPTIONS[tier],
                    "",
                    f"Reviewed {inv['reviewed']} · {len(tier_entries)} entries · Source: {inv['source']}",
                    "",
                ]
                if not tier_entries:
                    md_lines.extend([
                        f"No entries in `{name}/inventory.json` are currently classified as `{tier}`.",
                        "",
                        f"Check [canonical.md](../canonical.md) for core tools and [inventory.md](../inventory.md) for all entries.",
                        "",
                    ])
                else:
                    for entry in tier_entries:
                        model_note = f" (`{entry['model_id']}`)" if entry.get("model_id") else ""
                        md_lines.append(
                            f"- **[{entry['name']}]({entry['link']})**{model_note}: "
                            f"{entry['route']} | {entry['type']} | {entry['status']} (`{entry['cost_class']}`): {entry['notes']}"
                        )
                    md_lines.append("")
                outputs[folder / tier / f"{tier}.md"] = "\n".join(md_lines)
    return outputs


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] not in ("--write", "--check"):
        raise SystemExit("Usage: python3 scripts/sync_tiers.py --write|--check [ROOT]")
    mode = args[0]
    root = Path(args[1]) if len(args) > 1 else Path.cwd()
    outputs = expected_outputs(root)

    if mode == "--write":
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(f"Wrote {len(outputs)} tier and markdown files.")
        return

    stale = []
    for path, content in outputs.items():
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            stale.append(str(path.relative_to(root)))
    if stale:
        raise SystemExit("Out-of-date tier/markdown files: " + ", ".join(stale))
    print(f"Verified {len(outputs)} tier and markdown files.")


if __name__ == "__main__":
    main()
