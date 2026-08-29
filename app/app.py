
import sys
from pathlib import Path

import pandas as pd
import streamlit as st


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


# ============================================================
# MODEL PREDICTION
# ============================================================

from src.predict import predict_churn


# ============================================================
# FINAL MODEL RESULTS
# ============================================================

RESULTS_PATH = PROJECT_ROOT / "data" / "processed" / "final_model_results.csv"

final_results_df = pd.read_csv(RESULTS_PATH)

final_result = final_results_df.iloc[0]

FINAL_THRESHOLD = final_result["Threshold"]
FINAL_ACCURACY = final_result["Accuracy"]
FINAL_PRECISION = final_result["Precision"]
FINAL_RECALL = final_result["Recall"]
FINAL_F1 = final_result["F1-Score"]
FINAL_ROC_AUC = final_result["ROC-AUC"]



# Load final deployed model results
RESULTS_PATH = PROJECT_ROOT / "data" / "processed" / "final_model_results.csv"

final_results_df = pd.read_csv(RESULTS_PATH)

final_result = final_results_df.iloc[0]

FINAL_THRESHOLD = final_result["Threshold"]
FINAL_ACCURACY = final_result["Accuracy"]
FINAL_PRECISION = final_result["Precision"]
FINAL_RECALL = final_result["Recall"]
FINAL_F1 = final_result["F1-Score"]
FINAL_ROC_AUC = final_result["ROC-AUC"]

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.predict import predict_churn


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            font-size: 1.1rem;
            opacity: 0.75;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 1rem;
        }

        .result-box {
            padding: 1.2rem;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            margin-top: 1rem;
        }

        .small-text {
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Customer Churn Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict customer churn probability using a machine learning model '
    'and identify customers who may require retention attention.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Customer Profile</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

with col2:
    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

with col3:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )


st.divider()


# ============================================================
# SERVICE INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📡 Service Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col2:
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

with col3:
    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


st.divider()


# ============================================================
# CONTRACT & PAYMENT
# ============================================================

st.markdown(
    '<div class="section-title">💳 Contract & Payment</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

with col3:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


st.divider()


# ============================================================
# BILLING INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">💰 Billing Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.50,
        step=1.0
    )

with col2:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=846.00,
        step=10.0
    )


st.markdown("")
st.markdown("### 🔮 Generate Prediction")

predict_button = st.button(
    "Analyze Churn Risk",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTIONdir /B models
# ============================================================


if predict_button:

    customer = {
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,

        "gender": gender,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method
    }

    result = predict_churn(customer)

    probability = result["churn_probability"]
    prediction = result["prediction"]

    st.divider()

    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.markdown("## 📈 Churn Risk Assessment")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    with result_col2:

        if probability >= 0.70:
            risk_level = "HIGH"
        elif probability >= 0.40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        st.metric(
            "Risk Level",
            risk_level
        )

    with result_col3:

        if prediction == 1:
            st.metric(
                "Model Decision",
                "LIKELY TO CHURN"
            )
        else:
            st.metric(
                "Model Decision",
                "LIKELY TO STAY"
            )

    st.progress(
        min(max(probability, 0.0), 1.0)
    )

    st.caption(
        "Risk level is based on the predicted probability. "
        "The model's binary decision uses a classification "
        "threshold of 0.40."
    )

    if prediction == 1:

        st.error(
            "⚠️ **Model Decision: Likely to Churn** — "
            "the predicted probability meets or exceeds the "
            "0.40 classification threshold."
        )

    else:

        st.success(
            "✅ **Model Decision: Likely to Stay** — "
            "the predicted probability is below the "
            "0.40 classification threshold."
        )

    # ========================================================
    # BUSINESS RECOMMENDATION
    # ========================================================

    st.markdown("### 💡 Business Recommendation")

    if probability >= 0.70:

        recommendation = (
            "Prioritize this customer for immediate retention "
            "outreach. Consider personalized offers, contract "
            "incentives, or proactive support."
        )

    elif probability >= 0.40:

        recommendation = (
            "This customer shows moderate-to-elevated churn "
            "risk. Consider proactive engagement and targeted "
            "retention offers."
        )

    else:

        recommendation = (
            "The customer currently shows relatively low churn "
            "risk. Continue normal engagement and service support."
        )

    st.info(recommendation)




# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.markdown("## 📊 Model Performance")

st.markdown(
    "Performance comparison of the machine learning models "
    "evaluated during model development."
)

model_results = {
    "Model": [
        "Logistic Regression",
        "XGBoost",
        "Random Forest",
        "Decision Tree"
    ],
    "Accuracy": [
        80.53,
        79.46,
        78.68,
        71.64
    ],
    "ROC-AUC": [
        0.8361,
        0.8384,
        0.8172,
        0.6343
    ],
    "Churn Precision": [
        0.65,
        0.63,
        0.62,
        0.47
    ],
    "Churn Recall": [
        0.57,
        0.55,
        0.50,
        0.46
    ],
    "Churn F1": [
        0.61,
        0.59,
        0.56,
        0.46
    ]
}

st.dataframe(
    model_results,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FINAL DEPLOYED MODEL
# ============================================================

st.markdown("### 🏆 Final Deployed Model")

st.success("**Logistic Regression**")

st.write(
    "Logistic Regression was selected for deployment based on "
    "its strong overall classification performance and "
    "interpretability. The classification threshold was tuned "
    "across multiple values from 0.30 to 0.60, with 0.40 selected "
    "because it produced the highest F1-score among the tested "
    "thresholds."
)


# ============================================================
# FINAL MODEL METRICS
# ============================================================

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns(5)

with metric_col1:
    st.metric(
        "Accuracy",
        f"{FINAL_ACCURACY:.2%}"
    )

with metric_col2:
    st.metric(
        "Precision",
        f"{FINAL_PRECISION:.2%}"
    )

with metric_col3:
    st.metric(
        "Recall",
        f"{FINAL_RECALL:.2%}"
    )

with metric_col4:
    st.metric(
        "F1-Score",
        f"{FINAL_F1:.2%}"
    )

with metric_col5:
    st.metric(
        "ROC-AUC",
        f"{FINAL_ROC_AUC:.4f}"
    )


# ============================================================
# CLASSIFICATION THRESHOLD
# ============================================================

st.markdown("### 🎯 Classification Threshold")

st.metric(
    "Selected Threshold",
    f"{FINAL_THRESHOLD:.2f}"
)

st.write(
    f"Customers with a predicted churn probability of "
    f"{FINAL_THRESHOLD:.0%} or higher are classified as "
    "likely to churn."
)

st.caption(
    "The 0.40 threshold produced the highest F1-score (0.627) "
    "among the evaluated thresholds, providing a balance between "
    "churn precision and recall."
)



# ============================================================
# MODEL INFORMATION
# ============================================================

with st.expander("🤖 About the ML Model"):

    st.write(
        """
        **Algorithm:** Logistic Regression

        **Evaluation metrics:** Accuracy, ROC-AUC, Precision, Recall,
        and F1-score.

        **Classification threshold:** 0.40

        The prediction pipeline applies the same feature encoding,
        feature alignment, and numerical scaling used during model
        development before generating the churn probability.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Customer Churn Prediction • Machine Learning Portfolio Project"
)

