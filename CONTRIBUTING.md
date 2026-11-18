# Share a stack

Document a workflow you use. Include its purpose, inputs, tools, steps, output and a way for another person to check the result. Free, paid and mixed workflows are welcome. Describe each tool’s access route and costs as accurately as your experience allows.

1. Fork the repository and copy [the JSON template](templates/workflow.json) into `stacks/<category>/community/<your-github-login>/<workflow-name>.json`. Use your lowercase GitHub login and a short lowercase filename with hyphens.
2. Replace the example values with your own. Use an ISO date for the last review that is no later than today in UTC, link each tool to its official source by hostname (not an IP address), and say what you actually tried. Link an example if you own it or its creator has published it for viewing.
3. Open a pull request. Link the contribution to your GitHub profile, identify coauthors and outside material, and complete the rights and [CLA](CLA.md) statements in the PR template.
4. A maintainer checks attribution, sources, accuracy, rights and placement. Update your entry through a new pull request when a tool or workflow changes.

### Rights and credit

Submit original descriptions and data you can license. For a group submission, identify every rights holder and arrange their assent with a maintainer before merge. An employer’s material requires permission from someone authorized to grant it. Keep client details, credentials and unpublished personal material out of every file and its history. Link to official products, media or examples. This collection accepts text and links only.

Outside contributors may change only JSON workflow files directly inside their own lowercase login folder in an existing category. The scope check uses the pull request author, checks both paths of a rename, and rejects moves between folders. Because Git may report an edited move as a deletion and an addition, outside contributors cannot combine additions and deletions across different folders in one PR. It does not grant permission to edit another author’s work. Authors keep their bylines. A maintainer compares the folder to the contributor’s GitHub profile, checks permission from coauthors and verifies that a community submission contains only its own data. Maintainers review all changes outside that folder separately. The validator checks the author field against the folder name. It cannot establish identity or ownership.

### Updating the guide and curated data

Outside contributors should open an issue describing a proposed curated correction, with its source and the relevant location. A maintainer reviews the source and submits any accepted correction in a maintainer-authored PR. The trusted scope helper recognizes the repository owner `aunysillyme` as a maintainer; changes to that list require owner review. The maintainer route also covers repository maintenance. It does not replace source, attribution, rights or agreement review, including manual agreement from any other rights holders.

1. For curated Video data, the maintainer links the source, describes the change and updates the review date when verifying `stacks/video/canonical.json` or `inventory.json`.
2. If the published guide or CSV changes, compare the affected text or rows with the repository snapshot, update the matching data in the same PR, and refresh the source SHA-256 in [the Video README](stacks/video/README.md).
3. Merging changes updates this repository. To feature a community workflow or amend the website guide, a maintainer selects it, preserves its credit and license, then submits the change in the website’s separate editorial and deployment process.

### Check a submission

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` from the checkout. Both use the Python standard library. The check validates JSON fields, category and contributor paths, and the format of source URLs. The GitHub workflow uses the base revision’s validator and scope helper on the tested merge commit, and runs the agreement check for every PR, including maintainer PRs. For the PR introducing this helper, the preceding base revision has no helper, so this new scope step cannot pass until the helper is in the base; maintainers must review that bootstrap separately. The new validation rules likewise take effect after they reach the base. Requiring them for merges and requiring owner review, especially for workflow and policy changes, are separate repository settings. The PR workflow itself can be changed by a PR, so these settings and review remain necessary. Before accepting public submissions, configure and verify required code-owner approval and required checks on the default branch. A pull request can edit its own workflow definition. Test with a fork that changes a workflow and confirm it cannot merge without a maintainer approving the actual changes. An organization-controlled required workflow is another way to protect the check definition. A maintainer checks that links resolve to the claimed sources, that dates and costs are credible, and that the contributor controls the submitted handle.
