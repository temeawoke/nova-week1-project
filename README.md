📊 Nova Financial Insights – Sentiment and Time Series Analysis

This project analyzes financial news headlines to uncover correlations between news sentiment and stock price movements, using natural language processing (NLP), time series analysis, and financial indicators. The goal is to provide actionable insights that support investment strategies and predictive financial modeling.

🧠 Project Objectives
Sentiment Analysis: Determine the emotional tone (positive, neutral, or negative) of financial news headlines.

Time Series Analysis: Track publication frequency trends and align them with market events.

Topic Modeling: Extract key themes from news data using NLP techniques.

Technical Indicator Analysis: Analyze stock performance using indicators like MA, RSI, and MACD.

Publisher Insights: Identify the most active and impactful news publishers.

🗂️ Project Structure

nova-week1-project/
│
├── data/                         # Raw and processed data
│   ├── raw_analyst_ratings.csv
│   └── processed/
│
├── notebooks/                    # Exploratory and modeling notebooks
│   ├── eda_sentiment_analysis.ipynb
│   └── time_series_analysis.ipynb
│
├── src/                          # Core scripts
│   ├── eda_sentiment_analysis.py
│   ├── topic_modeling.py
│   └── technical_indicators.py
│
├── outputs/                      # Saved plots and results
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview
📌 Key Features
✅ Clean and preprocess text data

✅ Perform sentiment classification using rule-based and model-based approaches

✅ Visualize sentiment distribution and time-based trends

✅ Generate word clouds and bar charts for publishers

✅ Analyze trends and publishing patterns

✅ Model stock technical indicators (MA, RSI, MACD)

✅ Apply topic modeling with LDA to uncover themes

⚙️ Setup Instructions
Clone the repository:

git clone https://github.com/temeawoke/nova-week1-project.git
cd nova-week1-project
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate (Windows)
Install dependencies:

pip install -r requirements.txt
💡 For TA-Lib on Windows, install the .whl file manually if pip installation fails.

📈 Example Visualizations
Sentiment Distribution Plot (Positive/Neutral/Negative)

WordCloud of most frequent headline words

Weekly publication trends by publisher

Time series overlays with stock data

🧩 Dependencies
pandas, numpy

matplotlib, seaborn

nltk, spacy, gensim

scikit-learn

wordcloud

ta or TA-Lib

datetime