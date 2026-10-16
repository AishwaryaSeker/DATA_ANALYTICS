
import pandas as pd
from pathlib import Path

# Load scraped data
folder = Path(__file__).parent
df = pd.read_csv(folder / "scraped_data.csv")

print("=== DATASET OVERVIEW ===")
print("Total books:", len(df))
print("Columns:", list(df.columns))

print("\n=== FIRST 5 BOOKS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== PRICE SUMMARY ===")
print(df["price_gbp"].describe().round(2))

print("\n=== AVERAGE PRICE BY RATING ===")
print(df.groupby("rating")["price_gbp"].mean().round(2))

print("\n=== MOST EXPENSIVE BOOK ===")
print(df.loc[df["price_gbp"].idxmax()])

# Save cleaned data
df = df.drop_duplicates()
df = df.dropna(subset=["title", "price_gbp", "rating"])

df.to_csv(folder / "cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
