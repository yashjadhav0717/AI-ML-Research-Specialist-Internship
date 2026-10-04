"""
Data Preprocessing Module
Customer Churn Prediction and Business Analytics
"""

import os
import pandas as pd


PROJECT_PATH = r"C:\Users\Yash\OneDrive\Desktop\AI-ML-Research-Specialist-Internship\Task-06-Final-Data-Science-Capstone"

DATA_PATH = os.path.join(
    PROJECT_PATH,
    "data",
    "raw",
    "Telco_customer_churn.xlsx"
)


def load_data():
    """Load the Telco churn dataset."""
    df = pd.read_excel(DATA_PATH, sheet_name="Telco_Churn")
    return df


def clean_data(df):
    """Clean and prepare the dataset for machine learning."""

    df = df.copy()

    # Convert Total Charges to numeric
    df["Total Charges"] = pd.to_numeric(
        df["Total Charges"],
        errors="coerce"
    )

    # Remove rows where Total Charges could not be converted
    df = df.dropna(subset=["Total Charges"])

    # Leakage-prone and identifier columns
    columns_to_drop = [
        "CustomerID",
        "Count",
        "Country",
        "State",
        "City",
        "Zip Code",
        "Lat Long",
        "Latitude",
        "Longitude",
        "Churn Value",
        "Churn Score",
        "CLTV",
        "Churn Reason"
    ]

    df = df.drop(
        columns=columns_to_drop,
        errors="ignore"
    )

    # Create binary target
    df["Churn"] = (
        df["Churn Label"]
        .map({"Yes": 1, "No": 0})
    )

    # Remove original target label
    df = df.drop(
        columns=["Churn Label"],
        errors="ignore"
    )

    return df


def prepare_dataset():
    """Load and clean the dataset."""

    df = load_data()
    df = clean_data(df)

    return df


if __name__ == "__main__":

    df = prepare_dataset()

    print("Dataset successfully prepared.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nMissing values:")
    print(df.isnull().sum())