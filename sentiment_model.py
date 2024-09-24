from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    return classifier(text)