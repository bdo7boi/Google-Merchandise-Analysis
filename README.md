# 🛍️ Google Merchandise Product Performance Analysis by Theme

## 📘 Project Overview
This project explores product performance within the **Google Merchandise Store** dataset by analyzing purchase and revenue trends across themed product groups such as **Google**, **Android**, and **YouTube**.

Using **Python (Pandas)** for data processing and **Tableau** for visualization, the project demonstrates a full end-to-end data analysis workflow — from data cleaning and feature engineering to aggregated insights and visual storytelling.

---

## 🎯 Objectives
- Combine user, event, and item datasets into a single analytical DataFrame.
- Categorize products into **themes/brands** (e.g., Google, Android, YouTube).
- Calculate **total purchases** and **total sales (USD)** per theme.
- Export cleaned and aggregated data for use in **Tableau dashboards**.

---

## 🧩 Dataset
**Source:** Google Merchandise Sales Data(https://www.kaggle.com/datasets/mexwell/google-merchandise-sales-data)
**Files Used:**
- `events1.csv` — customer interactions (purchases, events, timestamps)
- `users.csv` — user IDs and visit metadata
- `items.csv` — product details and prices

Each file was read using **Pandas**, merged using common keys (`user_id`, `item_id`), and cleaned for analysis.

---

## 🧠 Data Processing Steps
1. **Read and clean CSV files**  
   Converted date columns to `datetime` and dropped redundant ID columns.

2. **Merged datasets**  
   Joined events → items → users to create a unified view of transactions.

3. **Assigned Product Themes**  
   Used a Python function to classify products by brand name for better
   visualization of trends. 
