import streamlit as st
import pandas as pd
import joblib
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SalaryIQ | AI Salary Predictor",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# HTML HELPER
# =========================================================

def html(content):
    st.html(textwrap.dedent(content)
           )


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

[data-testid="stHeader"] {
    background: transparent !important;
}
.block-container {
    padding-top: 1rem !important;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(37, 99, 235, 0.20),
            transparent 28%
        ),
        radial-gradient(
            circle at 95% 5%,
            rgba(124, 58, 237, 0.20),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #071426 50%,
            #0b1025 100%
        );

    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding: 1.2rem 1.4rem 3rem 1.4rem;
}


/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #020617 0%,
            #06142b 60%,
            #081b35 100%
        );

    border-right: 1px solid rgba(96,165,250,0.18);
}

/* FORCE SIDEBAR VISIBLE */
[data-testid="stSidebar"] {
    transform: translateX(0) !important;
    visibility: visible !important;
    opacity: 1 !important;
    width: 300px !important;
    min-width: 300px !important;
}

[data-testid="stSidebar"][aria-expanded="false"] {
    transform: translateX(0) !important;
    visibility: visible !important;
    width: 300px !important;
    min-width: 300px !important;
}

.sidebar-brand {
    text-align: center;
    padding: 10px 5px 25px 5px;
}

.sidebar-logo {
    font-size: 42px;
}

.sidebar-name {
    font-size: 25px;
    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #60a5fa,
            #a78bfa
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sidebar-subtitle {
    color: #94a3b8;
    font-size: 12px;
}

.sidebar-card {
    padding: 18px;
    border-radius: 18px;

    background: rgba(15,23,42,0.70);

    border: 1px solid rgba(96,165,250,0.15);

    margin-top: 18px;
}

.sidebar-card-title {
    font-size: 15px;
    font-weight: 750;
    margin-bottom: 12px;
    color: #e2e8f0;
}

.sidebar-item {
    color: #dbeafe;
    padding: 7px 0;
    font-size: 13px;
}


/* =========================
   HERO
========================= */

.hero {
    padding: 35px 38px;

    min-height: 250px;

    border-radius: 26px;

    background:
        radial-gradient(
            circle at 75% 30%,
            rgba(59,130,246,0.30),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(124,58,237,0.30),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #102c62,
            #25205d
        );

    border: 1px solid rgba(96,165,250,0.30);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.35);

    position: relative;
    overflow: hidden;
}

.hero-badge {
    display: inline-block;

    padding: 7px 14px;

    border-radius: 999px;

    background: rgba(59,130,246,0.15);

    border: 1px solid rgba(96,165,250,0.35);

    color: #93c5fd;

    font-size: 12px;

    font-weight: 700;
}

.hero-title {
    font-size: 56px;

    line-height: 1;

    font-weight: 850;

    margin-top: 15px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #93c5fd,
            #c4b5fd
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-tagline {
    font-size: 22px;

    font-weight: 700;

    color: #60a5fa;

    margin-top: 10px;
}

.hero-description {
    color: #cbd5e1;

    max-width: 720px;

    font-size: 14px;

    line-height: 1.7;

    margin-top: 8px;
}


/* =========================
   SECTION CARD
========================= */

.section-card {
    padding: 21px;

    border-radius: 20px;

    background:
        rgba(8,20,40,0.82);

    border: 1px solid rgba(148,163,184,0.14);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.18);

    margin-bottom: 18px;
}

.section-title {
    font-size: 20px;

    font-weight: 750;
}

.section-subtitle {
    color: #64748b;

    font-size: 12px;

    margin-top: 4px;

    margin-bottom: 18px;
}


/* =========================
   INPUTS
========================= */

.stTextInput input,
.stNumberInput input {

    background: #0b1629 !important;

    color: #f8fafc !important;

    border: 1px solid #263b5a !important;

    border-radius: 11px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {

    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 1px #6366f1 !important;
}

.stSelectbox div[data-baseweb="select"] > div {

    background: #0b1629 !important;

    border: 1px solid #263b5a !important;

    border-radius: 11px !important;
}

label {
    color: #cbd5e1 !important;

    font-size: 13px !important;
}


/* =========================
   SKILL CARDS
========================= */

.skill-card {

    padding: 13px;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            rgba(15,30,55,0.95),
            rgba(8,20,40,0.95)
        );

    border: 1px solid rgba(96,165,250,0.16);

    text-align: center;

    min-height: 85px;
}

.skill-icon {
    font-size: 24px;
}

.skill-name {
    font-size: 13px;

    font-weight: 700;

    margin-top: 3px;
}


/* =========================
   PREDICT BUTTON
========================= */

.stButton > button {
    letter-spacing: 0.2px;
    cursor: pointer;

    width: 100%;

    height: 57px;

    border: none;

    border-radius: 14px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #4f46e5,
            #7c3aed
        );

    color: white;

    font-size: 17px;

    font-weight: 800;

    box-shadow:
        0 12px 35px rgba(79,70,229,0.38);

    transition: 0.2s;
}

.stButton > button:hover {

    transform: translateY(-2px)  scale(1.01);

    box-shadow:
        0 18px 45px rgba(79,70,229,0.52);
}


/* =========================
   RIGHT INFO CARDS
========================= */

.info-card {

    padding: 19px;

    border-radius: 19px;

    background:
        linear-gradient(
            145deg,
            rgba(25,25,70,0.82),
            rgba(10,20,45,0.90)
        );

    border: 1px solid rgba(124,58,237,0.25);

    margin-bottom: 17px;
}

.info-title {

    font-size: 18px;

    font-weight: 750;

    margin-bottom: 14px;
}

.info-row {

    color: #cbd5e1;

    font-size: 13px;

    line-height: 1.55;

    margin: 12px 0;
}


/* =========================
   RESULT
========================= */

.prediction-card {

    padding: 25px;

    border-radius: 22px;

    background:
        radial-gradient(
            circle at 15% 50%,
            rgba(16,185,129,0.22),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            rgba(5,70,65,0.82),
            rgba(8,35,55,0.92)
        );

    border: 1px solid rgba(52,211,153,0.32);

    box-shadow:
        0 20px 55px rgba(0,0,0,0.28);
}

.prediction-label {

    color: #a7f3d0;

    font-size: 13px;

    font-weight: 700;
}

.prediction-value {

    font-size: 50px;

    font-weight: 850;

    color: #34d399;

    margin: 3px 0;
}

.prediction-note {

    color: #94a3b8;

    font-size: 12px;
}


/* =========================
   METRIC CARDS
========================= */

.metric-card {

    padding: 19px;

    border-radius: 16px;

    background:
        rgba(10,25,45,0.90);

    border: 1px solid rgba(96,165,250,0.18);

    text-align: center;
}

.metric-title {

    color: #64748b;

    font-size: 11px;

    font-weight: 600;
}

.metric-value {

    color: #f8fafc;

    font-size: 20px;

    font-weight: 800;

    margin-top: 4px;
}


/* =========================
   FOOTER
========================= */

.footer {

    text-align: center;

    color: #475569;

    font-size: 11px;

    margin-top: 35px;
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
# SIDEBAR
# =========================================================

with st.sidebar:

    html("""
    <div class="sidebar-brand">

        <div class="sidebar-logo">📊</div>

        <div class="sidebar-name">
            SalaryIQ
        </div>

        <div class="sidebar-subtitle">
            AI Salary Predictor
        </div>

    </div>
    """)

    html("""
    <div class="sidebar-card">

        <div class="sidebar-card-title">
            🧭 Navigation
        </div>

        <div class="sidebar-item">
            🏠 Salary Predictor
        </div>

        <div class="sidebar-item">
            🧠 How It Works
        </div>

        <div class="sidebar-item">
            📊 Model Insights
        </div>

        <div class="sidebar-item">
            ℹ️ About Project
        </div>

    </div>
    """)

    html("""
    <div class="sidebar-card">

        <div class="sidebar-card-title">
            ⚙️ Powered By
        </div>

        <div class="sidebar-item">
            🐍 Python
        </div>

        <div class="sidebar-item">
            🐼 Pandas
        </div>

        <div class="sidebar-item">
            🧠 Scikit-learn
        </div>

        <div class="sidebar-item">
            🌲 Random Forest
        </div>

        <div class="sidebar-item">
            🚀 Streamlit
        </div>

    </div>
    """)

    html("""
    <div style="
        margin-top:35px;
        padding:12px;
        color:#64748b;
        font-size:12px;
        text-align:center;
    ">
        Better data.<br>
        Smarter predictions.<br>
        Better decisions.
    </div>
    """)


# =========================================================
# MAIN + RIGHT COLUMN
# =========================================================

main_col, right_col = st.columns(
    [3.55, 1.25],
    gap="large"
)


# =========================================================
# MAIN
# =========================================================

with main_col:

    # HERO

    html("""
    <div class="hero">

        <div class="hero-badge">
            🤖 AI • MACHINE LEARNING • RANDOM FOREST
        </div>

        <div class="hero-title">
            SalaryIQ
        </div>

        <div class="hero-tagline">
            Predict Smarter. Plan Better.
        </div>

        <div class="hero-description">
            AI-powered salary prediction for data and technology
            professionals. Enter job, company and technical skill
            information to estimate the average annual salary.
        </div>

    </div>
    """)


    # =====================================================
    # JOB INFORMATION
    # =====================================================

    html("""
    <div class="section-card">

        <div class="section-title">
            💼 Job Information
        </div>

        <div class="section-subtitle">
            Enter details about the position you're targeting.
        </div>

    </div>
    """)

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
            "⭐ Company Rating",
            0.0,
            5.0,
            3.5,
            0.1
        )


    # =====================================================
    # COMPANY DETAILS
    # =====================================================

    html("""
    <div class="section-card">

        <div class="section-title">
            🏢 Company Details
        </div>

        <div class="section-subtitle">
            Additional information about the employer.
        </div>

    </div>
    """)

    company1, company2 = st.columns(2)

    with company1:

        age = st.number_input(
            "Company Age (years)",
            min_value=0,
            max_value=300,
            value=20
        )

    with company2:

        employer_provided = st.selectbox(
            "Employer Provided Salary?",
            [0, 1],
            format_func=lambda x:
                "Yes" if x == 1 else "No"
        )


    # =====================================================
    # SKILLS
    # =====================================================

    html("""
    <div class="section-card">

        <div class="section-title">
            🧠 Technical Skills
        </div>

        <div class="section-subtitle">
            Select technologies required for the role.
        </div>

    </div>
    """)

    s1, s2, s3, s4, s5 = st.columns(5)

    with s1:

        html("""
        <div class="skill-card">

            <div class="skill-icon">🐍</div>

            <div class="skill-name">
                Python
            </div>

        </div>
        """)

        python_yn = st.selectbox(
            "Python",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s2:

        html("""
        <div class="skill-card">

            <div class="skill-icon">📊</div>

            <div class="skill-name">
                R
            </div>

        </div>
        """)

        r_yn = st.selectbox(
            "R",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s3:

        html("""
        <div class="skill-card">

            <div class="skill-icon">⚡</div>

            <div class="skill-name">
                Spark
            </div>

        </div>
        """)

        spark = st.selectbox(
            "Spark",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s4:

        html("""
        <div class="skill-card">

            <div class="skill-icon">☁️</div>

            <div class="skill-name">
                AWS
            </div>

        </div>
        """)

        aws = st.selectbox(
            "AWS",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s5:

        html("""
        <div class="skill-card">

            <div class="skill-icon">📗</div>

            <div class="skill-name">
                Excel
            </div>

        </div>
        """)

        excel = st.selectbox(
            "Excel",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )


    # =====================================================
    # PREDICT
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    predict = st.button(
        "✨  Predict My Salary"
    )


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


        # RESULT

        html(f"""
        <div class="prediction-card">

            <div class="prediction-label">
                💰 AI ESTIMATED AVERAGE SALARY
            </div>

            <div class="prediction-value">
                ${prediction:.2f}K
            </div>

           <div class="prediction-note">
    AI-generated estimate based on job, company and skill attributes.
    Use this result as a reference, not a guaranteed salary quote.
</div>

        </div>
        """)


        st.markdown("<br>", unsafe_allow_html=True)


        # METRICS

        m1, m2, m3 = st.columns(3)

        with m1:

            html(f"""
            <div class="metric-card">

                <div class="metric-title">
                    ANNUAL ESTIMATE
                </div>

                <div class="metric-value">
                    ${prediction:.2f}K
                </div>

            </div>
            """)

        with m2:

            html(f"""
            <div class="metric-card">

                <div class="metric-title">
                    MONTHLY ESTIMATE
                </div>

                <div class="metric-value">
                    ${monthly:,.2f}
                </div>

            </div>
            """)

        with m3:

            html("""
            <div class="metric-card">

                <div class="metric-title">
                    MODEL USED
                </div>

                <div class="metric-value">
                    Random Forest
                </div>

            </div>
            """)

       

# =========================================================
# RIGHT PANEL
# =========================================================

with right_col:

    html("""
    <div class="info-card">

        <div class="info-title">
            💡 Why SalaryIQ?
        </div>

        <div class="info-row">
            📊 Data-driven salary estimation
        </div>

        <div class="info-row">
            🎯 Uses job & company information
        </div>

        <div class="info-row">
            🧠 Considers technical skills
        </div>

        <div class="info-row">
            ⚡ Fast prediction
        </div>

    </div>
    """)


    html("""
    <div class="info-card">

        <div class="info-title">
            🌲 Model Information
        </div>

        <div class="info-row">
            🌲 Random Forest Regressor
        </div>

        <div class="info-row">
            🔄 One-hot encoded categorical data
        </div>

        <div class="info-row">
            🧹 Missing-value imputation
        </div>

        <div class="info-row">
            ⚙️ Tuned hyperparameters
        </div>

    </div>
    """)


    html("""
    <div class="info-card">

        <div class="info-title">
            🚀 Project Stack
        </div>

        <div class="info-row">
            🐍 Python
        </div>

        <div class="info-row">
            🐼 Pandas
        </div>

        <div class="info-row">
            🧠 Scikit-learn
        </div>

        <div class="info-row">
            🌲 Random Forest
        </div>

        <div class="info-row">
            🚀 Streamlit
        </div>

    </div>
    """)


    html("""
    <div class="info-card">

        <div class="info-title">
            ℹ️ About Prediction
        </div>

        <div class="info-row">
            This prediction is generated by a
            machine-learning model trained on
            job-market data.
        </div>

        <div class="info-row">
            Use the estimate as a reference,
            not as a guaranteed salary quote.
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

html("""
<div class="footer">

    SalaryIQ • AI Salary Prediction Platform<br>

    Built with Python • Pandas • Scikit-learn •
    Random Forest • Streamlit

</div>
""")
