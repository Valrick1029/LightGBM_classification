import pandas as pd
import matplotlib.pyplot as plt
import json
from data_drift import detect_data_drift
from model_drift import evaluate_model_drift

def generate_monitoring_report(reference_df, current_df, y_true, y_pred,
                               out_prefix="monitoring_report"):
    
    # === DRIFT DATA ===
    psi_report, drifted_features = detect_data_drift(reference_df, current_df)

    # === METRIC DRIFT ===
    metric_report = evaluate_model_drift(y_true, y_pred)

    # === Save text report ===
    with open(f"{out_prefix}.txt", "w") as f:
        f.write("=== DATA DRIFT (PSI) ===\n")
        for k, v in psi_report.items():
            f.write(f"{k}: {v}\n")
        f.write("\nDrift detected:\n")
        f.write(str(drifted_features))

        f.write("\n\n=== MODEL DRIFT ===\n")
        f.write(json.dumps(metric_report, indent=4))

    # === Barplot PSI ===
    plt.figure(figsize=(10, 6))
    psi_values = {k: v for k, v in psi_report.items() if v is not None}
    plt.bar(range(len(psi_values)), list(psi_values.values()))
    plt.xticks(range(len(psi_values)), psi_values.keys(), rotation=90)
    plt.title("PSI per Feature")
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_psi.png")
    plt.close()

    print(f"Report saved as {out_prefix}.txt and {out_prefix}_psi.png")