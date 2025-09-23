# 🛒 Store Item Demand Forecasting

![Demand Forecasting](https://raw.githubusercontent.com/OsasAnalyst/store-item-demand-forecasting/main/Demand-Forecasting-Types-1024x576.jpg)
  
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

---

# Exploratory Data Analysis (EDA)

Before building forecasting models, I performed an exploratory analysis of the dataset to understand its structure, trends, and variability.

### Dataset Overview

- **Shape**: `(730,500, 4)` → daily sales records for 10 stores and 50 items over 5 years (2013–2017).  
- **Columns**:  
  - `date` → daily timestamp (2013-01-01 to 2017-12-31)  
  - `store` → store identifier (1 to 10)  
  - `item` → item identifier (1 to 50)  
  - `sales` → number of units sold (integer, min = 0, max = 214)  

### Summary Statistics

| Feature | Mean  | Min | 25% | 50% | 75% | Max | Std Dev |
|---------|------:|----:|----:|----:|----:|----:|--------:|
| store   | 5.5   | 1   | 3   | 5.5 | 8   | 10  | 2.87    |
| item    | 25.5  | 1   | 13  | 25.5| 38  | 50  | 14.43   |
| sales   | 50.61 | 0   | 29  | 45  | 67  | 214 | 27.83   |

- Sales are **highly variable** (std ≈ 27.8).  
- Items and stores are uniformly distributed (1–50 items, 1–10 stores).  
- The median sales per day is **45 units**, but outliers reach **200+ units**.  

---

### Store-Level Sales Distribution

Each store shows relatively similar overall demand, with no extreme outliers.   

![Store-Level Sales](https://github.com/user-attachments/assets/9e3820b0-6534-46cc-9aec-014de30e77d2)

---

### Total Daily Sales Across All Stores & Items

Aggregating across all stores and items, sales show **clear weekly and yearly seasonality**:  
- Weekly cycles → peaks and troughs likely tied to weekdays/weekends.  
- Yearly cycles → higher demand during certain months (e.g., holidays).  


![Total Daily Sales](https://github.com/user-attachments/assets/d811b60d-2024-4ed4-81e3-830f01e4f0fe)

---

### Sales Trends for Sample Items

Individual items show diverse sales behaviors:  
- Some items have **steady demand**.  
- Others exhibit **strong seasonality** or **sporadic spikes**.  
 

![Sample Item Sales](https://github.com/user-attachments/assets/080f33f3-43a2-45f6-af32-9dbef5992757)


---


---

---

# Feature Engineering

Before building forecasting models, the raw sales data needed to be transformed so I could use it effectively.

### Making the Data Stationary
I first checked if the sales series was stationary, which means it doesn’t have trends or big changes over time. Using a statistical test, I found it was not stationary. To fix this, I applied a **log transformation** to stabilize the variance and then **differencing** to remove trends. After this, the data became stationary and ready for classical models like ARIMA.

### Creating Time-Based Features
For machine learning models, I added new features from the date:  
- **Year, month, day** → to capture seasonal effects.  
- **Day of the week** → to capture weekday/weekend patterns.  
- **Week of the year** → to detect yearly trends.  
- **Weekend flag** → to separate weekend behavior from weekdays.  

These features help the models understand patterns in the sales data that repeat over time.

### Scaling Sales Values
I also scaled the raw sales values to make the numbers easier for machine learning models to work with. Scaling ensures that one feature does not dominate the model because of its size.

### Lag and Rolling Features
I created features that capture past sales information:  
- **Lag features** → yesterday’s sales, last week’s sales, and other past days.  
- **Rolling averages** → average sales over the last 7, 14, or 28 days.  

These features help the models learn short-term and medium-term patterns in sales.

### Consistent Processing
I applied all these steps in a **single preprocessing routine** so that train, validation, and test sets are treated the same way. The lag and rolling features were computed carefully so that no future information leaks into past data.

### Final Dataset
After feature engineering, the data was split into **train, validation, and test sets**, with input features (`X`) and target sales (`y`) ready for model training. This dataset includes:  
- Store and item identifiers  
- Time-based features  
- Lag and rolling features  
- Scaled sales values for machine learning  

These engineered features give my models the information they need to make accurate sales predictions at the store-item level.


