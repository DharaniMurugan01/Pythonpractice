# class Employee:
#     Stream="cse"
#     def __init__(self,id):
#         self.empid=id
# ob=Employee(101)
# ob1=Employee(102)
# print(ob.empid,ob.Stream)
# print(ob1.empid,ob1.Stream)
# print(Employee.Stream)

class Employee:
    def __init__(self):
        self.name="dhar"
        self._age=20
    # def getage(self):
    #      return self.__age
ob=Employee()
print(ob.name)
print(ob._age)
