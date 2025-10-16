# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 09:03:52 2025

@author: user
"""

import joblib
import pandas as pd
import streamlit as st



st.title('Heart_attack.pkl')
loadedmodel=joblib.load(open('C:/Users/user/Desktop/Etude/Heart_attack.pkl','rb'))

sex_mapping={
    "Female":0,
    "Male":1
    }
Thal_mapping={
    
    "fixed":0,
    "normal":1,
    "reversable":2
}
ChestPain_mapping={
    
    "typical":3,
    "asymptomatic":0,
    "nonanginal":1,
    "nontypical":2
}



Age=st.number_input('Number of age', min_value=0 ,max_value=100, value=45)
Sex=st.selectbox('sex status', list(sex_mapping.keys()))
RestBP=st.number_input('RestBP', min_value=100 ,max_value=200, value=145)
Chol	=st.number_input('Chol', min_value=0 ,max_value=400, value=200)
Fbs=st.number_input('level of Fbs', min_value=0 ,max_value=5, value=1)
RestECG=st.number_input('RestECG', min_value=0 ,max_value=5, value=2)
MaxHR=st.number_input('MaxHR', min_value=100, max_value=300, value=150)
ExAng	=st.number_input('ExAng', min_value=0 ,max_value=5, value=2)
Oldpeak=st.number_input('Oldpeak', min_value=0 ,max_value=10, value=3)
Thal=st.selectbox('Thal', list(Thal_mapping.keys()))
ChestPain=st.selectbox('ChestPain', list(ChestPain_mapping.keys()))


if st.button("Predict Heart attack"):
    input_df = pd.DataFrame([[Age, Sex, ChestPain, RestBP, Chol, Fbs, RestECG, MaxHR, ExAng, Thal]]),
    input_df.columns = ['Age', 'Sex', 'ChestPain', 'RestBP', 'Chol', 'Fbs', 'RestECG', 'MaxHR', 'ExAng', 'Thal']
    input_df["Sex"]=input_df["Sex"].map(sex_mapping)
    input_df["Thal"]=input_df["Thal"].map(Thal_mapping)
    input_df["ChestPain"]=input_df["ChestPain"].map(ChestPain_mapping)
    prediction=loadedmodel.predict(input_df)[0]
    st.success(f"Estimated Monthly Rent: {int(prediction):,} RWF")

if _name_ as '_name_':
    main()