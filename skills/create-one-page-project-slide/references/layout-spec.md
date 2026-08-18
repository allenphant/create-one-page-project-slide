# One-Page Project Slide Specification

## Contents

1. Content model
2. Locked baseline layout
3. Typography and density
4. Color and contrast
5. Status / impact rail
6. HTML and SVG requirements
7. Review checklist

## 1. Content model

Use this hierarchy:

- Official tool/project name
- One sentence explaining the integrated value
- `01 Pain`: three short problem cards
- `02 Solution`: four connected workflow cards
- `03 Deployment`: three executive-level pills
- Impact: one verified or user-reported before/after result

Content limits:

- Pain card title: 2–6 words
- Pain card explanation: one line
- Solution step title: 2–6 words
- Solution explanation: one line
- Deployment pill: 2–8 words
- Value proposition: one sentence
- Testimonial: one short sentence

If content does not fit, shorten it. Do not shrink text to preserve detail.

## 2. Locked baseline layout

Use this layout as the default for every one-page project slide unless the user explicitly requests a different composition. It is the approved, repeatable baseline.

Canvas: 1920×1080. Outer safe margin: 72 px. Top brand bar: 16 px. Main content begins at y=220 and ends at y=895.

Fixed grid:

- Left content: x=72, width=1400.
- Inter-column gap: 32 px.
- Right rail: x=1504, width=344.
- Right rail height: 675 px.
- Standard section gap: 24 px.

Header contract:

- Main title is the official tool/project name at x≈72, y≈117; use 52–60 px.
- Value proposition sits below at y≈160; use 17–20 px.
- Optional version/status capsule is right-aligned to x=1848 and must size to its text. Measure the rendered label or widen the capsule; never hard-code a narrow capsule that clips or spills text.

Recommended vertical allocation:

- Header and hero: y=16–190.
- Current friction: x=72, y=220, w=1400, h=174.
- Target production chain: x=72, y=418, w=1400, h=322.
- Deployment/governance: x=72, y=764, w=1400, h=131.
- Right status rail: x=1504, y=220, w=344, h=675.

Main columns:

- Left: 1400 px.
- Gap: 32 px.
- Right: 344 px.

Left column, top to bottom:

1. Current friction: one surface with exactly three horizontal items.
2. Target production chain: one surface with exactly four connected workflow cards.
3. Deployment/governance: one surface with three pills.

Target-card contract:

- Card row starts at x=104, y=526; card height is 182 px.
- Cards 1–3 are 286 px wide; card 4 is 334 px wide and carries the value moment.
- Card x positions are 104, 438, 772, and 1106 px.
- Card inset is 26–32 px on every side.
- Step prefix is a separate brand-color text element (`01`, `02`, `03`, `04`) at x=130/464/798/1132 px; adjacent English label begins at x=166/500/834/1168 px. Both share a baseline of y≈563 px. Do not use a standalone filled number circle by default.
- Chinese title baseline is y≈598; body baselines are y≈634 and y≈658.
- Optional final control line baseline is y≈687 and must retain at least 18 px below it.
- Arrows sit in the gaps and are vertically centered around y=617.
- Do not put the step prefix above, below, or materially offset from its neighboring label. Do not let title or body text hug the card edge.

Right column, top to bottom:

Use one of two modes:

1. **Verified impact mode**: user-feedback label, primary verified/user-reported outcome, before/after, supporting metrics, and short attributed testimonial.
2. **Current-stage mode**: current stage, what is being confirmed, what becomes fixed next, and a next-focus callout. Use this mode when user feedback, before/after timings, or formal outcome metrics do not exist.

For current-stage mode, keep the callout in a separate lower zone. Give it at least 18–24 px bottom breathing room; do not place the final text baseline close to the callout border.

Center card content vertically when the card is taller than its copy. Avoid content crowded at the top with unexplained blank space below.

## 3. Typography and density

Use a local Traditional Chinese-friendly font stack:

```css
font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", Arial, sans-serif;
```

At 1920×1080:

- Main tool name: 52–60 px
- Value proposition: 17–20 px
- Section heading: 21–24 px
- Card title: 18–21 px
- Body: 14–16 px minimum
- Main KPI: 76–90 px
- Supporting metric: 19–22 px

Use at most three practical text levels within a content section.

## 4. Color and contrast

Default consultant palette:

- Page: `#F5F7F4`
- Surface: `#FFFFFF`
- Main text: `#172522`
- Secondary text: `#60706C`
- Border: `#D8E2DE`

Use the supplied brand color for:

- Step numbers
- Key KPI
- Small accents
- Flow arrows
- Active markers

Derive a dark brand tone for the impact panel and a pale tint for cards or pills. Do not use a bright brand color for small text on a light background when contrast is insufficient.

## 5. Status / impact rail

Keep the right rail narrow and vertically organized. Do not place before/after or supporting metrics side by side when this makes the left content unnecessarily narrow. If no verified impact exists, switch to current-stage mode rather than adding placeholder metrics.

The right rail must support the main story, not compete with it. Its heading should identify the mode (`CURRENT STAGE`, `READINESS`, or `USER-REPORTED OUTCOME`) and its content should be grouped into clear vertical zones separated by rules or deliberate spacing.

For chart-to-narrative architectures, show the chain explicitly in the main flow and/or right rail:

```text
chart/table data → language model → narrative text → QA / human approval
```

Do not describe the language model only in a footer or hide it inside a generic “render report” step.

Calculate:

```text
reduction_percent = (before - after) / before × 100
saved = before - after
speed_multiplier = before / after
```

Preferred labels:

- 使用者實際操作回饋 / User-reported outcome
- 作業時間縮短 / Cycle time reduced
- 導入前 / Before
- 導入後 / After
- 單次作業節省 / Saved per run
- 處理速度 / Processing speed

State that the figure is user-reported when it is not a formal benchmark.

## 6. HTML and SVG requirements

HTML:

- Standalone file
- No CDN dependency
- No network fonts
- Fixed 16:9 slide with responsive letterboxing
- Print-friendly 16:9 page rule

SVG:

- `viewBox="0 0 1920 1080"`
- Use vector `<rect>`, `<circle>`, `<line>`, `<path>`, gradients, and filters
- Preserve text as `<text>`/`<tspan>`
- Include `<title>` and `<desc>`
- Do not embed a raster screenshot as the slide
- Avoid `<foreignObject>` for the main slide content

## 7. Review checklist

- Is the main title the official tool name?
- Can every body line be read when the full slide is visible?
- Are there exactly three pain items and four solution steps?
- Is deployment summarized rather than diagrammed in detail?
- Are right-panel metrics arranged vertically?
- Is every quantitative claim sourced or calculated?
- Is the testimonial short and clearly attributed?
- Is there any decorative or technical noise that can be deleted?
- Does PNG rendering match HTML/SVG?
- Are prior versions preserved?

### Known failure modes to prevent

- Do not use a fixed-width capsule whose label is longer than the capsule; size the shape from the text and right-align it to the safe margin.
- Do not compress a callout so its last line sits close to the bottom border. Move the text up or increase the callout height.
- Do not align a step prefix by approximate x/y intuition. Use the target-card contract and check the rendered baseline visually.
- For editable PPTX, do not translate an SVG text baseline directly into a textbox top coordinate. Use top-anchored text boxes, zero internal insets, an explicit installed font, and a small optical upward calibration; otherwise text will visibly drift downward while card geometry remains fixed.
- Do not apply one vertical-anchor rule to every PPTX text box. Body lines near a surface bottom need explicit breathing room; compact pill/control text must use a text box matching the pill height with `valign=middle` and zero insets.
- Do not let a card's title, body, or final control line lose its content inset. Preserve 26–32 px side padding and 18–24 px bottom breathing room.
- Do not turn missing user feedback or missing KPI data into invented “impact” figures. Use current-stage mode and label unknowns explicitly.
- Do not let a dark status rail become a second competing composition. It should explain readiness or validation status and reinforce the left-to-right transformation.
- Do not stop at a detector-clean result. Render the final PNG, view it at full-slide scale, and fix visible optical spacing or clipping before delivery.
