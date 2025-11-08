# 🏬 Store Item Demand Forecasting: Predictive Intelligence for Retail Operations

This repository presents a complete **data science and business intelligence project** focused on building a reliable, automated **demand forecasting system** for a multi-store retail business. The project integrates **machine learning modeling**, **data automation**, and an interactive **Power BI dashboard**, providing decision-makers with accurate, actionable insights to improve inventory management and sales planning.

---

## Executive Summary

Retail businesses face a constant challenge balancing supply and demand. Overstock leads to waste, while stockouts result in lost sales and unhappy customers.  
This project tackles that challenge by developing **predictive machine learning models** to forecast product demand across **10 stores and 50 items**.  

The goal was to shift from reactive, intuition-driven decisions to a **data-driven forecasting system**. The result is an accurate, scalable, and explainable solution that:
- Enhances **inventory and supply chain planning**  
- Reduces **stockouts and overstocking costs**  
- Provides **visibility into sales trends** for the coming year  

The final deliverables include:
- A high-performing **Ensemble Model** (built from XGBoost, LightGBM, and Random Forest)
- A fully **automated forecasting pipeline**
- An interactive **Power BI dashboard** for business monitoring and decision support

---

## Data Overview

The forecasting model was trained on a **five-year retail sales dataset (2013–2017)**, used to predict demand for **2018**.  
The dataset represents a real-world multi-store and multi-item structure, allowing model generalization across locations and products.

**Key details:**
- **Data Coverage:** 10 stores × 50 items = 500 store-item combinations  
- **Time Span:** Daily sales records (2013–2017), forecasting 2018  
- **Main Features:** store, item, date, and sales  

**Preprocessing & Feature Engineering:**
- Cleaned missing values and handled outliers
- Generated **lag features** (1, 7, 14, 28 days) to capture time dependencies  
- Added **rolling averages** (7-day, 14-day, 28-day) for trend detection  
- Extracted **calendar-based features**: year, month, weekday, and weekend flags  
- Stored all preprocessed data in **SQLite** for easy Power BI integration  

**Integration:**
An SQLite database acts as the data hub - combining processed datasets, predictions, and feature tables for easy connection to Power BI.

---

## ⚙️ Work Overview: End-to-End Pipeline

The workflow follows a full machine learning lifecycle from raw data to visualization.

1. **Data Ingestion & Validation** - Load and inspect raw CSVs for missing values and anomalies.  
2. **Feature Engineering** - Generate lag, rolling mean, and calendar features to capture demand trends.  
3. **Model Training & Evaluation** – Train **ARIMA**, **SARIMA**, **Random Forest**, **XGBoost**, **LightGBM**, and deep learning models like **GRU** and **LSTM** on the prepared datasets.  
4. **Ensemble Modeling** – Combine predictions from top models to form a more stable and accurate forecast.  
5. **Forecast Generation** – Produce store-item forecasts for the year 2018.  
6. **Database Integration** – Store final forecasts in SQLite database.  
7. **Visualization & Insights** – Build a Power BI dashboard showing trends, comparisons, and performance summaries.

**Power BI Dashboard Highlights:**
- **Forecast Trends Over Time:** Line chart of ensemble forecast  
- **Model Comparison:** Column chart comparing model predictions  
- **Store Demand:** Treemap ranking stores by total forecast  
- **Matrix Breakdown:** Table comparing store-item forecasts across models

![Dashboard](https://github.com/user-attachments/assets/2eb63b13-25ec-4646-a3d9-a93247fa38fb)

---

## 🧮 Model Performance

The ensemble-based approach consistently outperformed individual models, offering strong predictive stability and reliability.

**Model Highlights:**
- **Best Overall:** Ensemble Model (combining XGBoost + LightGBM)
- **Key Metrics:**
  - **MAE (Mean Absolute Error):** ~6.12  
  - **RMSE (Root Mean Square Error):** ~7.95  
- **Observation:** XGBoost and LightGBM produced closely aligned forecasts, confirming robust generalization.  
- **Outcome:** The ensemble captured consistent seasonal and store-level patterns with minimal bias.

---

## Recommendations

1. **Optimize Inventory for Top Stores:**  
   Focus stocking and logistics efforts on **Store 8 (224.1k)**, **Store 5 (217.1k)**, and **Store 2 (210.4k)** - the highest forecasted locations.  
2. **Prioritize Key Items:**  
   Ensure availability of **Items 7, 37, and 8**, as they contribute the most to projected demand.  
3. **Adopt the Ensemble Forecast:**  
   Use the Ensemble model’s predictions as the baseline for operational and planning decisions.  
4. **Data-Driven Decisions:**  
   Leverage the Power BI dashboard for real-time insights to monitor shifts in demand patterns.

---

## Path Forward / Future Work

To move from prototype to production-grade forecasting, the following enhancements are planned:

- **🔄 Live Data Automation:** Integrate a continuous data pipeline and enable automatic retraining.  
- **🌐 API Deployment:** Serve forecasts via a REST API to business systems (ERP/WMS).  
- **📈 Hierarchical Forecasting:** Expand from store-item forecasts to regional or category-level analysis.  
- **🧠 External Feature Expansion:** Include external factors like promotions, seasonality events, or weather data.  
- **🧪 Continuous Evaluation:** Automate performance tracking using Power BI alerts and monitoring dashboards.

---

## 🧰 Tech Stack

| Tool | Purpose |
| :---------------- | :----------------------------------------------------------- |
| **Python** | Data processing, model training, and feature engineering |
| **pandas, numpy** | Data manipulation and transformation |
| **ARIMA, SARIMA, XGBoost, LightGBM, Random Forest, GRU, LSTM** | Core forecasting and machine learning frameworks used for traditional, ensemble, and deep learning models. |
| **joblib** | Model persistence and serialization |
| **SQLite** | Lightweight database for structured storage |
| **Power BI** | Visualization and business reporting |
| **Jupyter Notebooks** | Exploration, modeling, and workflow documentation |

---

## 🧱 Repository Structure

├── data/
│   ├── forcasting.db               
│   ├── raw_sales_data.csv           
│
├── python_notebook/
│   ├── demand_forecasting.ipynb      
│   ├── forecasting_pipeline.ipynb   
│
├── models/
│   ├── xgb_model.pkl
│   ├── rf_model.pkl
│   ├── lgbm_model.pkl
│   └── forecast_results.csv 
│
├── reports/
│   ├── demand_forecasting_presentation.pptx 
│   ├── dl_forecast_metrics.xlsx
│   ├── ml_forecast_metrics.xlsx
│   └── distribution_of_sales_across_model.png
│
├── powerbi_dashboard/
│   ├── demand_forecasting_dashboard.pbix
│   ├── demand_forecasting_dashboard_screenshot.png
│   └── dax_measures.docx
│
├── images/
│   ├── forecast_vs_actual.png
│   ├── seasonal_pattern_example.png
│
└── README.md

---

## 📫 Contact

If you’re interested in collaboration, feedback, or have questions about this project, feel free to reach out.

| Detail            | Information                                                                                   |
| :---------------- | :-------------------------------------------------------------------------------------------- |
| 👤 **Author**     | [Osaretin Idiagbonmwen](https://www.linkedin.com/in/osaretin-idiagbonmwen-33ab85339)          |
| 📧 **Email**      | [oidiagbonmwen@gmail.com](mailto:oidiagbonmwen@gmail.com)                                     |
| 🐙 **GitHub**     | [OsasAnalyst](https://github.com/OsasAnalyst)                                                 |
| 📂 **Repository** | [Store Item Demand Forecasting](https://github.com/OsasAnalyst/store-item-demand-forecasting) |

---

⭐ *If you found this project useful, consider starring the repository to support more open-source data science projects like this!*

