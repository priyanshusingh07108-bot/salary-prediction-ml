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
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

/* ================= GLOBAL ================= */

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(37,99,235,0.18), transparent 25%),
        radial-gradient(circle at 95% 10%, rgba(124,58,237,0.18), transparent 25%),
        linear-gradient(135deg, #020617 0%, #071426 50%, #0b1025 100%);
    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding: 1.4rem 1.5rem 3rem 1.5rem;
}

/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #020617 0%, #06142b 60%, #081b35 100%);
    border-right: 1px solid rgba(96,165,250,0.18);
}

.sidebar-logo {
    text-align: center;
    padding: 15px 5px 25px 5px;
}

.sidebar-logo-icon {
    font-size: 42px;
}

.sidebar-logo-title {
    font-size: 25px;
    font-weight: 800;
    background: linear-gradient(90deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sidebar-subtitle {
    color: #94a3b8;
    font-size: 12px;
}

.sidebar-card {
    margin-top: 25px;
    padding: 18px;
    border-radius: 18px;
    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(96,165,250,0.15);
}

.sidebar-card-title {
    font-weight: 700;
    margin-bottom: 12px;
}

.sidebar-item {
    color: #cbd5e1;
    padding: 7px 0;
    font-size: 14px;
}

/* ================= HERO ================= */

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 38px;
    border-radius: 25px;

    background:
        radial-gradient(circle at 75% 35%, rgba(59,130,246,0.28), transparent 22%),
        radial-gradient(circle at 90% 80%, rgba(124,58,237,0.30), transparent 25%),
        linear-gradient(135deg, #102c62, #25205d);

    border: 1px solid rgba(96,165,250,0.28);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.30);

    margin-bottom: 22px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;

    color: #93c5fd;
    background: rgba(37,99,235,0.16);
    border: 1px solid rgba(96,165,250,0.30);

    font-size: 12px;
    font-weight: 700;
}

.hero-title {
    font-size: 58px;
    line-height: 1;
    font-weight: 850;
    margin-top: 15px;

    background: linear-gradient(
        90deg,
        #ffffff,
        #93c5fd,
        #c4b5fd
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-tagline {
    font-size: 23px;
    font-weight: 700;
    color: #60a5fa;
    margin-top: 10px;
}

.hero-description {
    color: #cbd5e1;
    max-width: 760px;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 8px;
}

/* ================= SECTION ================= */

.section {
    padding: 22px;
    border-radius: 20px;

    background: rgba(8,20,40,0.80);

    border: 1px solid rgba(148,163,184,0.14);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.16);

    margin-bottom: 18px;
}

.section-title {
    font-size: 20px;
    font-weight: 750;
}

.section-subtitle {
    color: #64748b;
    font-size: 12px;
    margin-top: 3px;
    margin-bottom: 18px;
}

/* ================= INPUTS ================= */

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
}

.stSelectbox div[data-baseweb="select"] > div {

    background: #0b1629 !important;

    border: 1px solid #263b5a !important;

    border-radius: 11px !important;

    color: #f8fafc !important;
}

label {
    color: #cbd5e1 !important;
    font-size: 13px !important;
}

/* ================= SKILL CARDS ================= */

.skill-card {

    padding: 15px;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            rgba(15,30,55,0.95),
            rgba(8,20,40,0.95)
        );

    border: 1px solid rgba(96,165,250,0.16);

    text-align: center;

    min-height: 115px;
}

.skill-icon {
    font-size: 25px;
}

.skill-name {
    font-size: 14px;
    font-weight: 700;
    margin-top: 4px;
}

/* ================= BUTTON ================= */

.stButton > button {

    width: 100%;
    height: 55px;

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
        0 12px 35px rgba(79,70,229,0.35);

    transition: 0.2s;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 18px 45px rgba(79,70,229,0.50);
}

/* ================= RIGHT CARDS ================= */

.info-card {

    padding: 20px;

    border-radius: 19px;

    background:
        linear-gradient(
            145deg,
            rgba(25,25,70,0.80),
            rgba(10,20,45,0.85)
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

    display: flex;

    gap: 10px;

    margin: 13px 0;

    color: #cbd5e1;

    font-size: 13px;

    line-height: 1.5;
}

/* ================= PREDICTION ================= */

.prediction-card {

    padding: 25px;

    border-radius: 22px;

    background:
        radial-gradient(
            circle at 15% 50%,
            rgba(16,185,129,0.20),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            rgba(5,70,65,0.80),
            rgba(8,35,55,0.90)
        );

    border: 1px solid rgba(52,211,153,0.30);

    box-shadow:
        0 20px 55px rgba(0,0,0,0.25);

    margin-top: 20px;
}

.prediction-label {

    color: #a7f3d0;

    font-size: 13px;

    font-weight: 700;
}

.prediction-value {

    font-size: 48px;

    font-weight: 850;

    color: #34d399;

    margin: 3px 0;
}

.prediction-description {

    color: #94a3b8;

    font-size: 12px;
}

/* ================= METRICS ================= */

.metric-card {

    padding: 19px;

    border-radius: 16px;

    background: rgba(10,25,45,0.90);

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

/* ================= FOOTER ================= */

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

    st.markdown("""
    <div class="sidebar-logo">

        <div class="sidebar-logo-icon">📊</div>

        <div class="sidebar-logo-title">
            SalaryIQ
        </div>

        <div class="sidebar-subtitle">
            AI Salary Predictor
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
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
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">

        <div class="sidebar-card-title">
            ⚙️ Powered By
        </div>

        <div class="sidebar-item">🐍 Python</div>
        <div class="sidebar-item">🧠 Scikit-learn</div>
        <div class="sidebar-item">🌲 Random Forest</div>
        <div class="sidebar-item">🚀 Streamlit</div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        margin-top:35px;
        padding:15px;
        color:#64748b;
        font-size:12px;
        text-align:center;
    ">
        Better data.<br>
        Smarter predictions.<br>
        Better decisions.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# MAIN LAYOUT
# =========================================================

main_col, right_col = st.columns(
    [3.7, 1.25],
    gap="large"
)


# =========================================================
# MAIN COLUMN
# =========================================================

with main_col:

    # ---------------- HERO ----------------

    st.markdown("""
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
    """, unsafe_allow_html=True)


    # =====================================================
    # JOB INFORMATION
    # =====================================================

    st.markdown("""
    <div class="section">

        <div class="section-title">
            💼 Job Information
        </div>

        <div class="section-subtitle">
            Enter details about the position you're targeting.
        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

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

    with c2:

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

    st.markdown("""
    <div class="section">

        <div class="section-title">
            🏢 Company Details
        </div>

        <div class="section-subtitle">
            Additional information about the employer.
        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        age = st.number_input(
            "Company Age (years)",
            min_value=0,
            max_value=300,
            value=20
        )

    with c2:

        employer_provided = st.selectbox(
            "Employer Provided Salary?",
            [0, 1],
            format_func=lambda x:
                "Yes" if x == 1 else "No"
        )


    # =====================================================
    # SKILLS
    # =====================================================

    st.markdown("""
    <div class="section">

        <div class="section-title">
            🧠 Technical Skills
        </div>

        <div class="section-subtitle">
            Select technologies required for the role.
        </div>

    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4, s5 = st.columns(5)

    with s1:

        st.markdown("""
        <div class="skill-card">

            <div class="skill-icon">🐍</div>
            <div class="skill-name">Python</div>

        </div>
        """, unsafe_allow_html=True)

        python_yn = st.selectbox(
            "Python",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s2:

        st.markdown("""
        <div class="skill-card">

            <div class="skill-icon">📊</div>
            <div class="skill-name">R</div>

        </div>
        """, unsafe_allow_html=True)

        r_yn = st.selectbox(
            "R",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s3:

        st.markdown("""
        <div class="skill-card">

            <div class="skill-icon">⚡</div>
            <div class="skill-name">Spark</div>

        </div>
        """, unsafe_allow_html=True)

        spark = st.selectbox(
            "Spark",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s4:

        st.markdown("""
        <div class="skill-card">

            <div class="skill-icon">☁️</div>
            <div class="skill-name">AWS</div>

        </div>
        """, unsafe_allow_html=True)

        aws = st.selectbox(
            "AWS",
            [0, 1],
            format_func=lambda x:
                "Required" if x == 1 else "No",
            label_visibility="collapsed"
        )

    with s5:

        st.markdown("""
        <div class="skill-card">

            <div class="skill-icon">📗</div>
            <div class="skill-name">Excel</div>

        </div>
        """, unsafe_allow_html=True)

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


        # =================================================
        # RESULT
        # =================================================

        st.markdown(
            f"""
            <div class="prediction-card">

                <div class="prediction-label">
                    💰 AI ESTIMATED AVERAGE SALARY
                </div>

                <div class="prediction-value">
                    ${prediction:.2f}K
                </div>

                <div class="prediction-description">
                    Estimated annual salary based on the
                    information provided.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # METRICS
        # =================================================

        m1, m2, m3 = st.columns(3)

        with m1:

            st.markdown(
                f"""
                <div class="metric-card">

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
                <div class="metric-card">

                    <div class="metric-title">
                        MONTHLY ESTIMATE
                    </div>

                    <div class="metric-value">
                        ${monthly:,.2f}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with m3:

            st.markdown(
                """
                <div class="metric-card">

                    <div class="metric-title">
                        MODEL USED
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


# =========================================================
# RIGHT SIDE PANEL
# =========================================================

with right_col:

    st.markdown("""
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
    """, unsafe_allow_html=True)


    # ---------------- MODEL ----------------

    st.markdown("""
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
            🧹 Median/mode imputation
        </div>

        <div class="info-row">
            ⚙️ Tuned hyperparameters
        </div>

    </div>
    """, unsafe_allow_html=True)


    # ---------------- PROJECT ----------------

    st.markdown("""
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
            🚀 Streamlit
        </div>

        <div class="info-row">
            🐙 GitHub
        </div>

    </div>
    """, unsafe_allow_html=True)


    # ---------------- NOTE ----------------

    st.markdown("""
    <div class="info-card">

        <div class="info-title">
            ℹ️ Note
        </div>

        <div class="info-row">
            Salary predictions are estimates generated
            by a machine-learning model and should be
            used as a reference rather than an exact salary quote.
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

SalaryIQ • AI Salary Prediction Platform<br>
Built with Python • Pandas • Scikit-learn • Random Forest • Streamlit

</div>
""", unsafe_allow_html=True)
