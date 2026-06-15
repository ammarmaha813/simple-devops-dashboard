from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_api_info_endpoint_returns_application_details() -> None:
    response = client.get("/api/info")
    payload = response.json()

    assert response.status_code == 200
    assert payload["app"] == "DevOps Dashboard"
    assert payload["version"] == "1.0.0"
    assert payload["status"] == "healthy"


def test_api_time_endpoint_returns_current_time() -> None:
    response = client.get("/api/time")
    payload = response.json()

    assert response.status_code == 200
    assert "time" in payload
    assert isinstance(payload["time"], str)
    assert payload["time"]
