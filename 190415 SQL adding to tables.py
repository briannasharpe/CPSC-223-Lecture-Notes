#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:02:20 2019

@author: heroname
"""

"""
Relationship
1. 1-1 (spouse)
2. 1-m (ownership, person-car)
3. m-m (person-school attendance)

[person]
  |     \ owns
  |      [car]
[school]
"""

import sqlite3

class Car:
    def __init__(self, m=None, v=None):
        self._make = m
        self._vin = v
        
class School:
    def __init__(self, n=None, sid=None):
        self._name = n
        self._sId = sid
        self._persons = []
        
    def create(n, sId):
        conn = sqlite3.connect('190415.db', isolation_level=None)
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO School VALUES ("{0}", {1})'.format(n, sId)
        cur.execute(sqlStmt)
        cur.close()
        
        """
        1. create a [school] table with 2 columns: school name, school id
        2. create [school attendance] table with 2 columns: SSN, school id
        
        Create table Person (firstName varchar(10), lastName varchar(10), SSN int)
        CREATE TABLE School (schoolName varchar(15), schoolID int)
        Create table SchoolAttendance (SSN int, schoolID int)
        """
class Person:
    def __init__(self, fn=None, ln=None, ssn=None):
        self._firstName = fn
        self._lastName = ln
        self._SSN = ssn
        self._cars = []
        self._schools = []
    
    def create(fn, ln, ssn): 
        # insert one record into databse
        conn = sqlite3.connect('190415.db', isolation_level=None)
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO Person VALUES ("{0}", "{1}", {2})'.format(fn, ln, ssn)
        cur.execute(sqlStmt)
        cur.close()
        # return person object
        pObj = Person(fn, ln, ssn)
        return pObj
        
    def searchPersonObjects(cond=None):
        conn = sqlite3.connect('190415.db')
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
        conn = sqlite3.connect('190415.db')
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO Car VALUES("{0}", "{1}", {2})'.format(cObj._make, cObj._vin, self._SSN)
        cur.execute(sqlStmt)
        conn.commit()
        conn.close()
        
    def addSchool(self, sObj):
        self._schools.append(sObj)
        sObj._persons.append(self)
        conn = sqlite3.connect('190415.db')
        cur = conn.cursor()
        sqlStmt = 'INSERT INTO School VALUES("{0}", {1})'.format(sObj._name, sObj._sId)
        cur.execute(sqlStmt)
        sqlStmt = 'INSERT INTO SchoolAttendance VALUES({0}, {1})'.format(self._SSN, sObj._sId)
        cur.execute(sqlStmt)
        conn.commit()
        conn.close()

p1Obj = Person.create("b", "b", 123456)
p2Obj = Person.create("c", "p", 654321)
p3Obj = Person.create("j", "k", 207520)
s1Obj = School.create("CBX", 41026)
s2Obj = School.create("SKY", 23946)
s3Obj = School.create("DLS", 59798)
p1Obj.addSchool(s1Obj)
p2Obj.addSchool(s2Obj)
p3Obj.addSchool(s1Obj)