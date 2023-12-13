 # exercitiul 1
import csv
import math
import numpy as np
lista_orase = []

def coordonate_orase():
    with open('coordonate.txt', 'r') as fisier:
        reader = csv.reader(fisier)
        for count, (c1, c2) in enumerate(reader):
            oras = [float(c1), float(c2)]
            lista_orase.append(oras)
        return lista_orase
lista_orase=coordonate_orase()
#print(lista_orase)
#ex1 subp2

def calculare_distanta(index_oras_1, index_oras_2):
    coordonate1=lista_orase[index_oras_1]
    #print(coordonate1)
    #print(coordonate1[0])
    coordonate2=lista_orase[index_oras_2]
    #print(coordonate2)
    #print(coordonate2[0])
    distanta= math.sqrt(abs((float(coordonate2[0])-float(coordonate1[0]))*2 - (float(coordonate2[1])-float(coordonate1[1]))*2))
    return distanta


print(calculare_distanta(0,3))

#ex1 subp3

def graf():
    matr = [[0] * 4 for _ in range(4)]
    for i in range(0, len(lista_orase) - 1):
        for j in range(0, len(lista_orase) - 1):
            matr[i][j] = calculare_distanta(i, j)
    return matr

matr = graf()
arr = np.array(matr)
print(arr)