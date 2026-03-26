# Store Item Demand Forecasting

A machine learning project that predicts how much of each product a store will sell - so businesses can stock the right amount at the right time.

---

## The Problem

Retail stores deal with a tough balancing act every day.

Order too much stock - products sit on shelves and go to waste.
Order too little - shelves go empty and customers leave unhappy.

Most stores still guess based on experience or simple spreadsheets. This project replaces that guesswork with a machine learning system that learns from 5 years of sales history to predict future demand across **10 stores and 50 items**.

---

## What Was Built

- A machine learning model that forecasts daily product demand
- An ensemble approach combining XGBoost, LightGBM, and Random Forest for better accuracy
- A REST API built with FastAPI so any system can request a forecast
- A Docker container so the app runs the same way on any machine
- A Power BI dashboard for business monitoring and decision support
- An automated forecasting pipeline stored in SQLite

---

## How It Works

**Input:** Store number, item number, date, and recent sales history (lag and rolling averages)

**Output:** Predicted sales number for that store-item combination

The model learned patterns like:
- Which days of the week sell more
- How last week's sales affect this week
- Seasonal trends across the year

---

## Data

- **Source:** Five years of daily retail sales (2013–2017)
- **Scope:** 10 stores × 50 items = 500 store-item combinations
- **Goal:** Forecast demand for 2018

**Features used:**
- Store and item identifiers
- Calendar features: year, month, day of week, weekend flag, week of year
- Lag features: sales from 1, 7, 14, and 28 days ago
- Rolling averages: 7-day, 14-day, and 28-day moving averages

---

## Models Trained

| Model | Type |
| :---- | :--- |
| ARIMA | Classical time series |
| SARIMA | Seasonal time series |
| Random Forest | Machine learning |
| XGBoost | Machine learning |
| LightGBM | Machine learning |
| GRU | Deep learning |
| LSTM | Deep learning |

**Best result:** Ensemble of XGBoost + LightGBM + Random Forest

| Metric | Score |
| :----- | :---- |
| MAE | ~6.12 |
| RMSE | ~7.95 |

---

## API Deployment

The forecasting model is served as a REST API using **FastAPI** and packaged with **Docker**.

### Run Locally with Docker

**Step 1 — Build the image:**
```bash
docker build -t demand-forecasting-api .
```

**Step 2 — Run the container:**
```bash
docker run -p 8000:8000 demand-forecasting-api
```

**Step 3 — Open the interactive docs:**
```
http://127.0.0.1:8000/docs
```

### Sample API Request

Send a `POST` request to `/predict`:
```json
{
  "store": 1,
  "item": 1,
  "date": "2018-01-01",
  "lag_1": 13.0,
  "lag_7": 15.0,
  "lag_14": 12.0,
  "lag_28": 11.0,
  "rolling_mean_7": 14.2,
  "rolling_mean_14": 13.8,
  "rolling_mean_28": 13.1
}
```

### Sample Response
```json
{
  "store": 1,
  "item": 1,
  "date": "2018-01-01",
  "forecasted_sales": 47.83
}
```

---

## Power BI Dashboard

An interactive dashboard was built to help business teams monitor forecasts without needing to touch the code.

**What it shows:**
- Forecast trends over time
- Model comparison chart
- Store demand ranked by volume
- Store-item breakdown table

![Dashboard](https://github.com/user-attachments/assets/2eb63b13-25ec-4646-a3d9-a93247fa38fb)

---

## Business Recommendations

**1. Focus on your top stores**
Stores 8, 5, and 2 have the highest forecasted demand. Make sure they are stocked first.

**2. Protect your top items**
Items 7, 37, and 8 drive the most volume. Running out of these hurts the most.

**3. Use the ensemble forecast as your baseline**
The ensemble model was more stable and accurate than any single model on its own.

**4. Monitor with the dashboard**
Use the Power BI dashboard to catch demand shifts early before they become stock problems.

---

## Repository Structure
```
├── app/
│   ├── main.py                   
│   ├── model.py                  
│   └── schema.py                 
│
├── data/
│   ├── forcasting.db
│   └── demand_forecasting_data.zip
│
├── python_notebook/
│   ├── demand_forecasting.ipynb
│   └── forecasting_pipeline.ipynb
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
│   └── seasonal_pattern_example.png
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
| :--- | :------ |
| Python | Data processing and model training |
| pandas, numpy | Data manipulation |
| XGBoost, LightGBM, Random Forest | Core ML models |
| ARIMA, SARIMA | Classical time series models |
| GRU, LSTM | Deep learning models |
| FastAPI | REST API for serving predictions |
| Docker | Containerization for deployment |
| joblib | Saving and loading models |
| SQLite | Lightweight database storage |
| Power BI | Business dashboard and reporting |
| Jupyter Notebooks | Exploration and modeling |

---

## Contact

| Detail | Information |
| :----- | :---------- |
| **Author** | [Osaretin Idiagbonmwen](https://www.linkedin.com/in/osaretin-idiagbonmwen-33ab85339) |
| **Email** | [oidiagbonmwen@gmail.com](mailto:oidiagbonmwen@gmail.com) |
| **GitHub** | [OsasAnalyst](https://github.com/OsasAnalyst) |
| **Repository** | [Store Item Demand Forecasting](https://github.com/OsasAnalyst/store-item-demand-forecasting) |

---
