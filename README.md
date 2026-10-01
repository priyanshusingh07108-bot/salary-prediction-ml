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
