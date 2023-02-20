import csv

class WORDLEDATA:
    def __init__(self, data):
        self.data = data
        self.string = self.GetString()
        self.strLen = len(self.string)
        self.strArr = self.GetArr()

    def GetString(self):
        string = ""
        with open(self.data) as wordle:
            dataList = list(csv.reader(wordle))
            for row in dataList:
                if row[2] != "Word":
                    string = string + row[2]

        return string

    def GetArr(self):
        string = ""
        strArr = []
        with open(self.data) as wordle:
            dataList = list(csv.reader(wordle))
            for row in dataList:
                if row[2] != "Word":
                    strArr.append(row[2])
        return strArr
