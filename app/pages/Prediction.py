import os
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Prediction | IDS ML",
    page_icon="🔍",
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

    .risk-badge {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div style="font-size: 1.6rem; font-weight: 800; color: #67e8f9;">🔍 Threat Prediction Engine</div>
        <div style="color: #cbd5e1; margin-top: 0.35rem;">
            Upload a network traffic CSV, validate its features, and classify each flow using the trained Decision Tree model.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


def find_model_artifact():
    project_root = Path(__file__).resolve().parents[2]
    candidates = [
        project_root / "models" / "decision_tree.pkl",
        project_root / "decision_tree.pkl",
        project_root / "model.pkl",
        project_root / "trained_model.pkl",
        project_root / "app" / "models" / "decision_tree.pkl",
        project_root / "app" / "decision_tree.pkl",
        Path.cwd() / "models" / "decision_tree.pkl",
        Path.cwd() / "decision_tree.pkl",
    ]

    for path in candidates:
        if path.exists():
            return path

    for path in project_root.rglob("*.pkl"):
        name = path.name.lower()
        if "decision" in name or "tree" in name or "model" in name:
            return path

    return None


def normalize_prediction(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        return "ATTACK" if int(value) != 0 else "BENIGN"

    text = str(value).strip().upper()
    if text in {"0", "FALSE", "BENIGN", "NORMAL"}:
        return "BENIGN"
    if text in {"1", "TRUE", "ATTACK", "MALICIOUS"}:
        return "ATTACK"
    return text


def prepare_features(df, model):
    label_like = {"label", "target", "class", "attack", "result"}
    candidate_features = []

    if hasattr(model, "feature_names_in_"):
        expected = list(model.feature_names_in_)
        col_map = {col.lower(): col for col in df.columns}
        for feat in expected:
            if feat in df.columns:
                candidate_features.append(feat)
            elif feat.lower() in col_map:
                candidate_features.append(col_map[feat.lower()])
            else:
                pass

    if not candidate_features:
        candidate_features = [
            col for col in df.columns
            if col.lower() not in label_like and col.lower() not in {"id", "index", "flow_id"}
        ]

    if not candidate_features:
        raise ValueError("No usable feature columns were found for prediction.")

    features_df = df[candidate_features].copy()

    for col in features_df.columns:
        if features_df[col].dtype == "object":
            features_df[col] = pd.to_numeric(features_df[col], errors="coerce")
        else:
            features_df[col] = pd.to_numeric(features_df[col], errors="coerce")

    features_df = features_df.fillna(0)

    return features_df


def get_risk_level(attack_percentage):
    if attack_percentage >= 50:
        return "Critical"
    if attack_percentage >= 25:
        return "High"
    if attack_percentage >= 10:
        return "Medium"
    return "Low"


uploaded_file = st.file_uploader("Upload CSV for prediction", type=["csv"])

if uploaded_file is not None:
    progress = st.progress(0.0)
    status_text = st.empty()

    status_text.text("Reading uploaded file...")
    progress.progress(0.1)

    try:
        input_df = pd.read_csv(uploaded_file, low_memory=False)
    except Exception as e:
        st.error(f"Unable to read the uploaded file: {e}")
        st.stop()

    status_text.text("Validating columns and feature set...")
    progress.progress(0.25)

    required_columns = []
    if "Label" in input_df.columns:
        required_columns.append("Label")
    if "label" in input_df.columns:
        required_columns.append("label")

    missing_columns = [col for col in required_columns if col not in input_df.columns]
    if missing_columns:
        st.warning("The uploaded file does not include the expected label column. Prediction can still proceed if the model accepts the feature set.")

    status_text.text("Loading trained Decision Tree model...")
    progress.progress(0.35)

    model_path = find_model_artifact()

    if model_path is None:
        st.error("No trained model was found. Please place a .pkl model file in the project folder or update the model path inside Prediction.py.")
        st.stop()

    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"Unable to load the model artifact: {e}")
        st.stop()

    status_text.text("Preparing feature matrix...")
    progress.progress(0.5)

    try:
        features = prepare_features(input_df, model)
    except Exception as e:
        st.error(f"Feature preparation failed: {e}")
        st.stop()

    status_text.text("Running Decision Tree inference...")
    progress.progress(0.75)

    start_time = time.perf_counter()

    try:
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(features)
            confidence_scores = np.max(probabilities, axis=1)
            predictions = model.predict(features)
        else:
            confidence_scores = None
            predictions = model.predict(features)
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    elapsed_time = round(time.perf_counter() - start_time, 3)

    progress.progress(1.0)
    status_text.text("Prediction completed successfully.")

    result_df = input_df.copy()
    result_df["Prediction"] = [normalize_prediction(x) for x in predictions]

    if confidence_scores is not None:
        result_df["Prediction_Confidence"] = [round(float(x), 3) for x in confidence_scores]

    attack_count = int((result_df["Prediction"] == "ATTACK").sum())
    benign_count = int((result_df["Prediction"] == "BENIGN").sum())
    total_flows = len(result_df)
    attack_percentage = round((attack_count / total_flows) * 100, 2) if total_flows else 0.0
    benign_percentage = round((benign_count / total_flows) * 100, 2) if total_flows else 0.0
    risk_level = get_risk_level(attack_percentage)

    st.success("Prediction completed successfully.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📊 Prediction Summary</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Flows", f"{total_flows:,}")
    with c2:
        st.metric("Attacks", f"{attack_count:,}")
    with c3:
        st.metric("Benign", f"{benign_count:,}")
    with c4:
        st.metric("Attack %", f"{attack_percentage}%")

    st.markdown("")
    col1, col2 = st.columns([0.8, 1.2])

    with col1:
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="section-title">🚨 Risk Level</div>
                <div class="risk-badge" style="background: {'#ef4444' if risk_level in {'Critical','High'} else '#22c55e' if risk_level == 'Low' else '#f59e0b'};">
                    {risk_level}
                </div>
                <div class="muted" style="margin-top: 0.6rem;">
                    Attack rate: <b>{attack_percentage}%</b><br>
                    Benign rate: <b>{benign_percentage}%</b><br>
                    Processing time: <b>{elapsed_time}s</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="panel-card">
                <div class="section-title">🧠 Prediction Confidence</div>
                <div class="muted">
                    Confidence is shown when the model supports probability estimation.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if confidence_scores is not None:
            st.metric("Average Confidence", f"{round(float(confidence_scores.mean()), 3):.3f}")
            st.metric("Maximum Confidence", f"{round(float(confidence_scores.max()), 3):.3f}")
        else:
            st.info("Prediction confidence is not available for this model artifact.")

    with col2:
        st.markdown(
            """
            <div class="panel-card">
                <div class="section-title">📈 Prediction Distribution</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        pred_counts = result_df["Prediction"].value_counts()
        fig_pie = px.pie(
            names=pred_counts.index,
            values=pred_counts.values,
            title="Prediction Distribution",
            color_discrete_sequence=["#22d3ee", "#0f766e"],
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📊 Attack Timeline</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    time_candidates = [col for col in input_df.columns if "time" in col.lower() or "date" in col.lower() or "timestamp" in col.lower()]
    if time_candidates:
        time_col = time_candidates[0]
        try:
            timeline_df = input_df.copy()
            timeline_df[time_col] = pd.to_datetime(timeline_df[time_col], errors="coerce")
            timeline_df = timeline_df.dropna(subset=[time_col]).sort_values(time_col)
            timeline_df["Prediction"] = result_df["Prediction"]
            timeline_counts = timeline_df.groupby([pd.Grouper(key=time_col, freq="H"), "Prediction"]).size().reset_index(name="Count")
            fig_timeline = px.line(
                timeline_counts,
                x=time_col,
                y="Count",
                color="Prediction",
                title=f"Hourly Prediction Trend ({time_col})",
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
        except Exception:
            st.info("Timestamp column detected but could not be parsed automatically.")
    else:
        st.info("No timestamp-like column was detected. Timeline visualization skipped.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🧾 Prediction Preview</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    preview_cols = [col for col in result_df.columns if col not in {"Prediction_Confidence"}]
    st.dataframe(result_df[preview_cols].head(20), use_container_width=True, hide_index=True)

    st.markdown("")
    st.download_button(
        "Download predicted CSV",
        result_df.to_csv(index=False),
        file_name="predicted_flows.csv",
        mime="text/csv",
    )

    report_text = (
        f"IDS Prediction Report\n"
        f"Model: {model_path.name}\n"
        f"Flows analyzed: {total_flows}\n"
        f"Attacks: {attack_count}\n"
        f"Benign: {benign_count}\n"
        f"Attack percentage: {attack_percentage}%\n"
        f"Benign percentage: {benign_percentage}%\n"
        f"Risk level: {risk_level}\n"
        f"Processing time: {elapsed_time}s\n"
    )
    st.download_button(
        "Export report",
        report_text,
        file_name="prediction_report.txt",
        mime="text/plain",
    )

    st.session_state.prediction_history.append(
        {
            "flows": total_flows,
            "attacks": attack_count,
            "benign": benign_count,
            "risk": risk_level,
            "processing_time": elapsed_time,
        }
    )

    if st.session_state.prediction_history:
        st.markdown("")
        st.markdown(
            """
            <div class="panel-card">
                <div class="section-title">🕘 Prediction History (Session)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        history_df = pd.DataFrame(st.session_state.prediction_history)
        st.dataframe(history_df.tail(10), use_container_width=True, hide_index=True)