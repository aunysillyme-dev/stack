# Design stack

[Read Auny's Design Stack guide](https://aunysillyme.dev/stack/design/) for the searchable web directory and workflow overview.

Auny's curated design tools, step-by-step workflows and 291-entry resource inventory organized across 13 categories.

- **Core tools and workflows:** [canonical.md](canonical.md) (plain text) · [canonical.json](canonical.json)
- **Full resource inventory (291):** [inventory.md](inventory.md) (plain text) · [inventory.json](inventory.json)
- **Resources by tier:** [free/](free/free.md) (`244`, [JSON](free/free.json)) · [freemium/](freemium/freemium.md) (`31`, [JSON](freemium/freemium.json)) · [premium/](premium/premium.md) (`16`, [JSON](premium/premium.json))
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

## Inventory

Every entry in [inventory.json](inventory.json) records its category, access tier (`free`, `freemium` or `paid`), concise notes and official HTTPS source link. Paid and paywalled items stay grouped after free and freemium resources so public builds can exclude paid entries cleanly. Check current license and pricing terms on each linked site before reusing assets or code.

| Category | Free & freemium | Paid | Total |
| --- | ---: | ---: | ---: |
| 01. Agent skills & DESIGN.md | 26 | 0 | 26 |
| 02. UI libraries & systems | 32 | 4 | 36 |
| 03. Shaders & 3D | 18 | 3 | 21 |
| 04. Animation, video & film | 34 | 2 | 36 |
| 05. AI image & design generation | 9 | 2 | 11 |
| 06. Software, type & colour tools | 12 | 0 | 12 |
| 07. Galleries & UI inspiration | 21 | 4 | 25 |
| 08. Site & craft teardowns | 28 | 0 | 28 |
| 09. Identity case studies | 16 | 0 | 16 |
| 10. Trends & award rules | 29 | 1 | 30 |
| 11. Logo, brand & icons | 22 | 0 | 22 |
| 12. Tokens, a11y & UX | 18 | 0 | 18 |
| 13. Vector & generative research | 10 | 0 | 10 |
| **Total** | **275** | **16** | **291** |

[Browse community workflows](community/) · [Category metadata](stack.json)
