#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:15:49 2019

@author: heroname
"""

input_string = 'First Name:John,Last Name:Chen'
field_list = input_string.split(',')
print(field_list)

for e in field_list:
    name, value = e.split(':')
    print(name, value)

#String Join
inp_list = ['First Name', 'John']
out_string = ':'.join(inp_list)
print(out_string)

inp_string = '     This is a test string     '
print('inp_string before stripping : ', inp_string)
out_string = inp_string.strip()
print('inp_string after stripping : ', inp_string)
print('inp_string : ', out_string)

#With argument (default truncates spaces)
inp_string = '*****This is a test string*****'
print('inp_string before stripping : ', inp_string)
out_string = inp_string.strip('*')
print('inp_string after stripping : ', inp_string)
print('inp_string : ', out_string)

# Substring matching
inp_string = 'This is an ice cream'
idx = inp_string.index('ice')
print('index() method : ', idx) #12th element bc index starts at 0

'''
idx = inp_string.index('fire')
print('index() method : ', idx) #error
'''

idx = inp_string.find('fire')
print('find() method (no matching) : ', idx) # -1 = couldn't find a match

out_string = inp_string.upper()
print(out_string)

out_string = inp_string.lower()
print(out_string)

frm_string = 'The field name is "{0}" and its value is {1}'
out_string = frm_string.format('First Name', 'John')
print(out_string)
out_string = frm_string.format('Last Name', 'Chen')
print(out_string)

#define field length (right)
frm_string = 'The field name is "{0:>15}" and its value is {1}'
out_string = frm_string.format('First Name', 'John')
print(out_string)

#define field length (left)
frm_string = 'The field name is "{0:<15}" and its value is {1}'
out_string = frm_string.format('First Name', 'John')
print(out_string)

#define field length (both ends)
frm_string = 'The field name is "{0:^15}" and its value is {1}'
out_string = frm_string.format('First Name', 'John')
print(out_string)

#using keywords
#*args, *kwargs
#lists can be passed as keyword/parameter
frm_string = 'The field name is "{p1}" and its value is {p2}'
out_string = frm_string.format(p1='First Name', p2='John')
print(out_string)

# range()
r = range(10)
print(type(r), r)
'''
from e in r:
    print(e)
'''
for e in range(0, 10, 3):
    print(e)





