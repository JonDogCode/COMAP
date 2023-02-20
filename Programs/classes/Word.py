import math
from Programs.classes.Rubric import Rubric
from Programs.classes.WordAPI import WordAPI


class Word:
    def __init__(self, string, rubric):
        self.value = string
        self.rubric = rubric
        self.charArr = self.CharArr()
        self.repeatedLetters = self.RepeatedLetters()
        self.commonPhonics = self.CommonPhonics()

        wordAPI = WordAPI()
        self.freq = math.log(WordAPI.GetFrequency(wordAPI, self.value) + 1, 10) / 7.0
        self.score = self.GetScore()

        if self.repeatedLetters != 0:
            self.doubleLetters = self.DoubleLetters()
        else:
            self.doubleLetters = 0

    def CharArr(self):
        charArr = []
        for char in self.value:
            charArr.append(char)
        return charArr

    def RepeatedLetters(self):

        charSet = set(self.value)
        dictionary = {char: 0 for char in charSet}

        for char in self.value:
            dictionary[char] += 1

        summ = 0
        for char in dictionary:
            if dictionary[char] == 1:
                dictionary[char] -= 1
            summ += dictionary[char]
        if summ == 4:
            summ = 3
        return summ

    def DoubleLetters(self):
        charA, charB = '', ''
        dLCount = 0
        i = 0

        while i < len(self.value):
            if i != 0:
                charB = charA
                charA = self.charArr[i]
                if charA == charB:
                    dLCount = dLCount + 1


            else:
                charA = self.charArr[i]
            i = i + 1

        return dLCount

    def CommonPhonics(self):
        totalMultiplier = 1.0
        b = self.value[1]
        a = self.value[0]
        i = 0

        while i < 4:
            if a + b in self.rubric.sclrDict.keys():
                totalMultiplier *= self.rubric.sclrDict[a + b]
            b = self.value[1 + i]
            a = self.value[i]
            i += 1

        return totalMultiplier

    # def WordFrequency(self):

    def GetScore(self):
        score = 0
        for char in self.value:
            score = score + self.rubric.charValArr[(ord(char) - 97)][1]

        score *= self.commonPhonics

        if self.repeatedLetters != 0:
            power = math.pow(2, self.repeatedLetters - 1)
            score = math.pow(score, power)

        score /= self.freq

        return int(score)

    def GetData(self):
        print("Chosen Word is: " + str(self.value))
        print("Repeated Letters: " + str(self.repeatedLetters))
        print("Double Letters: " + str(self.doubleLetters))
        print("Phonics: " + str(self.commonPhonics))
        print("Word Frequency: " + str(self.freq))
        print("Score: " + str(self.score))


s = "C:\\Users\\silas\\Desktop\\COMAP\\Programs\\CSV\\WordGrading\\scalarValues.csv"

c = "C:\\Users\\silas\\Desktop\\COMAP\\Programs\\CSV\\WordGrading\\charVals.csv"

R = Rubric(c, s)

word = Word("scour", R)


word.GetData()
