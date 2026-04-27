import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset Students Performance in Exams
df = pd.read_csv("exam_scores.csv")

print(df.head())

# ---------------- EDA ----------------
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode().iloc[0])
print("Variance:\n", df.var(numeric_only=True))
print("Std Dev:\n", df.std(numeric_only=True))
print("Min:\n", df.min(numeric_only=True))
print("Max:\n", df.max(numeric_only=True))
print("Missing:\n", df.isnull().sum())

corr = df.corr(numeric_only=True)

# ---------------- Plots ----------------

# Histogram
plt.hist(df["math"], bins=20)
plt.title("Math Score Distribution")
plt.show()

# Boxplot
sns.boxplot(x=df["math"])
plt.title("Math Boxplot")
plt.show()

# Scatter
plt.scatter(df["math"], df["reading"])
plt.title("Math vs Reading")
plt.show()

# Line
plt.plot(df["math"].head(50))
plt.title("Math Trend")
plt.show()

# Bar
means = df.mean(numeric_only=True)
means.plot(kind="bar")
plt.title("Average Scores")
plt.show()

# Pie
means.plot(kind="pie", autopct="%1.1f%%")
plt.title("Score Share")
plt.ylabel("")
plt.show()

# Heatmap
sns.heatmap(corr, annot=True)
plt.title("Correlation")
plt.show()

# Violin
sns.violinplot(data=df)
plt.title("Score Distribution")
plt.show()

# Pairplot
sns.pairplot(df)
plt.show()

# Countplot (create category)
df["level"] = pd.cut(df["math"], bins=[0,50,70,100], labels=["Low","Medium","High"])
sns.countplot(x=df["level"])
plt.title("Math Level Count")
plt.show()

print("Done")
