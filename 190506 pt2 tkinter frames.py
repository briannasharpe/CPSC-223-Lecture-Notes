#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:52:34 2019

@author: heroname
"""

import tkinter as tk

win = tk.Tk()

f1 = tk.Frame(win, bd=2, relief='sunken', bg='yellow')
lL1 = tk.Label(f1, text='L-1')
lL1.pack(side=tk.LEFT)
lL2 = tk.Label(f1, text='L-2')
lL2.pack(side=tk.TOP, anchor='w', expand=True, fill=tk.BOTH)
#f1.pack(side=tk.TOP)
f1.grid(column=0, row=0) #does not move as a grid

f2 = tk.Frame(win, bd=2, relief='sunken')
lL3 = tk.Label(f2, text='L-3')
lL3.pack(side=tk.LEFT)
lL4 = tk.Label(f2, text='L-4')
lL4.pack(side=tk.TOP)
#f2.pack(side=tk.TOP)
f2.grid(column=0, row=1)

win.mainloop()