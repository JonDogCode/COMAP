from classes.CSV import *
from classes.Character import *


print("Welcome to Wordle Probability Simulator\n\n")

filename = "CSV/WordleData.csv"

WordleData = WORDLEDATA(filename)

print(WordleData.string)

i = 0
charList = []

while i < 26:
    C = character(chr(i + 97), 0, 0)
    charList.append(C)
    i = i + 1

a = 0
i = 0
for char in WordleData.string:
    a = ord(char) - 97
    print(str(a) + "  " + str(i))
    charList[a].count = charList[a].count + 1
    i = i + 1

percentList = []
for C in charList:
    C.percent = C.count / WordleData.strLen * 100

for C in charList:
    print(str(C.count) + " occurrences of " + str(C.char) + "\t---------------\t" + str(C.percent) + "%")
    percentList.append([C.char, C.percent])


def CharSort(l):
    return l[1]


percentList.sort(key=CharSort, reverse=True)

for L in percentList:
    print(str(L[0]) + "\t------------------\t" + str(L[1]))
