from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from backend.utils import get_weather

app = FastAPI()

model = joblib.load("model/heat_stress_model.pkl")


# Request schema
class UserInput(BaseModel):
    city: str
    age: int
    working_hours: int
    hydration_level: int


@app.get("/")
def home():
    return {"message": "AI Urban Heat Stress Predictor API Running"}


@app.post("/predict")
def predict(data: UserInput):

    try:
        weather = get_weather(data.city)

        features = np.array([[
            weather["temperature"],
            weather["humidity"],
            weather["wind_speed"],
            weather["uv_index"],
            data.age,
            data.working_hours,
            data.hydration_level
        ]])

        risk_score = float(model.predict(features)[0])

        if risk_score < 25:
            category = "Safe"
        elif risk_score < 50:
            category = "Moderate"
        elif risk_score < 75:
            category = "High"
        else:
            category = "Critical"

        return {
            "city": data.city,
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "risk_score": round(risk_score, 2),
            "category": category
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))