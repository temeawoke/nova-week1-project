# eda_sentiment_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load dataset
df = pd.read_csv("data/raw_analyst_ratings.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing dates or headlines
df = df.dropna(subset=['date', 'headline'])

# ========== BASIC STATS ==========
print("\n--- Basic Info ---")
print(df.info())
print("\n--- Summary Stats ---")
print(df.describe(include='all'))

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# ========== TEXT LENGTH ANALYSIS ==========
df['headline_length'] = df['headline'].apply(len)
df['word_count'] = df['headline'].apply(lambda x: len(x.split()))

print("\n--- Headline Length Stats ---")
print(df[['headline_length', 'word_count']].describe())

# ========== STOCK SYMBOLS ==========
print("\n--- Top 10 Stock Symbols ---")
print(df['stock'].value_counts().head(10))

# ========== PUBLISHERS ==========
print("\n--- Top 10 Publishers ---")
print(df['publisher'].value_counts().head(10))

# ========== ARTICLES OVER TIME ==========
articles_per_day = df['date'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
articles_per_day.plot()
plt.title("Number of Articles Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Articles")
plt.grid(True)
plt.tight_layout()
plt.savefig("articles_over_time.png")
plt.close()

# ========== WORD CLOUD ==========
all_text = ' '.join(df['headline'].dropna().astype(str).str.lower())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Headlines")
plt.tight_layout()
plt.savefig("headline_wordcloud.png")
plt.close()

# ========== DISTRIBUTIONS ==========
plt.figure(figsize=(10, 4))
sns.histplot(df['headline_length'], bins=50, kde=True)
plt.title("Distribution of Headline Length")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("headline_length_distribution.png")
plt.close()

plt.figure(figsize=(10, 4))
sns.histplot(df['word_count'], bins=50, kde=True, color='orange')
plt.title("Distribution of Word Count per Headline")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("word_count_distribution.png")
plt.close()