import pandas as pd
from category_encoders.hashing import HashingEncoder

def preprocess(df):
    df = df.drop_duplicates()
    
    # заполнение пропусков
    df = df.fillna(0)

    # encoding
    encoder = HashingEncoder(n_features=16)
    df_hash = encoder.fit_transform(df["wallet_address"])
    df = df.drop("wallet_address", axis=1)
    df = pd.concat([df, df_hash], axis=1)

    # feature selection
    df = df[selected_features]

    return df

def main():
    df = pd.read_csv("data/validated/data_validated.csv")
    df = preprocess(df)
    df.to_csv("data/processed/data_preprocessed.csv", index=False)

if __name__ == "__main__":
    main()