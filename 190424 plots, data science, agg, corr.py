#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:06:42 2019

@author: heroname
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('iris.csv')
print(data.head())
print(len(data.index))
print(data['species'].unique())

print(data['sepal_length'].mean())

print(data.mean())

print(data.min())
print(data.max())

print(data.std())

"""
plot types
1. box plot         .plot(kind='box') [single]     .plot(kind='box') [multiple]
2. histogram        .hist()
3. line             .plot.kde()
"""
'''
plt.clf()
data['sepal_length'].plot(kind='box')
plt.show()

plt.clf()
data.plot(kind='box')
plt.show()

plt.clf()
data['sepal_length'].hist()
plt.show()

plt.clf()
data['sepal_length'].plot.kde()
plt.show()

print(data.groupby('species').mean())

print(data.groupby('species').std())

print(data['species'] == 'setosa')

data[data['species'] == 'setosa'].plot(kind='box')
data[data['species'] == 'versicolor'].plot(kind='box')
data[data['species'] == 'virginica'].plot(kind='box')

data[data['species'] == 'setosa'].plot.kde()
data[data['species'] == 'versicolor'].plot.kde()
data[data['species'] == 'virginica'].plot.kde()
'''

# comment graphs to see
#print(data.groupby('species').agg(['mean','min', 'max']))
#print(data.groupby('species').agg([np.mean, np.min, np.max]))

print(data.groupby('species')[['sepal_length', 'sepal_width']].agg([np.mean, np.min, np.max]))
# aggregation - default set to column

plt.clf()
data.plot(kind='scatter', x='petal_length', y='petal_width')
plt.show()

plt.clf()
data.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()

print(data.corr())