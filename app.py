import streamlit as st
import joblib
import numpy as np

# Page config (responsive feel)
st.set_page_config(page_title="Bike Demand App", layout="centered")

# Load model
try:
    model = joblib.load("best_model.pkl")
except:
    st.error("Model not loading. Check .pkl file.")
    st.stop()

# Title
st.title("🚴 Bike Demand Prediction")
st.markdown("### Enter details below")

# Use columns for better UI
col1, col2 = st.columns(2)

with col1:
    season = st.selectbox("Season", [1, 2, 3, 4])
    yr = st.selectbox("Year", [0, 1])
    mnth = st.slider("Month", 1, 12)
    holiday = st.selectbox("Holiday", [0, 1])
    weekday = st.slider("Weekday", 0, 6)

with col2:
    workingday = st.selectbox("Working Day", [0, 1])
    weathersit = st.selectbox("Weather Condition", [1, 2, 3, 4])
    temp = st.slider("Temperature", 0.0, 1.0)
    atemp = st.slider("Feeling Temp", 0.0, 1.0)
    hum = st.slider("Humidity", 0.0, 1.0)
    windspeed = st.slider("Wind Speed", 0.0, 1.0)

st.markdown("---")

# Prediction
if st.button("🚀 Predict Demand"):
    try:
        features = np.array([[season, yr, mnth, holiday, weekday,
                              workingday, weathersit, temp,
                              atemp, hum, windspeed]])

        prediction = model.predict(features)

        st.success(f"🎯 Predicted Bike Count: {int(prediction[0])}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
