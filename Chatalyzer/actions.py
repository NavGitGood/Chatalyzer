import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getTopAuthorsByMessages(df, num):
    author_value_counts = df['Author'].value_counts() # Number of messages per author
    top_n_author_value_counts = author_value_counts.head(num) # Number of messages per author for the top 10 most active authors
    # top_n_author_value_counts.plot.pie() # Plot a bar chart using pandas built-in plotting apis
    
    print(top_n_author_value_counts)
    # fig, axes = plt.subplots(1, 2)  # horizontal
    fig, axes = plt.subplots(2)  # vertical
    axes[0].title.set_text('First Plot')
    axes[1].title.set_text('Second Plot')
    plt.gcf().canvas.set_window_title('Analysis Visualization')
    top_n_author_value_counts.plot.pie(ax=axes[0])
    top_n_author_value_counts.plot.pie(ax=axes[1])

    plt.show()

def getTopAuthorsByWords(df, num):
    sorted_total_word_count_grouped_by_author = df.sort_values('Word_Count', ascending=False)
    top_10_sorted_total_word_count_grouped_by_author = sorted_total_word_count_grouped_by_author.head(num)
    top_10_sorted_total_word_count_grouped_by_author.plot.barh()
    plt.xlabel('Number of Words')
    plt.ylabel('Authors')
    plt.title('Authors by Words')
    plt.gcf().canvas.set_window_title('Analysis Visualization')
    plt.show()

def getTopAuthorsByLetters(df, num):
    sorted_total_letter_count_grouped_by_author = df.sort_values('Letter_Count', ascending=False)
    top_n_sorted_total_letter_count_grouped_by_author = sorted_total_letter_count_grouped_by_author.head(num)
    top_n_sorted_total_letter_count_grouped_by_author.plot.barh()
    plt.xlabel('Number of Letters')
    plt.ylabel('Authors')
    plt.title('Authors by Letters')
    plt.gcf().canvas.set_window_title('Analysis Visualization')
    plt.show()

def getFrequencyOfWordCount(df, num):
    plt.figure(figsize=(15, 2)) # To ensure that the bar plot fits in the output cell of a Jupyter notebook
    word_count_value_counts = df['Word_Count'].value_counts()
    top_n_word_count_value_counts = word_count_value_counts.head(num)
    top_n_word_count_value_counts.plot.bar()
    plt.xlabel('Word Count')
    plt.ylabel('Frequency')
    plt.show()

def getFrequencyOfLetterCount(df, num):
    plt.figure(figsize=(15, 2)) # To ensure that the bar plot fits in the output cell of a Jupyter notebook
    letter_count_value_counts = df['Letter_Count'].value_counts()
    top_n_word_count_value_counts = letter_count_value_counts.head(num)
    top_n_word_count_value_counts.plot.bar()
    plt.xlabel('Letter Count')
    plt.ylabel('Frequency')
    plt.show()

def getMostMessagesByDate(df, num):
    df['Date'].value_counts().head(num).plot.barh() # Top 10 Dates on which the most number of messages were sent
    plt.xlabel('Number of Messages')
    plt.ylabel('Date')
    plt.show()

def getMostMessagesByTime(df, num):
    df['Time'].value_counts().head(num).plot.barh() # Top 10 Dates on which the most number of messages were sent
    plt.xlabel('Number of Messages')
    plt.ylabel('Time')
    plt.show()

def getMostMessagesByHour(df, num):
    df['Hour'].value_counts().head(num).sort_index(ascending=False).plot.barh() # Top 10 Dates on which the most number of messages were sent
    plt.xlabel('Number of Messages')
    plt.ylabel('Hour of day')
    plt.show()

def messageSentimentPolarityScatter(df):
    df = df.groupby(['real-sentiment-polarity'])['Message'].count()
    df = pd.DataFrame(df, dtype=np.int8).reset_index()
    print(df)
    df.plot.scatter(x='real-sentiment-polarity', y='Message')
    plt.show()