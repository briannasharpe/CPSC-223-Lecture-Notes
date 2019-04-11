#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:08:30 2019

@author: heroname
"""

"""
Person
<--- First Name     Last Name     SSN
     --------------------------------
                 |             |     
                 |             |     
                 |             |     
                 |             |     
                 |             |     
     --------------------------------
1. read each record from Person table
2. check the condition on the record

SQL
1. insert
2. select
3. update
4. delete
"""

import sqlite3

# sqlite connection object
conn = sqlite3.connect('test_db_4-8.db', isolation_level=None)

# do things
# get cursor object from connection object
cur = conn.cursor()

cur.execute('DROP TABLE Person')
cur.execute('CREATE TABLE Person (firstName varchar(15), lastName varchar(10), SSN int)')

cur.execute('INSERT INTO Person VALUES ("Amy", "Chen", 12345678)')

cur.execute('SELECT * from Person')
data = cur.fetchall()
print(data)

cur.execute('UPDATE Person Set SSN = 4637869 WHERE firstName = "Amy"')
cur.execute('DELETE FROM Person')

#conn.commit() # database will make sure all changes are in the database from previous commit to current commit

# close the database
conn.close()