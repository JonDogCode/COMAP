import csv
import math

# Cleaned COMAP / NYT Wordle Data
wordleData = "CSV\CleanWordleData.csv"

# Write file
logRegress = "CSV\expRegress.csv"

# Create writer object
with open(logRegress, "w", encoding="utf-8-sig") as logRegress:
    logRegress.truncate()
    writer = csv.writer(logRegress)

    with open(wordleData, encoding="utf-8-sig") as wordle:
        dataList = list(csv.reader(wordle))
        i, j = 0, 0
        for row in dataList:
            logged = math.log(float(row[4]))
            # xlogged = math.log(float(row[0]))

            newRow = [row[0], logged]
            writer.writerow(newRow)
        wordle.close()
    logRegress.close()
