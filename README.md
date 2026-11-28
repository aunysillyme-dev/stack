# Stack

[![Stack review](https://github.com/aunysillyme-dev/stack/actions/workflows/checks.yml/badge.svg)](https://github.com/aunysillyme-dev/stack/actions/workflows/checks.yml)
[![License: CC BY 4.0 data, MIT code](https://img.shields.io/badge/license-CC%20BY%204.0%20data%20%2F%20MIT%20code-blue)](LICENSE.md)

**Stack is a directory of AI stacks for anything people build with AI: curated tools, models, and workflows as open JSON.** Design, video, compute, and agentic tools are the live stacks. Anyone can propose another.

[Browse the guides](https://aunysillyme.dev/stack/) · [Submit a workflow](CONTRIBUTING.md) · [Open an issue](https://github.com/aunysillyme-dev/stack/issues) · [Join a discussion](https://github.com/aunysillyme-dev/stack/discussions)

![stack trailer](docs/stack-trailer.gif)

Without: scattered blog posts, dead links and lists nobody updates.

With: curated stacks of tools, models and workflows for any kind of AI work, kept current by contributors.

## Contents

- [Taxonomy](#taxonomy)
- [Design](#design)
- [Video](#video)
- [Compute](#compute)
- [Agentic tools](#agentic-tools)
- [Make a music video from stills](#make-a-music-video-from-stills)
- [Use the collection as data](#use-the-collection-as-data)
- [Share and reuse a workflow](#share-and-reuse-a-workflow)
- [Common questions](#common-questions)
- [Read next](#read-next)
- [Credits](#credits)

## Taxonomy

Every catalog entry uses the same four fields: **name**, **link**, **one-line description**, and a **tag** of `free`, `freemium`, or `paid`. In JSON, those fields are `name`, `url` or `link`, `use` or `notes`, and `cost_class`. Older video rows may store `subscription` or `metered`. Both count as `paid` and land in `premium/`.

| Stack | What it covers | Start here |
| --- | --- | --- |
| [01 Design](01-design-stack/) | AI image, UI, brand, design-to-code, and the earlier 13 resource groups | [Design guide](https://aunysillyme.dev/stack/design/) · [README](01-design-stack/README.md) |
| [02 Video](02-video-stack/) | Generation, editing, upscaling, lip-sync, and end-to-end workflows | [Video guide](https://aunysillyme.dev/stack/video/) · [README](02-video-stack/README.md) |
| [03 Compute](03-compute-stack/) | GPU clouds and free or cheap inference APIs | [README](03-compute-stack/README.md) |
| [04 Agentic tools](04-agentic-stack/) | Coding agents, the Claude Agent SDK, MCP, and agent frameworks | [README](04-agentic-stack/README.md) |

| Stack | Core | Inventory |
| --- | --- | --- |
| [01 Design](01-design-stack/) | 35 tools and 5 workflows ([text](01-design-stack/canonical.md) · [JSON](01-design-stack/canonical.json)) | 319 resources ([inventory.md](01-design-stack/inventory.md) · [free/](01-design-stack/free/free.md) · [freemium/](01-design-stack/freemium/freemium.md) · [premium/](01-design-stack/premium/premium.md)) and [community/](01-design-stack/community/) |
| [02 Video](02-video-stack/) | 24 tools and 7 workflows ([text](02-video-stack/canonical.md) · [JSON](02-video-stack/canonical.json)) | 54 resources ([inventory.md](02-video-stack/inventory.md) · [free/](02-video-stack/free/free.md) · [freemium/](02-video-stack/freemium/freemium.md) · [premium/](02-video-stack/premium/premium.md)) and [community/](02-video-stack/community/) |
| [03 Compute](03-compute-stack/) | 19 tools and 2 workflows ([text](03-compute-stack/canonical.md) · [JSON](03-compute-stack/canonical.json)) | 19 resources ([inventory.md](03-compute-stack/inventory.md) · [free/](03-compute-stack/free/free.md) · [freemium/](03-compute-stack/freemium/freemium.md) · [premium/](03-compute-stack/premium/premium.md)) and [community/](03-compute-stack/community/) |
| [04 Agentic tools](04-agentic-stack/) | 18 tools and 2 workflows ([text](04-agentic-stack/canonical.md) · [JSON](04-agentic-stack/canonical.json)) | 18 resources ([inventory.md](04-agentic-stack/inventory.md) · [free/](04-agentic-stack/free/free.md) · [freemium/](04-agentic-stack/freemium/freemium.md) · [premium/](04-agentic-stack/premium/premium.md)) and [community/](04-agentic-stack/community/) |

## Design

AI image, UI, brand, and design-to-code tools sit with the original design inventory. Highlights:

- [v0](https://v0.app/): Vercel AI builder for designing and shipping full-stack web apps. `freemium`
- [Google Stitch](https://stitch.google.com/): Google AI UI generator for mobile and web application screens. `freemium`
- [Lovable](https://lovable.dev/): AI app builder that turns a prompt into hosted full-stack software. `freemium`
- [Leonardo.Ai](https://leonardo.ai/): Generative image and video platform for prompts, custom models, edits, and upscaling. `freemium`
- [Gemini Image](https://deepmind.google/models/gemini-image/): Google DeepMind page for the Gemini image model, also called Nano Banana. `freemium`
- [Looka](https://looka.com/): AI logo and brand-kit maker for colors, files, and marketing templates. `freemium`
- [Onlook](https://www.onlook.com/): Free local-first visual editor for building interfaces in code. `free`

The full 319-entry list, including every earlier resource, is in [01-design-stack/inventory.md](01-design-stack/inventory.md).

## Video

The original image-to-video inventory and the production workflows stay. Newer generation, editing, upscaling, and lip-sync tools are added beside them.

- [Veo](https://deepmind.google/models/veo/): Google DeepMind page for Veo 3.1 video generation. `freemium`
- [Kling AI](https://kling.ai/): Video and image studio for text, image, and reference prompts. `freemium`
- [Luma](https://lumalabs.ai/): Creative platform for video and image generation with Ray and Uni models. The site says to try it free. `freemium`
- [Wan 2.2](https://github.com/Wan-Video/Wan2.2): Open weights and code for the Wan 2.2 large-scale video model. `free`
- [Descript](https://www.descript.com/): Text-based AI editor for video and audio. The site says to try it free. `freemium`
- [Topaz Video](https://www.topazlabs.com/topaz-video): Desktop video enhancer for upscaling, smoothing, stabilizing, and sharpening footage. `paid`
- [Sync](https://sync.so/): Lip-sync and visual dubbing studio and API. `freemium`

The full 54-entry list is in [02-video-stack/inventory.md](02-video-stack/inventory.md).

## Compute

- [Modal](https://modal.com/): GPU and CPU cloud that bills per second. The pricing page includes $30 of monthly free credit. `freemium`
- [Groq](https://groq.com/): Fast inference platform for running models at low latency. `freemium`
- [Cerebras](https://www.cerebras.ai/inference): Fast inference API. The product page offers $5 of free credit on a new account. `freemium`
- [OpenRouter](https://openrouter.ai/): One API that routes prompts across many models and prices. `freemium`
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/): Serverless model inference on Cloudflare's network. `freemium`
- [Google AI Studio](https://aistudio.google.com/): Browser console for prompting and shipping with the Gemini API. `freemium`
- [NVIDIA NIM](https://build.nvidia.com/): Catalog for trying NVIDIA NIM model APIs. `freemium`

The full 19-entry list, including RunPod, Lambda, Paperspace, Lightning AI, Vast.ai, and CoreWeave, is in [03-compute-stack/README.md](03-compute-stack/README.md).

## Agentic tools

- [Claude Code](https://code.claude.com/docs/en/overview): Agentic coding tool that reads a repo, edits files, and runs commands. `freemium`
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): Specialized workers inside one Claude Code session. `freemium`
- [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams): Experimental teams of Claude Code sessions. Off unless enabled. `freemium`
- [Claude Code dynamic workflows](https://code.claude.com/docs/en/workflows): Scripted orchestration that runs many subagents and cross-checks their results. `freemium`
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview): Python and TypeScript library for the Claude Code agent loop. `freemium`
- [Model Context Protocol](https://modelcontextprotocol.io/): Open protocol for connecting agents to tools and data. `free`
- [Cursor](https://cursor.com/): AI coding agent and editor for handing tasks to agents inside a repository. `freemium`
- [Google ADK](https://adk.dev/): Open-source Agent Development Kit for building and deploying agents. `free`

Jules, Codex, Gemini CLI, LangGraph, CrewAI, AutoGen, OpenHands, and the listed MCP servers are in [04-agentic-stack/README.md](04-agentic-stack/README.md).

## Make a music video from stills

Start with a finished track. Mark the changes in the song, plan a shot for each section and create stills that keep the character and palette consistent. Animate the selected stills, check motion and facial continuity, then cut the clips to the mastered audio. [Follow the music-video walkthrough](https://aunysillyme.dev/stack/video/#music) or [read the steps in plain text](02-video-stack/canonical.md) ([JSON](02-video-stack/canonical.json)).

## Use the collection as data

Start with [the catalog](catalog.json). Each numbered stack folder (`01-design-stack/`, `02-video-stack/`, `03-compute-stack/`, `04-agentic-stack/`, and later stacks such as `05-image-stack/`) contains a `stack.json`, human-readable Markdown (`canonical.md`, `inventory.md`), machine-readable JSON (`canonical.json`, `inventory.json`), and `free/`, `freemium/`, and `premium/` subfolders with both `.md` and `.json`. These committed files can be read offline. Check current pricing and terms with the provider when choosing a model.

## Share and reuse a workflow

Start with [the template](templates/workflow.json). Record the inputs, tools, access, steps, output and how you verified it. Workflows can use free tools, paid tools or both. An accepted entry stays under its author’s GitHub handle. The [generated credits](#credits) describe each contributor’s work. [Contribution and credit instructions](CONTRIBUTING.md)

A maintainer can select a merged workflow for the separately published website guide and preserve its attribution there. See the [licenses for data and code](LICENSE.md) and the [contributor certification](CONTRIBUTOR-CERTIFICATION.md). Use [private vulnerability reporting](https://github.com/aunysillyme-dev/stack/security/advisories/new) for security reports.

## Common questions

### What are the best AI tools for video generation?

[02-video-stack/inventory.json](02-video-stack/inventory.json) records dated model and platform entries with access routes, costs and evaluation status, plus newer generation, editing, upscaling, and lip-sync pages. [02-video-stack/canonical.json](02-video-stack/canonical.json) shows which of them Auny uses and the added finishing workflows.

### Which AI tools help with animation?

Animation sits inside the video stack. Start with the animation steps in [02-video-stack/canonical.json](02-video-stack/canonical.json), then check the image-to-video entries in [02-video-stack/inventory.json](02-video-stack/inventory.json). Design motion tools are listed under "Animation, video & film" in [01-design-stack/inventory.json](01-design-stack/inventory.json).

### Which AI tools do designers use?

[01-design-stack/canonical.json](01-design-stack/canonical.json) lists 35 core tools and 5 workflows. [01-design-stack/inventory.json](01-design-stack/inventory.json) adds 319 entries across 15 categories, including AI image, UI builders, brand tools, and design-to-code.

### Which AI tools help with UI design?

UI sits inside the design stack. The web interface workflow in [01-design-stack/README.md](01-design-stack/README.md) covers layout, tokens, accessible controls and checks. The inventory has "UI libraries & systems", "UI and website builders", and "Galleries & UI inspiration".

### Where do I run a model?

[03-compute-stack/inventory.json](03-compute-stack/inventory.json) lists GPU clouds and inference APIs, with a `free`, `freemium`, or `paid` tag on each one.

### Which tools run coding agents?

[04-agentic-stack/inventory.json](04-agentic-stack/inventory.json) lists Claude Code, the Agent SDK, MCP, Gemini CLI, Google ADK, Jules, Codex, Cursor, and frameworks such as LangGraph, CrewAI, AutoGen, and OpenHands.

### How do I submit a workflow?

Copy [templates/workflow.json](templates/workflow.json), fill in the inputs, tools, steps and how you verified the result, and open a pull request following [CONTRIBUTING.md](CONTRIBUTING.md).

### Can I add a new kind of stack?

Yes. Follow [Propose a new stack](CONTRIBUTING.md#propose-a-new-stack) and open a [New stack issue](https://github.com/aunysillyme-dev/stack/issues/new?template=new-stack.yml).

## Read next

- [Site guides](https://aunysillyme.dev/stack/): illustrated video and design guides.
- [CONTRIBUTING.md](CONTRIBUTING.md): workflow format, entry fields, credit and certification.
- [CHANGELOG.md](CHANGELOG.md): what changed and when.

## License

Data is CC BY 4.0 and code is MIT. See [LICENSE.md](LICENSE.md).

For agents: start with [AGENTS.md](AGENTS.md) and [llms.txt](llms.txt).

<!-- credits:start -->
## Credits

- [@aunysillyme](https://github.com/aunysillyme): Curated the [Video tools and workflows](02-video-stack/canonical.json), including the production pipeline and creative techniques.
- [@aunysillyme](https://github.com/aunysillyme): Curated the [Design tools and workflows](01-design-stack/canonical.json) and the [design resource inventory](01-design-stack/inventory.json).
<!-- credits:end -->
