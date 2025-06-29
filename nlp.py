from textblob import TextBlob

print(" Welcome to the Sentiment Analyzer!")
print("Type a sentence to analyze its sentiment.")
print("Type 'exit' to quit.\n")

while True:
    text = input(" Your sentence: ")
    
    if text.lower() == 'exit':
        print(" Exiting. Goodbye!")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = " Positive"
    elif polarity < 0:
        sentiment = " Negative"
    else:
        sentiment = " Neutral"

    print(f"➡️ Sentiment: {sentiment} (Score: {polarity:.2f})\n")
