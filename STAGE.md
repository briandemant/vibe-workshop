# Stage 07: CI on Push with 100% Coverage and Lint/Format Gate

In this stage, you will add continuous integration (CI) so every push to GitHub
automatically runs your test suite, enforces full test coverage, and enforces
that the code is properly linted and formatted.

## Why this stage matters

Manual testing is easy to forget, and inconsistent style or untested code
silently rots a project. CI gives fast feedback on every push. A coverage
gate makes "we'll add tests later" impossible to ignore. A lint/format gate
keeps the codebase consistent without relying on memory or review nitpicks.

## Your task

Set up a GitHub Actions workflow that runs on **push** and:

1. Verifies code formatting.
2. Verifies linting.
3. Runs your test suite.
4. Measures code coverage.
5. **Fails the build if any of the following are true:**
   - Code is not properly formatted.
   - Linting reports any issue.
   - Coverage drops below 100%.

## Requirements

- Add a workflow file under `.github/workflows/`.
- Trigger the workflow on **push** only.
- Run on a Linux runner.
- The workflow should:
  - check out the repository,
  - install `uv`,
  - set up Python 3.12,
  - sync dependencies,
  - check formatting using this repository's conventions (must fail on any
    formatting difference, not just warn),
  - check linting using this repository's conventions (must fail on any lint
    issue),
  - run the test suite using this repository's conventions,
  - measure coverage of the project source code,
  - fail the job if total coverage is under 100%.
- The workflow must pass on your branch.

## Constraints

- Use this repository's existing tooling conventions (`uv` + Python 3.12 +
  Ruff for lint/format, pytest for tests).
- Do not auto-fix formatting in CI; CI must fail when formatting is wrong,
  not silently rewrite files.
- Do not disable, broadly ignore, or weaken lint rules just to pass the gate.
- Do not remove, skip, or weaken existing tests to reach 100% coverage.
- Do not exclude real source files from coverage just to pass the gate.
  Reasonable exclusions (for example, `__main__` entrypoints or generated
  code) are allowed if clearly justified.
- Keep workflow steps clear and minimal.

## What to verify

Before marking this stage complete, confirm:

1. A push triggers the workflow automatically.
2. With clean code, all checks pass.
3. If you intentionally introduce a formatting difference, the job fails on
   the format check.
4. If you intentionally introduce a lint issue, the job fails on the lint
   check.
5. If you intentionally drop coverage (for example, add an untested
   function), the job fails on the coverage gate - not only because of a
   failing test.
6. Format, lint, and coverage output are visible in the Actions run logs.

## Stretch goals (optional)

- Split format, lint, test, and coverage into separate jobs so failures are
  easier to spot.
- Add a coverage and/or CI status badge to `README.md`.
- Run CI on pull requests as well as pushes.
- Upload the coverage report as a workflow artifact.
- Cache `uv` downloads to speed up the workflow.
