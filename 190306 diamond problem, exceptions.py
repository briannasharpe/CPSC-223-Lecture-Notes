#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:03:23 2019

@author: heroname
"""

# diamond problem

class A:
    def tMethod(self):
        print('Entering A.tMethod()')
        print('A.tMethod()')
        print('Exiting A.tMethod()')

class B(A):
    def tMethod(self):
        print('Entering B.tMethod()')
        super().tMethod()
        print('B logic')
        print('Exiting B.tMethod()')
        
class C(A):
    def tMethod(self):
        print('Entering C.tMethod()')
        super().tMethod()
        print('C logic')
        print('Exiting C.tMethod()')
        
class D(A):
    def tMethod(self):
        print('Entering D.tMethod()')
        super().tMethod()
        print('D logic')
        print('Exiting D.tMethod()')
    
class E(B,C,D):
    def tMethod(self):
        print('Entering E.tMethod()')
        super().tMethod()
        print('E logic')
        print('Exiting E.tMethod()')
    
print(E.__mro__)
obj = E()
obj.tMethod()    
   
print(obj.__class__) 
print(obj.__class__.__name__)
print(obj.__class__.__bases__)

cObj = obj.__class__.__bases__[0]

print(cObj.__bases__)

# exception
'''

def ReadRecords():
    try:
        f = open(fn, mode='r')
        rList = f.readlines
    except Exception as e:
        raise e
    return rList

except:
    raise CreateObjectsError('FileNotFoundError')

# main program
while aaaaaaaaa
    try:
        if op == '1':
            objList - createObjects()
        else:
            updateObject()
    except:
        print('Exception handled')
'''