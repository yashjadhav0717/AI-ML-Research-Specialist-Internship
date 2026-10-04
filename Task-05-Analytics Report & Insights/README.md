# Task 05 - Analytics Report and Insights Documentation

## Project Overview

This project develops professional data analysis and reporting skills using the Global Superstore dataset. The analysis converts transactional business data into key performance indicators, analytical findings, business insights, and actionable recommendations.

The project follows a complete business analytics workflow:

Data Validation -> KPI Analysis -> Trend Analysis -> Visualization -> Business Insights -> Recommendations

## Business Objectives

The analysis aims to:

- Evaluate overall sales and profit performance.
- Identify important sales and profitability trends.
- Compare product categories and regions.
- Analyze customer segment performance.
- Identify high-performing and low-performing products.
- Examine the relationship between discount, sales, and profit.
- Develop stakeholder-friendly business insights.
- Provide actionable recommendations for business improvement.

## Dataset

The analysis uses the cleaned Global Superstore transactional dataset.

Dataset characteristics used in the analysis:

- Records: 51,290
- Variables: 29
- Major business fields include Sales, Profit, Quantity, Discount, Category, Region, Segment, Product, Customer, Order Date, and Shipping information.

## Key Performance Indicators

The analysis evaluates:

- Total Sales
- Total Profit
- Total Quantity
- Average Sales
- Average Profit
- Average Discount
- Profit Margin
- Total Customers
- Total Orders
- Average Shipping Days

## Analysis Performed

### 1. Data Quality Assessment

The dataset was reviewed for missing values, duplicate records, data types, and date consistency.

### 2. Category Analysis

Sales, profit, quantity, discount, and profit margin were compared across product categories.

### 3. Regional Analysis

Regional sales, profit, quantity, discount, and profit margin were analyzed to identify geographic performance differences.

### 4. Customer Segment Analysis

Customer segments were compared based on sales, profit, quantity, and discount.

### 5. Product Analysis

Products were ranked according to sales and profit to identify high-performing and low-performing products.

### 6. Monthly Sales Analysis

Monthly sales trends were analyzed to identify changes in business performance over time.

### 7. Correlation Analysis

Relationships between Sales, Profit, Quantity, and Discount were examined.

### 8. Business Insights

Analytical findings were interpreted from a business perspective to identify performance drivers and areas requiring attention.

## Visualizations

The notebook generates visualizations including:

- Sales by Category
- Sales by Region
- Sales by Customer Segment
- Top 10 Products by Sales
- Monthly Sales Trend
- Discount vs Profit
- Sales vs Profit
- Correlation Heatmap
- Sales Distribution
- Profit Distribution

## Key Business Insights

The analysis identifies Technology as the strongest major product category by sales, Consumer as the strongest customer segment by sales, and Central as the strongest region by sales in the analyzed results.

The analysis also identifies a negative relationship between Discount and Profit and a positive relationship between Sales and Profit. These relationships provide useful evidence for evaluating discount policies and revenue-growth strategies.

## Recommendations

1. Optimize discount strategies to protect profitability.
2. Continue supporting high-performing categories.
3. Strengthen inventory and promotional activity for high-performing products.
4. Investigate products with weak or negative profitability.
5. Improve performance in underperforming regions.
6. Establish continuous KPI monitoring through a business dashboard.

## Project Structure

```text
Task-05-Analytics Report & Insights/
|
|-- dataset/
|   |-- cleaned_global_superstore.csv
|
|-- notebook/
|   |-- Task_05_Analytics_Report.ipynb
|
|-- visualizations/
|   |-- Generated analytical charts
|
|-- report/
|   |-- Analytics_Report_and_Insights.docx
|
|-- README.md
```

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Microsoft Word
- Git and GitHub

## Expected Outcome

The project demonstrates the ability to move from raw transactional data to professional business reporting. It combines quantitative analysis, visualization, interpretation, executive communication, and actionable recommendations to support data-driven decision-making.

## Author

Yash Vikram Jadhav
