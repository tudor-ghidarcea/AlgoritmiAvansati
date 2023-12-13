import math

intrare = []
while True:
    line = input()
    if line:
        intrare.append(line)
    else:
        break
f = '\n'.join(intrare)
f=f.splitlines()
line=f[0]
v=line.split()
x=float (v[0])
y=float (v[1])
A=(x,y)

line=f[1]
v=line.split()
x=float (v[0])
y=float (v[1])
B=(x,y)

line=f[2]
v=line.split()
x=float (v[0])
y=float (v[1])
C=(x,y)

line=f[3]
v=line.split()
x=float (v[0])
y=float (v[1])
D=(x,y)

#functie care calculeaza distanta dintre 2 puncte
def dist(p1, p2):
    return math.sqrt(pow((p1[0] - p2[0]) , 2) + pow((p1[1] - p2[1]),2))

def get_Circle(A,B,C):

    # calculez lungimile laturilor triunghiului ABC
    AB = dist(A,B)
    BC = dist(B,C)
    AC = dist(A,C)

    # Formula 2(A.x *(B.y-C.y) + B.x *(C.y-A.y)+ C.x*(A.y-B.y)) pentru arie
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    # coordonate centru de cerc
    # Formula pentru coordona carteziana x ((A.x^2 + A.y^2)*(B.y-C.y)+(B.x^2+B.y^2)*(C.y-A.y)+(C.x^2+C.y^2)*(A.y-B.y))/D
    x = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1])
         + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / D
    # Formula pentru y ((A.x^2 + A.y^2)*(B.x-C.x)+(B.x^2+B.y^2)*(C.x-A.x)+(C.x^2+C.y^2)*(A.x-B.x))/D
    y = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0])
         + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / D
    center_of_circle = (x,y)

    # raza cercului

    r = (AB * BC * AC) / D


    return center_of_circle, r

def position_to_circle(A,B,C,D):
    #calculez cercul punct & raza
    center_of_circle,r = get_Circle(A,B,C)

    distance = dist(center_of_circle, D)
    if round(distance - r, 2) == 0: # trebuie sa rotunjesc altfel nu va fi precis distanta=r
        return 0 # D se află pe cerc
    if distance < r:
        return -1 # D se află în interiorul cercului
    return 1 # D se află în exteriorul cercului
if position_to_circle(A,B,C,D) == -1:
    print("Muchia AC este ilegala.")
else:
    print("Muchia AC este legala.")

if position_to_circle(A, B, D, C) == -1:
    print("Muchia BD este ilegala.")
else:
    print("Muchia BD este legala.")