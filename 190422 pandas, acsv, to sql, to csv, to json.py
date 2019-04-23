#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:14:45 2019

@author: heroname
"""

"""
output/input    .csv     SQL     JSON

.cs               x       x       .
SQL               x       .       .
JSON             (x)     (x)      .




"""

import pandas as pd

data = pd.read_csv('zoo.csv')

print(type(data)) # data frame
print(data.columns)

print('The 3rd column name : ', data.columns[2])

print(data.index) # row id
print('=======')
#print(data) # everything
print('First six rows : ', data.head(6))
print('Last six rows : ', data.last(6))

col_data = data['animal']
print(type(col_data))
print(col_data)

col_data = data[['animal', 'water_need']
print(type(col_data))
print(col_data) # data frame

row_data = data.loc[2, :] # : all columns
print(type(row_data)) # series object
print(row_data)

#row_data = data.loc[3:10, :] #3rd ~ 10th row
row_data = data.loc[3:10, 'animal':'uniq_id'] # 3rd ~ 10th row with specific columns
print(type(row_data)) # data frame
print(row_data)

row_data = data.loc[3:10, 'animal']
print(type(row_data)) # series (row number = index)
print(row_data)

row_data = data_iloc[3:5, 0] # variation of loc
print(type(row_data)) # series
print(row_data)

conn = sqlite3.connect('190410.db')
pd.to_sql('zoo', con=conn, if_exists='replace') # write data to sql

"""
select * from zoo

select * from Person
"""

df = pd_read_sql_query('SELECT * FROM Person', conn)
print (df)

df.to_csv('person.csv') # write to csv file

# write to json file
data.to_json('zoo.json', orient='columns') # by columns [column 1: ["0", 'aaa'],["1", 'bbb']]
data.to_json('zoo.json', orient='records') # by row index (list, each element is a row) 
data.to_json('zoo.json', orient='split') # separates everything [index: [0,1,2,3,4] data: ['aaa',1001,100],['bbb',1002,200]]

df_1 = pd.read_json('zoo.json', orient='split')
print(df_1)

