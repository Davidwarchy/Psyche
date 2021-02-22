# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:22:09 2021

@author: JOHN WARUTUMO

Euler (pronounced \oila\) is a system for managing mathematical complexity. Simply put:
    >the aim is to discover patterns in data
    >the aim is to do it quickly and luckily
euler aims at helping managing inputs, mathematical operations and change/addition in inputs or operations.

"""
import json
f = open('C:/Users/JOHN WARUTUMO/Desktop/Psyche/paths.txt')
j = json.load(f)
f.close()
path = j['math']#the path string for the math functions directory

import os

l = list()

folder = path
for (dirpath,dirnames,filenames) in os.walk(folder):
    l+=[os.path.join(dirpath,file)for file in filenames]  

L = []

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
             L.append(os.path.join(root, file))

import re    
patt = re.compile(r'\ndef ((?:\w+\d*)+\(.*\):)')#how functions start in python         
'''
\ndef - newline followed by def
(\w+\d*) - one or more alphanumeric followed by optional numbers
?: indicates that the group isn't to be captured'
(\w+\d*)+ - numbers may occur between words
\(.*\): - opening bracket followed by any xters except newline, then followed by a colon
'''
S = []
for p in L:
    f = open(p)
    txt = f.read()
    fxns = patt.findall(txt)
    if fxns:
        S.append(( p, fxns ))#append the file and the functions in it as a tuple pair
    f.close()
    