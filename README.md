# Stack

[![Stack review](https://github.com/aunysillyme-dev/stack/actions/workflows/checks.yml/badge.svg)](https://github.com/aunysillyme-dev/stack/actions/workflows/checks.yml)
[![License: CC BY 4.0 data, MIT code](https://img.shields.io/badge/license-CC%20BY%204.0%20data%20%2F%20MIT%20code-blue)](LICENSE.md)

**Stack is a growing directory of AI stacks for anything people build with AI: curated tools, models and workflows as open JSON. Video and design are the first two live stacks, compute and more are coming, and anyone can propose a new stack.** Start with the video or design stack, share a workflow, or propose a new stack.

[Browse the guides](https://aunysillyme.dev/stack/) · [Submit a workflow](CONTRIBUTING.md) · [Open an issue](https://github.com/aunysillyme-dev/stack/issues) · [Join a discussion](https://github.com/aunysillyme-dev/stack/discussions)

![stack trailer](docs/stack-trailer.gif)

Without: scattered blog posts, dead links and lists nobody updates.

With: curated stacks of tools, models and workflows for any kind of AI work, kept current by contributors.

## Choose a stack

| Stack | Start here | What’s available |
| --- | --- | --- |
| [Video](video/) | [Read the video guide](https://aunysillyme.dev/stack/video/) | Auny’s tools and step-by-step workflows for storyboarding, consistent characters, animation and editing. The [model inventory](video/inventory.json) records dated access routes and evaluation notes. |
| [Design](design/) | [Read the design guide](https://aunysillyme.dev/stack/design/) | Auny’s 26 core free/freemium tools, 4 workflows and 291-entry [resource inventory](design/inventory.json) across 13 categories, plus open [community submissions](design/community/). |

## Make a music video from stills

![Video Stack, from idea to finished video. A practical guide by Auny.](https://aunysillyme.dev/assets/video-stack-preview.png)

Start with a finished track. Mark the changes in the song, plan a shot for each section and create stills that keep the character and palette consistent. Animate the selected stills, check motion and facial continuity, then cut the clips to the mastered audio. [Follow the music-video walkthrough](https://aunysillyme.dev/stack/video/#music) or [read the steps as JSON](video/canonical.json).

## Use the collection as data

Start with [the catalog](catalog.json). Each listed folder contains a `stack.json` with its publication status and the paths available for that category. For example, [Video’s metadata](video/stack.json) points to [curated workflows](video/canonical.json), the model inventory and the [community folder](video/community/). These committed files can be read offline. Check current pricing and terms with the provider when choosing a model.

## Share and reuse a workflow

Start with [the template](templates/workflow.json). Record the inputs, tools, access, steps, output and how you verified it. Workflows can use free tools, paid tools or both. An accepted entry stays under its author’s GitHub handle. The [generated credits](#credits) describe each contributor’s work. [Contribution and credit instructions](CONTRIBUTING.md)

A maintainer can select a merged workflow for the separately published website guide and preserve its attribution there. See the [licenses for data and code](LICENSE.md) and the [contributor certification](CONTRIBUTOR-CERTIFICATION.md). Use [private vulnerability reporting](https://github.com/aunysillyme-dev/stack/security/advisories/new) for security reports.

## Common questions

### What are the best AI tools for video generation?

[video/inventory.json](video/inventory.json) records dated model and platform entries with access routes, costs and evaluation status. [video/canonical.json](video/canonical.json) shows which of them Auny uses and in what order.

### Which AI tools help with animation?

Animation sits inside the video stack. Start with the animation steps in [video/canonical.json](video/canonical.json), then check the image-to-video entries in [video/inventory.json](video/inventory.json). Design motion tools are listed under "Animation, video & film" in [design/inventory.json](design/inventory.json).

### Which AI tools do designers use?

[design/canonical.json](design/canonical.json) lists 26 core free and freemium tools with 4 workflows. [design/inventory.json](design/inventory.json) adds 291 entries across 13 categories, including AI image and design generation.

### Which AI tools help with UI design?

UI sits inside the design stack. The web interface workflow in [design/README.md](design/README.md) covers layout, tokens, accessible controls and checks. The inventory has "UI libraries & systems" and "Galleries & UI inspiration" categories.

### How do I submit a workflow?

Copy [templates/workflow.json](templates/workflow.json), fill in the inputs, tools, steps and how you verified the result, and open a pull request following [CONTRIBUTING.md](CONTRIBUTING.md).

### Can I add a new kind of stack?

Yes. Follow [Propose a new stack](CONTRIBUTING.md#propose-a-new-stack) and open a [New stack issue](https://github.com/aunysillyme-dev/stack/issues/new?template=new-stack.yml).

## Read next

- [Site guides](https://aunysillyme.dev/stack/): illustrated video and design guides.
- [CONTRIBUTING.md](CONTRIBUTING.md): workflow format, credit and certification.
- [CHANGELOG.md](CHANGELOG.md): what changed and when.

## License

Data is CC BY 4.0 and code is MIT. See [LICENSE.md](LICENSE.md).

For agents: start with [AGENTS.md](AGENTS.md) and [llms.txt](llms.txt).

<!-- credits:start -->
## Credits

- [@aunysillyme](https://github.com/aunysillyme): Curated the [Video tools and workflows](video/canonical.json), including the production pipeline and creative techniques.
- [@aunysillyme](https://github.com/aunysillyme): Curated the [Design tools and workflows](design/canonical.json) and the [design resource inventory](design/inventory.json).
<!-- credits:end -->
