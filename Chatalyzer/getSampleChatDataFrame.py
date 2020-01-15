import pandas as pd
from sample_chat_helpers.parser import parse
from constants import sample_discrete_columns, sample_continuous_columns

data = parse()

def getDataFrame():
    df = pd.DataFrame(data, columns=sample_discrete_columns)
    return df

def getAugmentedDataFrame():
    df = getDataFrame()
    df['Word_Count'] = df['Message'].apply(lambda s : len(s.split(' ')))
    df['Letter_Count'] = df['Message'].apply(lambda s : len(s))
    return df

def wordCountByAuthor():
    df = getAugmentedDataFrame()
    return df[['Author', 'Word_Count']].groupby('Author').sum()

def letterCountByAuthor():
    df = getAugmentedDataFrame()
    return df[['Author', 'Letter_Count']].groupby('Author').sum()
