#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:27:55 2019

@author: heroname
"""

"""
2nd gen of data science
UW Application - underwriter 
Claim Application - adjustors
Billing Application - billing stack
OLAP - On-line Analytical Processing


UW db         Chain db       Billing db   
||               ||             ||
----------------------------------------
|               OLAP db                |
----------------------------------------

3rd gen
Data Science Life Cycle
1. Data Collection
2. Data Preparation
3. Data Analysis
4. Reporting
"""

import pandas as pd
import sqlite3

person_data = {'firstName':['John', 'Amy'], 'lastName':['Chen', 'Sampson'], 'SSN':[1234,5678]}
df = pd.DataFrame(person_data)
print(df)

con = sqlite3.connect('190410.db')
data = pd.read_sql_query('SELECT * FROM Person', con)
print(data)

"""
to 190410.db

insert into Person VALUES ('John', 'Chen', 123)
insert into Person VALUES ('James', 'Chang', 356)
insert into Person VALUES ('Amy', 'Sampson', 357)
"""

cols = data['lastName']
print(type(cols))
print(cols)

cols = data[['firstName', 'lastName']]
print(type(cols))
print(cols)

j_obj = data.to_json(orient='columns') # pass columns for json object to list data by columns
print(j_obj)

