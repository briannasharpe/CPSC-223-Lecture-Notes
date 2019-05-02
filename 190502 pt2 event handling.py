#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:56:00 2019

@author: heroname
"""

import tkinter as tk

def handle_key_event(event):
    print('User typed the key : ', event.char)

def handle_mouse_event(event):
    print('User click at : ', event.x, event.y)

win = tk.Tk()

win.bind('<Key>', handle_key_event)
win.bind('<Button-1>', handle_mouse_event)
win.mainloop()