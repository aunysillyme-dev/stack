# Design stack: core tools and workflows

Curated by @aunysillyme · Reviewed 2026-11-28

Source: https://github.com/aunysillyme-dev/stack/blob/main/design/README.md

## Core tools (35)

- **[Penpot](https://github.com/penpot/penpot):** Open-source vector design, components and interactive prototyping with CSS-native layouts and SVG export.
- **[Paper](https://paper.design):** HTML and CSS design canvas that coding agents inspect and edit directly over MCP.
- **[Figma](https://www.figma.com/pricing/):** Collaborative UI layout, shared component libraries and design-system handoff on the free starter tier or paid seats.
- **[Stageshow](https://github.com/benjitaylor/skills):** MIT agent skill and React faux-UI component kit for hero product visuals, bento cards and recorded UI demos.
- **[Impeccable](https://impeccable.style/):** Open-source frontend craft commands, anti-slop detect audits and hierarchy polish guidance for coding agents.
- **[unslop](https://github.com/heydamir/unslop):** CC BY 4.0 review skill that strips generic AI UI habits across spacing, typography, icons, contrast and motion.
- **[GradientDeck UI](https://ui.gradientdeck.com/):** Free, no-signup library of over 1,270 DESIGN.md token and style rule files extracted from real shipped sites.
- **[UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill):** MIT searchable design dataset (styles, palettes, font pairings and UX checklists) usable offline by coding agents.
- **[shadcn/ui](https://ui.shadcn.com/):** MIT accessible React and Tailwind component code owned directly in the project repository.
- **[21st.dev](https://21st.dev):** Community React and Tailwind UI pattern registry with CLI and MCP installation; check per-component license notes.
- **[React Bits](https://reactbits.dev):** Animated React text, background, card and micro-interaction primitives (MIT with Commons Clause).
- **[Astryx](https://astryx.atmeta.com/):** MIT customizable React 19 and StyleX design system (180+ components) with CLI and MCP integration.
- **[transitions.dev](https://transitions.dev):** Copy-paste UI transitions, interactive components, agent skill and MCP server for web apps.
- **[Lenis](https://github.com/darkroomengineering/lenis):** MIT smooth-scroll engine for coordinated scroll-linked interface sections and editorial pages.
- **[Paper Shaders](https://shaders.paper.design/):** Apache-2.0 zero-dependency React WebGL2 shaders for mesh gradients, dithering, halftone and fluted glass.
- **[Three.js](https://threejs.org):** MIT 3D WebGL and WebGPU engine paired with React Three Fiber or postprocessing pipelines for interactive scenes.
- **[Rive](https://rive.app/):** Interactive vector state machines with MIT runtimes; free to browse community files and embed playback.
- **[HyperFrames](https://github.com/heygen-com/hyperframes):** Programmatic HTML-to-video motion and explainer toolkit with local frame inspection and deterministic timing.
- **[snapcn](https://snapcn.dev):** Registry of 53 MIT Remotion demo components (captions, terminals, device frames) with CLI and MCP access.
- **[Ideogram](https://ideogram.ai):** Generative image creation with strong typography and clean graphic compositions (free tier plus paid plans).
- **[Recraft](https://www.recraft.ai/docs/trust-and-security/ownership):** Generative raster and scalable vector illustration tool for icons, brand graphics and editable SVG output.
- **[Style Dictionary](https://styledictionary.com/):** Build pipeline that compiles W3C Design Tokens JSON into CSS custom properties, iOS, Android and JS targets.
- **[Radix Colors](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale):** 12-step accessible color scale specification separating app backgrounds, interactive states and text contrast.
- **[Phosphor Icons](https://phosphoricons.com/):** MIT multi-weight icon system (Thin through Fill and Duotone) for matching optical weight to type scales.
- **[SVGO](https://github.com/svg/svgo/releases/tag/v4.0.0):** MIT SVG optimizer that strips editor metadata and shrinks icon and illustration payloads before commit.
- **[Playwright](https://github.com/microsoft/playwright):** Apache-2.0 headless browser runner used for light/dark viewport screenshots, visual regression checks and demo capture.
- **[v0](https://v0.app/):** Freemium. Vercel AI builder for designing and shipping full-stack web apps.
- **[Google Stitch](https://stitch.google.com/):** Freemium. Google AI UI generator for mobile and web application screens.
- **[Leonardo.Ai](https://leonardo.ai/):** Freemium. Generative image and video platform for prompts, custom models, edits, and upscaling.
- **[Krea](https://www.krea.ai/):** Freemium. Generative image workspace on the Krea product homepage.
- **[Lovable](https://lovable.dev/):** Freemium. AI app builder that turns a prompt into hosted full-stack software.
- **[Looka](https://looka.com/):** Freemium. AI logo and brand-kit maker for colors, files, and marketing templates.
- **[Framer](https://www.framer.com/):** Freemium. Website builder with an AI design agent, hosting, and a free start.
- **[Black Forest Labs](https://bfl.ai/):** Freemium. API home for FLUX image models from Black Forest Labs.
- **[Onlook](https://www.onlook.com/):** Free. Free local-first visual editor for building interfaces in code.

## Workflows (5)

### Design production from research to QA gate

Source: https://github.com/aunysillyme-dev/stack/blob/main/design/README.md#how-a-design-job-runs

1. Research before drawing. Collect the same artifact from 8 to 12 peer brands alongside recent award-winning work in the category, then record what holds up, what fails and which cliches to skip.
2. Choose directions by mechanism. Propose directions that differ in how they work (type-led system, structural metaphor or interactive behavior) rather than one idea styled three ways, and tie every brief adjective to something observable.
3. Build in layers. Separate background surfaces, environment texture, hero subjects, annotations, typography and brand marks so each layer renders and scales cleanly before compositing depth and contrast.
4. Render and look. Export and inspect real desktop, tablet and mobile views yourself before sharing; zoom in on generated imagery and vector exports to catch anatomical, text or alignment defects.
5. Pass the gate. Verify core message, contrast ratios (WCAG 2.2 AA), type ramp, spacing tokens and asset licenses first; verify brand marks at 16px, in monochrome, blurred and against unintended second readings.

### Web interface and landing-page build

Source: https://github.com/aunysillyme-dev/stack/blob/main/design/README.md#web-interface-workflow

1. Benchmark layout patterns and typography pairings against curated web galleries (Minimal Gallery, Footer.design, CTA Gallery) and pull relevant DESIGN.md rules before writing markup.
2. Lock color, spacing and type tokens first using Radix 12-step contrast semantics, OKLCH lightness checks and Style Dictionary or CSS custom properties.
3. Assemble accessible controls from headless and copy-owned primitives (Radix UI Primitives, shadcn/ui, Astryx, 21st.dev) and add subtle state transitions (transitions.dev, NumberFlow, Lenis) only where they clarify cause and effect.
4. Render full-page desktop and mobile screenshots in both light and dark modes with Playwright at real target viewports.
5. Run automated WCAG checks with axe-core alongside an anti-slop review pass (Impeccable, unslop) before shipping or publishing.

### Brand mark, icon system and token handoff

Source: https://github.com/aunysillyme-dev/stack/blob/main/design/README.md#brand-and-token-workflow

1. Audit peer brand guidelines and search USPTO Design Search Codes to confirm the visual direction does not collide with crowded category shapes.
2. Draft distinctive vector mark concepts in Penpot, Figma or Recraft and refine grid, clearspace and lockup geometry.
3. Run the four mark stress tests: readability at 16px favicon scale, single-color silhouette contrast, Gaussian blur balance and unintended second-reading inspection.
4. Pair licensed typography (Fontshare, Adobe Fonts, Realtime Colors) and match icon weight to body copy scale using open multi-weight families such as Phosphor Icons or Lucide.
5. Optimize final SVG assets with SVGO, assemble the 6-file modern favicon and Apple app-icon set, and export platform tokens through Style Dictionary.

### Interactive shader, 3D hero and product-demo motion

Source: https://github.com/aunysillyme-dev/stack/blob/main/design/README.md#motion-and-shader-workflow

1. Select camera motion, curve timing and pacing references from 60fps.design, Shot Cafe or Eyecannndy before building effects.
2. Build layered WebGL, 3D or faux-UI product scenes using Paper Shaders, Three.js, Stageshow or Rive state machines with explicit pointer and viewport budgets.
3. Wire prefers-reduced-motion static fallbacks and verify foreground text contrast over animated surfaces against WCAG failure F83.
4. Capture deterministic frames or product walkthrough clips via Playwright, HyperFrames or snapcn instead of relying on unverified screen recordings.
5. Inspect frame pacing, loop seams, alpha edges and compressed payload sizes before committing assets.

### Turn a brand still into an interface

Source: https://stitch.google.com/

1. Make or choose a brand still in Leonardo, Krea, Reve, or another image tool and lock the palette, type mood, and subject before drawing screens.
2. Generate a first UI pass in Google Stitch or v0 from that still and a short brief that names the page, the audience, and the one action.
3. Move the chosen layout into an editable codebase with Lovable, Bolt, Onlook, Locofy, or Anima, and keep the components in the repo.
4. Check desktop and mobile, text contrast, and the brand mark at small sizes, then fix the layout in the same tool before publishing.
