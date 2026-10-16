
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folder location
folder = Path(__file__).parent
df = pd.read_csv(folder / "cleaned_data.csv")

# Create folder to save graphs
charts_folder = folder / "charts"
charts_folder.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: Book price distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="price_gbp", bins=10, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(charts_folder / "price_distribution.png")
plt.show()

# Chart 2: Average price by rating
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="rating", y="price_gbp", errorbar=None)
plt.title("Average Book Price by Rating")
plt.xlabel("Star Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig(charts_folder / "average_price_by_rating.png")
plt.show()

# Chart 3: Top 10 expensive books
top10 = df.nlargest(10, "price_gbp").sort_values("price_gbp")

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x="price_gbp", y="title")
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig(charts_folder / "top10_expensive_books.png")
plt.show()

print("Task 3 completed successfully!")
print("All charts saved in:", charts_folder)
