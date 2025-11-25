import pandas as pd
import numpy as np

def calculate_psi(expected: pd.Series, actual: pd.Series, buckets: int = 10) -> float:
    """Расчёт PSI между эталонным (expected) и текущим (actual) распределениями."""
    def get_bins(series, buckets):
        return np.percentile(series, np.linspace(0, 100, buckets + 1))

    bins = get_bins(expected, buckets)

    expected_counts = np.histogram(expected, bins=bins)[0] / len(expected)
    actual_counts = np.histogram(actual, bins=bins)[0] / len(actual)

    expected_counts = np.where(expected_counts == 0, 1e-6, expected_counts)
    actual_counts = np.where(actual_counts == 0, 1e-6, actual_counts)

    psi = np.sum((actual_counts - expected_counts) * np.log(actual_counts / expected_counts))
    return psi


def detect_data_drift(reference_df: pd.DataFrame, current_df: pd.DataFrame, threshold: float = 0.2):
    """Возвращает фичи, в которых дрейф превышает threshold."""
    drift_report = {}

    common_cols = [col for col in reference_df.columns if col in current_df.columns]

    for col in common_cols:
        try:
            psi = calculate_psi(reference_df[col], current_df[col])
            drift_report[col] = psi
        except Exception:
            drift_report[col] = None

    drifted_features = {k: v for k, v in drift_report.items() if v is not None and v > threshold}

    return drift_report, drifted_features