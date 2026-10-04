"""
Machine Learning Model Training Module
Customer Churn Prediction and Business Analytics
"""

import os

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from data_preprocessing import prepare_dataset


PROJECT_PATH = r"C:\Users\Yash\OneDrive\Desktop\AI-ML-Research-Specialist-Internship\Task-06-Final-Data-Science-Capstone"

REPORT_PATH = os.path.join(
    PROJECT_PATH,
    "reports"
)

os.makedirs(REPORT_PATH, exist_ok=True)


def create_preprocessor(X):

    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                numeric_features
            ),
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_features
            )
        ]
    )

    return preprocessor


def train_models():

    df = prepare_dataset()

    X = df.drop(
        columns=["Churn"]
    )

    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    preprocessor = create_preprocessor(X)

    models = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000
            ),

        "Decision Tree":
            DecisionTreeClassifier(
                random_state=42
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                n_jobs=-1
            )
    }

    trained_models = {}

    for name, model in models.items():

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ]
        )

        pipeline.fit(
            X_train,
            y_train
        )

        trained_models[name] = pipeline

        print(
            f"{name} trained successfully."
        )

    return (
        trained_models,
        X_train,
        X_test,
        y_train,
        y_test
    )


if __name__ == "__main__":

    models, X_train, X_test, y_train, y_test = train_models()

    print(
        f"\nTraining samples: {len(X_train)}"
    )

    print(
        f"Testing samples: {len(X_test)}"
    )