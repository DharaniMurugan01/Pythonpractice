class Student:
    def __init__(self):
        self._name="dhar"
    def _funname(self):
        return "hi bro"
class Subject(Student):
    pass
ob=Student()
ob1=Subject()
print(ob._name) 
print(ob._funname())
print(ob1._name)
print(ob1._funname())