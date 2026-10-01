import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="SalaryIQ | AI Salary Predictor",
    page_icon="💼",
    layout="wide"
)

# =========================
# CUSTOM DESIGN
# =========================
st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(59,130,246,0.20), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(124,58,237,0.20), transparent 30%),
        linear-gradient(135deg, #07111f, #0f172a);
    color: white;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

.hero {
    padding: 40px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        rgba(37,99,235,0.30),
        rgba(124,58,237,0.25)
    );
    border: 1px solid rgba(148,163,184,0.20);
    margin-bottom: 30px;
}

.badge {
    color: #93c5fd;
    font-size: 13px;
    font-weight: 700;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    margin-top: 10px;
    background: linear-gradient(90deg,#ffffff,#60a5fa,#c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 17px;
    margin-top: 10px;
}

.section {
    padding: 25px;
    border-radius: 20px;
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(148,163,184,0.15);
    margin-bottom: 20px;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 13px;
    margin-bottom: 20px;
}

.stTextInput input,
.stNumberInput input {
    background: #111827 !important;
    color: white !important;
    border-radius: 12px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #111827 !important;
    border-radius: 12px !important;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    color: white;
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
}

.prediction {
    margin-top: 30px;
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(16,185,129,0.18),
        rgba(37,99,235,0.20)
    );
    border: 1px solid rgba(96,165,250,0.30);
}

.prediction-label {
    color: #a7f3d0;
    font-size: 15px;
    font-weight: 600;
}

.prediction-value {
    font-size: 52px;
    font-weight: 800;
    color: #34d399;
    margin: 8px 0;
}

.metric {
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(148,163,184,0.15);
}

.metric-title {
    color: #94a3b8;
    font-size: 12px;
}

.metric-value {
    font-size: 22px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():
    return joblib.load("salary_prediction_model.pkl")


model = load_model()


# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">

<div class="badge">🤖 AI • MACHINE LEARNING • RANDOM FOREST</div>

<div class="hero-title">
💼 SalaryIQ
</div>

<div class="hero-subtitle">
AI-powered salary prediction for data and technology professionals.
Estimate the average annual salary using job, company and skill information.
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# JOB INFORMATION
# =========================
st.markdown("""
<div class="section">

<div class="section-title">💼 Job Information</div>

<div class="section-subtitle">
Enter details about the position.
</div>

</div>
""", unsafe_allow_html=True)

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
        "Company Revenue",
        "Unknown / Non-Applicable"
    )

    rating = st.slider(
        "Company Rating",
        0.0,
        5.0,
        3.5,
        0.1
    )


# =========================
# COMPANY DETAILS
# =========================
st.markdown("""
<div class="section">

<div class="section-title">🏢 Company Details</div>

<div class="section-subtitle">
Additional information about the employer.
</div>

</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    age = st.number_input(
        "Company Age",
        min_value=0,
        max_value=300,
        value=20
    )

with c2:

    employer_provided = st.selectbox(
        "Employer Provided Salary",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# =========================
# SKILLS
# =========================
st.markdown("""
<div class="section">

<div class="section-title">🧠 Technical Skills</div>

<div class="section-subtitle">
Select technologies required for the role.
</div>

</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    python_yn = st.selectbox(
        "🐍 Python",
        [0, 1],
        format_func=lambda x: "Required" if x == 1 else "No"
    )

with s2:
    r_yn = st.selectbox(
        "📊 R",
        [0, 1],
        format_func=lambda x: "Required" if x == 1 else "No"
    )

with s3:
    spark = st.selectbox(
        "⚡ Spark",
        [0, 1],
        format_func=lambda x: "Required" if x == 1 else "No"
    )

with s4:
    aws = st.selectbox(
        "☁️ AWS",
        [0, 1],
        format_func=lambda x: "Required" if x == 1 else "No"
    )

with s5:
    excel = st.selectbox(
        "📗 Excel",
        [0, 1],
        format_func=lambda x: "Required" if x == 1 else "No"
    )


# =========================
# PREDICTION
# =========================
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button("✨ Predict My Salary")


if predict:

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

    monthly = prediction * 1000 / 12

    # Prediction Card
    st.markdown(
        f"""
        <div class="prediction">

        <div class="prediction-label">
        ✨ AI ESTIMATED AVERAGE SALARY
        </div>

        <div class="prediction-value">
        ${prediction:.2f}K
        </div>

        <div class="prediction-label">
        Estimated annual salary
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Metrics
    m1, m2, m3 = st.columns(3)

    with m1:

        st.markdown(
            f"""
            <div class="metric">

            <div class="metric-title">
            ANNUAL ESTIMATE
            </div>

            <div class="metric-value">
            ${prediction:.2f}K
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:

        st.markdown(
            f"""
            <div class="metric">

            <div class="metric-title">
            MONTHLY ESTIMATE
            </div>

            <div class="metric-value">
            ${monthly:.2f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with m3:

        st.markdown(
            """
            <div class="metric">

            <div class="metric-title">
            MODEL
            </div>

            <div class="metric-value">
            Random Forest
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        "🎉 Prediction generated successfully!"
    )


# =========================
# FOOTER
# =========================
st.markdown(
    """
    <div class="footer">

    SalaryIQ • AI-powered salary estimation<br>
    Built with Python • Scikit-learn • Random Forest • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)
