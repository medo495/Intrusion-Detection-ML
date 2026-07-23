import streamlit as st

st.title("ℹ️ À propos du projet")

st.markdown("""
## 🛡️ Intrusion Detection System

Ce projet a pour objectif de développer un système
de détection d'intrusions basé sur le Machine Learning
en utilisant le dataset CICIDS2017.

Le système permet :

- Détecter automatiquement les attaques réseau
- Comparer plusieurs modèles de Machine Learning
- Déployer le meilleur modèle dans Streamlit
""")

st.divider()

st.subheader("⚙️ Technologies utilisées")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")

with col2:
    st.success("Scikit-Learn")
    st.success("XGBoost")
    st.success("Joblib")

with col3:
    st.success("Streamlit")
    st.success("Plotly")
    st.success("Git & GitHub")

st.divider()

st.subheader("👥 Équipe")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Membre 1**

    Prétraitement et modèles ML
    """)

with col2:
    st.info("""
    **Membre 2**

    Développement Streamlit
    """)

with col3:
    st.info("""
    **Membre 3**

    Validation et optimisation
    """)

st.divider()

st.subheader("🔄 Pipeline Machine Learning")

st.code("""
Fusion CSV
↓
Prétraitement
↓
Entraînement
↓
Évaluation
↓
Comparaison
↓
Sauvegarde modèle
↓
Déploiement Streamlit
""")

st.success("Projet académique basé sur CICIDS2017")