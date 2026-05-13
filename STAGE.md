# Stage 09: Build a `/time` Endpoint with Input Validation

In this stage, you'll add a new API endpoint that returns the current time.
The goal is to practice route design, input validation, and clear API responses.

## What you are building

Add a new endpoint that tells the current time:

- Method + path: `GET /time`
- It should return the server's current time in a JSON response.
- It should support a simple input option (for example, selecting a time format).
- Invalid input should return a clear error response.

## Requirements

1. Add a `GET /time` endpoint to the FastAPI app.
2. Return JSON (not plain text).
3. Support one constrained query parameter for output formatting.
   - Example idea: a `format` query parameter with a small allowed set of values.
4. Handle invalid values with a proper `400` response and an informative error payload.
5. Update the root help page (`/`) to document this endpoint:
   - Include at least one good request example.
   - Include at least one bad request example and expected error shape.
   - Make allowed values discoverable from the help page.
6. Add or update tests for:
   - Successful `/time` call(s)
   - Invalid input behavior
   - Root help page coverage for the new endpoint docs

## Acceptance checklist

- [ ] `/time` works and returns current time as JSON
- [ ] Invalid input returns `400` with clear error details
- [ ] `/` help page includes good and bad `/time` examples
- [ ] Tests pass
- [ ] Coverage remains at 100%

## Hints

- Keep implementation small and focused.
- Reuse response patterns already present in this repository.
- Let tests drive edge-case behavior before polishing output format.
