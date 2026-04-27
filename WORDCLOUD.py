import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import string

# load dataset Fake and real new dataset
df = pd.read_csv("Fake.csv")

# handle missing
df["title"] = df["title"].fillna("")
df["text"] = df["text"].fillna("")

# combine text
text = " ".join((df["title"] + " " + df["text"]).tolist()).lower()

# clean text
for ch in string.punctuation:
    text = text.replace(ch, " ")

words = [w for w in text.split() if w not in STOPWORDS and len(w) > 3]
clean_text = " ".join(words)

# wordcloud
wc = WordCloud(width=800, height=400, background_color="white").generate(clean_text)

plt.imshow(wc)
plt.axis("off")
plt.title("Word Cloud")
plt.show()
