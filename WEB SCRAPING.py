import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

books = soup.select("article.product_pod")

data = [(b.h3.a["title"], 
         b.select_one("p.price_color").text)
        for b in books]

df = pd.DataFrame(data, columns=["Book", "Price"])
print(df)

df.to_csv("books.csv", index=False)
