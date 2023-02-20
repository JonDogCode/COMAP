import csv

class Rubric:
    def __init__(self, CharFilename, ScalarFilename):
        self.cFile = CharFilename
        self.sFile = ScalarFilename
        self.charValArr = self.GetCharValArr()
        self.sclrArr = self.GetComboSclrArr()
        self.sclrDict = self.GetComboSclrDict()

    def GetCharValArr(self):
        with open(self.cFile, encoding="utf-8-sig") as rubric:
            charValArr = list(csv.reader(rubric))

        for N in charValArr:
            N[1] = int(N[1])
        return charValArr

    def GetComboSclrArr(self):
        with open(self.sFile, encoding="utf-8-sig") as rubric:
            sclrArr = list(csv.reader(rubric))

        returnArr = []
        i = 0
        for N in sclrArr:
            N[1] = float(N[1])
            N[2] = int(N[2])
            returnArr.append([N[0], N[1]])
        return returnArr

    def GetComboSclrDict(self):
        cSDict = {str(sclr[0]): sclr[1] for sclr in self.sclrArr}

        return cSDict







s = "C:\\Users\\silas\\Desktop\\COMAP\\Programs\\CSV\\WordGrading\\scalarValues.csv"

c = "C:\\Users\\silas\\Desktop\\COMAP\\Programs\\CSV\\WordGrading\\charVals.csv"

R = Rubric(c, s)



