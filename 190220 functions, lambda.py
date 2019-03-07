#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:00:25 2019

@author: heroname
"""

"""
def test_func(p1, p2):
    x = p1 + p2
    print('x : ', x)
"""

def test_func(p1, p2=7):
    print(locals())
    print('Reference : ', locals()['p2'])
    x = p1 + p2
    print(locals())
    print('p1 : ', p1, ' p2 : ', p2)
    print('x : ', x)

test_func(2, 3)

#test_func(3)

test_func(p2=10, p1=4)

# Passing unknown number of parameters

"""
def test_func1(*params):
    for p in params:
        print('Next parameter : ', p)
"""

def test_func1(*params):
    print(locals())
    for p in params:
        print('Next parameter : ', p)
     
test_func1(3,2)

# keyword parameter
def test_func2(**params):
    print(locals())
    
test_func2(p2=3,p5=2)

def test_func3(p1,p2):
    x = p1 + p2
    return x, p1 #return multiple values

r1, r2 = test_func3(1,5)
print('r : ', r1, r2)

# variable scope

def test_func1():
    global x
    x = 'Changed value.'
    print('x inside function : ', x)

x = 'Init value'
print('x before calling the function : ', x)
test_func1()
print('x after calling the function : ', x)

# Call it by value or call it by reference
def test_func5(p):
    if type(p) == int:
        p = p + 1
    else:
        p.append('new string')
"""
v = 3
print('v before calling : ', v)
test_func5(v)
print('v after calling : ', v)
"""
v = [1,2,3]
print('v before calling : ', v)
test_func5(v)
print('v after calling : ', v)

# Anonymous (Lambda) functions
def test_cond(e):
    return e%2 == 0
"""
    if e%2 == 0:
        return True
    else:
        return False
"""

print(test_cond(567))

print((lambda e: e%2 == 0)(567))

print((lambda x,y: x+y)(1,4))

# function object

print(id(test_cond), type(test_cond))
f_obj = test_cond
print('1002 : ', f_obj(1002))

def nested_func(f):
    print('Calling function f ')
    print(f(2003))

nested_func(test_cond)

# Callback function
l_obj = [4,5,1,3,8,2]
print('List before the sorting : ', l_obj)
l_obj.sort(reverse=True)
print('List before the sorting : ', l_obj)

def comp_key(e):
    return e['k1']

l_obj = [{'k1':3, 'k2':1}, {'k1':1, 'k2':5}, {'k1':7, 'k2':1}, {'k1':4, 'k2':1}]
print('List before the sorting : ', l_obj)
l_obj.sort(key=comp_key) #(key=lambda e: e)
print('List after the sorting : ', l_obj)

def sort(obj, key):
    for e in obj:
        val = key(e)
        print(val)

sort(l_obj, comp_key)