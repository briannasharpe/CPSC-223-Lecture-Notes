#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:08:37 2019

@author: heroname
"""

# map() function
orig_list = [3, 4, 6, 1, 9]

# list comprehension
output_list = [e ** 2 for e in orig_list]
print(output_list)

"""
# define function
pass function to map function
for each of the element in orig_list, map will call sq_func
"""

# using map
def sq_func(e):
    return e**2
output_list = map(sq_func, orig_list)
print(output_list)
for e in output_list:
    print(e)

"""
===============================================================================
"""
print("==================================================")

# filter() function
output_list = filter(lambda x: x%2==0, orig_list)
print(output_list)
for e in output_list:
    print(e) 

print("==================================================")

# reduce() function
sum_obj = 0
for e in orig_list:
    sum_obj += e
print(sum_obj)

from functools import reduce

#def sum_func(x, y):
#    return x+y
#output_list = reduce(sum_func, orig_list)
output_list = reduce(lambda x, y: x+y, orig_list)
print(output_list)

print("==================================================")

# everythin is public, no private in python

class testCls:
    
    attrib2 = 0
    
    def test_method1():
        pass
    
    def __init__(self, p=1): #def __init__(self, *params): ------ python does not allow overloading
        self._attrib1 = p
    
    def test_method(self): # self (keyword) refers to the object (incident level)
        self._attrib1 += 2
        testCls.attrib2 += 5
        
      
    def getAttrib1(self):
        return self._attrib1

    def setAttrib1(self, val):
        self._attrib1 = val

    a1 = property(getAttrib1, setAttrib1)

test_obj1 = testCls(1)
test_obj1.test_method() # call method to use .attrib1
print(test_obj1.attrib1, test_obj1.attrib2)
# > print(test_obj1.a1, test_obj1.attrib2)
test_obj1.a1 = testCls(2)

test_obj2 = testCls(2)
test_obj2.test_method()
print(test_obj2.attrib1, test_obj1.attrib1, test_obj1.attrib2)

#test_obj.test_method()
#print(test_obj.attrib1)

