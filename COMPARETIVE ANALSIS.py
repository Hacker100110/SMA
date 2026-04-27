import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

# load dataset
df = pd.read_csv("Reviews.csv")

# take small sample
reviews = df["Text"].dropna().astype(str).head(2000)

# clean
def clean(t):
    t = re.sub(r"http\S+|[^a-zA-Z ]", "", t)
    return t.lower()

reviews = [clean(t) for t in reviews]

# sentiment
def get_sentiment(t):
    s = TextBlob(t).sentiment.polarity
    return "Positive" if s>0 else "Negative" if s<0 else "Neutral"

result = {"Positive":0,"Negative":0,"Neutral":0}

for r in reviews:
    result[get_sentiment(r)] += 1

print(result)

# graph
pd.Series(result).plot(kind="bar")
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
