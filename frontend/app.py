import streamlit as st
import requests
import time

# Backend API URL (Render)
API_URL = "https://ai-urban-heat-stress-predictor.onrender.com/predict"

# Page configuration
st.set_page_config(
    page_title="AI Urban Heat Stress Predictor",
    page_icon="🌡️",
    layout="centered"
)

# Title
st.title("🌡️ AI Urban Heat Stress Predictor")
st.write("Predict heat stress risk using weather and personal factors.")

st.markdown("---")

# City input
city = st.text_input("Enter City", "Delhi")

# Age slider
age = st.slider("Age", 18, 80, 30)

# Working hours slider
working_hours = st.slider("Working Hours per Day", 1, 12, 8)

# Hydration slider
hydration_level = st.slider("Hydration Level (1=Low, 5=High)", 1, 5, 3)

st.markdown("---")

# Predict button
if st.button("Predict Heat Stress Risk"):

    data = {
        "city": city,
        "age": age,
        "working_hours": working_hours,
        "hydration_level": hydration_level
    }

    try:
        with st.spinner("Contacting backend and fetching weather data..."):
            response = requests.post(API_URL, json=data, timeout=60)

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction Successful")

            st.subheader("Prediction Result")

            st.write(f"**City:** {result['city']}")
            st.write(f"**Temperature:** {result['temperature']} °C")
            st.write(f"**Humidity:** {result['humidity']} %")
            st.write(f"**Risk Score:** {result['risk_score']}")

            category = result["category"]

            if category == "Safe":
                st.success(f"Risk Category: {category}")
            elif category == "Moderate":
                st.warning(f"Risk Category: {category}")
            else:
                st.error(f"Risk Category: {category}")

        else:
            st.error("Backend returned an error. Please try again.")

    except requests.exceptions.RequestException:
        st.warning(
            "Backend server is waking up (Render free tier). "
            "Please wait 30 seconds and click Predict again."
        )
