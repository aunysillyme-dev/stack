# Video stack

[Read Auny’s complete guide](https://aunysillyme.dev/stack/video/) for the storyboards, prompts, finishing checklist and model comparison.

- **Tools and workflows:** [canonical.md](canonical.md) (plain text) · [canonical.json](canonical.json) includes image creation, character continuity, animation, editing, lip-sync, upscaling, and finishing (24 tools, 7 workflows).
- **Inventory (54):** [inventory.md](inventory.md) (plain text) · [inventory.json](inventory.json) keeps the guide’s 28 dated model and platform entries, including access routes, costs and evaluation status, and adds 26 checked product pages. “Evaluating” records a candidate. “Parked” records a choice set aside.
- **Resources by tier:** [free/](free/free.md) (`4`, [JSON](free/free.json)) · [freemium/](freemium/freemium.md) (`18`, [JSON](freemium/freemium.json)) · [premium/](premium/premium.md) (`32`, [JSON](premium/premium.json)). Older rows may use `subscription` or `metered`. Both sit in premium, and the public tag for them is `paid`.
- [Community workflows](community/) are organized by contributor.
- Access information is recorded per route in the inventory. A paid hosted route and downloadable weights can have different terms. Check the provider before you use either.
- [Category metadata](stack.json) points software to those files.

### Source snapshot

Captured on November 18, 2026. The JSON files are committed snapshots. Reading and validating the collection works offline.

| Input | SHA-256 |
| --- | --- |
| [Video guide](https://aunysillyme.dev/stack/video/) | `a9bdd4789f9557342c81a4f80e24f158cbc5dbb14e25ba852df69ec387672f6a` |
| [Image-to-video CSV](https://aunysillyme.dev/stack/video/i2v-model-inventory.csv) | `89c53d5f6bd507657a318a752cd54578117c61530a9af12689692ae7d6c6f01b` |

The hash above covers the November 18 snapshot only. Entries added on November 28, 2026 were checked by opening each official product page. They are not rows in that CSV.

## Generation, editing, upscaling, and lip-sync

Each new entry is a name, a link, a one-line description, and a `free`, `freemium`, or `paid` tag.

### Video generation

- [Runway](https://runway.com/): Runway's current product home for AI video and content tools. The homepage offers an enterprise trial. `paid`
- [Kling AI](https://kling.ai/): Video and image studio for text, image, and reference prompts. `freemium`
- [Luma](https://lumalabs.ai/): Creative platform for video and image generation with Ray and Uni models. The site says to try it free. `freemium`
- [Pika](https://pika.art/): Creative platform for AI video, image, and audio, including hosted routes to other generators. `freemium`
- [Veo](https://deepmind.google/models/veo/): Google DeepMind page for Veo 3.1 video generation. `freemium`
- [Hailuo](https://hailuoai.video/): MiniMax video and image studio. The homepage currently features MiniMax H3. `freemium`
- [Seedance](https://seed.bytedance.com/en/seedance): Official ByteDance Seedance page, including Seedance 1.0 video examples and benchmarks. `freemium`
- [Wan 2.2](https://github.com/Wan-Video/Wan2.2): Open weights and code for the Wan 2.2 large-scale video model. `free`
- [Vidu](https://www.vidu.com/): AI video generator for text, image, and reference workflows. `freemium`
- [Viggle](https://viggle.ai/): Video and 3D workspace for remakes, scenes, characters, and motion. `freemium`

### Editing

- [Descript](https://www.descript.com/): Text-based AI editor for video and audio. The site says to try it free. `freemium`
- [Kapwing](https://www.kapwing.com/): Browser editor that generates and edits videos from a prompt. `freemium`
- [Opus Clip](https://www.opus.pro/): Turns long videos into short clips and can publish them to social platforms. `freemium`
- [VEED](https://www.veed.io/): Video workspace for generation, editing, dubbing, and subtitles. `freemium`
- [Captions](https://captions.ai/): AI video generator and editor aimed at ready-to-share social cuts. `freemium`
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve): Blackmagic editor and color tool with a free version and a paid Studio upgrade. `freemium`
- [invideo](https://invideo.io/): AI video editor for creating and revising clips in the browser. `freemium`

### Upscaling

- [Topaz Video](https://www.topazlabs.com/topaz-video): Desktop video enhancer for upscaling, smoothing, stabilizing, and sharpening footage. `paid`
- [Magnific](https://www.magnific.com/): Creative platform whose tools include video and image upscaling plus generation. `freemium`
- [Upscayl](https://github.com/upscayl/upscayl): Free and open-source desktop AI image upscaler. `free`
- [Video2X](https://github.com/k4yt3x/video2x): Open-source framework for machine-learning video super-resolution and frame interpolation. `free`

### Lip-sync

- [Sync](https://sync.so/): Lip-sync and visual dubbing studio and API. `freemium`
- [HeyGen](https://www.heygen.com/): Avatar and talking-video platform. The site says to try it free. `freemium`
- [LivePortrait](https://github.com/KlingAIResearch/LivePortrait): Open-source portrait animation project, now under Kling AI Research. `free`
- [D-ID](https://www.d-id.com/): Platform for AI-generated presenter and talking-head video. `paid`
- [Synthesia](https://www.synthesia.io/): Business AI video platform for presenter-style training and communication videos. `paid`

Two added workflows live in [canonical.json](canonical.json): finish a talking shot with lip-sync and upscale, and cut short clips from a long generation. The earlier production, still, character, music, and storyboard workflows are unchanged.
