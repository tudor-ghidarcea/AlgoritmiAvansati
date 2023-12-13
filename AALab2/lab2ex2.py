class Cromozom:
    precizie = 0

    def __init__(self, capete, n):
        self.capete = capete
        self.n = n
        self.l = [False] * n
        Cromozom.precizie = (self.capete[1] - self.capete[0]) / 2 ** self.n

    def set_biti(self, l):
        self.l = l

    @classmethod
    def transformare_sir_biti(cls, l, ob):
        for x in l:
            if x:
                x = 1
        count = len(l) - 1
        numar = 0
        for x in l:
            if x != 0:
                numar = numar + 2 ** count
            count = count - 1
        numar = numar * Cromozom.precizie
        ob.capete[0] = ob.capete[0] + numar
        return numar


c1 = Cromozom([1, 3], 4)
c1.set_biti([False, False, False, False])
print(c1.capete[0],c1.capete[1])
print(c1.precizie)
c1.transformare_sir_biti(c1.l, c1)
print(c1.capete[0],c1.capete[1])

print("")

c2 = Cromozom([2, 5], 7)
c2.set_biti([False, False, True, True, False, True, False])
print(c2.capete[0],c2.capete[1])
print(c2.precizie)
c2.transformare_sir_biti(c2.l, c2)
print(c2.capete[0],c2.capete[1])