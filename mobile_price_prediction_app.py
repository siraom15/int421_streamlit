import pandas as pd
import re
import streamlit as st
from sklearn.linear_model import LinearRegression
import joblib

# Load the trained model
model_filename = "linear_regression_model.pkl"
loaded_model = joblib.load(model_filename)

# Streamlit app
st.title("Mobile Price Prediction")

# Sidebar for user input
st.sidebar.header("Input Features")

# User input for RAM
ram = st.sidebar.slider("RAM (in GB)", min_value=1, max_value=16, value=8)

# User input for ROM/Storage
rom_storage = st.sidebar.slider("ROM/Storage (in GB)", min_value=16, max_value=512, value=128)

# User input for Battery
battery = st.sidebar.slider("Battery (mAh)", min_value=1000, max_value=10000, value=4000)

# User input for Rating
rating = st.sidebar.slider("Rating ?/5", min_value=1.0, max_value=5.0, value=4.5)

# Create a DataFrame from the user input
new_data_point = pd.DataFrame({'RAM': [ram], 'ROM/Storage': [rom_storage], 'Battery': [battery], 'Rating ?/5': [rating]})

# Predict the price using the loaded model
predicted_price = loaded_model.predict(new_data_point)

# Display the predicted price
st.header("Predicted Price in INR")
st.write(predicted_price[0])
