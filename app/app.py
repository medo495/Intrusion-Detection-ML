import streamlit as st

st.set_page_config(
    page_title="Cyber IDS Platform",
    page_icon="🛡️",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
    }

    .main .block-container {
        padding-top: 0.8rem;
        padding-bottom: 2rem;
    }

    .hero-card, .panel-card, .workflow-card, .nav-card {
        background: rgba(15, 23, 42, 0.92);
        border: 1px solid rgba(34, 211, 238, 0.2);
        border-radius: 20px;
        padding: 1.15rem 1.25rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }

    .hero-title {
        font-size: 2.25rem;
        font-weight: 800;
        color: #67e8f9;
        margin-bottom: 0.35rem;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1.0rem;
        line-height: 1.7;
    }

    .section-title {
        color: #67e8f9;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .muted {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    .pill {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        background: rgba(0, 229, 255, 0.12);
        color: #67e8f9;
        font-size: 0.85rem;
        margin: 0.2rem 0.2rem 0.2rem 0;
        border: 1px solid rgba(0, 229, 255, 0.22);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """
    <div class="hero-card">
        <div style="font-size: 1.3rem; font-weight: 800; color: #67e8f9;">🛡️ IDS ML Lab</div>
        <div style="color: #cbd5e1; margin-top: 0.4rem;">Cybersecurity monitoring dashboard</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("")
st.sidebar.caption("Project: Network Intrusion Detection System")
st.sidebar.caption("Dataset: CICIDS2017")
st.sidebar.caption("Model: Decision Tree")
st.sidebar.caption("Status: Operational")
st.sidebar.caption("Version: 2.0")

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Cybersecurity Threat Intelligence Platform</div>
        <div class="hero-subtitle">
            A professional intrusion detection solution for monitoring network traffic,
            analyzing suspicious behavior, and classifying flows as BENIGN or ATTACK using a trained Decision Tree model.
        </div>
        <div style="margin-top: 0.75rem;">
            <span class="pill">CICIDS2017</span>
            <span class="pill">Binary Classification</span>
            <span class="pill">Decision Tree</span>
            <span class="pill">Streamlit Dashboard</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset", "CICIDS2017", help="Public intrusion detection dataset")
with col2:
    st.metric("Model", "Decision Tree", help="Final selected classifier")
with col3:
    st.metric("Classes", "BENIGN / ATTACK", help="Binary classification target")
with col4:
    st.metric("Runtime", "Live", help="Real-time analysis workflow")

st.markdown("")

left, right = st.columns([1.35, 1.0])

with left:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📌 Project Overview</div>
            <div class="muted">
                This system is designed to support cybersecurity engineering research by combining
                machine learning, data analysis, and interactive visualization. The workflow covers
                dataset inspection, preprocessing, traffic classification, and report generation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🧠 Selected Model</div>
            <div class="muted">
                The final classifier is a Decision Tree model trained offline and saved using Joblib.
                It is used for predicting whether a network flow is BENIGN or ATTACK.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🧩 Main Workflow</div>
    </div>
    """,
    unsafe_allow_html=True,
)

wf1, wf2, wf3, wf4 = st.columns(4)

with wf1:
    st.markdown(
        """
        <div class="workflow-card">
            <div style="font-size: 1.1rem; color: #67e8f9;">1. Data Intake</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Upload network flow data in CSV format.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with wf2:
    st.markdown(
        """
        <div class="workflow-card">
            <div style="font-size: 1.1rem; color: #67e8f9;">2. Validation</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Verify the required columns and inspect quality issues.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with wf3:
    st.markdown(
        """
        <div class="workflow-card">
            <div style="font-size: 1.1rem; color: #67e8f9;">3. Inference</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Run the trained Decision Tree model to generate predictions.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with wf4:
    st.markdown(
        """
        <div class="workflow-card">
            <div style="font-size: 1.1rem; color: #67e8f9;">4. Reporting</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Visualize results and export a prediction report.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🏗️ Architecture</div>
            <div class="muted">
                CSV upload → field validation → preprocessing → Decision Tree inference → visualization/reporting.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_b:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📚 Dataset Information</div>
            <div class="muted">
                CICIDS2017 contains labeled network traffic designed for intrusion detection research.
                The current deployment focuses on a binary setting: BENIGN vs ATTACK.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🧭 Navigation</div>
    </div>
    """,
    unsafe_allow_html=True,
)

nav1, nav2, nav3 = st.columns(3)

with nav1:
    st.markdown(
        """
        <div class="nav-card">
            <div style="font-size: 1.05rem; color: #67e8f9;">📊 Dashboard</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Explore dataset quality, distributions, and descriptive statistics.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with nav2:
    st.markdown(
        """
        <div class="nav-card">
            <div style="font-size: 1.05rem; color: #67e8f9;">🔍 Prediction</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Upload a CSV, validate features, and infer threat labels.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with nav3:
    st.markdown(
        """
        <div class="nav-card">
            <div style="font-size: 1.05rem; color: #67e8f9;">ℹ️ About</div>
            <div class="muted" style="margin-top: 0.4rem;">
                Review project objectives, methodology, and institutional details.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )