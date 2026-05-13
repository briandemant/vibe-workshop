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

## Stage Help Page

Whenever a stage adds or changes an API endpoint, the `/` HTML help page must be updated.

- Update `src/app.py` `root_help()` to mention the new or changed endpoint.
- For every documented endpoint, include:
  - A short label with method and route.
  - At least one good usage example (working request).
  - At least one bad usage example showing invalid input and error response.
- When an endpoint accepts constrained values (for example, allowed categories), make the allowed values discoverable on the help page.
- Extend `tests/test_root_help.py` with assertions that verify the new endpoint appears and both good and bad examples are present.

This convention applies even when `STAGE.md` does not explicitly require a help page update.

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
- CI also enforces formatting with `uv run ruff format . --check` on every push.

## Testing

Use pytest through `uv run`.

- Run all tests with `uv run pytest`.
- Run targeted tests with `uv run pytest <path-or-nodeid>`.
- CI enforces 100% coverage with `uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=100` on every push.

## Repository Layout

Common locations used in this repository:

- `main.py`: simple Python entrypoint.
- `.opencode/skill/`: project-local opencode skills.
- `.opencode/command/`: project-local opencode slash commands.
- `plans/`: plan documents and templates.

## Bash Conventions

Prefer single-command bash invocations.

- Do not chain commands with `&&`, `;`, or `|` unless strictly needed.
- Strictly needed examples: a follow-up command depends on a side effect that must happen in the same shell.
- When commands are independent, run them as separate bash calls instead of chaining.
- Avoid prefixing commands with environment variables (for example `FOO=bar git ...`) unless required.
- This helps command-specific permission allowlists (for example `git *`) match reliably and reduces unnecessary approval prompts.
