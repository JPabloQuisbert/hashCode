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
            if i == 0: rows, cols, low, high = line.split(' ')
    return int(rows), int(cols), int(low), int(high)

if __name__=='__main__':
    b=analizar_data("data/a_example.in")
    print(b)
