# Stage 05 - Consistent Recommendation Response Format

## Goal

Make recommendation endpoints return a shared JSON response object while preserving existing behavior.

## Context

- Related files: `src/app.py`, `tests/test_recommendations.py`, `tests/test_category_recommendations.py`, `tests/test_root_help.py`
- Stage requirement highlights:
  - `GET /recommendations` should return `{ "recommendations": [...], "fallback": false }`.
  - `GET /recommendations/{category}` should return `{ "recommendations": [...], "fallback": false, "category": "..." }`.
  - Category validation and 422 invalid-category behavior remain unchanged.
  - Help page examples should reflect the new response format.

## Approach

Refactor recommendation generation into a small helper used by both endpoints. Update both recommendation handlers to return object responses with shared keys. Keep invalid-category handling as-is. Update tests to assert the new shape and preserve existing validation checks.

## Steps

- [x] Refactor recommendation ID generation so both endpoints share logic.
- [x] Update `GET /recommendations` response to object format with `recommendations` and `fallback`.
- [x] Update `GET /recommendations/{category}` response to include `recommendations`, `fallback`, and `category`.
- [x] Keep invalid category 422 response detail unchanged.
- [x] Update root help good example for category recommendations to show object response format.
- [x] Update tests for new response contract:
  - [x] base recommendations endpoint assertions
  - [x] category recommendations endpoint assertions
  - [x] root help examples remain covered
- [ ] Run verification:
  - [ ] `uv run ruff format .`
  - [ ] `uv run ruff check .`
  - [ ] `uv run pytest`

## Out of Scope

- Making `fallback` dynamically true in any scenario
- Changing endpoint routes or category allowlist values
- Adding persistence or external services

## Open Questions

- None
