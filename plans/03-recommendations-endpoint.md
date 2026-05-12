# Stage 03 - Recommendations Endpoint

## Goal

Add a `GET /recommendations` endpoint to the FastAPI app that returns a JSON array of 10 random UUID strings, generated fresh per request. Also update the `/` HTML help page to include the new endpoint.

## Context

- Related files:
  - `src/app.py` (route registration, alongside existing `/` and `/healthcheck`)
  - `tests/test_recommendations.py` (new)
  - `tests/test_root_help.py` (extend with recommendations link assertion)
  - `STAGE.md` (student-facing brief for this stage)
- Related issues or links: Stage 03 brief - add `/recommendations` endpoint returning 10 random UUIDs.
- Constraints:
  - Response must be valid JSON.
  - Response body must be an array (list) of exactly 10 items.
  - Each item must be a string in UUID format.
  - Values must be randomly generated per request.
  - Keep existing `/healthcheck` behavior unchanged.
  - Keep `/` returning HTML and extend its GET endpoint list to include `/recommendations`.
  - Use Python stdlib `uuid` (no new dependency).

## Approach

Add a handler in `src/app.py` that returns a `list[str]` of 10 `uuid.uuid4()` values converted to strings. FastAPI will serialize the list as JSON. Extend the root help HTML to list `GET /recommendations` under GET endpoints. Add focused tests that verify HTTP status, JSON content type, response shape, item UUID validity, per-request regeneration, and root help link visibility.

## Steps

- [ ] Add `GET /recommendations` in `src/app.py` returning `list[str]`.
- [ ] Generate values with `uuid.uuid4()` for each request.
- [ ] Update `root_help()` in `src/app.py` to include a link for `GET /recommendations` under GET endpoints.
- [ ] Add `tests/test_recommendations.py` to verify:
  - [ ] HTTP 200 from `/recommendations`
  - [ ] JSON content type
  - [ ] list length is 10
  - [ ] each item parses as a valid UUID
  - [ ] two requests return different sets of UUIDs
- [ ] Extend `tests/test_root_help.py` to verify:
  - [ ] `href="/recommendations"` is present
  - [ ] `GET /recommendations` text is present
- [ ] Run verification commands:
  - [ ] `uv run ruff format .`
  - [ ] `uv run ruff check .`
  - [ ] `uv run pytest`

## Testing Plan

- Use `fastapi.testclient.TestClient` for endpoint tests.
- Validate shape and UUID format using `uuid.UUID(...)` parsing.
- Check for per-request randomness by comparing two responses.
- Keep existing healthcheck and root help tests passing, including the new recommendations link assertions.

## Out of Scope

- Persisting recommendations.
- Query parameters like configurable result count.
- Authentication/rate limiting.
- Additional business logic beyond UUID generation.

## Open Questions

- None.
