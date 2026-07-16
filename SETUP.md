# SETUP.md

# Intrusion Detection System using Machine Learning

This guide explains how to set up the project from scratch.

---

# 1. Clone the Repository

Clone the GitHub repository.

```bash
git clone <YOUR_GITHUB_REPOSITORY>

cd Intrusion-Detection-ML
```

---

# 2. Recommended Project Architecture

The project should have the following structure.

```
Intrusion-Detection-ML/

│
├── app/
│   ├── app.py
│   ├── pages/
│   └── assets/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── models/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│
├── reports/
│
├── requirements.txt
│
├── README.md
│
├── SETUP.md
│
└── .gitignore
```

---

# 3. Create a Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

---

## Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 5. Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

# 6. Install Jupyter Kernel

Install Jupyter Notebook and ipykernel.

```bash
pip install notebook ipykernel
```

Register the project kernel.

```bash
python -m ipykernel install --user --name intrusion-detection-ml --display-name "Python (Intrusion Detection ML)"
```

---

# 7. Open the Project

Open the project folder using VS Code.

```
File

↓

Open Folder

↓

Intrusion-Detection-ML
```

---

# 8. Select the Correct Kernel

Open any notebook.

Example

```
01_EDA.ipynb
```

At the top-right corner click

```
Select Kernel
```

Choose

```
Python (Intrusion Detection ML)
```

If the kernel does not appear:

Restart VS Code.

If it still does not appear:

```bash
python -m ipykernel install --user --name intrusion-detection-ml --display-name "Python (Intrusion Detection ML)"
```

---

# 9. Verify the Installation

Run the following code.

```python
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn
import xgboost
import joblib

print("Environment successfully configured!")
```

If no errors appear, the environment is correctly configured.

---

# 10. Download the Dataset

Download the CICIDS2017 dataset.

Recommended source

https://www.unb.ca/cic/datasets/ids-2017.html

Download the generated CSV files.

---

# 11. Place the Dataset

Create the following folder.

```
data/

└── raw/
```

Copy all downloaded CSV files into

```
data/raw/
```

Example

```
data/

└── raw/

    Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

    Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv

    Friday-WorkingHours-Morning.pcap_ISCX.csv

    Monday-WorkingHours.pcap_ISCX.csv

    Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv

    Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv

    Tuesday-WorkingHours.pcap_ISCX.csv

    Wednesday-workingHours.pcap_ISCX.csv
```

---

# 12. Run the Notebooks

Run the notebooks in the following order.

## Notebook 1

```
01_EDA.ipynb
```

Purpose

* Dataset exploration
* Class distribution
* Missing values
* Duplicate analysis

---

## Notebook 2

```
02_Preprocessing.ipynb
```

Purpose

* Merge CSV files
* Remove duplicates
* Handle NaN values
* Handle infinite values
* Encode labels
* Save cleaned dataset

Output

```
data/processed/clean_dataset.csv
```

---

## Notebook 3

```
03_Model_Training.ipynb
```

Purpose

* Load cleaned dataset
* Train Decision Tree
* Train Random Forest
* Train XGBoost
* Compare models
* Save the best model

Output

```
models/

best_model.pkl

label_encoder.pkl
```

---

# 13. Running the Streamlit Application

Move to the project root.

Run

```bash
streamlit run app/app.py
```

The application will automatically open in your browser.

---

# 14. Git Workflow

Before starting work

```bash
git pull origin Main
```

Create your own branch

```bash
git checkout -b feature-your-name
```

Example

```bash
git checkout -b feature-streamlit
```

Commit changes

```bash
git add .

git commit -m "Describe your changes"

git push origin feature-streamlit
```

Never work directly on the **Main** branch.

---

# 15. Common Problems

## Kernel not found

Run

```bash
python -m ipykernel install --user --name intrusion-detection-ml --display-name "Python (Intrusion Detection ML)"
```

Restart VS Code.

---

## ModuleNotFoundError

The virtual environment is probably not activated.

Activate it again.

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Wrong Python Interpreter

Press

```
Ctrl + Shift + P
```

Search

```
Python: Select Interpreter
```

Choose

```
venv
```

Then reopen the notebook and select

```
Python (Intrusion Detection ML)
```

---

# 16. Final Checklist

Before starting development, make sure that:

* ✅ Repository cloned
* ✅ Virtual environment created
* ✅ Virtual environment activated
* ✅ Dependencies installed
* ✅ Jupyter kernel installed
* ✅ Correct kernel selected
* ✅ Dataset downloaded
* ✅ Dataset copied into `data/raw/`
* ✅ Notebook 01 runs successfully
* ✅ Notebook 02 runs successfully
* ✅ Notebook 03 runs successfully
* ✅ Streamlit launches correctly
* ✅ Git is connected to the remote repository

If every item above is completed, the project is fully configured and ready for development.
