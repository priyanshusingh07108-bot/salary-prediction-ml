
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("salary_prediction_model.pkl")

st.title("💰 Employee Salary Prediction")
st.write("Enter job details to predict the average salary.")

# User inputs
job_title = st.text_input("Job Title", "Data Scientist")

location = st.text_input("Location", "New York, NY")

size = st.selectbox(
    "Company Size",
    ["1 to 50 employees", "51 to 200 employees",
     "201 to 500 employees", "501 to 1000 employees",
     "1001 to 5000 employees", "5001 to 10000 employees",
     "10000+ employees"]
)

ownership = st.selectbox(
    "Type of ownership",
    ["Company - Private", "Company - Public",
     "Nonprofit Organization", "Subsidiary or Business Segment"]
)

industry = st.text_input("Industry", "Biotech & Pharmaceuticals")

sector = st.text_input("Sector", "Biotech & Pharmaceuticals")

revenue = st.text_input("Revenue", "Unknown / Non-Applicable")

rating = st.slider("Company Rating", 0.0, 5.0, 3.5)

age = st.number_input("Company Age", min_value=0, max_value=300, value=20)

employer_provided = st.selectbox(
    "Employer Provided Salary",
    [0, 1]
)

python_yn = st.selectbox("Python Required?", [0, 1])
r_yn = st.selectbox("R Required?", [0, 1])
spark = st.selectbox("Spark Required?", [0, 1])
aws = st.selectbox("AWS Required?", [0, 1])
excel = st.selectbox("Excel Required?", [0, 1])


if st.button("Predict Salary"):

    input_data = pd.DataFrame([{
        "Job Title": job_title,
        "Location": location,
        "Size": size,
        "Type of ownership": ownership,
        "Industry": industry,
        "Sector": sector,
        "Revenue": revenue,
        "Rating": rating,
        "age": age,
        "employer_provided": employer_provided,
        "python_yn": python_yn,
        "R_yn": r_yn,
        "spark": spark,
        "aws": aws,
        "excel": excel
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Average Salary: ${prediction:.2f}K")
