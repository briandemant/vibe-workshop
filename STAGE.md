# Stage 05 - Consistent Recommendation Response Format

## Goal

Make the recommendation endpoints return a single, shared JSON response format so clients can parse responses the same way every time.

## Why this matters

Right now `GET /recommendations` and `GET /recommendations/{category}` both return a bare JSON array. That works, but in real APIs you almost always want a JSON object with named fields so you can extend the response later (metadata, flags, pagination, etc.) without breaking clients.

In this stage you will introduce that structure.

## The shared response format

All recommendation endpoints must return a JSON object with this shape:

```json
{
  "recommendations": ["..."],
  "fallback": false
}
```

- `recommendations` is the list of recommendation IDs (same generation rules as before).
- `fallback` is a boolean. For now it is always `false`.

The category endpoint must additionally include the requested category:

```json
{
  "recommendations": ["..."],
  "fallback": false,
  "category": "drama"
}
```

## Your task

Update the existing endpoints so they conform to this shared format:

- `GET /recommendations`
- `GET /recommendations/{category}`

Requirements:

- Routes and HTTP methods stay the same.
- Recommendation ID generation rules stay the same.
- Successful responses return the JSON object shown above (not a bare array).
- The category endpoint includes the `category` field with the validated category value.
- Invalid category still returns HTTP 422 with the existing error detail.
- Update tests so they describe the new response shape clearly.
- Update the `/` help page so the documented examples reflect the new format.

## Suggested workflow

1. Look at the current responses for both endpoints.
2. Decide how to construct the new response object cleanly (avoid duplicating logic between the two endpoints).
3. Update each endpoint to return the new shape.
4. Update tests that asserted the old bare-array shape.
5. Update the help page examples (good and bad) to match the new format.
6. Run formatting, linting, and tests.

## Acceptance criteria

- `GET /recommendations` returns an object with `recommendations` (list of 10) and `fallback: false`.
- `GET /recommendations/{category}` returns an object with `recommendations` (list of 10), `fallback: false`, and `category` set to the requested category.
- Invalid category still returns HTTP 422 with the existing error detail.
- All tests pass.
- The `/` help page shows the new response format in its examples.

## Constraints

- Do not add persistence, auth, or new categories.
- Do not change ID generation rules.
- Keep changes focused and minimal.

## Definition of done

- Code is formatted and lint-clean (`uv run ruff format .`, `uv run ruff check .`).
- Tests pass (`uv run pytest`).
- API responses follow the shared format described above.
