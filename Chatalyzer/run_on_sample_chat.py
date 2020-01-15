from getSampleChatDataFrame import getDataFrame, getAugmentedDataFrame, wordCountByAuthor, letterCountByAuthor
from actions import getTopAuthorsByMessages, getTopAuthorsByWords, getTopAuthorsByLetters, getFrequencyOfWordCount, getFrequencyOfLetterCount, messageSentimentPolarityScatter
from sentiment import augmentBySentimentPolarity, augmentByRealSentimentPolarity, augmentBySentimentSubjectivity, augmentByRealSentimentSubjectivity
from sentimentCalculator import augmentDataFrameWithMappedSentimentPolarity

augmentedDataframe = getAugmentedDataFrame()


# print(augmentDataFrameWithMappedSentimentPolarity(augmentedDataframe))

# sentimentdf = augmentBySentimentPolarity(augmentedDataframe)
# sentimentdf = augmentByRealSentimentPolarity(sentimentdf)
# sentimentdf = augmentBySentimentSubjectivity(sentimentdf)
# sentimentdf = augmentByRealSentimentSubjectivity(sentimentdf)
# print(sentimentdf)
total_word_count_grouped_by_author = wordCountByAuthor()
# total_letter_count_grouped_by_author = letterCountByAuthor()

# messageSentimentPolarityScatter(sentimentdf)
getTopAuthorsByMessages(augmentedDataframe, 5)
# getTopAuthorsByWords(total_word_count_grouped_by_author, 5)
# getTopAuthorsByLetters(total_letter_count_grouped_by_author, 5)
# getFrequencyOfWordCount(augmentedDataframe, 50)
# getFrequencyOfLetterCount(augmentedDataframe, 50)