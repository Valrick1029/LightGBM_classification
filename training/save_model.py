import joblib
import json
from datetime import datetime

def save(model, features):
    model_path = "models/model.pkl"
    joblib.dump(model, model_path)

    metadata = {
        "model_path": model_path,
        "trained_at": str(datetime.now()),
        "features": features,
        "model_version": "1.0.0"
    }

    with open("models/metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("Модель и метаданные сохранены.")