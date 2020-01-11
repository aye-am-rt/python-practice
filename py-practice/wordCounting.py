import os
import re
import string
import sys


def read_and_analyze():
    try:
        lineList = []
        f = open('words.txt')
        line = f.readline()
        while line:
            line = line.strip('\n')
            if len(str(line)) >= 1:
                lineList.append(line)
            line = f.readline()
        f.close()
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data. ")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    print("*******************************************")
    allWords = []
    counterDictionary = {}

    for eachLine in lineList:
        wordsListOfaLine = re.sub('[' + string.punctuation + ']', '', eachLine).split()
        allWords.extend(wordsListOfaLine)

    for word in allWords:
        counterDictionary[word] = counterDictionary.get(word, 0) + 1

    print("\n" + str(counterDictionary))


if __name__ == "__main__":
    print(os.getcwd())
    os.chdir('../FolderOfFile')
    print(os.getcwd())

    read_and_analyze()
