from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_healthcheck_returns_200() -> None:
    response = client.get("/healthcheck")
    assert response.status_code == 200


def test_healthcheck_message_prefix() -> None:
    response = client.get("/healthcheck")
    message = response.json()["message"]
    assert message.startswith("hello the time is")
