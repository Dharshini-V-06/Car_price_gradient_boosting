import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and LabelEncoder
with open('car_price.pkl', 'rb') as f:
    model, le = pickle.load(f)

st.title("Car Price Prediction App 🚗")

st.markdown("""
This app predicts the **Selling Price** of a car based on its features.
""")

# Sidebar inputs
st.sidebar.header("Car Details")

year = st.sidebar.number_input("Year of Purchase", min_value=2000, max_value=2025, value=2015)
present_price = st.sidebar.number_input("Present Price (in Lakhs)", min_value=0.1, value=5.0)
kms_driven = st.sidebar.number_input("Kms Driven", min_value=0, value=20000)
owner = st.sidebar.selectbox("Number of Previous Owners", [0,1,2,3])

fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.sidebar.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.sidebar.selectbox("Transmission Type", ["Manual", "Automatic"])

# Convert categorical features using the LabelEncoder
fuel_type_encoded = le.fit_transform([fuel_type])[0]
seller_type_encoded = le.fit_transform([seller_type])[0]
transmission_encoded = le.fit_transform([transmission])[0]

# Prepare input for prediction
input_data = np.array([[year, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]])

# Predict button
if st.button("Predict Selling Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs")
