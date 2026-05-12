# Stage 04 - Category-Based Recommendations

## Goal

Add a category-specific recommendations endpoint that returns 10 generated IDs for a requested allowed category. IDs are fake UUID-shaped strings where the first section is the requested category padded to 8 characters.

## Context

- Related files: `src/app.py`, `tests/test_category_recommendations.py` (new)
- Constraints:
  - Allowed categories: `action`, `børn`, `comedy`, `drama`, `entertainment`.
  - Valid category returns HTTP 200 and JSON array of length 10.
  - Each returned ID uses `8-4-4-4-12` sections, with first section as zero-padded category.
  - Invalid category returns HTTP 422 and includes allowed categories.
  - Existing endpoints remain working.

## Approach

Add `GET /recommendations/{category}` in `src/app.py`. Validate the category against a constant allowlist and raise `HTTPException(status_code=422, detail=...)` for invalid values. For valid values, generate IDs from `uuid4()` by replacing the first section with `category.ljust(8, "0")`.

## Steps

- [ ] Add category allowlist and `GET /recommendations/{category}` endpoint.
- [ ] Return 422 JSON detail with allowed categories for invalid category.
- [ ] Generate 10 category-prefixed UUID-shaped recommendation IDs for valid category.
- [ ] Add tests for:
  - [ ] valid category returns 200 and 10 items
  - [ ] first section equals padded category
  - [ ] shape of remaining sections is `4-4-4-12`
  - [ ] invalid category returns 422 and includes allowed categories
- [ ] Run verification:
  - [ ] `uv run ruff format .`
  - [ ] `uv run ruff check .`
  - [ ] `uv run pytest`

## Out of Scope

- Persistence or database-backed recommendations
- Authentication and authorization
- Custom category management beyond the fixed allowlist

## Open Questions

- None
