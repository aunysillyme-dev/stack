# Working on Stack

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing. It defines contribution scope, rights checks and credit. Maintainers also follow [the review guide](.github/MAINTAINING.md).

- Look up categories in [catalog.json](catalog.json). Keep each category at the repository root. Follow its `stack.json` to find the curated files and community directory.
- Use [templates/workflow.json](templates/workflow.json) for community submissions. Preserve authorship, sources, review dates and access terms. Read the [licenses](LICENSE.md) and [contributor certification](CONTRIBUTOR-CERTIFICATION.md) when evaluating reuse and rights.
- In a community PR, edit only workflow JSON directly inside `<category>/community/<your-github-login>/` and the generated README credit block. Run `python3 scripts/credits.py --write` to update that block.
- Run `python3 scripts/sync_tiers.py --write` after editing `canonical.json` or `inventory.json` to keep `canonical.md`, `inventory.md`, and `free/`, `freemium/`, `premium/` `.json`/`.md` files in sync.
- Run `python3 scripts/validate.py`, `python3 scripts/sync_tiers.py --check`, and `python3 -m unittest discover -s tests -v`. All work offline with the Python standard library.
- Maintainers updating curated Design, Video, Compute, or Agentic data keep `canonical.json`, `inventory.json`, their Markdown and tier outputs, the category `README.md` (and source hashes in [Video](02-video-stack/README.md) when snapshots apply) in sync with [CONTRIBUTING.md](CONTRIBUTING.md). Website publication has a separate editorial review.
