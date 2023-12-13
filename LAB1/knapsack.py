def knapsack(total, greutati, valori, saci):
 if(saci==0 or total==0):
    return 0
 if(greutati[saci-1]>total):
    return knapsack(total, greutati, valori, saci-1)
 else:
    return max(valori[saci-1]+knapsack(total-greutati[saci-1], greutati, valori, saci-1), knapsack(total,greutati, valori, saci-1))

print('Introduceti valorile:')

valori=list(map(int, input().split(' ')))

print('Introduceti greutatile:')

greutati=list(map(int, input().split(' ')))

total=int(input('Introduceti capacitatea totala:'))

saci=len(greutati)

print(knapsack(total, greutati, valori, saci))

#complexitate de timp O(2^n)