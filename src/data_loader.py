import pandas as pd

DATA_PATH = "data/raw/Sample - Superstore.csv"

def load_data():
    """Load the Superstore dataset from a CSV file."""
    df = pd.read_csv(DATA_PATH, encoding="cp1252")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())