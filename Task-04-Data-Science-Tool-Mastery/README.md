# Task 04 - Data Science Tool Mastery Project

## 📌 Project Overview

This project demonstrates practical proficiency in industry-standard data science tools and Python libraries through an end-to-end analysis of the Titanic dataset.

The project covers the complete data science workflow, starting from dataset loading and exploration to data cleaning, visualization, feature engineering, machine learning, model evaluation, and prediction on unseen test data.

The primary objective is to gain hands-on experience with essential data science tools and create a portfolio-ready implementation.

---

## 🎯 Objectives

The main objectives of this project are:

1. Master industry-standard data science tools and libraries.
2. Demonstrate practical data analysis and manipulation skills.
3. Perform exploratory data analysis on a real-world dataset.
4. Handle missing values and improve data quality.
5. Create meaningful data visualizations.
6. Apply feature engineering and preprocessing techniques.
7. Build and evaluate a machine learning classification model.
8. Generate predictions on unseen test data.
9. Export analytical results and processed datasets.
10. Create a reusable and portfolio-ready data science project.

---

## 📊 Dataset

The project uses the Titanic passenger dataset.

### Training Dataset

- File: `titanic.csv`
- Records: 891
- Features: 12
- Target Variable: `Survived`

### Test Dataset

- File: `test.csv`
- Records: 418
- Features: 11
- Target variable: Not provided

The training dataset contains the `Survived` target variable, while the test dataset is used for generating predictions from the trained machine learning model.

---

## 🛠️ Technologies and Tools

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical and statistical computation |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| Jupyter Notebook | Interactive development and documentation |
| Git | Version control |
| GitHub | Project hosting and portfolio |

---

## 🔄 Project Workflow

The project follows a complete data science workflow:

```text
Dataset Loading
      ↓
Dataset Exploration
      ↓
Data Quality Analysis
      ↓
Missing Value Analysis
      ↓
Duplicate Analysis
      ↓
NumPy Numerical Analysis
      ↓
Pandas Data Analysis
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Data Visualization
      ↓
Feature Engineering
      ↓
Feature Encoding
      ↓
Train-Validation Split
      ↓
Machine Learning
      ↓
Model Evaluation
      ↓
Final Model Training
      ↓
Test Dataset Prediction
      ↓
Result Export
```

---

## 🔍 Exploratory Data Analysis

The following areas were analyzed:

- Dataset dimensions
- Data types
- Statistical summary
- Missing values
- Duplicate records
- Passenger gender distribution
- Passenger class distribution
- Age distribution
- Fare distribution
- Survival distribution
- Survival rate by gender
- Survival rate by passenger class
- Survival rate by age group
- Numerical feature correlations

---

## 🧹 Data Cleaning

The following preprocessing operations were performed:

- Missing `Age` values were handled using the median.
- Missing `Fare` values were handled using the median.
- Missing `Embarked` values were handled using the mode.
- Duplicate records were checked.
- Unnecessary columns were excluded from the machine learning feature set.
- Categorical variables were converted into numerical features.

The cleaned datasets were exported to the `output/processed_data` directory.

---

## 📈 Data Visualization

Multiple visualizations were created using Matplotlib and Seaborn.

### Generated Visualizations

- Age Distribution
- Fare Distribution
- Survival Distribution
- Survival by Gender
- Survival by Passenger Class
- Survival Rate by Gender
- Survival Rate by Passenger Class
- Survival Rate by Age Group
- Correlation Heatmap
- Confusion Matrix

All generated figures are stored in:

```text
output/figures/
```

---

## 🤖 Machine Learning

### Model Used

**Logistic Regression**

Logistic Regression was selected because the project focuses on binary classification where the target variable represents whether a passenger survived or did not survive.

### Features Used

```text
Pclass
Sex
Age
SibSp
Parch
Fare
Embarked
```

### Target Variable

```text
Survived
```

Where:

```text
0 = Did Not Survive
1 = Survived
```

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

The model was first evaluated using an 80/20 train-validation split.

After evaluation, a final Logistic Regression model was trained using the complete labelled training dataset.

---

## 🔮 Test Dataset Prediction

After training the final model, predictions were generated for the 418 records present in `test.csv`.

The prediction file contains:

```text
PassengerId
Survived
```

The generated file is:

```text
output/processed_data/predictions.csv
```

---

## 📁 Project Structure

```text
Task-04-Data-Science-Tool-Mastery/
│
├── dataset/
│   ├── titanic.csv
│   └── test.csv
│
├── notebook/
│   └── Data_Science_Tool_Mastery.ipynb
│
├── output/
│   │
│   ├── figures/
│   │   ├── age_distribution.png
│   │   ├── correlation_heatmap.png
│   │   ├── fare_distribution.png
│   │   ├── survival_by_age_group.png
│   │   ├── survival_by_class.png
│   │   ├── survival_by_gender.png
│   │   ├── survival_distribution.png
│   │   ├── survival_rate_by_class.png
│   │   ├── survival_rate_by_gender.png
│   │   └── confusion_matrix.png
│   │
│   ├── results/
│   │   ├── statistical_summary.csv
│   │   ├── missing_values.csv
│   │   ├── survival_rate_by_gender.csv
│   │   ├── survival_rate_by_class.csv
│   │   ├── survival_rate_by_age_group.csv
│   │   ├── correlation_matrix.csv
│   │   ├── classification_report.txt
│   │   ├── model_results.csv
│   │   ├── feature_coefficients.csv
│   │   └── key_findings.csv
│   │
│   └── processed_data/
│       ├── titanic_cleaned.csv
│       ├── test_cleaned.csv
│       └── predictions.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📤 Output Files

### Figures

All visualization files are stored in:

```text
output/figures/
```

### Analysis Results

Statistical and machine learning results are stored in:

```text
output/results/
```

### Processed Data

Cleaned datasets and final predictions are stored in:

```text
output/processed_data/
```

---

## 💡 Key Insights

The analysis demonstrates several important patterns in the Titanic dataset:

- Passenger gender had a significant relationship with survival.
- Passenger class was an important factor associated with survival.
- Survival rates varied across different passenger classes.
- Passenger age showed considerable variation across the dataset.
- Passenger fares showed significant variation.
- Data visualization helped identify relationships between passenger characteristics and survival outcomes.
- Logistic Regression successfully learned patterns from the selected features.
- The final model was used to generate predictions for the separate 418-record test dataset.

---

## 📚 Skills Demonstrated

### Python

- Python programming
- File handling
- Data processing
- Structured workflow development

### NumPy

- Array operations
- Statistical calculations
- Numerical analysis

### Pandas

- Data loading
- Data inspection
- Data cleaning
- Filtering
- GroupBy operations
- Feature creation
- Data export

### Data Visualization

- Matplotlib
- Seaborn
- Histograms
- Bar charts
- Statistical plots
- Correlation heatmaps

### Machine Learning

- Feature selection
- Categorical encoding
- Train-validation splitting
- Logistic Regression
- Model prediction
- Model evaluation
- Classification metrics
- Confusion matrix

### Git & GitHub

- Version control
- Project organization
- Repository management
- Portfolio development

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd Task-04-Data-Science-Tool-Mastery
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Notebook

Open:

```text
notebook/Data_Science_Tool_Mastery.ipynb
```

### 6. Run All Cells

Execute the notebook from top to bottom.

The notebook will automatically generate:

- Data analysis results
- Visualizations
- Machine learning evaluation
- Processed datasets
- Final test predictions

---

## 📦 Requirements

The project requires the following Python packages:

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
openpyxl
```

These dependencies are also listed in:

```text
requirements.txt
```

---

## 📝 Conclusion

This project demonstrates a complete practical implementation of a data science workflow using Python and industry-standard libraries. It combines numerical computing, data manipulation, visualization, statistical analysis, machine learning, model evaluation, and prediction into a single structured project.

The project provides practical evidence of proficiency with the Python data science ecosystem and can be used as a portfolio project to demonstrate applied data science skills.

---

## 👨‍💻 Author

**Yash Vikram Jadhav**

B.Sc. Artificial Intelligence Student

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Data Science
- Python Development
- Generative AI
- Data Analytics

---

## 📌 Project Status

**Status:** Completed ✅

**Task:** Task 04 - Data Science Tool Mastery

**Project Type:** Data Science / Machine Learning

**Model:** Logistic Regression
