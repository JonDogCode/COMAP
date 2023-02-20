import csv
import math


class Functions:
    def __init__(self, x):
        self.x = int(x)
        self.k = (.00003 * math.pow(self.x, 2)) - (0.0189 * self.x) + 13.25
        self.e = math.e
        self.High = self.UpperBound()
        self.Low = self.LowerBound()
        self.PredictedVal = self.PredictedValue()

    # upper bound
    def UpperBound(self):
        a_High = 380000
        n_High = 0.00135
        lnConst_High = math.log(a_High)
        yint_High = 22000

        exponent_High = n_High * (self.k + (lnConst_High * self.x))

        High = (a_High * math.pow(self.e, - exponent_High)) + yint_High

        return High

    # lower bound
    def LowerBound(self):
        a_Low = 300000
        n_Low = 0.00145
        lnConst_Low = math.log(a_Low)
        yint_Low = 17500

        exponent_Low = n_Low * (self.k + (lnConst_Low * self.x))

        Low = (a_Low * math.pow(self.e, - exponent_Low)) + yint_Low

        return Low

    # the predicted value for the number of Wordle results
    def PredictedValue(self):
        a_Mid = 340000
        n_Mid = 0.00140
        lnConst_Mid = math.log(a_Mid)
        yint_Mid = 19750

        exponent_Mid = n_Mid * (self.k + (lnConst_Mid * self.x))

        Mid = (a_Mid * math.pow(self.e, - exponent_Mid)) + yint_Mid

        return Mid

    def GetHighVal(self):
        return self.High

    def GetLowVal(self):
        return self.Low

    def GetPredictedVal(self):
        return self.PredictedVal


def GraphTest():  # Print a CSV object to the console for use in Excel
    filename = "../CSV/DataTest.csv"

    valList = []

    with open(filename, encoding="utf-8-sig") as wordle:
        dataList = list(csv.reader(wordle))

        for row in dataList:
            r = row[0]
            val = Functions(row[0])
            valList.append(val)

    i = 0
    for V in valList:
        print(str(i) + ", " + str(V.PredictedValue()) + ", " + str(V.UpperBound()) + ", " + str(V.LowerBound()))
        i = i + 1


dataPoint = int(input())

result = Functions(dataPoint)

p = result.GetPredictedVal()
l = result.GetLowVal()
h = result.GetHighVal()

print("Predicted Value: " + str(p))
print("Lower Bound: " + str(l))
print("Upper Bound: " + str(h))

avg = (h + l) / 2
plus = h - avg
minus = l - avg
pm = (plus + minus) / 2.0

print("Plus: " + str(plus) + "   Minus: " + str(minus) + "     PM: " + str(pm))

print ("Average of Upper and Lower Bounds: " + str(avg))
print("PlusMinus val: " + str(pm))

