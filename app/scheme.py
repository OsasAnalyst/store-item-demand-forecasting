from pydantic import BaseModel 
from datetime import date

class ForecastRequest(BaseModel):
    store: int
    item: int
    date: date
    lag_1: float
    lag_7: float
    lag_14: float
    lag_28: float
    rolling_mean_7: float
    rolling_mean_14: float
    rolling_mean_28: float

class ForecastResponse(BaseModel):
    store: int
    item: int
    date: str
    forecasted_sales: float
