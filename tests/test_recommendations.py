from uuid import UUID

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_recommendations_returns_200() -> None:
    response = client.get("/recommendations")
    assert response.status_code == 200


def test_recommendations_returns_json_content_type() -> None:
    response = client.get("/recommendations")
    assert response.headers["content-type"].startswith("application/json")


def test_recommendations_returns_ten_uuid_strings() -> None:
    response = client.get("/recommendations")
    payload = response.json()

    assert isinstance(payload, list)
    assert len(payload) == 10
    for item in payload:
        assert isinstance(item, str)
        UUID(item)


def test_recommendations_are_regenerated_per_request() -> None:
    first = client.get("/recommendations").json()
    second = client.get("/recommendations").json()
    assert set(first) != set(second)
