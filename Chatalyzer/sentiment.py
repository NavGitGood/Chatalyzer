from textblob import TextBlob

def calculateSentimentPolarity(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def calculateRealSentimentPolarity(msg):
    analysis = TextBlob(msg)
    return round(analysis.sentiment.polarity, 3)

def augmentBySentimentPolarity(df):
    df['sentiment-polarity'] = df['Message'].apply(lambda s: calculateSentimentPolarity(s))
    return df

def augmentByRealSentimentPolarity(df):
    df['real-sentiment-polarity'] = df['Message'].apply(lambda s: calculateRealSentimentPolarity(s))
    return df

def calculateSentimentSubjectivity(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.subjectivity > 0.5:
        return 'Subjective'
    elif analysis.sentiment.subjectivity == 0.5:
        return 'neutral'
    else:
        return 'Objective'

def calculateRealSentimentSubjectivity(msg):
    analysis = TextBlob(msg)
    return analysis.sentiment.subjectivity

def augmentBySentimentSubjectivity(df):
    df['sentiment-subjectivity'] = df['Message'].apply(lambda s: calculateSentimentSubjectivity(s))
    return df

def augmentByRealSentimentSubjectivity(df):
    df['real-sentiment-subjectivity'] = df['Message'].apply(lambda s: calculateRealSentimentSubjectivity(s))
    return df

