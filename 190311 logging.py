#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:54:13 2019

@author: heroname
"""

'''
LOGGING
'''
import logging

# default 'root'
logger = logging.getLogger('Test')

''' to console
logger.warning('This is a test message')
logger.info('This is just FYI')
logger.error('Something is wrong.')
'''

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
logger.addHandler(c_handler)

''' test.log
f_handler = logging.FileHandler('test.log')
f_handler.setLevel(logging.ERROR)
logger.addHandler(f_handler)
'''

f_handler = logging.FileHandler('test1.log')
f_handler.setLevel(logging.WARNING)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

''' to file '''
logger.warning('This is a test message')
logger.info('This is just FYI')
logger.debug('This is to debug the application')
logger.error('Something is wrong.')

try:
    1/0
except:
    logger.error('Error occurred.', exc_info=True)