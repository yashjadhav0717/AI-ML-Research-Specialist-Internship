"""
Exploratory Data Analysis Module
Customer Churn Prediction and Business Analytics
"""

import os

import matplotlib.pyplot as plt
import seaborn as sns

from data_preprocessing import prepare_dataset


PROJECT_PATH = r"C:\Users\Yash\OneDrive\Desktop\AI-ML-Research-Specialist-Internship\Task-06-Final-Data-Science-Capstone"

VISUALIZATION_PATH = os.path.join(
    PROJECT_PATH,
    "visualizations"
)

os.makedirs(VISUALIZATION_PATH, exist_ok=True)


def save_plot(filename):
    """Save and close the current plot."""

    path = os.path.join(
        VISUALIZATION_PATH,
        filename
    )

    plt.tight_layout()
    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def churn_distribution(df):

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Churn"
    )

    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")

    save_plot("01_churn_distribution.png")


def contract_vs_churn(df):

    plt.figure(figsize=(9, 5))

    sns.countplot(
        data=df,
        x="Contract",
        hue="Churn"
    )

    plt.title("Contract Type vs Customer Churn")
    plt.xlabel("Contract Type")
    plt.ylabel("Number of Customers")

    save_plot("04_contract_vs_churn.png")


def internet_service_vs_churn(df):

    plt.figure(figsize=(9, 5))

    sns.countplot(
        data=df,
        x="Internet Service",
        hue="Churn"
    )

    plt.title("Internet Service vs Customer Churn")
    plt.xlabel("Internet Service")
    plt.ylabel("Number of Customers")

    save_plot("05_internet_service_vs_churn.png")


def payment_method_vs_churn(df):

    plt.figure(figsize=(10, 5))

    sns.countplot(
        data=df,
        x="Payment Method",
        hue="Churn"
    )

    plt.xticks(rotation=30)

    plt.title("Payment Method vs Customer Churn")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")

    save_plot("06_payment_method_vs_churn.png")


def tenure_vs_churn(df):

    plt.figure(figsize=(9, 5))

    sns.boxplot(
        data=df,
        x="Churn",
        y="Tenure Months"
    )

    plt.title("Tenure Months vs Customer Churn")
    plt.xlabel("Churn")
    plt.ylabel("Tenure Months")

    save_plot("07_tenure_vs_churn.png")


def monthly_charges_vs_churn(df):

    plt.figure(figsize=(9, 5))

    sns.boxplot(
        data=df,
        x="Churn",
        y="Monthly Charges"
    )

    plt.title("Monthly Charges vs Customer Churn")
    plt.xlabel("Churn")
    plt.ylabel("Monthly Charges")

    save_plot("08_monthly_charges_vs_churn.png")


def senior_citizen_vs_churn(df):

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Senior Citizen",
        hue="Churn"
    )

    plt.title("Senior Citizen Status vs Customer Churn")
    plt.xlabel("Senior Citizen")
    plt.ylabel("Number of Customers")

    save_plot("09_senior_citizen_vs_churn.png")


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=["number"]
    )

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    save_plot("10_correlation_heatmap.png")


def run_eda():

    df = prepare_dataset()

    print("Running Exploratory Data Analysis...")

    churn_distribution(df)
    contract_vs_churn(df)
    internet_service_vs_churn(df)
    payment_method_vs_churn(df)
    tenure_vs_churn(df)
    monthly_charges_vs_churn(df)
    senior_citizen_vs_churn(df)
    correlation_heatmap(df)

    print(
        f"EDA visualizations saved to:\n{VISUALIZATION_PATH}"
    )


if __name__ == "__main__":
    run_eda()