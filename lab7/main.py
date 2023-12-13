
def verif_inter(l_semi):
    maxX, maxY = 9999999999, 9999999999
    minX, minY = -9999999999, -9999999999

    for semiplan in l_semi:
        stanga = -9999999999
        dreapta = 9999999999
        if semiplan[0] == 0:
            if semiplan[1] < 0:
                stanga = -1* semiplan[2] / semiplan[1]
            else:
                dreapta = -1* semiplan[2] / semiplan[1]

        else:
            if semiplan[0] < 0:
                stanga = -1 * semiplan[2] / semiplan[0]
            else:
                dreapta = -1 * semiplan[2] / semiplan[0]

        if semiplan[0] == 0:
            minY = max(minY, stanga)
            maxY = min(maxY, dreapta)
        else:
            minX = max(minX, stanga)
            maxX = min(maxX, dreapta)

    if minY > maxY or minX > maxX:
        return 0
    if (minX != -9999999999 and maxX != 9999999999) and (minY != -9999999999 and maxY != 9999999999):
        return 1
    return 2


l_semi = []
intrare = []
while True:
    line = input()
    if line:
        intrare.append(line)
    else:
        break
text = '\n'.join(intrare)
n = int(text[0])
text = '\n'.join(text.split('\n')[1:])
text = text.splitlines()
for line in text:
    date = line.split()
    semiplan=(float(date[0]), float(date[1]), float(date[2]))
    l_semi.append(semiplan)


rezultat = verif_inter(l_semi)
if rezultat== 0:
    print("intersectie vida")
elif rezultat == 1:
    print("intersectie nevida marginita")
else:
    print("intersectie nevida nemarginita")