from fastapi import FastAPI, HTTPException
import numpy as np
import joblib
from backend.utils import get_weather

app = FastAPI()

# Load model
model = joblib.load("model/heat_stress_model.pkl")

@app.get("/")
def home():
    return {"message": "AI Urban Heat Stress Predictor API Running"}

@app.post("/predict")
def predict(data: dict):
    try:
        weather = get_weather(data["city"])

        features = np.array([[
            weather["temperature"],
            weather["humidity"],
            weather["wind_speed"],
            weather["uv_index"],
            data["age"],
            data["working_hours"],
            data["hydration_level"]
        ]])

        risk = float(model.predict(features)[0])

        if risk < 25:
            category = "Safe"
        elif risk < 50:
            category = "Moderate"
        elif risk < 75:
            category = "High"
        else:
            category = "Critical"

        return {
            "risk_score": round(risk, 2),
            "category": category
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
