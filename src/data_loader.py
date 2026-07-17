import pandas as pd

DATA_PATH = "data/processed/cleaned_superstore.csv"

def load_data():
    """Load the Superstore dataset from a CSV file."""
    df = pd.read_csv(DATA_PATH, parse_dates=["Order Date", "Ship Date"])

    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())