import streamlit as st
import requests

# Backend API URL
API_URL ="https://ai-urban-heat-stress-predictor.onrender.com/predict"

st.set_page_config(page_title="Urban Heat Stress Predictor", layout="centered")

st.title("🌡 AI Urban Heat Stress Predictor")

st.markdown("Predict heat stress risk using weather and personal factors.")

st.divider()

# User Inputs
city = st.text_input("Enter City", "Delhi")

age = st.slider("Age", 18, 65, 30)

working_hours = st.slider("Working Hours per Day", 1, 12, 8)

hydration_level = st.slider("Hydration Level (1=Low, 5=High)", 1, 5, 3)

st.divider()

# Predict Button
if st.button("Predict Heat Stress Risk"):

    data = {
        "city": city,
        "age": age,
        "working_hours": working_hours,
        "hydration_level": hydration_level
    }

    try:
        response = requests.post(API_URL, json=data)
        result = response.json()

        st.subheader("Prediction Result")

        st.write(f"📍 City: **{result['city']}**")
        st.write(f"🌡 Temperature: **{result['temperature']}°C**")
        st.write(f"💧 Humidity: **{result['humidity']}%**")

        st.write(f"⚠ Risk Score: **{result['risk_score']}**")
        st.write(f"🚨 Category: **{result['category']}**")

        # Alerts
        if result["category"] == "Safe":
            st.success("Low heat stress risk. Stay hydrated.")

        elif result["category"] == "Moderate":
            st.warning("Moderate heat stress risk. Drink more water.")

        elif result["category"] == "High":
            st.error("High heat stress risk. Avoid outdoor work.")

        else:
            st.error("Critical heat stress risk! Seek shade and hydration immediately.")

    except Exception as e:
        st.error(f"Error: {e}")