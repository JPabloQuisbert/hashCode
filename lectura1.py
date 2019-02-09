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
            if i == 0: rows, cols, min_ing, max_cell = line.split(' ')
    return int(rows), int(cols), int(min_ing), int(max_cell)

def leer_pizza(filename):
    with open(filename,'r') as f:
        line=f.readline()
        R,C,L,H=line.split()
        pizza=f.readlines()
    return R,C,L,H,pizza

if __name__=='__main__':
    b=analizar_data("data/a_example.in")
    print(b)
    R,C,L,H,pizza=leer_pizza("data/a_example.in")
    print(R,C,L,H)
    print(pizza)
    
