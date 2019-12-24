import pandas as pd
from helpers.parser import parse

data = parse()

def printTable():
    df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])
    return df
