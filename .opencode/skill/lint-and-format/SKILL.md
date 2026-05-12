---
name: lint-and-format
description: Run formatting and linting with Ruff using uv in this repository.
allowed-tools:
  - bash
  - read
---

# lint-and-format

Use this skill when you need to format Python code and resolve lint issues.

## Steps

1. Run `uv run ruff format .`.
2. Run `uv run ruff check . --fix`.
3. Run `uv run ruff check .` to verify no remaining lint errors.

## Notes

- Respect the existing `ruff.toml` configuration.
- If fixes are not automatic, report the remaining errors and affected files.
- Do not use plain `python` or `pip` commands.
