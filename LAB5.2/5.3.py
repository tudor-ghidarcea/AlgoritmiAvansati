def determinant (puncte):           #determinantul pentru o lista cu trei puncte
    determinant = puncte[1][0]*puncte[2][1] + puncte[2][0] * puncte[0][1]\
          + puncte[0][0] * puncte[1][1] - puncte[0][1] * puncte[1][0]\
          - puncte[0][0] * puncte[2][1] - puncte[1][1] * puncte[2][0]
    return determinant
fisier = open("acoperire.txt")     #citirea
puncte=[]
n=int(fisier.readline())
for i in range (n):
    l=fisier.readline()
    line=l.split()
    x=int (line[0])
    y=int (line[1])
    puncte.append((x,y))
arr= [puncte[0], puncte[1]]
for i in range(2, n):       #calculam determinantul in ordine descrescatoare a vechimii nodurilor
        arr.append(puncte[i])
        print(arr)
        while len(arr)>2 and determinant([arr[-3], arr[-2], arr[-1]])<=0: #daca nu este viraj la stanga
            del arr[-2]
print("Varfurile acoperii convexe: ", * arr)