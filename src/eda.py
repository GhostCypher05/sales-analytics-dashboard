import data_loader

# Load the dataset
df = data_loader.load_data()

print("=" * 50)
print("FIRST FIVE ROWS OF THE DATASET")
print("=" * 50)


#Preview the first few rows of the dataset
print(df.head())

print("\n")

print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)

print(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

print("\n")

print("=" * 50)
for column in df.columns:
    print(column)
print("=" * 50)

print(df.columns)

print("\n")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

df.info()

print("\n")

print("=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)

print(df.describe())

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)

print(f"Duplicate rows: {df.duplicated().sum()}")