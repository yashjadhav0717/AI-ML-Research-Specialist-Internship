"""
Machine Learning Model Evaluation Module
Customer Churn Prediction and Business Analytics
"""

import os

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve
)

from model_training import train_models


PROJECT_PATH = r"C:\Users\Yash\OneDrive\Desktop\AI-ML-Research-Specialist-Internship\Task-06-Final-Data-Science-Capstone"

REPORT_PATH = os.path.join(
    PROJECT_PATH,
    "reports"
)

VISUALIZATION_PATH = os.path.join(
    PROJECT_PATH,
    "visualizations"
)

os.makedirs(REPORT_PATH, exist_ok=True)
os.makedirs(VISUALIZATION_PATH, exist_ok=True)


def evaluate_models():

    (
        models,
        X_train,
        X_test,
        y_train,
        y_test
    ) = train_models()

    results = []

    for name, model in models.items():

        predictions = model.predict(X_test)

        probabilities = model.predict_proba(
            X_test
        )[:, 1]

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        roc_auc = roc_auc_score(
            y_test,
            probabilities
        )

        results.append({

            "Model": name,

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1 Score": f1,

            "ROC-AUC": roc_auc

        })

    results_df = pd.DataFrame(results)

    output_path = os.path.join(
        REPORT_PATH,
        "model_performance.csv"
    )

    results_df.to_csv(
        output_path,
        index=False
    )

    print("\nModel Performance:")
    print(results_df)

    return (
        models,
        X_test,
        y_test,
        results_df
    )


def save_confusion_matrix(
    model,
    X_test,
    y_test,
    model_name="Logistic Regression"
):

    predictions = model.predict(X_test)

    cm = confusion_matrix(
        y_test,
        predictions
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    display.plot()

    plt.title(
        f"Confusion Matrix - {model_name}"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            VISUALIZATION_PATH,
            "12_confusion_matrix.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def save_roc_curve(
    models,
    X_test,
    y_test
):

    plt.figure(figsize=(8, 6))

    for name, model in models.items():

        probabilities = model.predict_proba(
            X_test
        )[:, 1]

        fpr, tpr, _ = roc_curve(
            y_test,
            probabilities
        )

        auc = roc_auc_score(
            y_test,
            probabilities
        )

        plt.plot(
            fpr,
            tpr,
            label=f"{name} (AUC={auc:.3f})"
        )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--"
    )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.title(
        "ROC Curve Comparison"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            VISUALIZATION_PATH,
            "13_roc_curve_comparison.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def save_classification_report(
    models,
    X_test,
    y_test
):

    report_path = os.path.join(
        REPORT_PATH,
        "classification_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        for name, model in models.items():

            predictions = model.predict(
                X_test
            )

            file.write(
                f"\n{name}\n"
            )

            file.write(
                "=" * 60
            )

            file.write("\n")

            file.write(
                classification_report(
                    y_test,
                    predictions
                )
            )

            file.write("\n\n")


if __name__ == "__main__":

    (
        models,
        X_test,
        y_test,
        results
    ) = evaluate_models()

    best_model_name = (
        results
        .sort_values(
            "ROC-AUC",
            ascending=False
        )
        .iloc[0]["Model"]
    )

    print(
        f"\nBest Model: {best_model_name}"
    )

    best_model = models[
        best_model_name
    ]

    save_confusion_matrix(
        best_model,
        X_test,
        y_test,
        best_model_name
    )

    save_roc_curve(
        models,
        X_test,
        y_test
    )

    save_classification_report(
        models,
        X_test,
        y_test
    )

    print(
        "\nEvaluation completed successfully."
    )