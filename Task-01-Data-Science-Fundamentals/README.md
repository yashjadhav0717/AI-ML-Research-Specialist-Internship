# Task 01 — Data Science Fundamentals

## Overview

This task focuses on building a strong foundation in Data Science through Python programming, statistics, data analysis, data types, data manipulation, and basic exploratory data analysis.

The assessment demonstrates the process of working with data, from understanding the problem and preparing data to performing statistical analysis, visualization, and interpreting results.

---

## Objectives

The main objectives of this task are:

1. Understand the Data Science lifecycle and different types of data analysis.
2. Apply Python programming fundamentals required for data analysis.
3. Understand statistical concepts such as mean, median, mode, variance, standard deviation, percentiles, probability, and correlation.
4. Identify and work with different data types and data structures.
5. Perform basic data cleaning, manipulation, and exploratory data analysis.
6. Follow Data Science best practices including clean code, meaningful variable names, documentation, and reproducible analysis.
7. Complete practical assignments and document the results in a structured Jupyter Notebook.

---

## Project Structure

```text
Task-01-Data-Science-Fundamentals/
│
├── README.md
│
├── notebook/
│   └── Data_Science_Fundamentals_Assessment.ipynb
│
├── report/
│   └── Data_Science_Fundamentals_Report.pdf
│
└── outputs/
    ├── marks_distribution.png
    ├── study_hours_vs_marks.png
    └── analysis_summary.csv
```

---

## Topics Covered

### 1. Data Science Fundamentals

* What is Data Science?
* Data Science lifecycle
* Data collection
* Data cleaning
* Exploratory Data Analysis
* Feature engineering
* Model building
* Model evaluation
* Deployment
* Monitoring

### 2. Types of Data Analysis

| Analysis Type         | Purpose                    |
| --------------------- | -------------------------- |
| Descriptive Analysis  | Understand what happened   |
| Diagnostic Analysis   | Understand why it happened |
| Predictive Analysis   | Predict what may happen    |
| Prescriptive Analysis | Determine possible actions |

### 3. Python Programming

The notebook covers:

* Variables
* Data types
* Operators
* Conditional statements
* For loops
* While loops
* Functions
* Lists
* Tuples
* Dictionaries
* Sets
* File handling

### 4. Statistical Foundations

The following concepts are implemented:

* Mean
* Median
* Mode
* Variance
* Standard deviation
* Percentiles
* Probability
* Correlation

### 5. Data Types

The assessment works with:

* Numerical data
* Categorical data
* Ordinal data
* Datetime data
* Text data

### 6. Data Analysis

The project demonstrates:

* Dataset creation
* Dataset inspection
* Missing-value detection
* Data filtering
* Sorting
* Grouping
* Statistical summaries
* Correlation analysis
* Performance categorization

### 7. Data Visualization

Basic visualizations include:

* Marks distribution
* Study hours vs. marks
* Statistical analysis charts

---

## Technologies and Libraries

### Programming Language

* Python 3.x

### Libraries

* NumPy
* Pandas
* Matplotlib
* Statistics

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## Dataset

A sample student dataset is used to demonstrate fundamental Data Science concepts.

The dataset contains fields such as:

| Column      | Description               | Data Type   |
| ----------- | ------------------------- | ----------- |
| Student_ID  | Unique student identifier | Numerical   |
| Name        | Student name              | Text        |
| Age         | Student age               | Numerical   |
| Study_Hours | Daily study hours         | Numerical   |
| Marks       | Student marks             | Numerical   |
| City        | Student city              | Categorical |

The dataset is used to perform statistical analysis and investigate relationships between variables.

---

## Analysis Performed

### Statistical Analysis

The following statistics are calculated for student marks:

* Mean
* Median
* Mode
* Variance
* Standard deviation
* Percentiles

### Correlation Analysis

The relationship between:

```text
Study Hours → Marks
```

is analyzed using Pearson correlation.

The analysis helps identify whether study hours and marks have a positive or negative linear relationship in the sample dataset.

Correlation indicates association and does not by itself establish causation.

---

## Outputs

The `outputs/` directory contains generated analysis results such as:

* Marks distribution visualization
* Study hours vs. marks scatter plot
* Analysis summary CSV

These outputs provide a visual and structured representation of the analysis performed in the notebook.

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Task

```bash
cd Task-01-Data-Science-Fundamentals
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib jupyter
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Notebook

Navigate to:

```text
notebook/
└── Data_Science_Fundamentals_Assessment.ipynb
```

Run the notebook cells sequentially to reproduce the analysis.

---

## Key Findings

Based on the sample analysis:

* Descriptive statistics provide a summary of student performance.
* The dataset can be grouped and analyzed by city.
* Students can be categorized based on their marks.
* Study hours and marks can be analyzed using correlation.
* Data visualization helps identify patterns that may not be immediately visible from raw data.
* Proper data handling and documentation improve the reliability and reproducibility of analysis.

---

## Data Science Best Practices

The following best practices are followed:

* Meaningful variable names
* Modular Python functions
* Clear notebook structure
* Markdown documentation
* Proper data type handling
* Missing-value checking
* Reproducible analysis
* Clear visualization labels
* Separation of code and generated outputs
* Avoiding unsupported conclusions from statistical results

---

## Learning Outcomes

After completing this task, the following foundational skills were demonstrated:

* Understanding the Data Science workflow
* Writing basic Python programs
* Working with NumPy and Pandas
* Performing descriptive statistical analysis
* Understanding different data types
* Manipulating datasets
* Performing basic Exploratory Data Analysis
* Creating basic visualizations
* Calculating correlation
* Interpreting analytical results responsibly

---

## Deliverables

| Deliverable           | Location    |
| --------------------- | ----------- |
| Main Jupyter Notebook | `notebook/` |
| Final Report          | `report/`   |
| Analysis Outputs      | `outputs/`  |
| Project Documentation | `README.md` |

---

## Author

**Yash Vikram Jadhav**

B.Sc. Artificial Intelligence Student

---

## Conclusion

This assessment provides a practical introduction to the fundamentals of Data Science. It combines Python programming, statistics, data structures, data manipulation, exploratory analysis, visualization, and responsible interpretation of analytical results.

The completed notebook demonstrates the ability to work with a structured dataset, analyze it using Python, generate meaningful insights, and document the analytical workflow in a reproducible manner.
