class Conover:
    def __init__(self, r=0, c=0):
        self._r = r
        self._c = c

    @classmethod
    def withrad(cls, r):
        return cls(r, 0)  # Only r given, c is 0

    @classmethod
    def withrandc(cls, r, c):
        return cls(r, c)  # Both r and c given

    @classmethod
    def withcolr(cls, c):
        return cls(0, c)  # Only c given, r is 0

    def getcolr(self):
        return self._c
ob1 = Conover.withrad(10)
print("Radius:", ob1._r, "Color:", ob1.getcolr())

ob2 = Conover.withcolr(7)
print("Radius:", ob2._r, "Color:", ob2.getcolr())

ob3 = Conover.withrandc(4, 9)
print("Radius:", ob3._r, "Color:", ob3.getcolr())
