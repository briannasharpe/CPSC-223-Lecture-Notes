#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:14:13 2019

@author: heroname
"""

var = 'test string 1'
var_list = list(var)
print(id(var_list), type(var_list), var_list)

# iterating
var_list = list()
it_obj = iter(var)
next_element = next(it_obj)
var_list.append(next_element)
next_element = next(it_obj)
var_list.append(next_element)
print(id(var_list), type(var_list), var_list)

cnt = len(var)
idx = 0
var_list = list()
while idx < cnt:
    var_list.append(var[idx])
    idx += 1
print(id(var_list), type(var_list), var_list)
"""
var_list = list()
it_obj = iter(var)
while True:
    next_element = next(it_obj)
    var_list.append(next_element)
print(id(var_list), type(var_list), var_list)

var_list = list()
it_obj = iter(var)
next_element = next(it_obj, None)
while next_element != None:
    var_list.append(next_element)
    next_element = next(it_obj, None)
print(id(var_list), type(var_list), var_list)
"""

# dict
var = {'key_1':1, 'key_2':2}
print(id(var), type(var), var)

var = dict(key_1=1, key_2=2)
print(id(var), type(var), var)

var = dict([['key_1',1], ['key_2',2]])
print(id(var), type(var), var)