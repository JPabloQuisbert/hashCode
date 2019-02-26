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
        count_ing[0]+=np.sum(1-line)
        count_ing[1]+=np.sum(line)
        #print(count_ing)
    return count_ing

def calcular_pizza(M,T,array):
    menor=[M,T].index(min([M,T]))
    if menor==0:
        print("menor mushroon",menor)
    else:
        print("menor tomates",menor)
    val_array=np.zeros_like(array)
    array=array.tolist()
    index=[]
    val_2=[(0,1),(1,0),(0,-1),(-1,0)]
    val_1=[(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if array[i][j]==menor:
                val_array[i][j]=3
                index.append((i,j))
                for elem in val_2:
                    try:
                        if i+elem[0]>=0 and j+elem[1]>=0:
                            val_array[i+elem[0]][j+elem[1]]=max(val_array[i+elem[0]][j+elem[1]],2)
                    except:
                        pass
                for elem in val_1:
                    try:
                        if i+elem[0]>=0 and j+elem[1]>=0:
                            val_array[i+elem[0]][j+elem[1]]=max(val_array[i+elem[0]][j+elem[1]],1)
                    except:
                        pass
    """
    for elem in index:        
        print(elem)
        """
            
    print("index ",index)
    print("val array", val_array)
    return val_array, index

def cortar(R,C,L,H,array):
    shapes=[]
    i=1
    j=2
    f=0
    while f==0: 
        if i<=R:
            if i*j<=H:
                shapes.append((i,j))
                if j<C:
                    j+=1
                else:
                    i+=1
                    j=1
            else:
                i+=1
                j=1
        else:
            f=1
    print("shapes ",shapes)
    return shapes

def greedy_cortes(shapes,pizza,index):
    corte_pizza=np.zeros_like(pizza)
    corte_pizza=corte_pizza.tolist()
    
    val_2=[(0,1),(1,0),(0,-1),(-1,0)]
    val_1=[(1,1),(1,-1),(-1,1),(-1,-1)]
    
    for indice in index:    
        for direccion in val_2:
            #para evitar que se detega el buvcle
            try:
                #para eliminar indices negativos
                if indice[0]+direccion[0]>=0 and indice[1]+direccion[1]>=0: 
                    pass
            except:
                pass
def buscar_nodos(i,j,pizza,H):
    direcciones=[(0,-1),(-1,0),(0,1),(1,0)]
    nodos={}
    beneficio=[]
    print("nodo inicio: ",i,j," H ",H)
    for elem in direcciones:
        m=i
        n=j
        tom=0
        mush=1
        try:
            if i+elem[0]>=0 and j+elem[1]>=0:
                for f in range(1,int(H)+1):
                    m+=elem[0]
                    n+=elem[1]
                    if m>=0 and n>=0 and m<pizza.shape[0] and n<pizza.shape[1]:
                        if pizza[m][n]==1:
                            tom+=1
                        else:
                            mush+=1
                        nodos[elem]=[[m,n],tom/mush]
                        print("imprimiendo f: ",f,"[",m,n,"]",elem,"cantidad",tom,mush)
                #print("fin for **********",list(nodos.values()))
                #beneficio.append([[m-elem[0],n-elem[1]],tom/mush])
        except:
            print("error externo")
    lista=list(nodos.values())
    print("nodos hallados ",sorted(list(nodos.values()),key=lambda x:x[1],reverse=True))
    beneficio=sorted(list(nodos.values()),key=lambda x:x[1],reverse=True)
    print("corte con mejor beneficio ","[",i,j,"]", beneficio[0][0])
    return nodos
    
def nodos():
    distActual={}
    while n<6:
        buscar_nodos

if __name__=='__main__': 
    b=analizar_data("data/d_big.in")
    print(b)
    R,C,L,H,pizza,pi=leer_pizza("data/b_small.in")
    print(R,C,L,H)  
    print(pizza)
    print(pi)

    fig,ax=plt.subplots()
    ax.imshow(pi)
    #ax.set_title(f'a_example.in shape is {pi.shape}, max. score {pi.size}\nmin. each ingredients is {L}, max. pizza cells per slice is {H}');
    M,T=contar_ingredientes(pi)
    print("tomates= ",T,"mushroom= ",M)
    print("calculo de valores:")
    pi2,indices=calcular_pizza(M,T,pi)
    cortar(int(R),int(C),int(L),int(H),pi)
    #ax.imshow(pi2)
    buscar_nodos(indices[2][0],indices[2][1],pi,H)
