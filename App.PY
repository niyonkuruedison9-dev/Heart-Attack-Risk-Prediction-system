# -*- coding: utf-8 -*-
"""
Heart Attack Prediction App
Created on Wed Oct 15 09:03:52 2025
@author: user
"""

import streamlit as st
import pandas as pd
import joblib

# --- App Title ---
st.title("❤️ Heart Attack Risk Prediction App")

# --- Load Trained Model ---
model_path = "C:/Users/user/Desktop/Etude/Heart_attack.pkl"
model = joblib.load(open(model_path, "rb"))

# --- Define Mappings ---
sex_map = {"Female": 0, "Male": 1}
thal_map = {"fixed": 0, "normal": 1, "reversable": 2}
cp_map = {
    "asymptomatic": 0,
    "nonanginal": 1,
    "nontypical": 2,
    "typical": 3
}
slope_map = {
    "upsloping": 0,
    "flat": 1,
    "downsloping": 2
}

# --- Collect Inputs ---
st.subheader("🩺 Enter Patient Details")

# Create four columns for organized input layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    Age = st.number_input("Age", 0, 120, 45)
    Sex = st.selectbox("Sex", list(sex_map.keys()))
    ChestPain = st.selectbox("Chest Pain Type", list(cp_map.keys()))
    RestBP = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

with col2:
    Chol = st.number_input("Cholesterol (mg/dl)", 100, 400, 200)
    Fbs = st.number_input("Fasting Blood Sugar > 120 (1=True, 0=False)", 0, 1, 0)
    RestECG = st.number_input("Resting ECG (0–2)", 0, 2, 1)

with col3:
    MaxHR = st.number_input("Maximum Heart Rate", 60, 220, 150)
    ExAng = st.number_input("Exercise Induced Angina (1=True, 0=False)", 0, 1, 0)
    Oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)

with col4:
    Slope = st.selectbox("Slope of Peak Exercise ST Segment", list(slope_map.keys()))
    Ca = st.number_input("Number of Major Vessels (0–3)", 0, 3, 0)
    Thal = st.selectbox("Thalassemia", list(thal_map.keys()))

# --- Predict Button ---
if st.button("🔍 Predict Heart Attack Risk"):
    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Age": Age,
        "Sex": sex_map[Sex],
        "ChestPain": cp_map[ChestPain],
        "RestBP": RestBP,
        "Chol": Chol,
        "Fbs": Fbs,
        "RestECG": RestECG,
        "MaxHR": MaxHR,
        "ExAng": ExAng,
        "Oldpeak": Oldpeak,
        "Slope": slope_map[Slope],
        "Ca": Ca,
        "Thal": thal_map[Thal]
    }])

    # --- Make Prediction ---
    prediction = model.predict(input_df)[0]
    
    # If your model supports probabilities:
    try:
        probability = model.predict_proba(input_df)[0][1] * 100
    except:
        probability = None

    # --- Display Result ---
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Attack!")
        if probability is not None:
            st.write(f"Estimated Probability: {probability:.1f}%")
    else:
        st.success("✅ Low Risk of Heart Attack.")
        if probability is not None:
            st.write(f"Estimated Probability: {probability:.1f}%")

# --- Footer ---
st.caption("Developed by Edson — Machine Learning Heart Attack Prediction System")
