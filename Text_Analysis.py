import spacy
from textblob import TextBlob
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(response):
    blob = TextBlob(response)
    sentiment_score = blob.sentiment.polarity
    print(f"Sentiment Score - {round(sentiment_score,2)}")
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

def extract_key_phrases(response):
    doc = nlp(response)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

def quality_assessment(sentiment, key_phrases):
    if sentiment == "Positive" and len(key_phrases) > 3:
        return "High Quality"
    elif sentiment == "Neutral" and len(key_phrases) > 2:
        return "Medium Quality"
    else:
        return "Low Quality"

def analyze_responses(file_path):
    df = pd.read_csv(file_path)
    
    results = []
    for response in df['response']:
        if response.strip():
            sentiment = analyze_sentiment(response)
            key_phrases = extract_key_phrases(response)
            quality = quality_assessment(sentiment, key_phrases)
            results.append({
                "response": response.strip(),
                "sentiment": sentiment,
                "key_phrases": key_phrases,
                "quality_assessment": quality
            })
    
    return results


# Main
results = analyze_responses("interview_responses.csv")

for id, result in enumerate(results, 1):
    print(f"Response {id}:")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Key Phrases: {', '.join(result['key_phrases'])}")
    print(f"Quality Assessment: {result['quality_assessment']}")
    print("\n")