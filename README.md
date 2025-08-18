# ❤️ Heart Disease Prediction & Analysis — Full ML Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-green?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Boost-yellow?logo=xgboost)

---

## 🚀 Quick Overview

Predict and analyze **heart disease risks** with a full **Machine Learning pipeline** — from preprocessing to Streamlit deployment.

**Try it Live:** [Ngrok Link](#)

---

## 🎬 Demo

![Streamlit App GIF](https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif)  
_Example of real-time predictions and interactive charts_

---

## 🎯 Features

- 🧹 Data Cleaning & Preprocessing
- 📉 Dimensionality Reduction (PCA)
- 🤖 Supervised Classification Models: Logistic Regression, Decision Trees, Random Forest, SVM
- 🔍 Unsupervised Clustering: K-Means & Hierarchical
- ⚙️ Hyperparameter Tuning with GridSearchCV / RandomizedSearchCV
- 💻 Streamlit Web UI for interactive predictions
- 🌐 Public deployment via Ngrok

---

## 🛠 Tools & Libraries

- Python 🐍 | Pandas | NumPy | Matplotlib | Seaborn
- Scikit-learn | XGBoost | RFE | PCA
- Streamlit | Joblib | Pickle

---

## 🗂 File Structure

Heart_Disease_Project/
│── data/
│ └── heart_disease.csv
│── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ └── 06_hyperparameter_tuning.ipynb
│── models/
│ └── final_model.pkl
│── ui/
│ └── app.py
│── deployment/
│ └── ngrok_setup.txt
│── results/
│ └── evaluation_metrics.txt
│── README.md
│── requirements.txt
│── .gitignore

## 📌 Dataset

We use the **UCI Heart Disease Dataset**, which contains patient health attributes for predicting heart disease.

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)

## ⚡ Installation

# Clone the repository

git clone <your-github-repo-url>
cd Heart_Disease_Project

# Create a virtual environment

python -m venv env

# Activate environment

# Windows

env\Scripts\activate

# macOS/Linux

source env/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run Streamlit app

streamlit run ui/app.py

## 🏃 How to Use

1. Open Jupyter notebooks in the `notebooks/` folder to explore preprocessing, PCA, feature selection, and model training.
2. Run `ui/app.py` with Streamlit for interactive predictions:
   ```bash
   streamlit run ui/app.py
   ```

---

### **4️⃣ Results / Evaluation**

Add a section to show **model performance**, like metrics, ROC curves, clustering visuals.

```markdown
## 📊 Results

- Supervised Models:
  - Logistic Regression Accuracy: 90%
  - Random Forest Accuracy: 93%
  - SVM Accuracy: 90%
```
