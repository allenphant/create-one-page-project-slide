# Codex Skills

Reusable skills for Codex workflows.

## `create-one-page-project-slide`

Turn a software project, workflow, SOP, product, or case study into a verified 16:9 one-page presentation slide covering:

- Pain points
- Solution workflow
- Deployment model
- Quantified impact

The skill can produce standalone HTML, 1920×1080 PNG, and editable native SVG deliverables.

## Install

Install the skill from this repository with the Codex skill installer:

```bash
python3 /path/to/install-skill-from-github.py \
  --repo allenphant/create-one-page-project-slide \
  --path skills/create-one-page-project-slide
```

Or install a pinned release:

```bash
python3 /path/to/install-skill-from-github.py \
  --repo allenphant/create-one-page-project-slide \
  --path skills/create-one-page-project-slide \
  --ref v0.1.0
```

## Use

```text
請使用 $create-one-page-project-slide，
把目前專案整理成一頁式投影片，內容包含痛點、解法、部署型式與量化成效。
```

## Validation

The skill includes deterministic helpers for impact calculations and Chromium-based rendering. Validate the skill folder with:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skills/create-one-page-project-slide
```

## License

MIT
