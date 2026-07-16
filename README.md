Voici un README complet que vous pouvez mettre à la racine du dépôt GitHub. Il est destiné à toute l'équipe et couvre l'installation, Git, Jupyter, Streamlit et l'organisation du projet.

# Intrusion Detection System using Machine Learning

## Description

Ce projet a pour objectif de développer un **Intrusion Detection System (IDS)** basé sur le Machine Learning en utilisant le jeu de données **CICIDS2017**.

Le système permettra :

* de détecter automatiquement les attaques réseau ;
* de comparer plusieurs modèles de Machine Learning ;
* d'intégrer le meilleur modèle dans une application **Streamlit**.

---

# Équipe

| Membre   | Responsabilités                                                  |
| -------- | ---------------------------------------------------------------- |
| Membre 1 | Prétraitement, entraînement des modèles, évaluation              |
| Membre 2 | Développement de l'application Streamlit                         |
| Membre 3 | Analyse des performances, optimisation et validation des modèles |

---

# Technologies

* Python 3.11+
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Plotly
* Matplotlib
* Joblib
* Git & GitHub

---

# Structure du projet

```
Intrusion-Detection-ML/

│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│
├── models/
│   ├── best_model.pkl
│   ├── label_encoder.pkl
│
├── app/
│   ├── app.py
│   ├── pages/
│   │      Dashboard.py
│   │      Prediction.py
│   │      About.py
│   │
│   ├── assets/
│
├── reports/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# Cloner le projet

```
git clone <URL_DU_REPO>

cd Intrusion-Detection-ML
```

---

# Création de l'environnement virtuel

## Windows

```
python -m venv venv

venv\Scripts\activate
```

## Linux / macOS

```
python3 -m venv venv

source venv/bin/activate
```

---

# Installer les dépendances

```
pip install -r requirements.txt
```

---

# Configuration du Kernel Jupyter

Installer Jupyter et le kernel.

```
pip install notebook ipykernel
```

Créer le kernel.

```
python -m ipykernel install --user --name intrusion-detection-ml --display-name "Python (Intrusion Detection ML)"
```

Ouvrir ensuite un notebook et sélectionner :

```
Python (Intrusion Detection ML)
```

---

# Vérification de l'installation

Lancer Python puis exécuter :

```python
import pandas
import numpy
import sklearn
import xgboost
import streamlit

print("Configuration OK")
```

Si aucun message d'erreur n'apparaît, l'installation est correcte.

---

# Lancer Streamlit

Depuis la racine du projet :

```
streamlit run app/app.py
```

---

# Workflow Git

Toujours récupérer les dernières modifications avant de commencer.

```
git pull origin Main
```

Créer une branche personnelle.

```
git checkout -b nom-branche
```

Exemple

```
git checkout -b feature-streamlit
```

ou

```
git checkout -b feature-model-training
```

Ajouter les fichiers

```
git add .
```

Faire un commit

```
git commit -m "Description des modifications"
```

Envoyer les modifications

```
git push origin nom-branche
```

Ne jamais travailler directement sur **main**.

---

# Règles de collaboration

Avant de commencer :

```
git pull origin main
```

Avant chaque push :

```
git status
```

Résoudre les conflits avant de continuer.

Faire des commits petits et fréquents.

---

# Répartition des tâches

## Membre 1

* Prétraitement
* Decision Tree
* Random Forest
* XGBoost
* Comparaison des modèles
* Sauvegarde du meilleur modèle

---

## Membre 2

Développement Streamlit

* Interface
* Dashboard
* Upload CSV
* Visualisations
* Export CSV
* Chargement du modèle

Le modèle sera intégré ultérieurement.

Pendant le développement, il peut utiliser des prédictions simulées.

```python
import random

predictions = [
    random.choice(["BENIGN", "ATTACK"])
    for _ in range(len(df))
]
```

---

## Membre 3

Validation technique

* Analyse des performances
* Analyse des erreurs
* Feature Importance
* Optimisation des hyperparamètres
* Comparaison des modèles
* Tests avec/sans Destination Port
* Mesure des temps d'entraînement et de prédiction

---

# Pipeline Machine Learning

Le pipeline suivi dans le projet est :

```
Fusion des fichiers CSV
        ↓
Suppression des doublons
        ↓
Traitement des valeurs infinies
        ↓
Traitement des valeurs manquantes
        ↓
Encodage des labels
        ↓
Séparation stratifiée Train/Test
        ↓
Entraînement
        ↓
Évaluation
        ↓
Comparaison des modèles
        ↓
Sauvegarde du meilleur modèle
        ↓
Déploiement Streamlit
```

---

# Évaluation des modèles

Les modèles sont évalués avec :

* Accuracy
* Precision
* Recall
* F1-score
* Macro-F1
* Matrice de confusion
* Temps d'entraînement
* Temps de prédiction

Compte tenu du déséquilibre du jeu de données, une attention particulière est portée au **Recall de la classe ATTACK** et au **Macro-F1**, conformément aux recommandations de l'encadrant.

---

# Modèles utilisés

* Decision Tree
* Random Forest
* XGBoost

Les performances sont comparées :

* avec la variable **Destination Port**
* sans la variable **Destination Port**

afin d'étudier son influence sur les résultats.

---

# Dataset

Nom :

```
CICIDS2017
```

Classification :

```
BENIGN

ATTACK
```

---

# Sauvegarde du modèle

Le meilleur modèle sera enregistré dans :

```
models/best_model.pkl
```

L'encodeur sera enregistré dans :

```
models/label_encoder.pkl
```

---

# Bonnes pratiques

* Toujours utiliser le même environnement virtuel.
* Toujours installer les dépendances avec `requirements.txt`.
* Utiliser `random_state=42` pour garantir la reproductibilité.
* Ne jamais modifier directement la branche `main`.
* Tester le code avant chaque commit.
* Documenter les nouvelles fonctionnalités.

---

# Contact

En cas de problème ou de conflit Git, prévenir l'équipe avant de modifier la branche principale.
