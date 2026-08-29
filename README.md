# ðŸ“Š Customer Churn Prediction



An end-to-end machine learning project that predicts the probability of customer churn and identifies customers who may require retention attention.



The project covers the complete machine learning workflow â€” from exploratory data analysis and preprocessing to model comparison, threshold tuning, prediction, and an interactive Streamlit application.



---



## ðŸš€ Project Overview



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



## ðŸŽ¯ Business Problem



Telecommunication companies lose revenue when customers discontinue their services.



The objective of this project is to answer:



> **"Is this customer likely to churn?"**



Instead of relying only on historical churn statistics, the model uses customer demographics, tenure, services, contract information, payment method, and billing information to estimate individual churn risk.



This can support proactive customer retention strategies.



---



## ðŸ“Š Dataset



The project uses the **Telco Customer Churn dataset**.



### Dataset characteristics



* **7,032 customers**

* **20 columns**

* Binary target variable: `Churn`

* Numerical and categorical features

* Churn distribution:



&#x20; * No: **73.46%**

&#x20; * Yes: **26.54%**



### Major feature groups



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



## ðŸ”Â Exploratory Data Analysis



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



## âš™ï¸Â Machine Learning Pipeline



The project follows an end-to-end machine learning workflow:



```text

Raw Dataset

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Data Cleaning

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Exploratory Data Analysis

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Feature Engineering

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Categorical Encoding

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Train/Test Split

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Feature Scaling

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Model Training

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Model Evaluation

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Threshold Tuning

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

Prediction Pipeline

&#x20;    Ã¢â€â€š

&#x20;    Ã¢â€“Â¼

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



## ðŸ¤– Models Evaluated



Four classification models were evaluated:



1. Logistic Regression

2. Decision Tree

3. Random Forest

4. XGBoost



### Model Comparison



| Model               |   Accuracy |    ROC-AUC |

| ------------------- | ---------: | ---------: |

| Logistic Regression | **80.53%** |     0.8361 |

| XGBoost             |     79.46% | **0.8384** |

| Random Forest       |     78.68% |     0.8172 |

| Decision Tree       |     71.64% |     0.6343 |



### Interpretation



Logistic Regression achieved the highest accuracy among the evaluated models, while XGBoost achieved a slightly higher ROC-AUC.



This shows why model selection should not rely on a single metric.



For this project, Logistic Regression was selected for deployment because it provided the strongest overall balance of classification performance for the selected operating threshold and offers a simple, interpretable model suitable for the application.



---



## ðŸŽšï¸Â Classification Threshold Tuning



The default classification threshold of 0.50 was evaluated along with several alternative thresholds.



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



This threshold increases sensitivity toward potential churners compared with the standard 0.50 threshold.



---



## Ã°Å¸Ââ€  Final Deployed Model



**Logistic Regression**



The deployed prediction pipeline uses:



* Logistic Regression

* Saved `StandardScaler`

* One-hot encoded features

* Classification threshold of **0.40**



### Final evaluation at threshold 0.40



| Metric    |      Score |

| --------- | ---------: |

| Accuracy  | **78.32%** |

| Precision | **57.79%** |

| Recall    | **68.45%** |

| F1-Score  | **62.67%** |

| ROC-AUC   | **83.61%** |



The ROC-AUC remains threshold-independent, while the classification metrics change according to the selected threshold.



---



## ðŸ–¥ï¸Â Streamlit Application



The project includes an interactive Streamlit application that allows users to enter customer information and receive an individual churn assessment.



### Application features



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



### Example



A sample prediction may look like:



```text

Churn Probability: 30.71%



Risk Level: LOW



Model Decision: LIKELY TO STAY



Classification Threshold: 0.40

```



---



## Ã°Å¸Ââ€”Ã¯Â¸Â Project Architecture



```text

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š   Raw Dataset    Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š       EDA        Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š  Preprocessing   Ã¢â€â€š

&#x20;                   Ã¢â€â€š Encoding/Scaling Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š Model Training   Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                Ã¢â€â€š Model Evaluation &     Ã¢â€â€š

&#x20;                Ã¢â€â€š Threshold Optimization Ã¢â€â€š

&#x20;                Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š Logistic         Ã¢â€â€š

&#x20;                   Ã¢â€â€š Regression       Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š Prediction       Ã¢â€â€š

&#x20;                   Ã¢â€â€š Pipeline         Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š Streamlit App    Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

&#x20;                            Ã¢â€â€š

&#x20;                            Ã¢â€“Â¼

&#x20;                   Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â

&#x20;                   Ã¢â€â€š Churn Risk       Ã¢â€â€š

&#x20;                   Ã¢â€â€š Assessment       Ã¢â€â€š

&#x20;                   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

```



---



## ðŸ“Â Project Structure



```text

customer-churn-prediction-ml/

Ã¢â€â€š

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ app/

Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ app.py

Ã¢â€â€š

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ data/

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ raw/

Ã¢â€â€š   Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ WA_Fn-UseC_-Telco-Customer-Churn.csv

Ã¢â€â€š   Ã¢â€â€š

Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ processed/

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ X_train.csv

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ X_test.csv

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ y_train.csv

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ y_test.csv

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ final_model_results.csv

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ logistic_regression_model.pkl

Ã¢â€â€š       Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ scaler.pkl

Ã¢â€â€š       Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ churn_threshold.pkl

Ã¢â€â€š

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ notebooks/

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ 01_EDA.ipynb

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ 02_Data_Preprocessing.ipynb

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ 03_Model_Training.ipynb

Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ 04_Prediction_Pipeline.ipynb

Ã¢â€â€š

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ src/

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ data_preprocessing.py

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ predict.py

Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ train_model.py

Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ utils.py

Ã¢â€â€š

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ .gitignore

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LICENSE

Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ README.md

Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ requirements.txt

```



---



## Ã°Å¸â€ºÂ Ã¯Â¸Â Tech Stack



**Programming Language**



* Python



**Data Analysis**



* Pandas

* NumPy

* Matplotlib

* Seaborn



**Machine Learning**



* Scikit-learn

* XGBoost



**Model Persistence**



* Joblib



**Application**



* Streamlit



**Development**



* Jupyter Notebook

* Git

* GitHub



---



## ðŸš€ Installation



### 1. Clone the repository



```bash

git clone https://github.com/AshishChoudhary002/customer-churn-prediction-ml.git

cd customer-churn-prediction-ml

```



### 2. Create a virtual environment



Windows:



```bash

python -m venv .venv

```



Activate it:



```bash

.venvScriptsactivate

```



### 3. Install dependencies



```bash

pip install -r requirements.txt

```



### 4. Run the application



```bash

python -m streamlit run app/app.py

```



The application will open in your browser.



---



## ðŸ“Š Business Interpretation



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



## ðŸ”Â® Future Improvements



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



## ðŸ“Å’ Key Learning Outcomes



This project helped demonstrate practical experience with:



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



## Ã°Å¸â€˜Â¨Ã¢â‚¬ÂÃ°Å¸â€™Â» Author



**Ashish Choudhary**



B.Tech â€” Artificial Intelligence & Data Science



GitHub:

https://github.com/AshishChoudhary002
