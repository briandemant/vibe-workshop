---
name: create-command
description: Create a new project-local OpenCode slash command.
allowed-tools:
  - read
  - write
  - edit
  - glob
---

# create-command

Use this skill to add a slash command under `.opencode/command/`.

## Command location

- Create commands as `.opencode/command/<command-name>.md`.
- The command name comes from the filename (for example `lint.md` becomes `/lint`).

## Required structure

Use Markdown with YAML frontmatter:

```md
---
description: <what the command does>
agent: build
---

<instruction prompt body>
```

## Prompt authoring

- Write direct instructions the agent can execute.
- Use `$ARGUMENTS` where user-supplied arguments should be inserted.
- Include repo-specific conventions (for example always use `uv run` for Python tooling).
- Keep commands task-focused and easy to reason about.

## Skill vs command

- Use a command for a quick, single-invocation task.
- Use a skill for a reusable multi-step workflow or policy.
