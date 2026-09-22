# Customer Shopping Behavior Analysis

An end-to-end data analytics and business intelligence project simulating a corporate workflow. This repository transforms raw transactional data into actionable insights using **Python**, **SQL Server**, and **Power BI**.

---

## 📌 Project Overview

This project analyzes **3,900 customer purchases** to uncover valuable spending patterns, evaluate product preferences, segment customers, and drive strategic retail decisions[cite: 1]. The workflow is structured across four main phases:

* **Data Preparation & Engineering (Python):** Cleaned raw data, handled missing values using category medians, standardized headers to snake_case, and engineered custom features (`age_group`, `purchase_frequency_days`)[cite: 1, 3].
* **Database Warehousing & Analysis (SQL Server):** Ingested the cleaned dataset into SQL Server to execute complex queries answering key business questions regarding revenue drivers, customer segmentation, and discount sensitivity.
* **Interactive Business Intelligence (Power BI):** Designed a dynamic dashboard to track high-level KPIs (Total Customers, Average Purchase Amount, Review Ratings) and slice data by demographics, shipping methods, and category performance.
* **Strategic Reporting:** Formulated professional documentation and executive presentation talking points to communicate findings to stakeholders effectively[cite: 1].

---

## 🛠️ How to Use This Project

### 1. Clone the Repository
```bash
git clone [https://github.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI.git](https://github.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI.git)
cd customer-trends-data-analysis-SQL-Python-PowerBI

2. Run the Data Pipeline
(Python)Open and run main.py (or the corresponding Jupyter Notebook) to load, clean, and feature-engineer the dataset.   Ensure your local database connection parameters (SQL Server / PostgreSQL / MySQL) are properly configured in the script.
3. Execute Business Queries (SQL)Open Project All Quries.sql in your SQL client.   Run the structured scripts against your database to extract insights on revenue distribution, customer loyalty tiers, and product rankings.
4. Explore the Dashboard (Power BI)Open Customer Behavour Deshboard.pbix in Power BI Desktop.
 Interact with the filters to explore visual patterns across subscription statuses, shipping types, and age groups[cite: 1, 2].
📊 Key Insights at a GlanceGender & Revenue: Male shoppers generated higher total revenue ($157,890) compared to female shoppers ($75,191).
 Subscription Gap: 73% of customers are non-subscribers, presenting a substantial growth opportunity to target high-frequency buyers with loyalty perks.   Discount Sensitivity: Top products like hats, sneakers, and coats experience discount rates near 50%, highlighting the need for careful margin management[cite: 1, 4].
📜 License
 MIT — Feel free to fork, star, and use this project for your portfolio.
👨‍💻 Author
Piash Barua
Executive Project Manager & Production Executive | Data Analytics & Cybersecurity Enthusiast
