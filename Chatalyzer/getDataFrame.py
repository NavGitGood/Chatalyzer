import pandas as pd
from whatsapp_helpers.parser import parse
from constants import discrete_columns, continuous_columns

data = parse()

def getDataFrame():
    df = pd.DataFrame(data, columns=discrete_columns)
    return df

def getNullAuthorDataFrame():
    df = getDataFrame()
    null_authors_df = df[df['Author'].isnull()]
    return null_authors_df

def getMediaDataFrame():
    df = getDataFrame()
    media_messages_df = df[df['Message'] == '<Media omitted>']
    return media_messages_df

def getCleanedDataFrame():
    df = getDataFrame()
    null_authors_df = getNullAuthorDataFrame()
    media_messages_df = getMediaDataFrame()
    messages_df = df.drop(null_authors_df.index) # Drops all rows of the data frame containing messages from null authors
    messages_df = messages_df.drop(media_messages_df.index) # Drops all rows of the data frame containing media messages
    return messages_df

def getAugmentedDataFrame():
    df = getCleanedDataFrame()
    df['Word_Count'] = df['Message'].apply(lambda s : len(s.split(' ')))
    df['Letter_Count'] = df['Message'].apply(lambda s : len(s))
    df['Hour'] = df['Time'].apply(lambda x : x.split(':')[0]) # The first token of a value in the Time Column contains the hour (Eg., "20" in "20:15")
    return df

def wordCountByAuthor():
    df = getAugmentedDataFrame()
    return df[['Author', 'Word_Count']].groupby('Author').sum()

def letterCountByAuthor():
    df = getAugmentedDataFrame()
    return df[['Author', 'Letter_Count']].groupby('Author').sum()

