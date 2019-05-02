#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:03:11 2019

@author: heroname
"""

"""
Customization
1. border (width and size)
2. colors
3. fonts
4. text position

relief = border style
"""

import tkinter as tk
import tkinter.font as tf

def handle_focusIn(event):
    print('Entering the First Name Entry object.')

def handle_focusOut(event):
    print('Exiting the First Name Entry object.')
    # validation logic for First Name
    print('Validating logic for', nameF.get())

win = tk.Tk()

nameF = tk.StringVar()
nameL = tk.StringVar()

f = tf.Font(family='Times', size=36, weight='bold')
f1 = tf.Font(family='Times', size=18)
f2 = tf.Font(family='Times', size=24)

lFirstName = tk.Label(win, text='First Name', bd=4, relief='sunken', bg='yellow', fg='blue', font=f1, anchor='ne') # anchor positions text in cell
lFirstName.grid(column=0, row=0, sticky='wens', pady=(8,4), padx=(8,4)) # sticky follows biggest cell size
eFirstName = tk.Entry(win, textvariable=nameF, bd=4, relief='groove', font=f)
eFirstName.grid(column=1, row=0, sticky='we')

eFirstName.bind('<FocusIn>', handle_focusIn)
eFirstName.bind('<FocusOut>', handle_focusOut)

lLastName = tk.Label(win, text='Last Name', bd=4, relief='raised', bg='red', fg='blue', font=f2)
lLastName.grid(column=0, row=1)
eLastName = tk.Entry(win, textvariable=nameL, bd=4, relief='ridge', font=f)
eLastName.grid(column=1, row=1, sticky='w')

bSubmit = tk.Button(win, text='Submit')
bSubmit.grid(column=1,row=2, sticky='e')

win.columnconfigure(1, weight=1)
win.rowconfigure(0, weight=1)

win.mainloop()