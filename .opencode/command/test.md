---
description: Run pytest with uv and summarize results.
agent: build
---

Run tests using pytest through uv.

- If `$ARGUMENTS` is provided, run `uv run pytest $ARGUMENTS`.
- If `$ARGUMENTS` is empty, run `uv run pytest`.
- Summarize pass/fail counts and key failures.
- If tests fail, list the failing test IDs and the first actionable error for each.
