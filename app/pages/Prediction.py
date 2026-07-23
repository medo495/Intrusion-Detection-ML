import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.title("🔍 Prediction")

uploaded_file = st.file_uploader(
    "📂 Importer un CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Aperçu")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    if st.button("🚀 Lancer la prédiction"):

        predictions = [
            random.choice(
                ["BENIGN", "ATTACK"]
            )
            for _ in range(len(df))
        ]

        df["Prediction"] = predictions

        st.success(
            "Prédiction terminée avec succès"
        )

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.subheader("📊 Répartition des prédictions")

        attack_count = (
            df["Prediction"]
            .value_counts()
            .reset_index()
        )

        attack_count.columns = [
            "Classe",
            "Nombre"
        ]

        fig = px.pie(
            attack_count,
            names="Classe",
            values="Nombre",
            title="BENIGN vs ATTACK"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Télécharger les résultats",
            csv,
            "predictions.csv",
            "text/csv"
        )