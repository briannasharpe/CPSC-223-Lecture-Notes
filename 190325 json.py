#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:08:07 2019

@author: heroname
"""

import json # javascript object notation

'''
python -----> javascript
----------|-------------
list          | array
dict          | object
string        | string
int           | int
set  ex.{4,5} | (X)      "Object of type 'set' is not JSON serializable"      

set -> list -> js
'''

# json encoding
testObj = [{'k0':{'k11':'r'}, 'k3':5}, 'string_01', 23, 5.6]
outString = json.dumps(testObj, indent=4)
print(outString)

# json decoding
inObj = json.loads(outString)
print(inObj)

#                         hook
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        print('Object to be encoded : ', type(o))
        obj = dict()
        if type(o) == Person:
            obj = o.__dict__
            obj['class'] = 'Person'
            return obj
        if type(o) == Car:
            obj = o.__dict__
            obj['class'] = 'Car'
            return obj

class Car:
    def __init(self, ln):
        self._licenseNo = ln

class Person:
    def __init__(self, fn=None, ln=None):
        self._firstName = fn
        self._lastName = ln
        self._cars = []
        
    def addCar(self, ln):
        self._cars.append(Car(ln))

    def __str__(self):
        return str(self.__dict__) # print content of object
    
    def __repr__(self):
        return str(self.__dict__)

lObj = list()
pObj = Person('John', 'Chen')
pObj.addCar('L123')
pObj.addCar('L234')
lObj.append(pObj)
pObj = Person('Amy', 'Sampson')
pObj.addCar('L675')
lObj.append(pObj)

outString = json.dumps(lObj, cls=CustomEncoder, indent=4)
print(outString)

'''
outString = json.dumps(pObj, cls=CustomEncoder, indent=4)
print(outString)

inObj = json.loads(outString)
# not a person object, needs custom decoder (pytohn dict by default)
print(inObj)
'''

class CustomDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)
        
    # hook for python to call
    def dict_to_object(self, o):
        print('Object to be decoded : ', o)
        obj = None
        if o['class'] == 'Person':
            obj = Person(o['_firstName'], o['_lastName'])
            '''not hard coded
            del o['class']
            obj = Person()
            obj.__dict__ = o
            '''
        return obj

inObj = json.loads(outString, cls=CustomDecoder)
print(inObj)

'''
relationship
    1-1
    1-m
    m-m
'''

























