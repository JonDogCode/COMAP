from Programs.classes.CSV import WORDLEDATA
from Programs.classes.Character import *
filename = "CSV/WordleData.csv"

WordleData = WORDLEDATA(filename)

HeaderString = "Splicing every 5-letter word used as the daily Wordle word of the day \n" \
               "from January 7, 2022, to December 31, 2022, and determining the percent occurrence \n" \
               "of each character gives the following data, with the character 'e' being most \n" \
               "common with a percent occurrence of 10.24% and the character 'j' being the least \n" \
               "common with a percent occurrence of 0.22%. \n" \
               "\n" \
               "This data is used to help determine the difficulty of the Wordle word of the day. \n\n\n"

yehaw = "hi"


def CharSort(l):
    return l[1]


def CharOccurrence(WordleData, filename):
    i = 0
    charList = []

    while i < 26:
        C = character(chr(i + 97), 0, 0)
        charList.append(C)
        i = i + 1

    i = 0
    for char in WordleData.string:
        a = ord(char) - 97
        charList[a].count = charList[a].count + 1
        i = i + 1

    for C in charList:
        C.percent = C.count / WordleData.strLen * 100

    percentList = []
    for C in charList:
        percentList.append([C.char, C.percent])

    percentList.sort(key=CharSort, reverse=True)
    with open(filename, 'w', encoding="utf-8-sig") as file:
        file.write(HeaderString)

        for L in percentList:
            file.write(str(L[0]) + "\t------------------\t" + str(L[1]) + "\n")


CharOccurrence(WordleData, "TXT\PercentOccurrences.txt")
