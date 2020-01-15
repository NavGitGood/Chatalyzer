from getDataFrame import getDataFrame, getCleanedDataFrame, getAugmentedDataFrame, wordCountByAuthor, letterCountByAuthor
from actions import getTopAuthorsByMessages, getTopAuthorsByWords, getTopAuthorsByLetters, getFrequencyOfWordCount, getFrequencyOfLetterCount, getMostMessagesByDate, getMostMessagesByTime, getMostMessagesByHour
from constants import discrete_columns, continuous_columns
from sentiment import augmentBySentiment

augmentedDataframe = getAugmentedDataFrame()
sentimentdf = augmentBySentiment(augmentedDataframe)
print(sentimentdf)
total_word_count_grouped_by_author = wordCountByAuthor()
total_letter_count_grouped_by_author = letterCountByAuthor()

getTopAuthorsByMessages(augmentedDataframe, 2)
getTopAuthorsByWords(total_word_count_grouped_by_author, 2)
# getTopAuthorsByLetters(total_letter_count_grouped_by_author, 2)
# getFrequencyOfWordCount(augmentedDataframe, 15)
# getFrequencyOfLetterCount(augmentedDataframe, 15)
# getMostMessagesByDate(augmentedDataframe, 2)
# getMostMessagesByTime(augmentedDataframe, 5)
# getMostMessagesByHour(augmentedDataframe, 5)