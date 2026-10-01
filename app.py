import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="SalaryIQ | AI Salary Predictor",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

/* ---------- GLOBAL ---------- */
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.18), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,0.14), transparent 28%),
        linear-gradient(135deg, #07111f 0%, #0b1220 45%, #111827 100%);
    color: #f8fafc;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ---------- HEADER ---------- */
.hero {
    padding: 35px 40px;
    border-radius: 24px;
    background:
        linear-gradient(135deg,
        rgba(37,99,235,0.30),
        rgba(124,58,237,0.25));
    border: 1px solid rgba(148,163,184,0.20);
    box-shadow: 0 20px 60px rgba(0,0,0,0.30);
    margin-bottom: 28px;
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    background: rgba(59,130,246,0.16);
    border: 1px solid rgba(96,165,250,0.30);
    color: #93c5fd;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0;
    background: linear-gradient(90deg, #ffffff, #93c5fd, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 17px;
    margin-top: 12px;
    max-width: 700px;
}

/* ---------- SECTION CARDS ---------- */
.section-card {
    padding: 24px;
    border-radius: 20px;
    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(148,163,184,0.16);
    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
    margin-bottom: 20px;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 3px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 13px;
    margin-bottom: 18px;
}

/* ---------- INPUTS ---------- */
.stTextInput input,
.stNumberInput input {
    background: rgba(15,23,42,0.85) !important;
    color: white !important;
    border: 1px solid rgba(148,163,184,0.22) !important;
    border-radius: 12px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(15,23,42,0.85) !important;
    border-radius: 12px !important;
    border-color: rgba(148,163,184,0.22) !important;
}

label {
    color: #cbd5e1 !important;
    font-weight: 500 !important;
}

/* ---------- BUTTON ---------- */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    color: white;
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    box-shadow: 0 10px 30px rgba(79,70,229,0.35);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 35px rgba(79,70,229,0.48);
}

/* ---------- PREDICTION ---------- */
.prediction-card {
    margin-top: 28px;
    padding: 35px;
    border-radius: 24px;
    text-align: center;
    background:
        linear-gradient(135deg,
        rgba(16,185,129,0.16),
        rgba(37,99,235,0.18));
    border: 1px solid rgba(96,165,250,0.28);
    box-shadow: 0 20px 55px rgba(0,0,0,0.25);
}

.prediction-label {
    color: #a7f3d0;
    font-size: 15px;
    font-weight: 600;
}

.prediction-value {
    font-size: 52px;
    font-weight: 850;
    margin: 7px 0;
    background: linear-gradient(90deg, #34d399, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.prediction-note {
    color: #94a3b8;
    font-size: 14px;
}

/* ---------- METRIC CARDS ---------- */
.metric-card {
    padding: 18px;
    border-radius: 16px;
    background: rgba(15,23,42,0.70);
    border: 1px solid rgba(148,163,184,0.15);
    text-align: center;
}

.metric-title {
    color: #94a3b8;
    font-size: 12px;
}

.metric-value {
    color: #f8fafc;
    font-size: 22px;
    font-weight: 700;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    return joblib.load("salary_prediction_model.pkl")


model = load_model()


# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">

<div class="badge">🤖 MACHINE LEARNING • RANDOM FOREST</div>

<div class="hero-title">
AI Salary Predictor
</div>

<div class="hero-subtitle">
Estimate the average annual salary for a data & technology role
using job title, company information, experience and technical skills.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# JOB INFORMATION
# =========================================================
st.markdown("""
<div class="section-card">

<div class="section-title">💼 Job Information</div>

<div class="section-subtitle">
Tell us about the role you're applying for.
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


# =========================================================
# COMPANY DETAILS
# =========================================================
st.markdown("""
<div class="section-card">

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


# =========================================================
# SKILLS
# =========================================================
st.markdown("""
<div class="section-card">

<div class="section-title">🧠 Technical Skills</div>

<div class="section-subtitle">
Select the technologies required for the role.
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


# =========================================================
# PREDICT BUTTON
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button("✨  Predict My Salary")


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

    # -----------------------------
    # Main Prediction
    # -----------------------------
    st.markdown(f"""

    <div class="prediction-card">

        <div class="prediction-label">
        ✨ AI ESTIMATED AVERAGE SALARY
        </div>

        <div class="prediction-value">
        ${prediction:.2f}K
        </div>

        <div class="prediction-note">
        Estimated annual salary
        </div>

    </div>

    """, unsafe_allow_html=True)


    # -----------------------------
    # Metrics
    # -----------------------------
    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-title">
        ANNUAL ESTIMATE
        </div>

        <div class="metric-value">
        ${prediction:.2f}K
        </div>

        </div>
        """, unsafe_allow_html=True)


    with m2:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-title">
        MONTHLY ESTIMATE
        </div>

        <div class="metric-value">
        ${monthly:.2f}
        </div>

        </div>
        """, unsafe_allow_html=True)


    with m3:

        st.markdown("""
        <div class="metric-card">

        <div class="metric-title">
        MODEL
        </div>

        <div class="metric-value">
        Random Forest
        </div>

        </div>
        """, unsafe_allow_html=True)


    st.success(
        "🎉 Prediction generated successfully! "
        "This estimate is produced by a machine-learning model."
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">

SalaryIQ • AI-powered salary estimation<br>
Built with Python • Scikit-learn • Random Forest • Streamlit

</div>
""", unsafe_allow_html=True)

    st.success("Prediction generated successfully! 🎉")
