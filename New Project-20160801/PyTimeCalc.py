import csv
import os
import shutil

files = list(os.listdir())
for file in files:
    print(file)

exampleFile = open('14PP.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
for row in exampleData:
    print(row[0],row[3])
