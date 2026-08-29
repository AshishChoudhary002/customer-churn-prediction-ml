# 📊 Customer Churn Prediction

An end-to-end machine learning project that predicts the probability of customer churn and identifies customers who may require retention attention.

This project covers the complete machine learning workflow — from exploratory data analysis and preprocessing to model comparison, threshold tuning, prediction, and an interactive Streamlit application.

---

## 🚀 Project Overview

Customer churn is a major business challenge for subscription-based companies. Identifying customers who are likely to leave allows businesses to take proactive retention actions.

This project uses the Telco Customer Churn dataset to build a binary classification system that estimates a customer's probability of churn.

The final system provides:

* Customer churn probability
* Churn risk classification
* Model decision
* Business-oriented recommendation
* Model performance information
* Interactive prediction interface

---

## 🎯 Business Problem

Telecommunication companies lose revenue when customers discontinue their services.

The objective of this project is to answer:

> **"Is this customer likely to churn?"**

Instead of relying only on historical churn statistics, the model uses customer demographics, tenure, services, contract information, payment method, and billing information to estimate individual churn risk.

This can support proactive customer retention strategies.

---

## 📊 Dataset

The project uses the **Telco Customer Churn dataset**.

### Dataset Characteristics

* **7,032 customers**
* **20 columns**
* Binary target variable: `Churn`
* Numerical and categorical features

### Churn Distribution

| Churn | Percentage |
| ----- | ---------: |
| No    |     73.46% |
| Yes   |     26.54% |

### Major Feature Groups

**Customer Profile**

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure

**Services**

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

**Contract & Billing**

* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

---

## 🔍 Exploratory Data Analysis

The exploratory analysis identified several features with meaningful relationships with customer churn.

Important observations included:

* **Contract type** showed a strong relationship with churn.
* **Month-to-month customers** were more vulnerable to churn than customers with longer contracts.
* **Tenure** was associated with customer retention.
* **Internet service type** showed differences in churn behavior.
* **Online security and technical support** were associated with churn patterns.
* **Payment method** showed differences in customer churn.
* **Monthly charges** and billing-related features provided useful predictive information.
* Customer demographics such as **Partner** and **Dependents** also showed relationships with churn.

The dataset was also checked for data quality issues and preprocessing requirements.

---

## ⚙️ Machine Learning Pipeline

The project follows an end-to-end machine learning workflow:

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Categorical Encoding
    ↓
Train/Test Split
    ↓
Feature Scaling
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Threshold Tuning
    ↓
Prediction Pipeline
    ↓
Streamlit Application
```

### Preprocessing

The preprocessing workflow includes:

* Conversion of `TotalCharges` to numeric format
* Handling categorical variables
* One-hot encoding using `drop_first=True`
* Numerical feature scaling using `StandardScaler`
* Train/test splitting
* Consistent feature alignment during prediction

---

## 🤖 Models Evaluated

Four classification models were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost

### Model Comparison

| Model                   |   Accuracy |    ROC-AUC |
| ----------------------- | ---------: | ---------: |
| **Logistic Regression** | **80.53%** |     0.8361 |
| XGBoost                 |     79.46% | **0.8384** |
| Random Forest           |     78.68% |     0.8172 |
| Decision Tree           |     71.64% |     0.6343 |

### Model Selection

Logistic Regression achieved the highest accuracy among the evaluated models, while XGBoost achieved a slightly higher ROC-AUC.

This demonstrates why model selection should not rely on a single metric.

For this project, **Logistic Regression was selected for deployment** because it provided a strong overall balance of classification performance at the selected operating threshold while remaining simple and interpretable.

---

## 🎚️ Classification Threshold Tuning

The default classification threshold of `0.50` was evaluated along with several alternative thresholds.

| Threshold | Precision |    Recall |  F1-Score |
| --------: | --------: | --------: | --------: |
|      0.30 |     0.513 | **0.759** |     0.612 |
|      0.35 |     0.545 |     0.722 |     0.621 |
|  **0.40** | **0.578** |     0.684 | **0.627** |
|      0.45 |     0.604 |     0.631 |     0.617 |
|      0.50 |     0.652 |     0.575 |     0.611 |
|      0.55 |     0.670 |     0.484 |     0.562 |
|      0.60 |     0.679 |     0.385 |     0.491 |

A threshold of **0.40** was selected because it produced the highest F1-score among the tested thresholds.

This threshold increases sensitivity toward potential churners compared with the standard `0.50` threshold.

---

## 🏆 Final Deployed Model

**Logistic Regression**

The deployed prediction pipeline uses:

* Logistic Regression
* Saved `StandardScaler`
* One-hot encoded features
* Classification threshold of **0.40**

### Final Evaluation at Threshold 0.40

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **78.32%** |
| Precision | **57.79%** |
| Recall    | **68.45%** |
| F1-Score  | **62.67%** |
| ROC-AUC   | **83.61%** |

> **Note:** ROC-AUC is threshold-independent, while accuracy, precision, recall, and F1-score change according to the selected classification threshold.

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application that allows users to enter customer information and receive an individual churn assessment.

### Application Features

* Customer profile input
* Service information input
* Contract and payment information
* Billing information
* Churn probability
* Risk level
* Model decision
* Business recommendation
* Model performance overview
* Selected model information
* Classification threshold explanation

### Example Prediction

```text
Churn Probability: 30.71%

Risk Level: LOW

Model Decision: LIKELY TO STAY

Classification Threshold: 0.40
```

---

## 🏗️ Project Architecture

```text
Raw Dataset
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Data Preprocessing
(Encoding + Scaling)
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
& Threshold Optimization
     │
     ▼
Logistic Regression
     │
     ▼
Prediction Pipeline
     │
     ▼
Streamlit Application
     │
     ▼
Churn Risk Assessment
```

---

## 📁 Project Structure

```text
customer-churn-prediction-ml/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── final_model_results.csv
│       ├── logistic_regression_model.pkl
│       ├── scaler.pkl
│       └── churn_threshold.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Prediction_Pipeline.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── predict.py
│   ├── train_model.py
│   └── utils.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost

### Model Persistence

* Joblib

### Application

* Streamlit

### Development

* Jupyter Notebook
* Git
* GitHub

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AshishChoudhary002/customer-churn-prediction-ml.git
cd customer-churn-prediction-ml
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app/app.py
```

The application will open in your browser.

---

## 📈 Business Interpretation

The model is designed as a **decision-support tool**, not as an automatic replacement for customer-retention teams.

Customers identified as higher risk could be considered for actions such as:

* Personalized retention offers
* Contract incentives
* Service-quality follow-up
* Technical support outreach
* Plan recommendations
* Customer satisfaction engagement

The appropriate intervention should depend on the company's retention strategy and the customer's individual circumstances.

---

## 🔮 Future Improvements

Potential future improvements include:

* Hyperparameter tuning
* Cross-validation
* Probability calibration
* More advanced feature engineering
* Model explainability using SHAP
* Automated model monitoring
* API-based serving
* Cloud deployment
* Customer-level retention strategy optimization

---

## 📌 Key Learning Outcomes

This project demonstrates practical experience with:

* Exploratory Data Analysis
* Data cleaning
* Categorical encoding
* Feature scaling
* Classification algorithms
* Model comparison
* Precision/recall trade-offs
* Classification threshold optimization
* Model persistence
* Prediction pipelines
* Streamlit application development
* Git/GitHub project organization

---

## 👨‍💻 Author

**Ashish Choudhary**

B.Tech — Artificial Intelligence & Data Science

GitHub:
https://github.com/AshishChoudhary002
