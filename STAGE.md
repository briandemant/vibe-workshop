# Stage 04: Category-Based Recommendations

In this stage, you will add an endpoint that returns recommendations for a selected category. To make it obvious which category each recommendation belongs to, you will also tag the returned IDs with the category name.

## Goal

Create an API endpoint that accepts a category and returns category-tagged recommendation IDs only for that category.

## Allowed Categories

- `action`
- `børn`
- `comedy`
- `drama`
- `entertainment`

## Requirements

- Add a new endpoint for category-based recommendations.
- The endpoint must accept one category input from the allowed list.
- If the category is allowed, return a JSON array of 10 recommendation IDs.
- Each ID must be a UUID-shaped string whose first 8-character section is the category name, right-padded with zeros if shorter. Examples:
  - `drama000-695e-41b7-94a6-d8a31a32f892`
  - `action00-1f2c-4a9b-9d1e-2c7e9c1a55ab`
  - `børn0000-...-...-...-...`
- The remaining sections of the UUID must keep the standard 8-4-4-4-12 layout.
- If the category is not in the allowed list (or is missing), return HTTP `422` with a JSON body that:
  - Indicates the category value is invalid.
  - Includes the full list of allowed categories.
- Keep all existing endpoints working unchanged.

## Examples

### Good example 1 - valid category `drama`

Request:

```http
GET /recommendations/drama
```

Response: HTTP `200`

```json
[
  "drama000-695e-41b7-94a6-d8a31a32f892",
  "drama000-1f2c-4a9b-9d1e-2c7e9c1a55ab",
  "drama000-7a02-4c63-86b1-9d50f6e3a4d2",
  "drama000-0e3d-41f5-8a2c-1b3f0c4d5e6f",
  "drama000-2b6e-4ad9-9c8f-5e7a8b9c0d1e",
  "drama000-9c4b-4e3a-8d2f-3a4b5c6d7e8f",
  "drama000-44a1-4b22-9c33-1d2e3f405162",
  "drama000-6f9b-4c8d-9e2a-7b8c9d0e1f23",
  "drama000-3e5d-4a1b-9c2f-8a7b6c5d4e3f",
  "drama000-5b8c-4d9e-9a1f-2b3c4d5e6f70"
]
```

### Good example 2 - valid category `børn`

Request:

```http
GET /recommendations/børn
```

Response: HTTP `200`

```json
[
  "børn0000-695e-41b7-94a6-d8a31a32f892",
  "børn0000-1f2c-4a9b-9d1e-2c7e9c1a55ab",
  "børn0000-7a02-4c63-86b1-9d50f6e3a4d2"
]
```

Note: the response is still an array of length `10`; the snippet above is shortened for readability. Every item starts with `børn0000-` and follows the `8-4-4-4-12` layout.

### Bad example - invalid category `sport`

Request:

```http
GET /recommendations/sport
```

Response: HTTP `422`

```json
{
  "error": "invalid category",
  "category": "sport",
  "allowed_categories": ["action", "børn", "comedy", "drama", "entertainment"]
}
```

The exact JSON keys are illustrative; what matters is that the response is `422`, clearly signals the category is invalid, and lists the allowed categories.

## Acceptance Criteria

Your stage is complete when all of the following are true:

- A request with a valid category returns HTTP `200`.
- The response is valid JSON and is an array of length `10`.
- Every item matches the shape `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`.
- Every item's first section equals the category name, right-padded with zeros to length 8.
- A request with an invalid or missing category returns HTTP `422`.
- The `422` response body is JSON and includes the list of allowed categories.
- Repeated requests for the same valid category return different ID values (per-request generation).

## Notes

- This is a fake/mock service - the category prefix is for demo clarity, not real UUID semantics.
- Reuse existing project patterns for routes, responses, and error handling.
- Keep the implementation small and focused; no persistence in this stage.
- Choose a clear URL shape (path or query parameter) and validate the input.
