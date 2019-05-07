#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:11:40 2019

@author: heroname
"""

import tkinter as tk

win = tk.Tk()

def toPageA():
    fHome.pack_forget()
    fB.pack_forget()
    fA.pack()

def toPageB():
    fHome.pack_forget()
    fA.pack_forget()
    fB.pack()

def toHome():
    fA.pack_forget()
    fB.pack_forget()
    fHome.pack()

fHome = tk.Frame(win)
bPageA = tk.Button(fHome, text='Page A', command=toPageA)
bPageA.pack()
bPageB = tk.Button(fHome, text='Page B', command=toPageB)
bPageB.pack()

fA = tk.Frame(win)
bHome = tk.Button(fA, text='Back Home', command=toHome)
bHome.pack()

fB = tk.Frame(win)
bHome = tk.Button(fB, text='Back Home', command=toHome)
bHome.pack()

fHome.pack()

win.mainloop()