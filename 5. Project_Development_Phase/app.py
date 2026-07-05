# OptiCrop - Streamlit Web Application
# Run with: streamlit run app.py
# Requires: model.pkl in the same folder (created by train_model.py)

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
from pathlib import Path
import pickle

MODEL_PATH = Path(__file__).parent / "model.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("model.pkl not found. Please run train_model.py first to generate the model.")
    st.stop()

st.set_page_config(page_title="OptiCrop", page_icon="🌾")

st.title("🌾 OptiCrop: Smart Crop Recommendation System")
st.write(
    "Enter your soil and climate parameters below to get the best-suited crop "
    "recommendation for your land."
)

# Input form
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=50.0)
    K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=50.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=400.0, value=100.0)

if st.button("Recommend Crop"):
    try:
        input_data = pd.DataFrame(
            [[N, P, K, temperature, humidity, ph, rainfall]],
            columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
        )
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        confidence = round(max(probabilities) * 100, 2)

        st.success(f"✅ Recommended Crop: **{prediction.upper()}** (Confidence: {confidence}%)")

        # Show top 3 alternate suggestions
        classes = model.classes_
        top3_idx = np.argsort(probabilities)[-3:][::-1]
        st.write("### Top 3 Suggestions:")
        for idx in top3_idx:
            st.write(f"- {classes[idx]} ({round(probabilities[idx]*100, 2)}%)")

    except Exception as e:
        st.error(f"Something went wrong while predicting: {e}")
        st.info("Please check that all input values are entered correctly and try again.")

st.markdown("---")
st.caption("OptiCrop | Smart Agricultural Crop Recommendation System | Built with Python & Streamlit")
