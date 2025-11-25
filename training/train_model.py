import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import joblib
import json

def train():
    df = pd.read_csv("data/processed/processed_data.csv")
    
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Загрузка параметров
    with open("config/model_params.pkl", "r") as f:
        params = json.load(f)
    
    model = lgb.LGBMClassifier(**params)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")
    print("Модель обучена и сохранена.")

if __name__ == "__main__":
    train()