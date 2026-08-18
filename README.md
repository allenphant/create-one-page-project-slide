# Agent Skills

Reusable, agent-agnostic skills for repeatable workflows.

## `create-one-page-project-slide`

Turn a software project, workflow, SOP, product, or case study into a verified 16:9 one-page presentation slide covering:

- Pain points
- Solution workflow
- Deployment model
- Quantified impact

The default deliverables are standalone HTML, 1920×1080 PNG, and editable native SVG.

### Optional editable PPTX

An editable PowerPoint file is an optional output. It requires the `officecli` tool; HTML, PNG, and SVG do not.

The skill does not install `officecli` automatically. If PPTX output is requested and `officecli` is missing, the agent should remind the user and wait for approval before changing the environment. After approval, install it with the official installer:

```bash
curl -fsSL https://d.officecli.ai/install.sh | bash
```

Once installed, the agent should create native editable PPTX objects, validate the file, and compare an Office-compatible render against the SVG/PNG reference. A structurally valid PPTX is not by itself proof of visual fidelity.

## Install

Clone the repository and copy the skill folder into the skill directory used by your agent:

```bash
git clone --depth 1 --branch v0.2.0 \
  https://github.com/allenphant/create-one-page-project-slide.git \
  /tmp/create-one-page-project-slide

cp -R /tmp/create-one-page-project-slide/skills/create-one-page-project-slide \
  /path/to/your-agent/skills/
```

The exact skill directory is agent-specific. Replace `/path/to/your-agent/skills/` with the directory documented by your agent, then restart or open a new session.

You can also ask your agent to install or load this skill from:

```text
Please load the create-one-page-project-slide skill from:
https://github.com/allenphant/create-one-page-project-slide/tree/v0.2.0/skills/create-one-page-project-slide
```

## Use

```text
Use the create-one-page-project-slide skill to turn this project into a one-page presentation covering pain points, solution, deployment model, and quantified impact.
```

## Validation

The skill includes deterministic helpers for impact calculations and Chromium-based rendering. Validate the `SKILL.md` structure with the validator provided by your agent ecosystem, then run the bundled helpers when creating a slide.

## License

MIT
