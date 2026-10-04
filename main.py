# Import necessary libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Download required nltk data
nltk.download("vader_lexicon")
nltk.download("stopwords")
nltk.download("punkt")
sid = SentimentIntensityAnalyzer()
# Sample text for emotion detection
text = '''
I am so happy today! The weather is beautiful,and everything is going well.
I feel very positive and motivated.
'''
# Function to detect emotion in text
def detect_emotion(text):
    # Analyze sentiment
    scores = sid.polarity_scores(text)
    # Display sentiment scores
    print("Sentiment Scores: ",scores)
    # Determine emotion based on scores
    if scores['compound'] >= 0.5:
        emotion = "Joy"
    elif scores["compound"] <= -0.5:
        emotion = "Sadness"
    elif scores["neg"] > 0.5:
        emotion = "Anger"
    elif scores["neu"] > 0.5:
        emotion = 'Neutral'
    else:
        emotion = "Mixed emotion"
    return emotion
# Detect and print the emotion
emotion = detect_emotion(text)
print("Detected Emotion: ",emotion)