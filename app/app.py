import streamlit as st

st.set_page_config(
    page_title="IDS ML Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# CSS
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

[data-testid="metric-container"] {
    background-color: #1E293B;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}

h1 {
    color: #00E5FF;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🛡️ Intrusion Detection System")

st.markdown("""
### Détection intelligente des attaques réseau

Application basée sur le Machine Learning et le dataset CICIDS2017.
""")

st.divider()

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📂 Dataset", "CICIDS2017")

with col2:
    st.metric("🤖 Modèles", "3")

with col3:
    st.metric("🎯 Classes", "2")

with col4:
    st.metric("🟢 Statut", "Actif")

st.divider()

# Objectifs
st.subheader("🎯 Objectifs du projet")

c1, c2 = st.columns(2)

with c1:
    st.success("Détection des attaques réseau")
    st.success("Analyse du trafic")
    st.success("Visualisation des données")

with c2:
    st.success("Machine Learning")
    st.success("Comparaison des modèles")
    st.success("Déploiement Streamlit")

st.divider()

# Description
st.subheader("📖 Présentation")

st.info("""
Ce projet vise à développer un système IDS (Intrusion Detection System)
basé sur le Machine Learning afin d'identifier automatiquement les
attaques réseau à partir du dataset CICIDS2017.
""")

st.divider()

# Technologies
st.subheader("⚙️ Technologies utilisées")

t1, t2, t3 = st.columns(3)

with t1:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")

with t2:
    st.success("Scikit-Learn")
    st.success("XGBoost")
    st.success("Joblib")

with t3:
    st.success("Streamlit")
    st.success("Plotly")
    st.success("Git & GitHub")

st.divider()

# Fonctionnalités
st.subheader("🚀 Fonctionnalités")

st.write("✅ Upload de fichiers CSV")
st.write("✅ Dashboard interactif")
st.write("✅ Visualisation des données")
st.write("✅ Prédiction des attaques")
st.write("✅ Export des résultats")

st.divider()

