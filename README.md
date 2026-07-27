# Sales Analytics Dashboard

An interactive sales analytics dashboard built with **Python, Pandas, Plotly, and Dash** to analyse sales performance, profitability, product performance, regional trends, and the relationship between discounts and profit. this has helped me solidify what I have learnt from my DataCamp courses

It was really an insightful experience and I'm super excited for more works to come
It's by no means perfect and can be better yet It is functional.

## Project Overview

The goal of this project was to transform raw sales data into an interactive dashboard that helps answer key business questions:

* Which regions generate the most sales and profit?
* Which product categories perform best?
* Which products generate the most sales and profit?
* Which customer segments contribute the most revenue?
* Which sub-categories are most and least profitable?
* How does discounting affect profitability?
* How do sales change over time?

## Dashboard Features

The dashboard includes:

* Total Sales KPI
* Total Profit KPI
* Total Orders KPI
* Total Customers KPI
* Monthly Sales Trend
* Sales by Region
* Profit by Region
* Sales by Category
* Profit by Category
* Top 10 Products by Sales
* Top 10 Products by Profit
* Sales by Customer Segment
* Profit by Customer Segment
* Sales by Sub-Category
* Profit by Sub-Category
* Discount vs Profit Analysis
* Interactive Region Filter

Changing the region filter dynamically updates the KPIs and visualisations.

## Key Insights

### Regional Performance

The **West region** generated the highest sales in the dataset.

### Category Performance

**Technology** was the strongest-performing category, generating more than **$840K in sales** and also producing the highest profit among the three categories.

### Discount and Profitability

Higher discount levels were generally associated with lower total profit, suggesting that aggressive discounting may negatively affect profitability.

### Furniture Performance

Furniture generated the lowest profit among the three major categories, making it an area worth investigating further for pricing, discounting, and cost optimisation.

### Product Performance

The top-performing products showed that a relatively small number of products contribute significantly to overall sales and profit.

## Technologies Used

* **Python**
* **Pandas** — data manipulation and analysis
* **Plotly Express** — interactive visualisations
* **Dash** — interactive web dashboard
* **Git & GitHub** — version control and project management

## Project Structure

```text
sales-analytics-dashboard/
│
├── assets/
│
├── data/
│   └── raw/
│       └── Sample - Superstore.csv
│
├── notebooks/
│
├── src/
│   ├── data_loader.py
│   ├── business_analysis.py
│   ├── plotly_visualization.py
│   └── dashboard.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/GhostCypher05/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
python src/dashboard.py
```

The Dash application will provide a local address in the terminal. Open that address in your browser to view the dashboard.

## What I Learned

This project strengthened my practical understanding of:

* Data cleaning and preparation with Pandas
* Exploratory data analysis
* Grouping and aggregating business data
* Building reusable Python functions
* Designing configuration-driven visualisations
* Creating interactive Plotly charts
* Building dashboards with Dash
* Implementing Dash callbacks and interactive filtering
* Separating data loading, business analysis, visualisation, and dashboard logic
* Translating analytical results into actionable business insights

## Future Improvements

Potential future improvements include:

* Adding date-range filtering
* Adding additional customer-level analysis
* Adding profit-margin analysis
* Adding downloadable reports
* Deploying the dashboard online
* Adding automated tests
* Improving dashboard responsiveness for mobile devices

## Project Status

**Completed — Portfolio Project 1**
