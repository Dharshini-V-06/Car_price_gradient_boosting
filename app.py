import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model and label encoder
with open('car_price.pkl', 'rb') as f:
    model, le = pickle.load(f)

st.title("Car Price Prediction App")

st.sidebar.header("Enter Car Details:")

# User Inputs
year = st.sidebar.number_input("Year of Purchase", min_value=2003, max_value=2018, value=2015)
present_price = st.sidebar.number_input("Present Price of the Car (in Lakhs)", min_value=0.1, max_value=100.0, value=5.0)
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=500, max_value=500000, value=20000)
fuel_type = st.sidebar.selectbox("Fuel Type", ("Petrol", "Diesel", "CNG"))
seller_type = st.sidebar.selectbox("Seller Type", ("Dealer", "Individual"))
transmission = st.sidebar.selectbox("Transmission Type", ("Manual", "Automatic"))
owner = st.sidebar.number_input("Number of Previous Owners", min_value=0, max_value=3, value=0)

# Encode categorical inputs
fuel_type_encoded = le.fit_transform(["Petrol", "Diesel", "CNG"])[["Petrol","Diesel","CNG"].index(fuel_type)]
seller_type_encoded = le.fit_transform(["Dealer", "Individual"])[["Dealer","Individual"].index(seller_type)]
transmission_encoded = le.fit_transform(["Manual", "Automatic"])[["Manual","Automatic"].index(transmission)]

# Prepare input dataframe
input_data = pd.DataFrame([[year, present_price, kms_driven, fuel_type_encoded,
                            seller_type_encoded, transmission_encoded, owner]],
                          columns=['Year', 'Present_Price', 'Kms_Driven',
                                   'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])

# Predict
if st.button("Predict Selling Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted selling price of the car is: ₹ {prediction:.2f} Lakhs")
