import streamlit as st

st.set_page_config(
    page_title="About | IDS ML",
    page_icon="ℹ️",
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

    .panel-card, .hero-card {
        background: rgba(15, 23, 42, 0.92);
        border: 1px solid rgba(34, 211, 238, 0.2);
        border-radius: 20px;
        padding: 1rem 1.1rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        margin-bottom: 0.8rem;
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

st.markdown(
    """
    <div class="hero-card">
        <div style="font-size: 1.6rem; font-weight: 800; color: #67e8f9;">ℹ️ Project Documentation</div>
        <div style="color: #cbd5e1; margin-top: 0.35rem;">
            A professional documentation page for the Network Intrusion Detection System developed as a graduation project.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")

st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">📌 Project Description</div>
        <div class="muted">
            This project presents an intelligent intrusion detection system based on Machine Learning.
            It uses the CICIDS2017 dataset to classify network flows as BENIGN or ATTACK through a trained Decision Tree classifier.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🎯 Objectives</div>
            <div class="muted">
                • Detect abnormal network traffic<br>
                • Support cyber threat analysis<br>
                • Provide a modern dashboard for demonstration<br>
                • Compare and validate machine learning models
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">⚙️ Technologies</div>
            <div class="muted">
                <span class="pill">Python</span>
                <span class="pill">Pandas</span>
                <span class="pill">NumPy</span>
                <span class="pill">Scikit-Learn</span>
                <span class="pill">Joblib</span>
                <span class="pill">Streamlit</span>
                <span class="pill">Plotly</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")
st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🧪 CICIDS2017 Dataset</div>
        <div class="muted">
            CICIDS2017 is a benchmark dataset widely used for intrusion detection research.
            It contains labeled network traffic generated under realistic attack scenarios,
            making it suitable for binary classification tasks such as BENIGN vs ATTACK.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🌳 Decision Tree Classifier</div>
        <div class="muted">
            The Decision Tree model is the final selected classifier for this project. It is trained offline
            and stored as a Joblib artifact. During inference, the system uses the model to predict whether
            each traffic flow is malicious or normal.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🧩 Workflow</div>
        <div class="muted">
            1. Upload a CSV dataset<br>
            2. Validate columns and feature structure<br>
            3. Run preprocessing and model inference<br>
            4. Visualize results and export predictions
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown(
    """
    <div class="panel-card">
        <div class="section-title">🏗️ Architecture Diagram</div>
        <div class="muted">
            Data upload → Validation → Preprocessing → Decision Tree Prediction → Dashboard / Report Export
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">👩‍🔬 Authors</div>
            <div class="muted">
                Student Name<br>
                Cybersecurity Engineering Track
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🎓 Supervisor</div>
            <div class="muted">
                Academic supervisor for the graduation project
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🏢 Company</div>
            <div class="muted">
                SOREMED
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )