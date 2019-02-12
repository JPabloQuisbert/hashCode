# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:16:40 2019

@author: Juan Pablo
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def analizar_data(file):

    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: rows, cols, min_ing, max_cell = line.split(' ')
    return int(rows), int(cols), int(min_ing), int(max_cell)


#leer el archivo
def leer_pizza(filename):
    with open(filename,'r') as f:
        line=f.readline()
        R,C,L,H=line.split()
        pizza=f.readlines()
        pi = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in pizza[0:]])
    return R,C,L,H,pizza,pi

#contar los ingredientes
def contar_ingredientes(array):
    count_ing=[0,0]
    for line in array:
        count_ing+=np.bincount(line)
    return count_ing


if __name__=='__main__':
    b=analizar_data("data/a_example.in")
    print(b)
    R,C,L,H,pizza,pi=leer_pizza("data/b_small.in")
    print(R,C,L,H)
    print(pizza)
    print(pi)
    fig,ax=plt.subplots()
    ax.imshow(pi)
    ax.set_title(f'a_example.in shape is {pi.shape}, max. score {pi.size}\nmin. ingredients is {L}, max. pizza slice is {H}');
    T,M=contar_ingredientes(pi)
    print("tomates= ",T,"mushroom= ",M)
