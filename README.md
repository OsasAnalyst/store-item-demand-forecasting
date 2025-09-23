# 🛒 Store Item Demand Forecasting

![Demand Forecasting](https://github.com/user-attachments/assets/0cfa3a8b-forecasting-banner-example)  
*Building smarter demand forecasts to cut stockouts, reduce overstocking, and improve e-commerce efficiency.*

---

# Executive Summary

For e-commerce businesses, **knowing how much of each product to stock and when** is critical. Poor demand forecasts lead to two expensive problems:  
- **Stockouts** → lost sales and unhappy customers  
- **Overstocking** → wasted storage and tied-up capital  

In this project, I tackled the **Store Item Demand Forecasting** challenge using historical sales data from multiple stores and products. The goal was to move beyond simple heuristics like moving averages and instead build **robust, data-driven forecasting models**.

I experimented with three modeling families:  
- **Classical time series models (ARIMA, SARIMA)**  
- **Machine learning models (Random Forest, XGBoost, LightGBM, Linear Models)**  
- **Deep learning models (Dense NN, LSTM, GRU)**  

The results show that **tree-based ensemble models (XGBoost, LightGBM)** consistently outperform others, with significant improvements over naive baselines. Even modest accuracy gains translate to **better inventory planning, fewer lost sales, and higher customer satisfaction** at scale.

---

# Project Objectives

The objective of this project is to **predict future product sales at the store–item level** so businesses can plan inventory more effectively.  

Key goals:  
1. **Develop Forecasting Models**  
   - Start with simple baselines (Naive, Mean).  
   - Progress to classical models (ARIMA/SARIMA).  
   - Apply machine learning and deep learning approaches.  

2. **Evaluate & Compare Methods**  
   - Use RMSE and MAE as primary metrics.  
   - Benchmark against naive baselines to ensure added value.  

3. **Generate Actionable Insights**  
   - Identify models suitable for real-world deployment.  
   - Show how better forecasts directly support **inventory planning, promotions, and supply chain efficiency**.  

📌 By achieving these objectives, the project demonstrates how data science can solve a **real-world retail problem** with clear financial impact.  

---

# Data Collection

The dataset comes from the **Kaggle Store Item Demand Forecasting** challenge. It includes **daily sales data** across multiple stores and items.  

It contains three files:  

- **`train.csv`** → historical sales records (used for training).  
- **`test.csv`** → periods for which we forecast demand.  
- **`sample_submission.csv`** → a template provided in the competition, though here we use it only to understand expected output format.  

Steps:  
- Downloaded and unzipped the dataset.  
- Loaded into **pandas DataFrames** for exploration and feature engineering.  

This dataset is ideal for testing both **time series forecasting techniques** and **supervised learning approaches**, since it captures seasonality, store effects, and item-specific demand patterns.  

---
