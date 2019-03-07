#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:09:47 2019

@author: heroname
"""

var = [2,4,6,6]
it_obj = iter(var)
n_e = next (it_obj)
print(id(n_e), n_e)

var = list()
var.append('v1')
var.append('v2')
print(id(var), type(var), var)

iVar = input('Please enter number : \n')

var = (2,5,7,4)
# var[2] = 'upd'

var = '''abcd
efg
hij'''
print(id(var), type(var), var)