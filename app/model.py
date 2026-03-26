import joblib
import numpy as np
from pathlib import Path

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"

xgb_model = joblib.load(MODELS_DIR / "xgb_model.pkl")
rf_model = joblib.load(MODELS_DIR / "rf_model.pkl")
lgbm_model = joblib.load(MODELS_DIR / "lgbm_model.pkl")


def predict_ensemble(features: dict):
    # Arrange features in exact order models were trained on
    feature_order = [
        "store", "item", "year", "month",
        "dayofweek", "is_weekend", "weekofyear",
        "lag_1", "lag_7", "lag_14", "lag_28",
        "rolling_mean_7", "rolling_mean_14", "rolling_mean_28"
    ]

    X = np.array([[features[f] for f in feature_order]])

    xgb_pred = xgb_model.predict(X)[0]
    rf_pred = rf_model.predict(X)[0]
    lgbm_pred = lgbm_model.predict(X)[0]

    ensemble_pred = np.mean([xgb_pred, rf_pred, lgbm_pred])

    return round(float(ensemble_pred), 2)

