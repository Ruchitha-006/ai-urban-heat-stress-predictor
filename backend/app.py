from fastapi import FastAPI, HTTPException
import numpy as np
import joblib
from backend.utils import get_weather

# Initialize FastAPI
app = FastAPI(
    title="AI Urban Heat Stress Predictor",
    description="Predicts heat stress risk using weather data and user inputs",
    version="1.0"
)

# Load trained ML model
model = joblib.load("model/heat_stress_model.pkl")


@app.get("/")
def home():
    return {"message": "AI Urban Heat Stress Predictor API Running"}


@app.post("/predict")
def predict(data: dict):
    """
    Predict heat stress risk based on:
    - city
    - age
    - working_hours
    - hydration_level
    """

    try:
        city = data["city"]
        age = data["age"]
        working_hours = data["working_hours"]
        hydration_level = data["hydration_level"]

        # Get weather data
        weather = get_weather(city)

        temperature = weather["temperature"]
        humidity = weather["humidity"]
        wind_speed = weather["wind_speed"]
        uv_index = weather["uv_index"]

        # Prepare ML input
        features = np.array([[
            temperature,
            humidity,
            wind_speed,
            uv_index,
            age,
            working_hours,
            hydration_level
        ]])

        # Predict risk score
        risk_score = float(model.predict(features)[0])

        # Risk category
        if risk_score < 25:
            category = "Safe"
        elif risk_score < 50:
            category = "Moderate"
        elif risk_score < 75:
            category = "High"
        else:
            category = "Critical"

        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "risk_score": round(risk_score, 2),
            "category": category
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))