from textblob import TextBlob

def calculateSentiment(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def augmentBySentiment(df):
    df['sentiment'] = df['Message'].apply(lambda s: calculateSentiment(s))
    return df