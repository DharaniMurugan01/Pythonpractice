class Myclass:
    x = 5  
    def __init__(self, age):
        self.age = age

    def display(self, name):
        print("name is", name)
        self.y = 10    

print(Myclass)
ob = Myclass(20)
print(ob)
ob.display("dhara")  
print(ob.x)          
print(ob.y)          
ob1 = Myclass(15)
print(ob1.age)      
