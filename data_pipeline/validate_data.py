import pandas as pd

def validate(df):
    assert len(df) > 0, "Dataset is empty!"
    assert "target" in df.columns, "Missing target column!"
    assert df.isna().mean().max() < 0.5, "Too many missing values!"
    return True

def main():
    df = pd.read_csv("data/raw/data_raw.csv")
    validate(df)
    df.to_csv("data/validated/data_validated.csv", index=False)

if __name__ == "__main__":
    main()