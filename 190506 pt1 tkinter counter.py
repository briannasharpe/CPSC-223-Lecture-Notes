#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:09:47 2019

@author: heroname
"""

import tkinter as tk

win = tk.Tk()

nameF = tk.StringVar()
nameL = tk.StringVar()

pCounter = 0

def showCount():
    global pCounter #no local named pCounter so global not needed
    pCounter += 1
    countStr = 'Person Count : ' + str(pCounter)
    lCounter.configure(text=countStr, bg='red')

# frames
f1 = tk.Frame(win)
f2 = tk.Frame(win)
f3 = tk.Frame(win)

lFirstName = tk.Label(win, text='First Name')
lFirstName.grid(column=0, row=0)
eFirstName = tk.Entry(win, textvariable=nameF)
eFirstName.grid(column=1, row=0)
lCounter = tk.Label(win, text='Person Count : 0', bd=2, relief='sunken')
lCounter.grid(column=2, row=0, rowspan=3, sticky='ns')
lLastName = tk.Label(win, text='Last Name')
lLastName.grid(column=0, row=1)
eLastName = tk.Entry(win, textvariable=nameL)
eLastName.grid(column=1, row=1)
bSubmit = tk.Button(win, text='Submit', command=showCount)
bSubmit.grid(column=1, row=2)

win.mainloop()