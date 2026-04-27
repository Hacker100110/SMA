
import pandas as pd

# load dataset (Tweets.csv from Kaggle)
df = pd.read_csv("Tweets.csv")

# keep only required columns and rename
df = df[["text", "airline_sentiment"]].rename(columns={"airline_sentiment": "sentiment"})

# cleaning
df["text"] = (
    df["text"]
    .str.lower()
    .str.replace(r"http\S+|www\S+", "", regex=True)
    .str.replace(r"@\w+|#", "", regex=True)
    .str.replace(r"[^a-z\s]", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# remove nulls and duplicates
df = df.dropna().drop_duplicates(subset="text")

print(df.head())

# save cleaned data
df.to_csv("cleaned_airline_sentiment.csv", index=False)

