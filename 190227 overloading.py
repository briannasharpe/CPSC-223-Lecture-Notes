#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:09:00 2019

@author: heroname
"""

class testCls:
    def __init__(self, p1, p2):
        self._attrib1 = p1
        self._attrib2 = p2
        
    # overload iter/next with iterable object
    def __iter__(self):
        self._pos = 0
        return self
    
    def __next__(self):
        if self._pos > 1:
            return None
        else:
            if self._pos == 0:
                val = self._attrib1
            else:
                val = self._attrib2
            self._pos += 1
        return val
        
    # built-in function overloading
    def __str__(self):
        return str(self._attrib1) + ', ' + str(self._attrib2)

    # Operator overloading
    # Numerical Operators
    def __add__(self, other):
        sum1 = self._attrib1 + self._attrib1
        sum2 = self._attrib2 + self._attrib2
        return testCls(sum1, sum2)

    # Comparison Operators
    def __gt__(self, other):
        if self._attrib1 > other._attrib1:
            return True
        if self._attrib1 == other._attrib1:
            if self._attrib2 > other._attrib2:
                return True
            else:
                return False
        else:
            return False
        
    # Sequence Operators (indexing, slicing)
    def __getitem__(self, ind):
        if ind == 0:
            return self._attrib1
        else:
            return self._attrib2
        
    # attribute access
    def __getattrib__(self, name):
        if name == "attrib1":
            return self._attrib1
    '''
    def __getattribute__(self, name):
        if name == "attrib1":
            return self._attrib1
    '''
test_obj = testCls(3,2)
print('Overloaded str() function : ', str(test_obj))
print('test_obj : ', test_obj)

test_obj1 = testCls(3,1)
test_obj2 = testCls(11,3)
#17,6
res_obj = test_obj + test_obj1 + test_obj2
print(res_obj)

#res_obj = test_obj.__add__(test_obj)

print(test_obj > test_obj1)

print(test_obj[0])

it = iter(test_obj)
print(next(it))
print(next(it))
print(next(it))

print('__getattrib__() : ', test_obj._attrib1)
print('__getattribute__() : ', test_obj._attrib1)

'''
test_list = list()
test_list.append(test_obj)
test_list.append(test_obj1)
test_list.append(test_obj2)
test_list = sort()
print(test_list)

r_list = test_list.sort()
print(r_list)
'''