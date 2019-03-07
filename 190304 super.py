#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:00:01 2019

@author: heroname
"""

'''
Polymorphism
1 Function overloading
2 Operator overloading
3 Method overriding
'''

class A:
    def tMethod(self):
        print('A implementation')

class B(A):
    def tMethod(self):
        super().tMethod()
        print('B implementation')

class C(B):
    def tMethod(self):
        super().tMethod()
        print('C implementation')
        
class D(C):
    def tMethod(self):
        super(C, self).tMethod()
        print('D implementation')

'''
aObj = A()
aObj.tMethod()
'''
aObj = D()
aObj.tMethod()
'''
bObj = B()
bObj.tMethod()
'''

class E:
    def tMethod(self):
        print('E implementation')
        
class F(A,E):
    def tMethod(self):
        super().tMethod()
        print('F implementation')
        
aObj = F()
print(F.__mro__)
aObj.tMethod()