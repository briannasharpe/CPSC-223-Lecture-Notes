#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:20:06 2019

@author: heroname
"""

"""
print('INPUT NAME')
var = input('Please enter name: ')
print ('Data entered by user: ', var)

print('WHILE LOOP')
no_elements = input('PLease enter the number of elements: ')
no_elements = int(no_elements)
cnt = 0
list_obj = list()

while cnt < no_elements:
    e = input('Please enter the value of the element: ')
    list_obj.append(int(e))
    cnt += 1

print(list_obj)

print('BUILD YOUR OWN')
no_elements = input('PLease enter the number of elements: ')
no_elements = int(no_elements)
cnt = 0
list_obj = list()

while cnt < no_elements:
    t = input('Please enter the type of the element: ')
    t = int(t)
    e = input('Please enter the value of the element: ')
    if t == 1:
        list_obj.append(int(e))
    else:
        list_obj.append(e)
    cnt += 1

print(list_obj)
"""

#Access a single element of a sequence object (indexing)
orig_list = [4,5,1,2,7,9,4]
working_list = orig_list.copy()
e = working_list[4]
print('Accessing single element : ', e)

working_list = orig_list.copy()
print('Accessing single element before pop: ', working_list)
e = working_list.pop() #e = working_list.pop(3)
print('Accessing single element after pop: ', working_list)
print('Accessing single element via pop: ', e)

#Slicing (Consecutive multiple elements)
working_list = orig_list.copy()
e = working_list[2:5]
print('Accessing multiple elements via slicing : ', e)

working_list = orig_list.copy()
del working_list[3]

# find all odd numbers from the list
working_list = orig_list.copy()
size = len(working_list)
cnt = 0
out_list = list()
while cnt < size:
    e = working_list[cnt]
    if e % 2 != 0:
        out_list.append(e)
    cnt += 1
print(out_list)

working_list = orig_list.copy()
it = iter(working_list)
e = next(it, None)
while e != None:
    if e%2 != 0:
        out_list.append(e)
    e = next(it, None)
print(out_list)

working_list = orig_list.copy()
out_list = list()
for e in working_list:
    if e%2 != 0:
            out_list.append(e)
print(out_list)

# List Comprehension
working_list = orig_list.copy()
out_list = [e for e in working_list if e%2!=0] #one line of code compresses the above
print(out_list)

dict_obj = {'k1':1, 'k2':2}
it = iter(dict_obj)
e = next(it, None)
print(e) #default puts the iterator on the keys

# Dictionary views
it = iter(dict_obj.items())
e = next(it, None)
print(e)

it = iter(dict_obj.keys())
e = next(it, None)
print(e)

it = iter(dict_obj.values())
e = next(it, None)
print(e)

dict_obj = dict()
#if already a list obj> append to the list
#if no list > create an empty list for that keys
#v = dict_obj['k1']
v= dict_obj.get('k1', [])
print(dict_obj)
