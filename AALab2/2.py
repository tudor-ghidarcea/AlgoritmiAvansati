class Cromozom:
    p = 0
    def __init__(self, interval, n):
        self.interval = interval
        self.n = n
        self.l = [False] * n
        Cromozom.p = (self.interval[1] - self.interval[0]) / 2 ** self.n
    def set_biti(self, l):
        self.l = l
    @classmethod
    def sir_biti(cls, l, ob):
        for x in l:
            if x:
                x = 1
        contor = len(l) - 1
        nr = 0
        for x in l:
            if x != 0:
                nr = nr + 2 ** contor
            contor = contor - 1
        nr = nr * Cromozom.p
        ob.interval[0] = ob.interval[0] + nr
        return nr


cromozom1 = Cromozom([2, 6], 4)
cromozom1.set_biti([False, False, False, False])
print(cromozom1.interval[0],cromozom1.interval[1])
print(cromozom1.p)
cromozom1.sir_biti(cromozom1.l, cromozom1)
print(cromozom1.interval[0],cromozom1.interval[1])

cromozom2 = Cromozom([3, 9], 7)
cromozom2.set_biti([False, False, True, True, False, True, False])
print(cromozom2.interval[0],cromozom2.interval[1])
print(cromozom2.p)
cromozom2.sir_biti(cromozom2.l, cromozom2)
print(cromozom2.interval[0],cromozom2.interval[1])