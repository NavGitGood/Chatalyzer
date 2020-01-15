from .dataframe_metrics import getDataFrame, getWordCountByAuthor, getLetterCountByAuthor, augmentDataFrameWithSentimentPolarity, augmentDataFrameWithDiscreetSentimentPolarity
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..helper import getColorMap

def messageCountByAuthor(num=None):
    df = getDataFrame()
    author_value_counts = df['Author'].value_counts()
    return author_value_counts.head(num)

def wordCountByAuthor(num=None):
    wordCountByAuthorDF = getWordCountByAuthor()
    wordCountGroupedByAuthor = wordCountByAuthorDF.sort_values('Word_Count', ascending=False)
    return wordCountGroupedByAuthor.head(num)

def letterCountByAuthor(num=None):
    letterCountByAuthorDF = getLetterCountByAuthor()
    letterCountGroupedByAuthor = letterCountByAuthorDF.sort_values('Letter_Count', ascending=False)
    return letterCountGroupedByAuthor.head(num)

def sentimentPolarityCountByAuthor():
    df = augmentDataFrameWithSentimentPolarity()
    df = df.groupby(['Author', 'sentiment-polarity'])['Message'].count()
    return pd.DataFrame(df, dtype=np.int8).reset_index()

def discreetSentimentForIndividual(author_name):
    df = augmentDataFrameWithDiscreetSentimentPolarity()
    return df.loc[df['Author'] == author_name]