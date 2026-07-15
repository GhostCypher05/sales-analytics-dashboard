import pandas as pd

def load_data():
    """Load the SampleSuperstore dataset from a CSV file."""
    file_path = "data/SampleSuperstore.csv"

    df = pd.read_csv(file_path)

    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())