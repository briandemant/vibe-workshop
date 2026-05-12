# AGENTS

This file defines normal working conventions for this repository.

## Project Basics

This is a Python project managed with `uv` and pinned to Python 3.12.

- Use `uv` for dependency and environment management.
- Keep changes small and easy to review.
- Follow existing repository structure and naming.

## STAGE.md

`STAGE.md` at the repository root is student-facing material for the current workshop stage.

- NEVER read `STAGE.md`.
- NEVER use `STAGE.md` as context, even indirectly.
- Write or overwrite `STAGE.md` only through the `/explain` command flow.

## Run Commands

Always run Python through `uv run` in this repository.

- Run app code with `uv run python <file>.py`.
- Do not run plain `python ...` directly.

## Dependencies

Use `uv` for all dependency changes.

- Add packages with `uv add <package>`.
- Remove packages with `uv remove <package>`.
- Sync environment with `uv sync` when needed.
- Do not use `pip install` directly.

## Linting and Formatting

Ruff is configured via `ruff.toml`.

- Format code with `uv run ruff format .`.
- Lint code with `uv run ruff check .`.
- When fixing lint issues automatically, use `uv run ruff check . --fix`.

## Testing

Use pytest through `uv run`.

- Run all tests with `uv run pytest`.
- Run targeted tests with `uv run pytest <path-or-nodeid>`.

## Repository Layout

Common locations used in this repository:

- `main.py`: simple Python entrypoint.
- `.opencode/skill/`: project-local opencode skills.
- `.opencode/command/`: project-local opencode slash commands.
- `plans/`: plan documents and templates.
