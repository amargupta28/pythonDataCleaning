import pandas as pd
import numpy as np

#Reading Excel file, one can read csv file as well.  Pandas has many inbuilt functions. https://pandas.pydata.org/docs/user_guide/index.html
fileRead = pd.read_excel('Coaches.xlsx')
print (fileRead)

#Just check the data for starting 5 rows.

print(fileRead.head())

#checking for null Data in row column format. If data exist in a cell it will state false and if null data then true. 

print(fileRead.isnull())
print(fileRead.isnull().sum())