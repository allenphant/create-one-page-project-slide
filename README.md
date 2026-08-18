# Codex Skills

Reusable skills for Codex workflows.

## `create-one-page-project-slide`

Turn a software project, workflow, SOP, product, or case study into a verified 16:9 one-page presentation slide covering:

- Pain points
- Solution workflow
- Deployment model
- Quantified impact

The skill can produce standalone HTML, 1920×1080 PNG, and editable native SVG deliverables.

## Install in Codex

Recommended: open a new Codex conversation and paste this prompt:

```text
Please install the Codex skill from:
https://github.com/allenphant/create-one-page-project-slide/tree/v0.1.1/skills/create-one-page-project-slide

After installation, confirm that $create-one-page-project-slide is available.
```

## Manual install (no Python required)

```bash
git clone --depth 1 --branch v0.1.1 \
  https://github.com/allenphant/create-one-page-project-slide.git \
  /tmp/create-one-page-project-slide

SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILL_DIR"
cp -R /tmp/create-one-page-project-slide/skills/create-one-page-project-slide \
  "$SKILL_DIR/"
```

Restart or open a new Codex conversation after installation.

## Use

```text
請使用 $create-one-page-project-slide，
把目前專案整理成一頁式投影片，內容包含痛點、解法、部署型式與量化成效。
```

## Validation

The skill includes deterministic helpers for impact calculations and Chromium-based rendering. Codex validates the skill structure during installation and can run the bundled helpers when creating a slide.

## License

MIT
