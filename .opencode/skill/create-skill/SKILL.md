---
name: create-skill
description: Create a new project-local OpenCode skill with consistent structure.
allowed-tools:
  - read
  - write
  - edit
  - glob
---

# create-skill

Use this skill to add a new reusable workflow under `.opencode/skill/`.

## Skill location

- Create skills at `.opencode/skill/<skill-name>/SKILL.md`.
- Keep skill names short, lowercase, and hyphen-separated.

## Required structure

Include YAML frontmatter at the top:

```md
---
name: <skill-name>
description: <one-sentence purpose>
---
```

Then include:

1. A short title (`# <skill-name>`).
2. When to use the skill.
3. A clear step-by-step workflow.
4. Constraints and repository-specific rules.

## Guidance

- Prefer imperative steps that can be followed exactly.
- Keep skills focused on one workflow.
- Put command snippets in backticks and use repo conventions (for example `uv run ...`).
- If a workflow is single-shot rather than reusable, prefer creating a command instead.
