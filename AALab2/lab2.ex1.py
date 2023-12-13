import math
import numpy as np


# 1.1
def citire():
    f = open("coordonate.txt", "r")
    lines = f.readlines()
    data = [tuple(line.strip().split()) for line in lines]
    return data


coordonate = citire()


# 1.2
def calculare_distanta(index_oras_1, index_oras_2):
    distanta = math.sqrt(abs(((float(coordonate[index_oras_2][0]) - float(coordonate[index_oras_1][0])) ** 2) - (
            (float(coordonate[index_oras_2][1]) - float(coordonate[index_oras_1][1])) ** 2)))
    return distanta


# 1.3
def graf():
    matrice_adiacenta = [[0] * 4 for _ in range(4)]
    for i in range(0, len(coordonate) - 1):
        for j in range(0, len(coordonate) - 1):
            matrice_adiacenta[i][j] = calculare_distanta(i, j)
    return matrice_adiacenta

matrice_adiacenta = graf()
arr = np.array(matrice_adiacenta)
print(arr)
