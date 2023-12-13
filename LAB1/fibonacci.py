import numpy as np

fisier = open("arra.txt", "r")
arrayNumereNp = np.loadtxt('arra.txt', delimiter=',')
fisier.close()
arrayNumere = arrayNumereNp.tolist()


def fibonacci(n):
    if n <= 0:
        print("introduceti un numar valid!")
    elif n <= len(arrayNumere):
        return arrayNumere[n - 1]
    else:
        aux = fibonacci(n - 1) + fibonacci(n - 2)
        arrayNumere.append(aux)
        return aux


fisier = open('arra.txt', 'a')
arrayNumereNp = np.asarray(arrayNumere)
np.save("arra.txt", arrayNumereNp)
fisier.close()
print(fibonacci(10))
print(arrayNumere)

#complexitate de timp exponentiala, O(n)
#complexitate de spatiu liniara






def fibonacci2(n2):
    array2 = []
    x2 = 1
    y2 = 1
    if n2 == 0 or n2 == 1:
        print(n2)
    else:
        array2.append(x2)
        array2.append(y2)
        while len(array2) != n2:
            aux2 = x2 + y2
            array2.append(aux2)
            x2 = y2
            y2 = aux2
    print(array2[n2 - 1])
    print(array2)

fibonacci2(11)

#complexitate de timp O(n), deoarece pentru orice numar, programul va face un numar de pasi egal cu numarul dat
#complexitate de spatiu la fel