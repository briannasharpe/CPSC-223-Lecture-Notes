#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:24:54 2019

@author: heroname
"""

'''
MODULES
'''
import cmodule as cm
from cmodule import testFunc

import sys # system library, system module

print(sys.path)


#import module.cmodule as cm
# module.cmodule.testunc()

cm.testFunc()

testObj = cm.TestCls()

testFunc()
