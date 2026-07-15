from data_loader import load_data

# Load the dataset
df = load_data()

print(f"Original dataset shape: {df.shape}")

# Remove duplicate rows
df = df.drop_duplicates()

print(f"Dataset shape after removing duplicates: {df.shape}")

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.csv", index=False)

print("Cleaned dataset saved successfully!")