# Stage 07 - CI on Push with 100% Coverage and Lint/Format Gate

## Goal

Add CI on `push` so formatting, linting, test execution, and 100% coverage are enforced automatically in GitHub Actions.

## Context

- Related issue: `#1`
- Related files: `.github/workflows/`, `README.md`, `AGENTS.md`, `pyproject.toml`, `ruff.toml`
- Constraints:
  - Trigger on `push` only
  - Use repository conventions (`uv`, Python 3.12, Ruff, pytest)
  - Fail CI when coverage is below 100%
  - Fail CI when formatting or lint checks fail
  - Keep validation outcome-based

## Approach

Create a single CI workflow that mirrors local developer checks. The workflow will sync dependencies with `uv`, run format and lint checks with Ruff, and run pytest with a strict coverage threshold. Then update `README.md` and `AGENTS.md` so contributors can reproduce and understand CI requirements.

## Steps

- [ ] Add a workflow under `.github/workflows/` that runs on `push` only.
- [ ] Set up Linux runner, Python 3.12, and `uv`.
- [ ] Run dependency sync before checks.
- [ ] Add formatting check step that fails on drift.
- [ ] Add lint check step that fails on findings.
- [ ] Add test + coverage step with fail-under 100%.
- [ ] Update `README.md` with CI gate details and local reproduction commands.
- [ ] Update `AGENTS.md` with CI gate policy for contributors.
- [ ] Verify locally that format, lint, tests, and coverage gates pass.

## Out of Scope

- Running workflow on `pull_request`
- Auto-fixing formatting in CI
- Relaxing lint rules or coverage threshold
- Adding badges, caching, or artifact uploads

## Open Questions

- Should CI remain one job for simplicity, or split checks into multiple jobs later for clearer failure isolation?
