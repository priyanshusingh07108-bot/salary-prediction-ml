# 💼 SalaryIQ — AI Salary Prediction

> An end-to-end Machine Learning project that predicts the average salary of data and technology professionals using job, company, and technical-skill information.

## 🚀 Live Demo

🌐 **Live App:**  
https://salary-prediction-mlgit-guuvrbo5fjrilzesxh3z6y.streamlit.app/

---

## 📌 Project Overview

SalaryIQ is a Machine Learning web application designed to estimate the average annual salary of a job based on different job-market attributes.

The application takes information such as:

- Job Title
- Location
- Company Size
- Type of Ownership
- Industry
- Sector
- Revenue
- Company Rating
- Company Age
- Employer-provided salary
- Python
- R
- Spark
- AWS
- Excel

and generates an estimated average salary using a trained **Random Forest Regression model**.

---

## 📸 Application Preview

![SalaryIQ Dashboard](salaryiq-dashboard.png)

---

## 🎯 Problem Statement

Salary varies significantly depending on job role, company characteristics, location, experience-related factors, and technical requirements.

The goal of this project is to build a Machine Learning model that can learn these patterns from historical job-market data and provide a salary estimate for a new job profile.

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Duplicate Removal
     ↓
Missing Value Handling
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Categorical Encoding
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Final Model
     ↓
Streamlit Deployment
```

---

## 📊 Model Performance

The final Random Forest Regression model was evaluated on a held-out test dataset.

| Metric | Score |
|---|---:|
| MAE | $23.12K |
| RMSE | $29.65K |
| R² Score | 0.173 |

### Final Model

**Random Forest Regressor**

- Number of Trees: `300`
- Maximum Depth: `5`
- Minimum Samples Split: `5`
- Minimum Samples Leaf: `2`
- Random State: `42`

The model achieved an R² score of approximately **0.17** on the test dataset.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Random Forest Regression

### Data Visualization
- Matplotlib
- Seaborn

### Web Application
- Streamlit

### Model Deployment
- Streamlit Community Cloud

### Version Control
- Git
- GitHub

### Model & Data Processing
- Joblib
- One-Hot Encoding
- SimpleImputer
- ColumnTransformer
- Pipeline

---

## 📂 Project Structure

```text
salary-prediction-ml/
│
├── app.py
├── salary_prediction_model.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit web application |
| `salary_prediction_model.pkl` | Trained Random Forest ML pipeline |
| `requirements.txt` | Python dependencies |
| `runtime.txt` | Python runtime version |
| `README.md` | Project documentation |

---

## ✨ Key Features

- 🤖 Machine Learning-based salary prediction
- 🌲 Random Forest Regression model
- 🧹 Data cleaning and preprocessing pipeline
- 🔤 Automatic categorical feature encoding
- 🩹 Missing-value handling using imputation
- 🎯 Hyperparameter tuning using GridSearchCV
- 📊 Model evaluation using MAE, RMSE and R²
- 💻 Interactive Streamlit web application
- ⚡ Real-time salary prediction
- ☁️ Deployed using Streamlit Community Cloud

---

## 🚀 Future Improvements

- Improve model performance with advanced ensemble models
- Experiment with XGBoost and Gradient Boosting
- Add more job-market features
- Increase dataset size for better generalization
- Add salary prediction confidence intervals
- Add interactive data visualizations
- Improve UI/UX of the Streamlit application
- Add model explainability using SHAP

---

## 👨‍💻 Author

**Priyanshu Kumar**

B.Tech Student | Machine Learning & Data Science Enthusiast

- GitHub: [@priyanshusingh07108-bot](https://github.com/priyanshusingh07108-bot)
