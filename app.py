import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and label encoders
with open('car_price.pkl', 'rb') as f:
    model, le_fuel, le_seller, le_transmission = pickle.load(f)

st.title("🚗 Car Selling Price Prediction")

st.sidebar.header("Enter Car Details:")

# User Inputs
year = st.sidebar.number_input("Year of Purchase", min_value=2003, max_value=2018, value=2015)
present_price = st.sidebar.number_input("Present Price of the Car (in Lakhs)", min_value=0.1, max_value=100.0, value=5.0)
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=500, max_value=500000, value=20000)
fuel_type = st.sidebar.selectbox("Fuel Type", le_fuel.classes_)
seller_type = st.sidebar.selectbox("Seller Type", le_seller.classes_)
transmission = st.sidebar.selectbox("Transmission Type", le_transmission.classes_)
owner = st.sidebar.number_input("Number of Previous Owners", min_value=0, max_value=3, value=0)

# Encode categorical inputs using the saved encoders
fuel_type_encoded = le_fuel.transform([fuel_type])[0]
seller_type_encoded = le_seller.transform([seller_type])[0]
transmission_encoded = le_transmission.transform([transmission])[0]

# Prepare input for prediction
input_data = pd.DataFrame([[year, present_price, kms_driven, fuel_type_encoded,
                            seller_type_encoded, transmission_encoded, owner]],
                          columns=['Year', 'Present_Price', 'Kms_Driven',
                                   'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])

# Predict selling price
if st.button("Predict Selling Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted selling price of the car is: ₹ {prediction:.2f} Lakhs")
