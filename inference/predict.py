import joblib
import pandas as pd
import numpy as np
from pathlib import Path

MODEL_PATH = Path("models/final_model.pkl")
FEATURES_PATH = Path("models/features.pkl")

# Загружаем все артефакты
model = joblib.load(MODEL_PATH)
feature_list = joblib.load(FEATURES_PATH)


def preprocess_input(data: dict) -> np.ndarray:
    
    df = pd.DataFrame([data])

    df = df[feature_list]

    return df_scaled


def predict(data: dict) -> float:

    X = preprocess_input(data)
    proba = model.predict_proba(X)[0, 1]
    return float(proba)