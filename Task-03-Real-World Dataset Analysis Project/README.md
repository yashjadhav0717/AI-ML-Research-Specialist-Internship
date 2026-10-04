# Task 3 – Real-World Dataset Analysis Project

## Project Overview

This project focuses on the analysis of a real-world retail dataset using Python and widely adopted data analysis and visualization libraries. The primary objective is to understand the dataset, perform data cleaning and preprocessing, conduct exploratory data analysis (EDA), identify meaningful patterns and relationships, and communicate business-oriented insights through visualizations and a structured analysis report.

The **Global Superstore** dataset was selected because it contains realistic transactional information related to customers, products, sales, profit, discounts, regions, categories, shipping, and order dates. The dataset provides a suitable foundation for demonstrating an end-to-end data analysis workflow.

---

## Objectives

The primary objectives of this project are:

1. Select and understand a real-world dataset from a reliable source.
2. Examine the dataset structure, variables, data types, and distributions.
3. Identify and handle missing values and duplicate records.
4. Convert and preprocess date-related fields.
5. Perform exploratory data analysis using Pandas and NumPy.
6. Analyze sales, profit, customers, products, categories, regions, and segments.
7. Identify trends, patterns, correlations, and potential outliers.
8. Create meaningful and interpretable data visualizations.
9. Generate actionable business insights and recommendations.
10. Document the complete analysis in a Jupyter Notebook and a structured report.

---

## Dataset

**Dataset:** Global Superstore  
**Source:** Kaggle  
**Primary Worksheet:** Orders

The dataset contains retail transaction-level information, including:

- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Customer Name
- Segment
- Country
- City
- State
- Region
- Product ID
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

The analysis primarily focuses on the `Orders` worksheet.

---

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Data analysis and programming |
| Pandas | Data loading, cleaning, transformation, and analysis |
| NumPy | Numerical and statistical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Interactive data analysis |
| Git | Version control |
| GitHub | Source code and project repository management |

---

## Project Workflow

### 1. Data Loading

The Global Superstore Excel dataset was loaded using Pandas. The required `Orders` worksheet was selected as the primary source for analysis.

### 2. Data Understanding

The dataset was examined to understand its structure and contents. The following activities were performed:

- Dataset dimensions
- Column names
- Data types
- First and last records
- Random sample records
- Descriptive statistics
- Categorical variable summaries
- Unique value analysis

### 3. Data Cleaning and Preprocessing

The dataset was evaluated for common data quality issues, including:

- Missing values
- Duplicate records
- Incorrect data types
- Date inconsistencies
- Potential outliers

Duplicate records were identified and removed where required.

The `Order Date` and `Ship Date` columns were converted to appropriate datetime formats.

Additional analytical features were created, including:

- Year
- Month
- Month Name
- Quarter
- Shipping Days

---

## Exploratory Data Analysis

The project performs exploratory analysis across multiple business dimensions.

### Sales Analysis

The following sales-related analyses were performed:

- Sales by category
- Sales by region
- Monthly sales trends
- Top products by sales
- Sales distribution

### Profit Analysis

Profitability was analyzed using:

- Profit by category
- Profit by region
- Profit by product
- Profit distribution
- Loss-making products
- Overall profit margin

### Customer Analysis

Customer-level analysis includes:

- Customer sales performance
- Customer profitability
- Top customers
- Customer contribution to overall sales

### Segment Analysis

The performance of different customer segments was evaluated based on sales and profitability.

### Discount Analysis

The relationship between discount levels and profitability was investigated using statistical analysis and scatter plots.

### Correlation Analysis

A correlation matrix and heatmap were created to examine relationships between key numerical variables, including:

- Sales
- Quantity
- Discount
- Profit

---

## Data Visualizations

Multiple visualization techniques were used to communicate analytical findings effectively.

The project includes:

- Bar charts
- Line charts
- Scatter plots
- Histograms
- Box plots
- Correlation heatmaps

The generated visualizations include:

- Sales by Category
- Profit by Category
- Sales by Region
- Monthly Sales Trend
- Top 10 Products
- Discount vs Profit
- Sales vs Profit
- Correlation Heatmap
- Sales Distribution
- Profit Distribution

---

## Key Dataset Statistics

After data preprocessing and duplicate removal, the analyzed dataset contained:

| Metric | Value |
|---|---:|
| Records | 51,290 |
| Columns | 28 |
| Total Sales | 12,642,501.91 |
| Total Profit | 1,467,457.29 |
| Overall Profit Margin | 11.61% |

These metrics were calculated directly from the analyzed Global Superstore dataset.

---

## Key Insights

The analysis provides insights into the following areas:

- Overall sales and profitability performance
- Category-level sales and profit contribution
- Regional sales and profitability differences
- Monthly sales trends and seasonality
- High-performing products and customers
- Loss-making products requiring further investigation
- Relationship between discounts and profitability
- Customer segment performance
- Distribution of key numerical variables
- Potential outliers affecting business metrics

The analysis also demonstrates that high sales volume does not necessarily result in high profitability. Therefore, evaluating both revenue and profit is important for effective business decision-making.

---

## Project Structure

```text
Task-03-Real-World Dataset Analysis Project/
│
├── dataset/
│   └── Global Superstore.xls
│
├── output/
│   ├── cleaned_global_superstore.csv
│   ├── descriptive_statistics.csv
│   ├── missing_value_analysis.csv
│   ├── correlation_matrix.csv
│   ├── category_analysis.csv
│   ├── regional_analysis.csv
│   ├── product_analysis.csv
│   ├── customer_analysis.csv
│   ├── segment_analysis.csv
│   ├── monthly_sales_analysis.csv
│   │
│   └── visualizations/
│       ├── sales_by_category.png
│       ├── profit_by_category.png
│       ├── sales_by_region.png
│       ├── monthly_sales_trend.png
│       ├── top_10_products.png
│       ├── discount_vs_profit.png
│       ├── sales_vs_profit.png
│       ├── correlation_heatmap.png
│       ├── sales_distribution.png
│       └── profit_distribution.png
│
├── Task-03-Real-World-Dataset-Analysis.ipynb
├── Real_World_Dataset_Analysis_Report.docx
└── README.md
```

---

## Installation and Setup

### Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Navigate to the Project Directory

```bash
cd AI-ML-Research-Specialist-Internship
```

### Install Required Dependencies

```bash
pip install pandas numpy matplotlib seaborn openpyxl xlrd jupyter
```

### Start Jupyter Notebook

```bash
jupyter notebook
```

### Open the Task 3 Directory

Navigate to:

```text
Task-03-Real-World Dataset Analysis Project/
```

Open the following notebook:

```text
Task-03-Real-World-Dataset-Analysis.ipynb
```

Run the notebook cells sequentially to reproduce the analysis.

---

## Output

The project generates structured analytical outputs in the `output/` directory.

These outputs include:

- Cleaned dataset
- Descriptive statistics
- Missing-value analysis
- Correlation matrix
- Category analysis
- Regional analysis
- Product analysis
- Customer analysis
- Segment analysis
- Monthly sales analysis
- Data visualization files

A detailed Word report is also included to document the methodology, data preparation, exploratory analysis, findings, interpretations, recommendations, and conclusion.

---

## Conclusion

This project demonstrates an end-to-end real-world data analysis workflow using Python. The Global Superstore dataset was systematically explored, cleaned, transformed, and analyzed to identify meaningful business patterns and relationships.

The project demonstrates practical skills in:

- Data preprocessing
- Exploratory data analysis
- Statistical analysis
- Data visualization
- Business intelligence
- Data interpretation
- Report preparation
- Version control using Git and GitHub

The resulting analysis provides a structured view of sales and profitability performance and can support data-driven decisions related to products, customers, regions, discounts, and sales strategies.

---

## Author

**Yash Vikram Jadhav**

B.Sc. Artificial Intelligence  
Yashwantrao Chavan Institute of Science, Satara

### Skills Demonstrated

Python, Pandas, NumPy, Matplotlib, Seaborn, Data Analysis, Exploratory Data Analysis, Data Visualization, Statistical Analysis, Business Analysis, Git, and GitHub.