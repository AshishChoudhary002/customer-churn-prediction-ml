import sys
from pathlib import Path

import streamlit as st

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.predict import predict_churn

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer information to predict the probability of churn."
)

st.divider()

# -----------------------------
# Customer Information
# -----------------------------

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.50
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=846.00
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

with col2:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

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

# -----------------------------
# Contract & Payment
# -----------------------------

st.header("Contract & Payment")

col3, col4 = st.columns(2)

with col3:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

with col4:
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

# -----------------------------
# Prediction Button
# -----------------------------

predict_button = st.button(
    "🔮 Predict Churn",
    type="primary",
    use_container_width=True
)

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

    st.header("Prediction Result")

    col5, col6 = st.columns(2)

    with col5:
        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    with col6:
        if prediction == 1:
            st.error("⚠️ Likely to Churn")
        else:
            st.success("✅ Likely to Stay")