import pandas as pd
import joblib


# Load trained model, scaler and threshold
model = joblib.load(
    "data/processed/logistic_regression_model.pkl"
)

scaler = joblib.load(
    "data/processed/scaler.pkl"
)

threshold = joblib.load(
    "data/processed/churn_threshold.pkl"
)


# Columns used for one-hot encoding
categorical_cols = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]


# Numerical columns
num_cols = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]


def predict_churn(customer_data):
    """
    Predict customer churn probability and class.

    Parameters
    ----------
    customer_data : dict
        Customer information.

    Returns
    -------
    dict
        Churn probability, prediction and result.
    """

    # Convert input to DataFrame
    customer_df = pd.DataFrame([customer_data])

    # One-hot encode categorical features
    customer_encoded = pd.get_dummies(
        customer_df,
        columns=categorical_cols,
        drop_first=True
    )

    # Ensure exactly the same features as the trained model
    customer_encoded = customer_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    # Scale numerical features
    customer_encoded[num_cols] = scaler.transform(
        customer_encoded[num_cols]
    )

    # Predict probability
    churn_probability = model.predict_proba(
        customer_encoded
    )[0, 1]

    # Apply selected threshold
    prediction = int(
        churn_probability >= threshold
    )

    return {
        "churn_probability": round(
            float(churn_probability), 4
        ),
        "prediction": prediction,
        "result": (
            "Likely to Churn"
            if prediction == 1
            else "Likely to Stay"
        )
    }