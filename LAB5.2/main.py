fisier = open("AA52.txt", "r")
n=fisier.readline()

punct1=fisier.readline()
punct1=punct1.split()
punct1[0] = int(punct1[0])
punct1[1] = int(punct1[1])

start=punct1            

punct2=fisier.readline()
punct2=punct2.split()
punct2[0] = int(punct2[0])
punct2[1] = int(punct2[1])

punct3=fisier.readline()

inainte=0
dreapta=0
stanga=0

while punct3!='':       #determinantul
    punct3=punct3.split()
    punct3[0] = int(punct3[0])
    punct3[1] = int(punct3[1])
    if (punct2[0] * punct3[1] + punct3[0] * punct1[1] + punct1[0] * punct2[1] - punct2[0] * punct1[1] - punct3[0] * punct2[1] - punct1[0] * punct3[1]) == 0:
        inainte=inainte+1
    elif (punct2[0] * punct3[1] + punct3[0] * punct1[1] + punct1[0] * punct2[1] - punct2[0] * punct1[1] - punct3[0] * punct2[1] - punct1[0] * punct3[1]) > 0:
        stanga=stanga+1
    else:
        dreapta=dreapta+1
    punct1=punct2
    punct2=punct3
    punct3 = fisier.readline()
punct3=start
if (punct2[0] * punct3[1] + punct3[0] * punct1[1] + punct1[0] * punct2[1] - punct2[0] * punct1[1] - punct3[0] * punct2[1] - punct1[0] * punct3[1]) == 0:        #utilez formula, dar folosesc start in locul lui punct3
    inainte=inainte+1
elif (punct2[0] * punct3[1] + punct3[0] * punct1[1] + punct1[0] * punct2[1] - punct2[0] * punct1[1] - punct3[0] * punct2[1] - punct1[0] * punct3[1]) > 0:
    stanga=stanga+1
else:
    dreapta=dreapta+1
print(stanga,dreapta,inainte)