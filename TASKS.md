# TASKS.md

# Project Task Distribution

This document defines the responsibilities of each team member. Every member should focus on their assigned tasks while collaborating with the rest of the team.

---

# Team Members

* **Member 1** – Machine Learning
* **Member 2** – Streamlit Application
* **Member 3** – Model Evaluation & Optimization

---

# Member 1 – Machine Learning Engineer

## Objective

Build, train and evaluate the machine learning models.

## Responsibilities

### Data Preparation

* Verify the cleaned dataset
* Perform train/test split using stratification
* Prepare datasets for training

### Model Training

Train the following models:

* Decision Tree
* Random Forest
* XGBoost

For each model:

* Train **with Destination Port**
* Train **without Destination Port**

Total experiments:

* Decision Tree (With Port)
* Decision Tree (Without Port)
* Random Forest (With Port)
* Random Forest (Without Port)
* XGBoost (With Port)
* XGBoost (Without Port)

### Model Evaluation

For every experiment compute:

* Accuracy
* Precision
* Recall
* F1-score
* Macro F1-score
* Confusion Matrix
* Training Time
* Prediction Time

### Model Comparison

Compare all six experiments.

Select the best-performing model.

### Model Export

Save:

```text
models/best_model.pkl
```

Save the label encoder:

```text
models/label_encoder.pkl
```

Deliverables

* Trained models
* Comparison table
* Saved model
* Saved encoder

---

# Member 2 – Streamlit Developer

## Objective

Develop the user interface.

## Responsibilities

### Project Structure

Create the Streamlit architecture.

```text
app/

pages/

assets/
```

### Pages

Develop:

* Home
* Dashboard
* Prediction
* About

### Dashboard

Display:

* Number of BENIGN flows
* Number of ATTACK flows
* Attack percentage
* Pie chart
* Bar chart
* Prediction statistics

### Prediction Page

Allow the user to:

* Upload a CSV file
* Display the uploaded data
* Run predictions
* Display predictions
* Download results as CSV

### Integration

Initially use dummy predictions if the model is not yet available.

Later replace them with:

```python
model.predict(data)
```

Deliverables

* Functional Streamlit application
* Clean UI
* Dashboard
* CSV upload
* Prediction page

---

# Member 3 – Model Evaluation & Optimization

## Objective

Improve and validate the machine learning models.

## Responsibilities

### Feature Importance

Analyse the importance of features.

Questions to answer:

* Which features are the most important?
* Is Destination Port among the most influential?
* Which features contribute the most to attack detection?

### Destination Port Analysis

Compare:

* Models with Destination Port
* Models without Destination Port

Analyse the impact on:

* Accuracy
* Recall
* Macro F1-score
* Training time

### Hyperparameter Optimization

Experiment with different parameters.

Examples

Decision Tree

* max_depth
* min_samples_split

Random Forest

* n_estimators
* max_depth
* min_samples_leaf

XGBoost

* learning_rate
* max_depth
* n_estimators

### Performance Analysis

Measure:

* Training time
* Prediction time

Compare the three models.

### Error Analysis

Analyse:

* False Positives
* False Negatives

Identify:

* Which attacks are difficult to detect.
* Why some attacks are misclassified.

### Final Recommendation

Recommend the best model considering:

* Performance
* Generalization
* Training time
* Prediction speed

Deliverables

* Feature importance analysis
* Hyperparameter comparison
* Performance comparison
* Final recommendation

---

# Collaboration Rules

Every member must:

* Pull the latest version before starting work.
* Work on a dedicated Git branch.
* Commit changes frequently.
* Push changes regularly.
* Open a Pull Request before merging into `Main`.

Useful commands:

```bash
git pull origin Main

git checkout -b feature-your-name

git add .

git commit -m "Describe your changes"

git push origin feature-your-name
```

---

# Communication

Before modifying another member's files:

* Inform the team.
* Avoid editing the same file simultaneously.
* Resolve merge conflicts together.

---

# Final Deliverables

By the end of the project, the team should provide:

* Cleaned dataset
* Trained ML models
* Model comparison
* Saved best model (`best_model.pkl`)
* Streamlit dashboard
* Source code
* Documentation
* Final report
* Presentation
