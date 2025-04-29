class Circle:
    def __init__(self,*args):
        if len(args)==0:
            self._r=1.0
            self._c="red"
        elif len(args)==1:
            self._r=args[0]
            self._c="red"
        elif len(args)==2:
            self._r=args[0]
            self._c=args[1]
        else:
            raise ValueError
    def getrad(self):
        return self._r
    def getcolor(self):
        return self._c
    def __str__(self):
        return f"Circle[radius={self._r}, color={self._c}]"
c=Circle()
print(c)
c1=Circle(1.0)
print(c1)
c2=Circle(2.0,"blue")
print(c2)
