import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .prediction-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
    }

    .prediction-value {
        font-size: 42px;
        font-weight: 700;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("salary_prediction_model.pkl")

model = load_model()

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">💰 Employee Salary Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict the average salary using job, company and skill information.</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Job Information
# -----------------------------
st.markdown('<div class="section-title">💼 Job Information</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    job_title = st.text_input(
        "Job Title",
        "Data Scientist"
    )

    location = st.text_input(
        "Location",
        "New York, NY"
    )

    industry = st.text_input(
        "Industry",
        "Biotech & Pharmaceuticals"
    )

    sector = st.text_input(
        "Sector",
        "Biotech & Pharmaceuticals"
    )

with col2:
    size = st.selectbox(
        "Company Size",
        [
            "1 to 50 employees",
            "51 to 200 employees",
            "201 to 500 employees",
            "501 to 1000 employees",
            "1001 to 5000 employees",
            "5001 to 10000 employees",
            "10000+ employees"
        ]
    )

    ownership = st.selectbox(
        "Type of Ownership",
        [
            "Company - Private",
            "Company - Public",
            "Nonprofit Organization",
            "Subsidiary or Business Segment"
        ]
    )

    revenue = st.text_input(
        "Revenue",
        "Unknown / Non-Applicable"
    )

    rating = st.slider(
        "Company Rating",
        0.0,
        5.0,
        3.5,
        0.1
    )

# -----------------------------
# Company Information
# -----------------------------
st.markdown('<div class="section-title">🏢 Company Information</div>',
            unsafe_allow_html=True)

age = st.number_input(
    "Company Age (years)",
    min_value=0,
    max_value=300,
    value=20
)

employer_provided = st.selectbox(
    "Employer Provided Salary?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# -----------------------------
# Skills
# -----------------------------
st.markdown('<div class="section-title">🧠 Required Skills</div>',
            unsafe_allow_html=True)

skill1, skill2, skill3, skill4, skill5 = st.columns(5)

with skill1:
    python_yn = st.selectbox(
        "Python",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with skill2:
    r_yn = st.selectbox(
        "R",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with skill3:
    spark = st.selectbox(
        "Spark",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with skill4:
    aws = st.selectbox(
        "AWS",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with skill5:
    excel = st.selectbox(
        "Excel",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button(
    "🔮 Predict Salary",
    use_container_width=True
):

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

    st.markdown(
        f"""
        <div class="prediction-box">
            <div>Predicted Average Salary</div>
            <div class="prediction-value">${prediction:.2f}K</div>
            <div>Estimated annual salary</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Prediction generated successfully! 🎉")
