import streamlit as st
import joblib
import numpy as np

# Page config
st.set_page_config(page_title="Bike Demand App", layout="centered")

# Custom CSS (THIS makes it look premium)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
    }

    .main-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }

    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }

    .stSlider, .stSelectbox {
        background-color: rgba(255,255,255,0.05);
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
try:
    model = joblib.load("best_model.pkl")
except:
    st.error("Model not loading. Check your .pkl file.")
    st.stop()

# Title
st.markdown("## 🚴 Bike Demand Prediction")



# Layout
col1, col2 = st.columns(2)

with col1:
    temperature = st.slider("🌡 Temperature", 0.0, 1.0, 0.5)
    humidity = st.slider("💧 Humidity", 0.0, 1.0, 0.5)

with col2:
    windspeed = st.slider("🌬 Wind Speed", 0.0, 1.0, 0.2)
    season = st.selectbox("🌸 Season", [1, 2, 3, 4])

st.markdown("</div>", unsafe_allow_html=True)

# Predict
if st.button("🚀 Predict Demand"):
    features = np.array([[temperature, humidity, windspeed, season]])
    prediction = model.predict(features)

    st.success(f"🎯 Predicted Bike Count: {int(prediction[0])}")
