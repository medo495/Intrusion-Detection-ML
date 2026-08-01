import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard | IDS ML",
    page_icon="📊",
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
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div style="font-size: 1.6rem; font-weight: 800; color: #67e8f9;">📊 Dataset Intelligence Dashboard</div>
        <div style="color: #cbd5e1; margin-top: 0.35rem;">
            Inspect dataset quality, detect irregularities, and understand the structure of the CICIDS2017 traffic data.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, low_memory=False)
    except Exception as e:
        st.error(f"Unable to read the uploaded file: {e}")
        st.stop()

    st.success("Dataset loaded successfully.")

    missing_values = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    total_rows, total_cols = df.shape

    health_score = max(0, 100 - (missing_values * 2) - (duplicate_rows * 3))
    if health_score >= 90:
        quality_label = "Excellent"
    elif health_score >= 75:
        quality_label = "Good"
    elif health_score >= 50:
        quality_label = "Fair"
    else:
        quality_label = "Needs Attention"

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📈 Dataset Summary</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Rows", f"{total_rows:,}")
    with c2:
        st.metric("Columns", f"{total_cols:,}")
    with c3:
        st.metric("Missing Values", f"{missing_values:,}")
    with c4:
        st.metric("Duplicate Rows", f"{duplicate_rows:,}")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🩺 Dataset Quality</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)
    with q1:
        st.metric("Health Score", f"{health_score}/100")
    with q2:
        st.metric("Quality Label", quality_label)
    with q3:
        st.metric("Numeric Features", len(df.select_dtypes(include="number").columns))

    st.progress(health_score / 100)

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🧾 Missing Values by Column</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    missing_by_col = df.isna().sum().sort_values(ascending=False)
    missing_by_col = missing_by_col[missing_by_col > 0]

    if not missing_by_col.empty:
        fig_missing = px.bar(
            x=missing_by_col.index,
            y=missing_by_col.values,
            labels={"x": "Column", "y": "Missing Values"},
            title="Missing Values Distribution",
            color=missing_by_col.values,
            color_continuous_scale="Tealgrn",
        )
        st.plotly_chart(fig_missing, use_container_width=True)
    else:
        st.info("No missing values detected.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📊 Feature Distributions</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) >= 1:
        selected_col = st.selectbox("Select a numeric feature", numeric_cols)

        hist_col, box_col = st.columns(2)

        with hist_col:
            fig_hist = px.histogram(
                df,
                x=selected_col,
                nbins=40,
                title=f"Distribution of {selected_col}",
                color_discrete_sequence=["#67e8f9"],
            )
            st.plotly_chart(fig_hist, use_container_width=True)

        with box_col:
            fig_box = px.box(
                df,
                y=selected_col,
                title=f"Box Plot of {selected_col}",
                color_discrete_sequence=["#22d3ee"],
            )
            st.plotly_chart(fig_box, use_container_width=True)
    else:
        st.info("No numeric columns available for visualization.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🔗 Correlation Heatmap</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(numeric_cols) > 1:
        corr_df = df[numeric_cols].corr()
        fig_corr = px.imshow(
            corr_df,
            color_continuous_scale="Tealgrn",
            title="Feature Correlation Matrix",
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.info("At least two numeric features are required for a correlation heatmap.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">🏷️ Class Distribution</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    label_candidates = [c for c in df.columns if c.lower() in {"label", "target", "class", "attack", "label_col"}]

    if label_candidates:
        label_col = label_candidates[0]
        class_counts = df[label_col].value_counts()
        fig_class = px.bar(
            class_counts,
            x=class_counts.index,
            y=class_counts.values,
            title=f"Distribution of {label_col}",
            color=class_counts.index,
            color_discrete_sequence=["#22d3ee", "#0f766e"],
        )
        st.plotly_chart(fig_class, use_container_width=True)
    else:
        st.info("No obvious label column detected in the dataset.")

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">📋 Descriptive Statistics</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(df.describe(include="all").T, use_container_width=True)

    st.markdown("")
    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">👀 Dataset Preview</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(df.head(15), use_container_width=True, hide_index=True)

    st.markdown("")
    csv_data = df.to_csv(index=False)
    st.download_button(
        "Download cleaned dataset",
        csv_data,
        file_name="dataset_preview.csv",
        mime="text/csv",
    )