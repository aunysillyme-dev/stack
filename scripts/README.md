# Scripts

Validation, generation, and contribution-check scripts used locally and in CI.

- [validate.py](validate.py): validates `catalog.json`, stack metadata, `canonical.json`, `inventory.json`, Markdown companions, tier subfolders, and community workflows. Inventory rows use name, link, a one-line description, and a `free`, `freemium`, or `paid` tag (`subscription` and `metered` remain valid on older video rows and count as paid).
- [sync_tiers.py](sync_tiers.py): generates and verifies `canonical.md`, `inventory.md`, and `free/`, `freemium/`, `premium/` JSON, Markdown, and README files (`--write` / `--check`)
- [check_contribution.py](check_contribution.py): checks PR file scope against `PR_AUTHOR` and [maintainers.txt](maintainers.txt)
- [check_certification.py](check_certification.py): checks contributor certification requirements on PRs
- [credits.py](credits.py): updates and verifies [CREDITS.md](../CREDITS.md) against workflow `credits` entries
- [maintainers.txt](maintainers.txt): maintainer GitHub handles allowed to edit core stack files
