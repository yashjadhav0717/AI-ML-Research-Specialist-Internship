
```markdow# Task 02 — Hands-On Data Lab Implementation

## Overview

This project is part of the **AI-ML Research Specialist Internship** and focuses on implementing fundamental Data Science concepts through a practical Jupyter Notebook.

The objective of this task is to build a working Data Science environment and perform a complete exploratory data analysis workflow using Python and commonly used Data Science libraries.

The project covers data preparation, data manipulation, data cleaning, numerical analysis, visualization, correlation analysis, and basic feature preprocessing.

---

## Objectives

The main objectives of this practical Data Lab are:

1. Set up and verify a Python-based Data Science environment.
2. Work with datasets using Pandas and NumPy.
3. Perform data selection, filtering, sorting, grouping, aggregation, and transformation.
4. Identify and handle missing values and duplicate records.
5. Perform basic data-quality checks.
6. Create meaningful data visualizations.
7. Calculate descriptive statistics.
8. Analyze relationships and correlations between variables.
9. Apply basic feature standardization using Scikit-learn.
10. Document observations, findings, and conclusions in a structured Jupyter Notebook.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Jupyter Notebook | Interactive Data Science environment |
| NumPy | Numerical computation |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Data preprocessing |
| Git & GitHub | Version control and project management |

---

## Project Structure

```text
Task-02-Hands-On-Data-Lab/
│
├── notebook/
│   └── Hands_On_Data_Lab_Implementation.ipynb
│
├── output/
│   ├── bar_chart.png
│   ├── line_chart.png
│   ├── histogram.png
│   ├── scatter_plot.png
│   ├── box_plot.png
│   └── correlation_heatmap.png
│
├── report/
│   └── Task-02-Hands-On-Data-Lab-Report.docx
│
└── README.md
```

---

## Dataset

For this practical exercise, a sample **Student Performance Dataset** was created using Pandas.

The dataset contains information about:

- Student ID
- Student Name
- Age
- Gender
- Department
- Study Hours
- Attendance
- Mathematics Score
- Python Score

An additional `Average_Score` and `Grade` column was created during the analysis.

---

## Data Analysis Operations

### Pandas Operations

The following Pandas operations were implemented:

- DataFrame creation
- Dataset inspection
- Column selection
- Multiple-column selection
- Row selection using `iloc`
- Row and column selection using `loc`
- Data filtering
- Data sorting
- Grouping
- Aggregation
- Column transformation
- Creating derived columns

### NumPy Operations

NumPy was used for:

- Mean calculation
- Maximum value
- Minimum value
- Standard deviation
- Array operations
- Total score calculation
- Average score calculation

---

## Data Cleaning

The project demonstrates practical data-cleaning techniques.

### Missing Values

Missing values were intentionally introduced into the dataset to demonstrate the cleaning process.

The following techniques were applied:

- Missing-value detection
- Missing-value counting
- Median imputation for numerical columns

### Duplicate Records

A duplicate record was intentionally introduced and then:

1. Identified using `duplicated()`
2. Counted
3. Removed using `drop_duplicates()`

### Data Quality Verification

The final dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Dataset shape

The final cleaned dataset contains:

```text
Missing Values: 0
Duplicate Records: 0
```

---

## Data Visualizations

The project includes six different visualizations.

### 1. Bar Chart

**File:** `bar_chart.png`

The bar chart compares the average student performance across different departments.

### 2. Line Chart

**File:** `line_chart.png`

The line chart represents student average scores across student IDs.

### 3. Histogram

**File:** `histogram.png`

The histogram shows the distribution of student average scores.

### 4. Scatter Plot

**File:** `scatter_plot.png`

The scatter plot analyzes the relationship between study hours and average academic performance.

### 5. Box Plot

**File:** `box_plot.png`

The box plot compares the distribution of average scores across departments.

### 6. Correlation Heatmap

**File:** `correlation_heatmap.png`

The correlation heatmap shows the relationships between:

- Study Hours
- Attendance
- Mathematics Score
- Python Score
- Average Score

---

## Statistical Analysis

Descriptive statistics were calculated using Pandas.

The analysis includes:

- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- Quartiles

The analysis was used to understand the distribution and general characteristics of the dataset.

---

## Correlation Analysis

A correlation matrix was generated to analyze relationships between numerical variables.

The analysis helps understand how variables such as:

- Study Hours
- Attendance
- Mathematics Score
- Python Score
- Average Score

are related to each other.

Correlation analysis provides an initial understanding of relationships in the dataset but does not establish causation.

---

## Feature Standardization

Scikit-learn's `StandardScaler` was used to demonstrate feature standardization.

The following features were standardized:

- Study Hours
- Attendance
- Mathematics Score
- Python Score

This demonstrates a basic preprocessing technique commonly used before applying Machine Learning algorithms.

---

## Key Insights

The practical analysis produced the following general observations:

- Students with higher study hours generally tend to achieve better academic scores.
- Higher attendance is generally associated with stronger academic performance.
- Mathematics and Python scores contribute to the calculated average score.
- Department-level grouping helps compare academic performance across departments.
- Correlation analysis helps identify relationships between academic variables.
- Data cleaning improves the quality and reliability of the dataset before analysis.
- Visualization makes patterns and distributions easier to interpret.

These observations are exploratory and should not be interpreted as causal relationships.

---

## Output Files

All generated visualizations are automatically saved in the project's `output` directory.

```text
output/
│
├── bar_chart.png
├── line_chart.png
├── histogram.png
├── scatter_plot.png
├── box_plot.png
└── correlation_heatmap.png
```

The notebook uses an absolute Windows output path during execution to save these visualization files.

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project

```bash
cd AI-ML-Research-Specialist-Internship
cd Task-02-Hands-On-Data-Lab
```

### 3. Install Dependencies

```bash
pip install -r ../../requirements.txt
```

Or install the required libraries directly:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Notebook

Navigate to:

```text
notebook/Hands_On_Data_Lab_Implementation.ipynb
```

### 6. Execute the Notebook

Run all cells sequentially using:

```text
Kernel → Restart Kernel and Run All Cells
```

After successful execution, the generated visualizations will be available in the `output` directory.

---

## Reproducibility

The notebook follows a structured and reproducible workflow:

```text
Environment Setup
        ↓
Dataset Creation
        ↓
Data Inspection
        ↓
Pandas & NumPy Operations
        ↓
Data Cleaning
        ↓
Descriptive Statistics
        ↓
Data Visualization
        ↓
Correlation Analysis
        ↓
Feature Standardization
        ↓
Final Insights
```

---

## Learning Outcomes

After completing this task, the following practical skills were demonstrated:

- Python Data Science environment setup
- NumPy numerical computation
- Pandas DataFrame manipulation
- Data filtering and sorting
- GroupBy and aggregation
- Data cleaning
- Missing-value handling
- Duplicate detection and removal
- Exploratory Data Analysis
- Statistical analysis
- Data visualization
- Correlation analysis
- Feature standardization
- Jupyter Notebook documentation

---

## Conclusion

The **Hands-On Data Lab** successfully demonstrates a complete basic Data Science workflow using Python.

The project combines data manipulation, cleaning, statistical analysis, visualization, correlation analysis, and preprocessing into a single structured Jupyter Notebook.

This practical implementation provides a strong foundation for further work in **Exploratory Data Analysis, Machine Learning, and Artificial Intelligence**.

---

## Author

**Yash Vikram Jadhav**

B.Sc. Artificial Intelligence  
Yashwantrao Chavan Institute of Science (YCIS), Satara

---

## Internship Task

**Program:** AI-ML Research Specialist Internship  
**Task:** Task 02 — Hands-On Data Lab Implementation
```