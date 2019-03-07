#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:09:28 2019

@author: heroname
"""

"""
# read a file
f = open('students.txt', mode='r')
data = f.read()
print('File content : ', data)
f.close() # resource leak if not closed

# read first line of a file
f = open('students.txt', mode='r')
data = f.readline()
print('File content : ', data)
f.close()

# read all lines of a file and create a list
f = open('students.txt', mode='r')
data = f.readlines()
print('File content : ', data)
f.close()

f = open('students.txt', mode='r')
data = f.read()
print('File content : ', data)
f.close()

# write a file
f = open('output.txt', mode='w')
f.write(data)
f.close()
"""

"""
f = open('students.txt', mode='r')
data = f.read()
print('File content : ', data)
f.close() # resource leak if not closed

# writelines
f = open('output.txt', mode='a')
f.writelines(data)
print('File content : ', data)
f.close()

f = open('students.txt', move='rb')
data = f.readlines()
print('File content : ', data)
f.close()
"""

# specif encoding
f = open('unc.txt', mode = 'w', encoding = 'utf-8')
s = "µÆÑ"
f.write(s)
f.close()

"""
f = open('unc.txt', mode = 'r', encoding = 'utf-16')
bs = f.read()
print('Content : ', bs)
f.close()
"""

"""
f = open('unc.txt', mode = 'rb')
bs = f.read()
print('Encoded bytes string : ', bs)

bs = s.encode('utf-8')
print(bs)
"""

f = open('unc.txt', mode = 'rb')
bs = f.read()
print('Encoded bytes string : ', bs)

# Context Management
# doesn't require f.close (in more complex scenarios)
with open('unc.txt', mode = 'rb') as f:
    bs = f.read()
print('Encoded bytes string with construct : ', bs)

# part of string method
bs = s.encode('utf-8')
print(bs)

"""
OS can only buffer small portions of data in memory
instead of letting OS do io, user tells where to do the buffer/how to do io
"""