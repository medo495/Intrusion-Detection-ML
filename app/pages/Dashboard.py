import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

uploaded_file = st.file_uploader(
    "📂 Choisir un fichier CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📈 Informations générales")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Lignes", df.shape[0])

    with c2:
        st.metric("Colonnes", df.shape[1])

    with c3:
        st.metric(
            "Valeurs manquantes",
            int(df.isnull().sum().sum())
        )

    st.divider()

    st.subheader("👀 Aperçu des données")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.divider()

    # =========================
    # Dataset Health
    # =========================

    st.subheader("🩺 Dataset Health")

    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    h1, h2, h3 = st.columns(3)

    with h1:
        st.metric(
            "Missing Values",
            int(missing_values)
        )

    with h2:
        st.metric(
            "Duplicate Rows",
            int(duplicate_rows)
        )

    with h3:

        if missing_values == 0 and duplicate_rows == 0:
            status = "🟢 Good"

        elif missing_values < 10:
            status = "🟡 Medium"

        else:
            status = "🔴 Poor"

        st.metric(
            "Dataset Status",
            status
        )

    st.divider()

    st.subheader("📊 Visualisations")

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_cols) > 0:

        selected_col = st.selectbox(
            "Choisir une colonne",
            numeric_cols
        )

        col1, col2 = st.columns(2)

        with col1:

            fig1 = px.histogram(
                df,
                x=selected_col,
                title=f"Distribution de {selected_col}"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

        with col2:

            fig2 = px.box(
                df,
                y=selected_col,
                title=f"Box Plot de {selected_col}"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    st.divider()

    st.subheader("📋 Statistiques descriptives")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    st.divider()

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Télécharger CSV",
        csv,
        "export.csv",
        "text/csv"
    )