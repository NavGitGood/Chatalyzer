from .filter import startsWithAuthor, startsWithDate
from .dataPoint import getDataPoint

parsedData = [] # List to keep track of data so it can be used by a Pandas dataframe
conversationPath = './data/_chat.txt'

def parse():
    # print("inside parse")
    with open(conversationPath, encoding="utf-8") as fp:
        # print("inside open")
        fp.readline() # Skipping first line of the file (usually contains information about end-to-end encryption)
        # print(fp.readline())
        # print(fp.readline())
        messageBuffer = [] # Buffer to capture intermediate output for multi-line messages
        date, time, author = None, None, None # Intermediate variables to keep track of the current message being processed
        
        while True:
            # print("inside whle true")
            line = fp.readline()
            # print(line)
            if not line: # Stop reading further if end of file has been reached
                # print("no line")
                # print(parsedData)
                return parsedData
                break
            line = line.strip() # Guarding against erroneous leading and trailing whitespaces
            if startsWithDate(line): # If a line starts with a Date Time pattern, then this indicates the beginning of a new message
                if len(messageBuffer) > 0: # Check if the message buffer contains characters from previous iterations
                    parsedData.append([date, time, author, ' '.join(messageBuffer)]) # Save the tokens from the previous message in parsedData
                messageBuffer.clear() # Clear the message buffer so that it can be used for the next message
                date, time, author, message = getDataPoint(line) # Identify and extract tokens from the line
                messageBuffer.append(message) # Append message to buffer
            else:
                messageBuffer.append(line) # If a line doesn't start with a Date Time pattern, then it is part of a multi-line message. So, just append to buffer