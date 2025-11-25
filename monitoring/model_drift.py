import json
from sklearn.metrics import roc_auc_score, f1_score

def evaluate_model_drift(y_true, y_pred, prev_metrics_path="prev_metrics.json",
                         metric="roc_auc", threshold=0.05):
    """Сравнивает текущие метрики с эталонными, проверяет дрейф."""
    if metric == "roc_auc":
        current_value = roc_auc_score(y_true, y_pred)
    elif metric == "f1":
        current_value = f1_score(y_true, y_pred)
    else:
        raise ValueError("Unsupported metric")

    with open(prev_metrics_path, "r") as f:
        prev_value = json.load(f)[metric]

    diff = prev_value - current_value
    drift = diff > threshold

    return {
        "previous": prev_value,
        "current": current_value,
        "difference": diff,
        "drift_detected": drift,
    }