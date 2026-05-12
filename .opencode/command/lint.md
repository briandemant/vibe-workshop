---
description: Format and lint Python code with Ruff via uv.
agent: build
---

Run repository linting and formatting in this order:

1. `uv run ruff format .`
2. `uv run ruff check . --fix`
3. `uv run ruff check .`

Report which files changed and whether any issues remain.
