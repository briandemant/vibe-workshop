# Stage 03: Recommendations Endpoint

In this stage, you will add a new API endpoint that returns recommendation IDs.

## Goal

Create a `GET /recommendations` endpoint that responds with a JSON array of 10 random UUID strings.

## Requirements

- Add a new route at `GET /recommendations`.
- The response body must be JSON.
- Return exactly 10 items.
- Each item must be a UUID string.
- UUID values should be randomly generated per request.

## Acceptance Criteria

Your stage is complete when all of the following are true:

- Requesting `GET /recommendations` returns HTTP `200`.
- The response is valid JSON.
- The response is an array with length `10`.
- Every item is a string in UUID format.
- Repeated requests return different values often enough to show randomness.

## Notes

- Reuse existing project patterns for route registration and response handling.
- Keep implementation small and focused.
- Do not add persistence for this stage.
