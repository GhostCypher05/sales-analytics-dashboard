import pandas as pd

RAW_DATA_PATH = "data/raw/Sample - Superstore.csv"
# Load the raw dataset
df = pd.read_csv(RAW_DATA_PATH, encoding="cp1252", parse_dates=["Order Date", "Ship Date"])

print("=" * 50)
print("DATA CLEANING")
print("=" * 50)

print(f"Original dataset shape: {df.shape}")

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

print("\nData Types After Conversion:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Remove duplicates
duplicates_count = df.duplicated().sum() 

print(f"Number of duplicate rows: {duplicates_count}")

df = df.drop_duplicates()

print(f"Dataset shape after cleaning: {df.shape}")

# Save cleaned dataset
df.to_csv("data/processed/cleaned_superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")