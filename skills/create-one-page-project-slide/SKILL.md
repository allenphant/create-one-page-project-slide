---
name: create-one-page-project-slide
description: Turn a software project, workflow, SOP, product, or case study into a verified 16:9 one-page presentation slide covering pain points, solution, deployment model, and quantified impact. Use when an agent is asked to create a 一頁式投影片, project one-pager, solution overview, executive summary slide, case-study slide, before/after impact slide, or matching HTML, PNG, and editable SVG deliverables from a repository or project documents.
---

# Create One-Page Project Slide

Create an evidence-based executive slide from project sources, then deliver matching HTML, PNG, and native SVG artifacts.

## Workflow

### 1. Establish scope

Resolve these inputs from the request or project before designing:

- Official project/tool name
- Audience and presentation language
- Owning organization
- Brand color and available brand assets
- User testimonial or measurable before/after result
- Desired output directory

Use reasonable project-derived defaults. Ask only when a missing choice would materially change the result.

### 2. Discover evidence

Read repository instructions first. Prefer the project's code graph or indexed discovery tools when available, then inspect README files, SOPs, architecture notes, deployment documents, user manuals, and relevant source.

Build an evidence set for:

- The old/manual workflow and its friction
- The product's actual workflow and safeguards
- The real deployment model at an executive level
- Measured or directly reported outcomes

Do not expose secrets, internal identifiers, patient/customer data, credentials, or sensitive infrastructure details.

Separate:

- Verified project facts
- User-reported outcomes
- Calculated values
- Unknowns that must not be claimed

For before/after time metrics, run:

```bash
python3 scripts/calculate_impact.py <before> <after>
```

Never invent a KPI. Label testimonial-derived metrics as user feedback and avoid implying a controlled benchmark.

### 3. Draft copy before layout

Prepare concise slide-ready copy:

1. Official tool name
2. One-sentence value proposition
3. Three pain points
4. Four solution steps
5. Three deployment pills
6. Testimonial and quantified impact

Present this copy for confirmation before drawing unless the user explicitly requests uninterrupted end-to-end execution.

Write for executives and customers. Remove code names, API names, database details, quotas, OAuth scopes, backup mechanics, version trivia, and other implementation noise unless essential to the audience.

### 4. Design the slide

Read [references/layout-spec.md](references/layout-spec.md) before creating the visual.

Use the locked baseline layout in that reference as the default. Do not invent a new card grid, impact-panel topology, or spacing rhythm unless the user explicitly requests a different visual direction. The baseline is intentionally low-freedom because repeatability matters more than novelty for this deliverable.

Before drawing, freeze these decisions:

- 1920×1080 canvas with 72 px outer safe margin and 16 px top brand bar.
- Header at the top; left content column 1400 px wide; 32 px gap; right rail 344 px wide.
- Left stack: current friction, target production chain, deployment/governance.
- Target chain: four connected cards with a shared internal rhythm; use a brand-color text prefix (`01`, `02`, `03`, `04`) followed by the adjacent English label on one visual baseline. Do not use a standalone number circle by default.
- Right rail: dark current-stage/status panel. Use a status/readiness panel when no verified before/after KPI exists; never force an impact metric panel with invented numbers.
- Use a content-sized top-right capsule. Measure the label or widen the capsule; never let text overflow a fixed narrow pill.

When the architecture includes chart/table data becoming narrative text through a language model, make that transformation explicit in the fourth solution step and in the right rail. Keep `metric ID`, source linkage, QA, and human approval visible so the model is not presented as an ungoverned black box.

Use a 1920×1080, 16:9 canvas. Make the official tool name the main title; do not use the performance metric as the title.

Default to the consultant-style layout in the reference:

- Header and tool-name hero
- Wide left column for pain, solution, and deployment
- Narrow dark impact panel on the right
- Vertical before/after and supporting metrics

Prefer larger typography and fewer words. Remove details before reducing font size.

Use CSS/SVG shapes for cards, steps, arrows, and accents. Do not add decorative imagery unless it materially improves comprehension and matches provided brand assets.

For solution cards, keep the step number as an independent brand-color text element immediately before the English label. This is the default across HTML, SVG, and editable PPTX because it is easier to align and avoids cross-renderer drift from vertically centered circle text.

For editable PPTX, do not apply one vertical-anchor rule to every text box. Body lines near a surface bottom need explicit breathing room; compact pill/control text must use a text box matching the pill height with `valign=middle` and zero insets.

### 5. Produce versioned artifacts

Create all three deliverables:

```text
deliverables/<project-slug>-one-page-slide-v1.html
deliverables/<project-slug>-one-page-slide-v1.png
deliverables/<project-slug>-one-page-slide-v1.svg
```

Requirements:

- HTML: standalone and network-independent
- PNG: exactly 1920×1080
- SVG: native vector shapes and `<text>` elements
- Do not embed the PNG in SVG
- Do not use `<foreignObject>` merely to wrap the HTML
- Preserve earlier versions; create `v2`, `v3`, and so on for material revisions

Optional editable Office output:

- If the user requests a `.pptx`, check whether `officecli` is already available before starting Office work.
- If `officecli` is missing, do not install it automatically. Tell the user that editable PPTX generation requires `officecli`, provide the official installation command only as an option, and wait for approval before changing the environment.
- If the user does not approve installation, continue with the HTML, PNG, and SVG deliverables when those formats satisfy the request; otherwise pause and explain that the PPTX portion is blocked.
- When `officecli` is available, load its PPTX specialization, create native editable objects rather than a full-slide raster image, and run `officecli validate` plus a structural check for `Pictures: 0`.

Render either HTML or SVG with:

```bash
python3 scripts/render_slide.py <input.html-or-svg> <output.png>
```

If browser execution is sandbox-blocked, request the required approval rather than replacing the visual verification with an assumption.

### 6. Inspect and revise

Open the rendered PNG with an image-viewing tool and verify:

- Tool name is the primary headline
- Text is readable at presentation scale
- No overflow, clipping, or scrollbars
- Cards do not have accidental empty areas
- Left/right balance matches the chosen hierarchy
- Impact metrics read vertically in the intended order
- Brand color has sufficient contrast
- Numbers and testimonial labels are accurate
- No unnecessary footer, warning, or infrastructure noise remains
- The locked layout contract is still intact after copy changes
- Every card has a visible 26–32 px content inset and at least 18–24 px bottom breathing room
- No capsule, card, or callout has text touching or exceeding its boundary
- Step prefixes and their neighboring labels share a visual baseline
- If a status panel is used, its heading, body, and callout have separate vertical zones rather than compressed baselines

Fix discovered issues and re-render. Do not merely report them.

### 7. Deliver

Show the PNG preview and link the HTML, PNG, and SVG files. Briefly state the design direction and the verified dimensions.

## Resources

- [references/layout-spec.md](references/layout-spec.md): exact content limits, layout ratios, typography, colors, and SVG rules
- `scripts/calculate_impact.py`: deterministic before/after calculations
- `scripts/render_slide.py`: Chromium-based rendering and PNG dimension verification
