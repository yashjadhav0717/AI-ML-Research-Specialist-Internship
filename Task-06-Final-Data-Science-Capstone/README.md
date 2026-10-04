# Customer Churn Prediction and Business Analytics Using Machine Learning

## Final Data Science Capstone Project

## 1. Project Overview

Customer churn is a major business challenge for subscription-based service providers. Losing customers directly affects recurring revenue and increases the cost of acquiring new customers.

This project develops a complete data science solution for analyzing customer churn behavior and predicting customers who are more likely to discontinue their services.

The project applies a complete data science workflow, including data understanding, data cleaning, exploratory data analysis, visualization, feature preparation, machine learning, model evaluation, feature importance analysis, and business recommendations.

The analysis is performed using the Telco Customer Churn dataset containing 7,043 customer records and 33 original features.

---

## 2. Problem Statement

The objective of this project is to understand the factors associated with customer churn and develop a machine learning model capable of predicting whether a customer is likely to churn.

The analysis focuses on identifying customer characteristics, service-related factors, contract patterns, billing behavior, and other variables that may contribute to customer churn.

The final solution is intended to support data-driven customer retention strategies.

---

## 3. Project Objectives

The primary objectives of this project are:

- Analyze customer data to understand churn behavior.
- Identify patterns and relationships associated with customer churn.
- Clean and preprocess the dataset.
- Perform exploratory data analysis.
- Create meaningful data visualizations.
- Prepare features for machine learning.
- Develop multiple classification models.
- Compare model performance using appropriate evaluation metrics.
- Identify important predictive features.
- Generate actionable business recommendations.
- Demonstrate a complete end-to-end Data Science workflow.

---

## 4. Dataset

The project uses the Telco Customer Churn dataset.

### Dataset Information

| Attribute | Value |
|---|---:|
| Total Customers | 7,043 |
| Original Features | 33 |
| Target Variable | Churn Label |
| Churned Customers | 26.54% |
| Problem Type | Binary Classification |

### Target Variable

The target variable is:

`Churn Label`

It contains two classes:

- `Yes` — Customer churned
- `No` — Customer remained with the company

---

## 5. Key Business Questions

The project investigates the following questions:

1. What percentage of customers are churning?
2. Which customer characteristics are associated with churn?
3. Does contract type influence customer churn?
4. Does customer tenure affect churn behavior?
5. How are monthly charges related to churn?
6. Does internet service type affect churn?
7. Does payment method show different churn patterns?
8. Which features are most important for churn prediction?
9. Which machine learning model performs best?
10. How can the business improve customer retention?

---

## 6. Technologies and Tools

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Development Environment

- Jupyter Notebook
- Visual Studio Code

### Data Format

- Microsoft Excel

### Version Control

- Git
- GitHub

---

## 7. Project Methodology

The project follows the following data science workflow:

```text
Data Collection
      |
      v
Data Understanding
      |
      v
Data Quality Analysis
      |
      v
Data Cleaning
      |
      v
Exploratory Data Analysis
      |
      v
Data Visualization
      |
      v
Feature Preparation
      |
      v
Train-Test Split
      |
      v
Data Preprocessing
      |
      v
Machine Learning
      |
      v
Model Evaluation
      |
      v
Feature Importance Analysis
      |
      v
Business Insights
      |
      v
Recommendations
```

---

## 8. Data Preparation

The following data preparation activities were performed:

- Dataset structure inspection.
- Data type verification.
- Missing value analysis.
- Duplicate record analysis.
- Numerical and categorical feature identification.
- Conversion of `Total Charges` into numerical format.
- Target variable encoding.
- Removal of identifier and leakage-prone variables.
- Numerical feature imputation and scaling.
- Categorical feature imputation and one-hot encoding.
- Stratified train-test split.

### Data Leakage Prevention

The following variables were excluded from machine learning features:

- CustomerID
- Count
- Country
- State
- City
- Zip Code
- Lat Long
- Latitude
- Longitude
- Churn Value
- Churn Score
- CLTV
- Churn Reason

Variables such as `Churn Score`, `Churn Value`, and `Churn Reason` are directly related to the churn outcome and could introduce target leakage into the model.

---

## 9. Exploratory Data Analysis

The exploratory analysis examined relationships between customer churn and:

- Gender
- Contract Type
- Internet Service
- Payment Method
- Tenure
- Monthly Charges
- Senior Citizen Status
- Partner Status
- Dependents
- Numerical feature correlations

The analysis used statistical summaries, cross-tabulation, box plots, bar charts, pie charts, and correlation analysis.

---

## 10. Data Visualizations

The project generated the following visualizations:

1. Customer Churn Distribution
2. Customer Churn Percentage
3. Gender vs Churn
4. Contract Type vs Churn
5. Internet Service vs Churn
6. Payment Method vs Churn
7. Tenure vs Churn
8. Monthly Charges vs Churn
9. Senior Citizen Status vs Churn
10. Correlation Heatmap
11. Machine Learning Model Performance Comparison
12. Random Forest Confusion Matrix
13. ROC Curve Comparison
14. Random Forest Feature Importance

All visualization outputs are stored in the `visualizations/` directory.

---

## 11. Machine Learning Models

Three classification algorithms were developed and evaluated:

### Logistic Regression

Logistic Regression was used as a baseline and interpretable classification model for predicting customer churn.

### Decision Tree

Decision Tree was implemented to capture non-linear relationships and decision rules within the customer data.

### Random Forest

Random Forest was implemented as an ensemble learning method and was also used for feature importance analysis.

---

## 12. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### Best Performing Model

Based on the project evaluation, Logistic Regression achieved the best overall ROC-AUC performance.

| Metric | Logistic Regression |
|---|---:|
| Accuracy | 80.20% |
| Precision | 64.35% |
| Recall | 56.95% |
| F1 Score | 60.43% |
| ROC-AUC | 84.87% |

The ROC-AUC score of 0.8487 indicates that the model demonstrates good ability to distinguish between customers who churn and customers who remain.

---

## 13. Feature Importance Analysis

Random Forest feature importance analysis identified the following important predictive features:

| Rank | Feature |
|---:|---|
| 1 | Total Charges |
| 2 | Tenure Months |
| 3 | Monthly Charges |
| 4 | Contract - Month-to-month |
| 5 | Contract - Two year |
| 6 | Online Security - No |
| 7 | Tech Support - No |
| 8 | Dependents - Yes |
| 9 | Payment Method - Electronic check |
| 10 | Dependents - No |
| 11 | Internet Service - Fiber optic |
| 12 | Online Backup - No |
| 13 | Gender - Male |
| 14 | Gender - Female |
| 15 | Partner - No |

These features indicate that customer tenure, billing characteristics, contract structure, subscribed services, and payment method are important factors associated with churn prediction.

Feature importance represents predictive contribution within the model and should not automatically be interpreted as causal relationships.

---

## 14. Key Business Insights

The analysis produced several important business insights:

### Customer Churn Rate

The overall churn rate is 26.54%, indicating that more than one-fourth of the customers in the dataset have churned.

### Contract Type

Contract-related variables, particularly month-to-month contracts, are important predictive factors.

### Customer Tenure

Tenure Months is one of the most important predictive features, indicating that customer lifecycle stage is strongly associated with churn prediction.

### Monthly Charges

Monthly Charges is among the most important numerical predictors and should be considered when analyzing customer retention.

### Service Features

Online Security, Tech Support, Online Backup, and Internet Service features contribute to the model's predictive capability.

### Payment Method

Electronic check appears among the important predictive features and represents a customer segment that may require further investigation.

---

## 15. Business Recommendations

Based on the analysis, the following recommendations are proposed:

### 1. Target High-Risk Customers

Use the churn prediction model to identify customers with higher churn probability and prioritize them for retention campaigns.

### 2. Encourage Long-Term Contracts

Develop incentives that encourage month-to-month customers to transition to longer-term contracts.

### 3. Improve New Customer Engagement

Strengthen onboarding, customer support, and engagement activities during the early customer lifecycle.

### 4. Review High Monthly Charges

Analyze customers with higher monthly charges to determine whether pricing or service-package structure contributes to churn.

### 5. Strengthen Technical Support and Security Services

Evaluate the relationship between Online Security and Tech Support services and customer retention.

### 6. Monitor Payment Method Segments

Investigate customers using electronic check payments and determine whether payment experience or related factors contribute to churn.

### 7. Implement Predictive Retention

Use the churn prediction model as a decision-support tool for prioritizing customer retention activities.

---

## 16. Limitations

The project has the following limitations:

- The analysis is based on historical customer data.
- The model cannot guarantee that a customer will actually churn.
- External factors such as competitor activity and economic conditions are not included.
- Customer preferences may change over time.
- Model performance depends on data quality and available features.
- Feature importance indicates predictive relationships rather than direct causation.
- Additional validation would be required before production deployment.

---

## 17. Future Scope

Future improvements can include:

- Deploying the churn prediction model as a web application.
- Developing an interactive customer churn dashboard.
- Integrating the model with CRM systems.
- Implementing automated high-risk customer alerts.
- Testing advanced algorithms such as XGBoost and Gradient Boosting.
- Performing customer segmentation.
- Incorporating customer feedback and support-ticket data.
- Including customer satisfaction and service usage data.
- Periodically retraining the model using new customer data.
- Developing personalized retention recommendations.

---

## 18. Project Structure

```text
Task-06-Final-Data-Science-Capstone/
│
├── data/
│   └── raw/
│       └── Telco_customer_churn.xlsx
│
├── notebook/
│   └── Final_Data_Science_Capstone.ipynb
│
├── src/
│
├── visualizations/
│   ├── 01_churn_distribution.png
│   ├── 02_churn_percentage.png
│   ├── 03_gender_vs_churn.png
│   ├── 04_contract_vs_churn.png
│   ├── 05_internet_service_vs_churn.png
│   ├── 06_payment_method_vs_churn.png
│   ├── 07_tenure_vs_churn.png
│   ├── 08_monthly_charges_vs_churn.png
│   ├── 09_senior_citizen_vs_churn.png
│   ├── 10_correlation_heatmap.png
│   ├── 11_model_performance_comparison.png
│   ├── 12_confusion_matrix.png
│   ├── 13_roc_curve_comparison.png
│   └── 14_feature_importance.png
│
├── reports/
│   ├── model_performance.csv
│   ├── classification_report.txt
│   └── final_project_summary.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 19. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project

```bash
cd Task-06-Final-Data-Science-Capstone
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

### Step 5: Open the Notebook

Open:

```text
notebook/Final_Data_Science_Capstone.ipynb
```

### Step 6: Run the Notebook

Run all cells sequentially from the beginning to reproduce the analysis.

---

## 20. Requirements

The main Python dependencies are:

```text
pandas
numpy
openpyxl
matplotlib
seaborn
scikit-learn
jupyter
```

---

## 21. Output Files

The project generates:

- Exploratory data analysis visualizations.
- Model comparison results.
- Classification report.
- Confusion matrix.
- ROC curve.
- Feature importance analysis.
- Final project summary.

These outputs are stored in the `visualizations/` and `reports/` directories.

---

## 22. Conclusion

This project demonstrates an end-to-end application of Data Science and Machine Learning to a real-world customer churn problem.

Through data analysis, visualization, predictive modeling, and business interpretation, the project identifies important factors associated with customer churn and provides practical recommendations for improving customer retention.

The Logistic Regression model achieved an accuracy of 80.20% and a ROC-AUC score of 84.87%, demonstrating strong predictive discrimination for the analyzed dataset.

The project provides a foundation for developing a production-level customer churn prediction and retention decision-support system.

---

## 23. Author

**Yash Vikram Jadhav**

B.Sc. Artificial Intelligence

Data Science and Machine Learning Project