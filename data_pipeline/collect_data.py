import pandas as pd
import requests


def fetch_from_api(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def main():
    df = fetch_from_api(API_URL)
    df.to_csv("data/raw/data_raw.csv", index=False)

if __name__ == "__main__":
    main()