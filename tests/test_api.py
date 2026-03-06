from fastapi.testclient import TestClient
from backend.app import app

# create test client
client = TestClient(app)


def test_home_endpoint():
    """
    Test the root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_endpoint():
    """
    Test prediction endpoint
    """

    payload = {
        "city": "Delhi",
        "age": 30,
        "working_hours": 8,
        "hydration_level": 3
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "city" in data
    assert "temperature" in data
    assert "humidity" in data
    assert "risk_score" in data
    assert "category" in data


def test_invalid_input():
    """
    Test invalid input case
    """

    payload = {
        "city": "",
        "age": -1,
        "working_hours": -5,
        "hydration_level": 0
    }

    response = client.post("/predict", json=payload)

    # expecting error or handled response
    assert response.status_code in [200, 400]