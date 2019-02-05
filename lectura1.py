# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:16:40 2019

@author: Juan Pablo
"""
import sys
import numpy as np

def analizar_data(file):

    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: rows, cols, ingredients, cells = line.split(' ')
    return int(rows), int(cols), int(ingredients), int(cells)

if __name__=='__main__':
    b=analizar_data("data/a_example.in")
    print(b)
