from textblob import TextBlob
import pandas as pd
from ..sample_chat_helpers.parser import parse
from ..config.constants import continuous_columns, discrete_columns
import numpy as np

data = parse()

def getDataFrame():
    df = pd.DataFrame(data, columns=discrete_columns)
    return df

def getAugmentedDataFrame():
    df = getDataFrame()
    df[continuous_columns[0]] = df[discrete_columns[1]].apply(lambda msg : len(msg.split(' ')))
    df[continuous_columns[1]] = df[discrete_columns[1]].apply(lambda msg : len(msg))
    return df

def getWordCountByAuthor():
    df = getAugmentedDataFrame()
    df = df[['Author', 'Word_Count']].groupby('Author').sum()
    return df.reset_index()

def getLetterCountByAuthor():
    df = getAugmentedDataFrame()
    df = df[['Author', 'Letter_Count']].groupby('Author').sum()
    return df.reset_index()

# Sentiment Calculation

def calculateSentimentPolarity(msg):
    analysis = TextBlob(msg)
    return round(analysis.sentiment.polarity, 2)    # rounding to 2 decimal places

def calculateDiscreetSentimentPolarity(msg):
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

def augmentDataFrameWithDiscreetSentimentPolarity():
    df = getAugmentedDataFrame()
    df['discreet-sentiment-polarity'] = df['Message'].apply(lambda msg: calculateDiscreetSentimentPolarity(msg))
    return df

def augmentDataFrameWithSentimentPolarity():
    df = getAugmentedDataFrame()
    df['sentiment-polarity'] = df['Message'].apply(lambda msg: calculateSentimentPolarity(msg))
    return df

