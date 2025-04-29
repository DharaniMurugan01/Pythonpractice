class Circle:
    def __init__(self,radious=1.0,color="blue"):
        self._radious=radious
        self._color=color
    def setrad(self,radious):
        self._radious=radious
    def setcolor(self,color):
        self._color=color
    def getrad(self):
        return self._radious
    def getcolor(self):
        return self._color
    def getArea(self,r):
        return 3.14*r*r
    def __str__(self):
        return f"Circle[radious={self._radious},color={self._color}]"
ob=Circle()
print(ob)
ob1=Circle(1.0)
print(1.0)
ob2=Circle(3.0,"yellow")
print(ob2)