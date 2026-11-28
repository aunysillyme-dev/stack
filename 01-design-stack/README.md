# Design stack

[Read Auny's Design Stack guide](https://aunysillyme.dev/stack/design/) for the searchable web directory and workflow overview.

Auny's curated design tools, step-by-step workflows and 319-entry resource inventory organized across 15 categories. Every inventory entry is a name, a link, a one-line description, and a `free`, `freemium`, or `paid` tag.

- **Core tools and workflows:** [canonical.md](canonical.md) (plain text) · [canonical.json](canonical.json) (35 tools, 5 workflows)
- **Full resource inventory (319):** [inventory.md](inventory.md) (plain text) · [inventory.json](inventory.json)
- **Resources by tier:** [free/](free/free.md) (`248`, [JSON](free/free.json)) · [freemium/](freemium/freemium.md) (`54`, [JSON](freemium/freemium.json)) · [premium/](premium/premium.md) (`17`, [JSON](premium/premium.json))
- **Community workflows:** [community/](community/) organized by GitHub login. [Submit a workflow](../CONTRIBUTING.md).
- **Category metadata:** [stack.json](stack.json)

## How a design job runs

1. Research before drawing. Collect the same artifact from 8 to 12 peer brands alongside recent award-winning work in the category, then record what holds up, what fails and which cliches to skip.
2. Choose directions by mechanism. Propose directions that differ in how they work (type-led system, structural metaphor or interactive behavior) rather than one idea styled three ways, and tie every brief adjective to something observable.
3. Build in layers. Separate background surfaces, environment texture, hero subjects, annotations, typography and brand marks so each layer renders and scales cleanly before compositing depth and contrast.
4. Render and look. Export and inspect real desktop, tablet and mobile views yourself before sharing; zoom in on generated imagery and vector exports to catch anatomical, text or alignment defects.
5. Pass the gate. Verify core message, contrast ratios (WCAG 2.2 AA), type ramp, spacing tokens and asset licenses first; verify brand marks at 16px, in monochrome, blurred and against unintended second readings.

## Web interface workflow

1. Benchmark layout patterns and typography pairings against curated web galleries (Minimal Gallery, Footer.design, CTA Gallery) and pull relevant DESIGN.md rules before writing markup.
2. Lock color, spacing and type tokens first using Radix 12-step contrast semantics, OKLCH lightness checks and Style Dictionary or CSS custom properties.
3. Assemble accessible controls from headless and copy-owned primitives (Radix UI Primitives, shadcn/ui, Astryx, 21st.dev) and add subtle state transitions (transitions.dev, NumberFlow, Lenis) only where they clarify cause and effect.
4. Render full-page desktop and mobile screenshots in both light and dark modes with Playwright at real target viewports.
5. Run automated WCAG checks with axe-core alongside an anti-slop review pass (Impeccable, unslop) before shipping or publishing.

## Brand and token workflow

1. Audit peer brand guidelines and search USPTO Design Search Codes to confirm the visual direction does not collide with crowded category shapes.
2. Draft distinctive vector mark concepts in Penpot, Figma or Recraft and refine grid, clearspace and lockup geometry.
3. Run the four mark stress tests: readability at 16px favicon scale, single-color silhouette contrast, Gaussian blur balance and unintended second-reading inspection.
4. Pair licensed typography (Fontshare, Adobe Fonts, Realtime Colors) and match icon weight to body copy scale using open multi-weight families such as Phosphor Icons or Lucide.
5. Optimize final SVG assets with SVGO, assemble the 6-file modern favicon and Apple app-icon set, and export platform tokens through Style Dictionary.

## Motion and shader workflow

1. Select camera motion, curve timing and pacing references from 60fps.design, Shot Cafe or Eyecannndy before building effects.
2. Build layered WebGL, 3D or faux-UI product scenes using Paper Shaders, Three.js, Stageshow or Rive state machines with explicit pointer and viewport budgets.
3. Wire prefers-reduced-motion static fallbacks and verify foreground text contrast over animated surfaces against WCAG failure F83.
4. Capture deterministic frames or product walkthrough clips via Playwright, HyperFrames or snapcn instead of relying on unverified screen recordings.
5. Inspect frame pacing, loop seams, alpha edges and compressed payload sizes before committing assets.

## Brand still to interface

1. Make or choose a brand still in Leonardo, Krea, Reve, or another image tool and lock the palette, type mood, and subject before drawing screens.
2. Generate a first UI pass in Google Stitch or v0 from that still and a short brief that names the page, the audience, and the one action.
3. Move the chosen layout into an editable codebase with Lovable, Bolt, Onlook, Locofy, or Anima, and keep the components in the repo.
4. Check desktop and mobile, text contrast, and the brand mark at small sizes, then fix the layout in the same tool before publishing.

## Image, UI, brand, and design-to-code additions

These 28 entries were added on 2026-11-28 after each link was opened. The 291 earlier resources are unchanged.

### AI image

- [Leonardo.Ai](https://leonardo.ai/): Generative image and video platform for prompts, custom models, edits, and upscaling. `freemium`
- [Krea](https://www.krea.ai/): Generative image workspace on the Krea product homepage. `freemium`
- [Black Forest Labs](https://bfl.ai/): API home for FLUX image models from Black Forest Labs. `freemium`
- [Gemini Image](https://deepmind.google/models/gemini-image/): Google DeepMind page for the Gemini image model, also called Nano Banana. `freemium`
- [Reve](https://reve.art/): Image creation and editing workspace. `freemium`
- [Photoroom](https://www.photoroom.com/): AI photo and video editor for product images, listing videos, and ads. `freemium`
- [Magnific](https://www.magnific.com/): AI creative platform for image, video, audio, upscaling, and brand workflows. Freepik now uses this name. `freemium`
- [Napkin AI](https://www.napkin.ai/): Turns text into diagrams and other visuals. `freemium`
- [Stability AI](https://stability.ai/): Enterprise generative image and video tools from the Stable Diffusion lab. `paid`

### UI and website builders

- [Framer](https://www.framer.com/): Website builder with an AI design agent, hosting, and a free start. `freemium`
- [Relume](https://www.relume.ai/): AI website builder for small businesses, free to start. `freemium`
- [Webflow](https://webflow.com/): Visual web platform for designing, hosting, and optimizing sites. `freemium`
- [Uizard](https://uizard.io/): AI-assisted UI design for apps, websites, and desktop software. `freemium`

### Design to code

- [v0](https://v0.app/): Vercel AI builder for designing and shipping full-stack web apps. `freemium`
- [Google Stitch](https://stitch.google.com/): Google AI UI generator for mobile and web application screens. `freemium`
- [Lovable](https://lovable.dev/): AI app builder that turns a prompt into hosted full-stack software. `freemium`
- [Bolt](https://bolt.new/): Prompt-to-app builder for websites, prototypes, and web apps. `freemium`
- [Builder.io](https://www.builder.io/): Visual development platform where teams and AI agents build on the same project. `freemium`
- [Anima](https://www.animaapp.com/): Design-to-code agent that turns Figma files, URLs, or prompts into apps. `freemium`
- [Locofy](https://www.locofy.ai/): Converts Figma and Penpot designs into frontend code. `freemium`
- [Onlook](https://www.onlook.com/): Free local-first visual editor for building interfaces in code. `free`
- [Subframe](https://www.subframe.com/): Design canvas connected to a codebase, with a coding agent. `freemium`

### Brand

- [Looka](https://looka.com/): AI logo and brand-kit maker for colors, files, and marketing templates. `freemium`
- [Kittl](https://www.kittl.com/): AI-first design platform for graphics and brand assets. `freemium`
- [Khroma](https://www.khroma.co/): Free AI color tool for discovering and saving palettes. `free`
- [Huemint](https://huemint.com/): Free AI color palette generator. `free`
- [Fontjoy](https://fontjoy.com/): Free font-pairing generator. `free`
- [Brandmark](https://brandmark.io/): AI logo maker that also builds cards and social graphics. `freemium`

## Inventory

Every entry in [inventory.json](inventory.json) records its category, access tier (`free`, `freemium` or `paid`), concise notes and official HTTPS source link. Paid and paywalled items stay grouped after free and freemium resources so public builds can exclude paid entries cleanly. Check current license and pricing terms on each linked site before reusing assets or code.

| Category | Free & freemium | Paid | Total |
| --- | ---: | ---: | ---: |
| 01. Agent skills & DESIGN.md | 26 | 0 | 26 |
| 02. UI libraries & systems | 32 | 4 | 36 |
| 03. Shaders & 3D | 18 | 3 | 21 |
| 04. Animation, video & film | 34 | 2 | 36 |
| 05. AI image & design generation | 17 | 3 | 20 |
| 06. Software, type & colour tools | 12 | 0 | 12 |
| 07. Galleries & UI inspiration | 21 | 4 | 25 |
| 08. Site & craft teardowns | 28 | 0 | 28 |
| 09. Identity case studies | 16 | 0 | 16 |
| 10. Trends & award rules | 29 | 1 | 30 |
| 11. Logo, brand & icons | 28 | 0 | 28 |
| 12. Tokens, a11y & UX | 18 | 0 | 18 |
| 13. Vector & generative research | 10 | 0 | 10 |
| 14. UI and website builders | 4 | 0 | 4 |
| 15. Design to code | 9 | 0 | 9 |
| **Total** | **302** | **17** | **319** |

[Browse community workflows](community/) · [Category metadata](stack.json)
