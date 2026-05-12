from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_category_recommendations_returns_ten_items() -> None:
    response = client.get("/recommendations/drama")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) == 10


def test_category_recommendations_use_category_prefix_and_uuid_shape() -> None:
    response = client.get("/recommendations/drama")
    payload = response.json()

    for item in payload:
        parts = item.split("-")
        assert len(parts) == 5
        assert parts[0] == "drama000"
        assert len(parts[1]) == 4
        assert len(parts[2]) == 4
        assert len(parts[3]) == 4
        assert len(parts[4]) == 12


def test_invalid_category_returns_422_with_allowed_categories() -> None:
    response = client.get("/recommendations/sport")

    assert response.status_code == 422
    body = response.json()
    detail = body["detail"]
    assert detail["error"] == "invalid category"
    assert detail["category"] == "sport"
    assert detail["allowed_categories"] == [
        "action",
        "børn",
        "comedy",
        "drama",
        "entertainment",
    ]
