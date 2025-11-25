import pandas as pd
from sklearn.metrics import roc_auc_score, classification_report
import joblib

def evaluate():
    df = pd.read_csv("data/processed/processed_data.csv")
    model = joblib.load("models/model.pkl")

    X = df.drop("target", axis=1)
    y = df["target"]

    preds = model.predict_proba(X)[:, 1]

    auc = roc_auc_score(y, preds)
    print("ROC-AUC:", auc)

    print(classification_report(y, preds > 0.5))

if __name__ == "__main__":
    evaluate()