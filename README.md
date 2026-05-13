# API server

This is a generic API that does not yet exist

## Prerequisites

- `uv` installed and available on your PATH
- `opencode` installed and available on your PATH

## Start OpenCode in this repo

Use the local wrapper so OpenCode picks up the repo-specific config:

```bash
./bin/opencode
```

The wrapper sets:

- `OPENCODE_CONFIG=.opencode-global/opencode.json`
- `OPENCODE_CONFIG_DIR=.opencode-global`

## Repository tour

- `AGENTS.md`: normal engineering conventions for this repo
- `.opencode/skill/`: project-local OpenCode skills
- `.opencode/command/`: project-local OpenCode slash commands
- `plans/`: planning templates and plan documents
- `.opencode-global/`: local OpenCode runtime configuration for the workshop

## Workshop flow

1. Start OpenCode with `./bin/opencode`.
2. rename `.opencode-global/opencode-global.json` to `.opencode-global/opencode.json`
3. Ask the agent to create or update a plan in `plans/`.
4. Use project commands (for example `/lint` and `/test`) as you iterate.

## CI quality gate

Pushes trigger GitHub Actions CI with strict quality gates:

- formatting must pass (`uv run ruff format . --check`)
- linting must pass (`uv run ruff check .`)
- tests must pass with full coverage (`uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=100`)

Run these locally before pushing to avoid CI failures.
