import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/final_model.pkl")

st.set_page_config(page_title="Loan Approval Classifier", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant information below to predict loan approval.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income (Monthly)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (Monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Mapping categorical to numerical
def preprocess_input():
    gender_map = {"Male": 1, "Female": 0}
    married_map = {"Yes": 1, "No": 0}
    education_map = {"Graduate": 1, "Not Graduate": 0}
    self_employed_map = {"Yes": 1, "No": 0}
    property_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}
    dependents_map = {"0": 0, "1": 1, "2": 2, "3+": 3}

    return pd.DataFrame([{
        "Gender": gender_map[gender],
        "Married": married_map[married],
        "Dependents": dependents_map[dependents],
        "Education": education_map[education],
        "Self_Employed": self_employed_map[self_employed],
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_map[property_area]
    }])

# Predict button
if st.button("Predict"):
    input_df = preprocess_input()
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("✅ Loan will likely be approved!")
    else:
        st.error("❌ Loan will likely be rejected.")
