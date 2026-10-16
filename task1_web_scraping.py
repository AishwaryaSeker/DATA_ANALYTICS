
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = []

for item in soup.select("article.product_pod"):
    title = item.select_one("h3 a")["title"]
    price_text = item.select_one(".price_color").get_text(strip=True)
    rating_class = item.select_one(".star-rating")["class"]
    rating_word = next(
        word for word in rating_class if word != "star-rating"
    )

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    books.append({
        "title": title,
        "price_gbp": float(
    price_text.replace("Â£", "").replace("£", "").strip()
),
        "rating": rating_map[rating_word]
    })

df = pd.DataFrame(books)

output_file = Path(__file__).parent / "scraped_data.csv"
df.to_csv(output_file, index=False)

print("Web scraping completed!")
print("Books collected:", len(df))
print(df.head())
print("CSV saved at:", output_file)
