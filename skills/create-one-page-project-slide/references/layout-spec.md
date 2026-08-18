# One-Page Project Slide Specification

## Contents

1. Content model
2. Default layout
3. Typography and density
4. Color and contrast
5. Impact panel
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

## 2. Default layout

Canvas: 1920×1080.

Recommended vertical allocation:

- Header: 6%
- Tool-name hero: 20%
- Main content: 70%
- Outer safe margin: about 4%

Recommended main columns:

- Left: 77–79%
- Gap: 1–2%
- Right: 20–22%

Left column, top to bottom:

1. Pain card with three horizontal items
2. Solution card with four horizontal connected steps
3. Deployment card with three horizontal pills

Right column, top to bottom:

1. User-feedback label
2. Primary percentage or outcome
3. Outcome description
4. Before card
5. Down arrow
6. After card
7. Saved-time row
8. Speed-multiplier row
9. Testimonial

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

## 5. Impact panel

Keep the impact panel narrow and vertically organized. Do not place before/after or supporting metrics side by side when this makes the left content unnecessarily narrow.

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
