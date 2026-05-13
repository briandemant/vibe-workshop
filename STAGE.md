# Stage 06: Create an interactive `/create-issue` command

In this stage you will build a project-local OpenCode slash command
that walks you through creating a GitHub issue -- interactively.

## What you will build

A new `/create-issue` command that:

1. Asks the user for a brief description of the task or bug.
2. Spars with the user -- asks clarifying questions, gives useful
   pushback, and helps sharpen the issue description. In particular
   the agent should:
   - Challenge vague scope or missing detail.
   - Ask whether tests are needed (and which kind) when the change
     is testable.
   - Ask whether documentation needs updating (README, help page,
     docstrings, etc.) when the change affects public behavior.
3. When the topic feels well-defined, asks the user to confirm.
4. Creates a GitHub issue (via `gh`) with one of these labels:
   **feature**, **spike**, or **bug**.

## Requirements

- The command file lives at `.opencode/command/create-issue.md`.
- The conversation is interactive -- the agent must not guess; it
  must ask and confirm.
- The agent picks the label based on the conversation context and
  confirms the choice with the user before creating the issue.
- The issue is created with `gh issue create` (title, body, label).
- After creation the command prints the new issue URL.

## Hints

- Look at existing commands in `.opencode/command/` for the file
  format (YAML frontmatter + prompt body).
- The `create-command` skill can help you scaffold the file.
- `$ARGUMENTS` can optionally seed the initial description, but the
  command should still confirm interactively.
- Keep the prompt instructions clear about the conversational flow:
  gather -> refine -> confirm -> create.

## Acceptance criteria

- `/create-issue` starts an interactive conversation.
- The agent asks at least one clarifying question before proposing
  to create the issue.
- The agent explicitly considers tests and documentation during the
  sparring phase.
- The user explicitly confirms before creation.
- The created issue has a title, body, and exactly one label
  (feature, spike, or bug).
- The issue URL is printed at the end.
