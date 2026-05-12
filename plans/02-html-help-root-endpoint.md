# Stage 02 - HTML Help at Root Endpoint

## Goal

Implement a student-facing `GET /` endpoint that returns HTML help content describing currently implemented API endpoints and how to use them.

## Context

- Related files: `src/app.py`, `tests/test_healthcheck.py`, `tests/test_root_help.py` (new)
- Related issues or links: Stage 02 brief for HTML help page at `/`
- Constraints:
  - Keep the existing `/healthcheck` behavior unchanged.
  - Root endpoint must return HTML, not JSON.
  - GET endpoints should be shown as plain links.
  - POST endpoints should be shown with `curl` usage examples when they exist.

## Approach

Add a small HTML response from `GET /` using FastAPI's `HTMLResponse`. The page will list current implemented endpoints by method and usage style. For this stage, `GET /healthcheck` is documented as a clickable link. Add focused tests that verify status code, HTML content type, and expected documentation text/link output.

## Steps

- [ ] Add `GET /` in `src/app.py` with `response_class=HTMLResponse`.
- [ ] Return a readable HTML page with a title and endpoint sections.
- [ ] Include a clickable link for `GET /healthcheck`.
- [ ] Include a POST section that defines the `curl` pattern for POST endpoints.
- [ ] Add tests in `tests/test_root_help.py` for:
  - [ ] HTTP 200 from `/`
  - [ ] `text/html` content type
  - [ ] presence of `/healthcheck` link
  - [ ] presence of POST + `curl` guidance text
- [ ] Run verification commands:
  - [ ] `uv run ruff format .`
  - [ ] `uv run ruff check .`
  - [ ] `uv run pytest`

## Testing Plan

- Unit-style endpoint tests with `fastapi.testclient.TestClient`.
- Positive coverage for content type and key student-facing strings.
- Regression check to ensure existing healthcheck tests still pass unchanged.

## Out of Scope

- Auto-discovering routes dynamically from `app.routes`
- Advanced HTML styling or templating engines
- Adding new business endpoints beyond help/documentation route

## Open Questions

- Should the help page later be generated dynamically as the endpoint list grows?
