import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('model.pkl')

# Set the title and description of the app
st.title("House Price Prediction Model")
st.write("This app predicts house prices based on features such as SqFt, Bedrooms, and Bathrooms.")

# Get user input for the features
sqft = st.number_input("Enter Square Footage (SqFt):", min_value=0)
bedrooms = st.number_input("Enter Number of Bedrooms:", min_value=0)
bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=0)

# Create a DataFrame from the inputs
input_data = pd.DataFrame({
    'Aera': [sqft],
    'Bedrooms': [bedrooms],
    'Bathrooms': [bathrooms]
})

# Make predictions when the user clicks the button
if st.button('Predict Price'):
    # Ensure the model is loaded and predict the house price
    prediction = model.predict(input_data)
    
    # Show the prediction result
    st.write(f"The predicted house price is:₹.{prediction[0]}")
