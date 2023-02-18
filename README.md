# COMAP

This repository contains the code and data (both raw and cleaned) used by {TEAM NUMBER} to determine and test a mathematical model to:

- Predict the number of submissions for a Wordle daily word problem on March 1, 2023.
- Predict a distribution curve for the required number of guesses to correctly solve a Wordle problem based on a random 5 letter word
- Determine the "difficulty" of a word based on character occurrences (See PercentOccurrences.txt), repeated letters, as well as a few other useful metrics.

# What to Expect:

Inside the Programs folder all of the programs used to clean data, process data, and to revisualize data were placed here. Inside the programs folder are a classes folder, containing a few classes used to make the code more readable; a CSV folder, for hiding away CSV files that are being read from and written to; and lastly a TXT folder for hiding away .txt files that are being written to. 

## File structure (Folders are in Italics)

- *Programs*
  - *classes*
    - Character.py - class for a charater object [holds a value, a count, and a percent occurrence]
    - CSV.py - class for CSV reading primarily used for easily accessing the clean Wordle data to the rest of the code
    - Functions.py - class to hold the equations for 3 different curves used to determine a curve to predict the number of responses submitted on March 1, 2023 (see Mathematical Model Goal 1)
    - Word.py - class for a word object of 5 letters [contains methods for determining repeated characters, solve difficulty, presence of double letters]
  - *CSV*
    - Assorted .csv files
  - *TXT*
    - Assorted .txt files
  - CharOccurence.py - program to determine the percent occurrence of each character through all of the Wordle words of the day in the given data set
  - ExpRegression.py - program to perform exponential regression on the data in order to determine a curve to predict the number of responses submitted on March 1, 2023 (see Mathematical Model Goal 1)
  - WordleMain.py - the main program. when run, all other programs are called and run in order for an outside user to easily run written code
