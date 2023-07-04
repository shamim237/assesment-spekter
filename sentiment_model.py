import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the required lexicon for sentiment analysis

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment_text(text):
    
    # Analyze sentiment of the given text
    sentiment = sia.polarity_scores(text)
    compound_score = sentiment['compound']

    # Determine the sentiment label based on the compound score
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'