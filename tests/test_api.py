from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict():
    payload = {
        "city": "Delhi",
        "age": 30,
        "working_hours": 8,
        "hydration_level": 3
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "temperature" in data
    assert "humidity" in data
    assert "risk_score" in data
    assert "category" in data