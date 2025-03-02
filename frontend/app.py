# frontend/app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Backend API URL
API_URL = "http://127.0.0.1:5000"

# Title of the app
st.title("Daily Step Tracker Dashboard")

# Upload step count data
st.header("Upload Step Count Data")
date = st.date_input("Date")
step_count = st.number_input("Step Count", min_value=0)
if st.button("Upload"):
    response = requests.post(f"{API_URL}/upload", json={"date": str(date), "step_count": step_count})
    if response.status_code == 200:
        st.success("Data uploaded successfully!")
    else:
        st.error("Failed to upload data.")

# Fetch and display historical data
st.header("Historical Data")
if st.button("Fetch Data"):
    response = requests.get(f"{API_URL}/data")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.write(df)
    else:
        st.error("Failed to fetch data.")

# Generate and display predictions
st.header("Step Count Predictions")
if st.button("Predict Next 7 Days"):
    response = requests.get(f"{API_URL}/predict")
    if response.status_code == 200:
        predictions = response.json()["predictions"]
        st.write("Predicted Step Counts for the Next 7 Days:")
        for i, steps in enumerate(predictions, start=1):
            st.write(f"Day {i}: {steps:.2f} steps")

        # Plot the predictions
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, 8), predictions, marker='o')
        plt.title("Predicted Step Counts for the Next 7 Days")
        plt.xlabel("Day")
        plt.ylabel("Step Count")
        st.pyplot(plt)
    else:
        st.error("Failed to generate predictions.")