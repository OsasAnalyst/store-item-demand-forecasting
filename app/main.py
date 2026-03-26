from fastapi import FastAPI
from app.scheme import ForecastRequest, ForecastResponse
from app.model import predict_ensemble

app = FastAPI(
    title="Store Item Demand Forecasting API",
    description="Predicts retail demand using an ensemble of XGBoost, LightGBM, and Random Forest.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict", response_model=ForecastResponse)
def predict(request: ForecastRequest):
    features = {
        "store": request.store,
        "item": request.item,
        "year": request.date.year,
        "month": request.date.month,
        "dayofweek": request.date.weekday(),     
        "is_weekend": int(request.date.weekday() >= 5),
        "weekofyear": request.date.isocalendar()[1],
        "lag_1": request.lag_1,
        "lag_7": request.lag_7,
        "lag_14": request.lag_14,
        "lag_28": request.lag_28,
        "rolling_mean_7": request.rolling_mean_7,
        "rolling_mean_14": request.rolling_mean_14,
        "rolling_mean_28": request.rolling_mean_28,
    }

    prediction = predict_ensemble(features)

    return ForecastResponse(
        store=request.store,
        item=request.item,
        date=str(request.date),
        forecasted_sales=prediction
    )