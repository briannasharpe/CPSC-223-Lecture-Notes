#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:25:16 2019

@author: heroname
"""

"""
table

Label | Entry
--------------
      |
      |
      |
"""

import tkinter as tk

win = tk.Tk()

name = tk.StringVar()

lFirstName = tk.Label(win, text='First Name')
lFirstName.grid(column=0, row=0)
eFirstName = tk.Entry(win, textvariable=name)
eFirstName.grid(column=1, row=0)

bSubmit = tk.Button(win, text='Submit')
bSubmit.grid(column=2,row=3)

win.mainloop()