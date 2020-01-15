from textblob import TextBlob

def calculateRealSentimentPolarity(msg):
    analysis = TextBlob(msg)
    return round(analysis.sentiment.polarity, 2)

def mapSentimentPolarity(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.polarity > 0.6:
        return 'very positive'
    elif 0.20 < analysis.sentiment.polarity <= 0.60:
        return 'positive'
    elif -0.20 <= analysis.sentiment.polarity <= 0.20:
        return 'neutral'
    elif -0.60 <= analysis.sentiment.polarity < -0.20:
        return 'negative'
    elif analysis.sentiment.polarity < -0.60:
        return 'very negative'

def augmentDataFrameWithMappedSentimentPolarity(df):
    df['sentiment-polarity'] = df['Message'].apply(lambda s: mapSentimentPolarity(s))
    return df[['Author', 'sentiment-polarity']].loc[df['Author'] == 'Jane']