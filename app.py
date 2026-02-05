import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Customer Churn Prediction")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("📉 Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict Churn"):
    features = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error(" Customer is likely to churn")
    else:
        st.success(" Customer is likely to stay")
