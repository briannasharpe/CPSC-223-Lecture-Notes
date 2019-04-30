#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:04:18 2019

@author: heroname
"""

"""
Python GUI Programming
Tkinter library

Label
First Name
[                ] Widget

Layout Management
- pack       pack widgets on top of another (default)
- grid
- place
"""

import tkinter as tk

win = tk.Tk()

def addPerson():
    name = fName.get()
    print('FirstName entered: ', name)
    return

fName = tk.StringVar()

frmData = tk.Frame(win)
frmCmd = tk.Frame(win)

# side options : TOP, LEFT, RIGHT, BOTTOM
# win -> frmData, last win -> frmCmd
FirstName = tk.Label(frmData, text='First Name', bg='red') #who u want the widget attached to
FirstName.pack(side=tk.TOP, anchor='w', expand=True, fill=tk.BOTH)

eFirstName = tk.Entry(frmData, textvariable=fName, bg='green')
eFirstName.pack(side=tk.TOP, anchor='w', expand=True, fill=tk.BOTH)

bSubmit = tk.Button(frmCmd, text='Submit', bg='blue', command=addPerson)
bSubmit.pack(side=tk.BOTTOM, anchor='e')

frmData.pack(side=tk.LEFT, anchor='nw', expand=True, fill=tk.X)
frmCmd.pack(side=tk.BOTTOM)

win.mainloop()

