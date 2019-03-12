#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:23:36 2019

@author: heroname
"""

class TestCls:
    def __init__(self):
        self._attrib1 = 3
        self._attrib2 = 4

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n == 0:
            val = self._attrib1
        else:
            if self._n == 1:
                val = self._attrib2
            else:
                raise StopIteration
        self._n += 1
        return val

testObj = TestCls()
'''
print(testObj)
it = iter(testObj)
print(next(it))
print(next(it))
print(next(it))
'''

for e in testObj:
    print(e)