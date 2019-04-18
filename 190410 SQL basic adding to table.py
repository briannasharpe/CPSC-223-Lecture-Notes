#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:09:57 2019

@author: heroname
"""

"""
RDBMS Application
1. Design Database Schema
    lay out table
2. Implement Python Classes
"""

import sqlite3

class Car:
    def __init__(self, m=None, v=None):
        self._make = m
        self._vin = v
        
class Person:
    def __init__(self, fn=None, ln=None, ssn=None):
        self._firstName = fn
        self._lastName = ln
        self._SSN = ssn
        self._cars = []
        self._schools = []

    def create(fn, ln, ssn): 
        # insert one record into databse
        conn = sqlite3.connect('test_db_4-10.db', isolation_level=None)
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO Person VALUES ("{0}", "{1}", {2})'.format(fn, ln, ssn)
        cur.execute(sqlStmt)
        cur.close()
        
    def searchPersonObjects(cond=None):
        conn = sqlite3.connect('test_db_4-10.db')
        cur = conn.cursor()
        sqlStmt = 'SELECT * from Person'
        cur.execute(sqlStmt)
        oList = cur.fetchall()
        pList = list()
        for o in oList:
            pObj = Person(o[0], o[1], o[2])
            pList.append(pObj)
        conn.close()
        return pList 
    
    def addCar(self, cObj):
        self._cars.append(cObj)
        conn = sqlite3.connect('test_db_4-10.db')
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO Car VALUES("{0}", "{1}", {2})'.format(cObj._make, cObj._vin, self._SSN)
        cur.execute(sqlStmt)
        conn.commit()
        conn.close()
        
#obj = Person('John', 'Chen', 123)

'''
while true:
    cmd = input('Enter a Command: ')
    if cmd == '1':
'''

pList = Person.searchPersonObjects()
cObj = Car('Ford', 'X123')
pList[0].addCar(cObj)