import sys
x=5
print(type(x))
y="hello"
print(type(y))
z=True
print(type(z))
print(type("Dhara"))
print(type('dhar'))    
a=[4, 'dhar', 4.5]
print(type(a))
print(a[0])
print(type(a[1]))
b=(4, 'yo',9.0)
print(type(b))
print(type(b[1]))
# b[0]=5
# print(b[0])
set={4,5,20,20,"dharani"}
print(set)
print(type(set))
# set[0]=3
# print(set[0])
# print(set[0])
set.add("dhar")
print(set)
set.remove("dhar")
print(set)
c=None
print(type(c))
print(c)
c=6
print(c)
c=7
print(c)
c="dhar"
print(c)
me={"name":"dhara", "age":20}
print(me)
print(me["name"])
print(type(me))
print(False)
i=0
for i in range(5):
    print(me)
j=0
while j<5:
    print(j)
    j+=1
v,m=50,60
print(v,m)
print(type(0x18d))
print(type(0o257))
g = (1 == True)
print(g)
h=(True+10)
print(h)
print(h-False)
age=int(input("Enter age"))
print((age))
print(type(age))
i=0
for i in range(2):
     print("apple","banana","orange",sep=",",end=".\n")
with open(sys.argv[1],'r') as test:
    print(test.read())
name=input("enter name")
age=int(input("Enter age"))
no_of_days=int(input("enter no of the days"))
salary=no_of_days*1000;
print("Salary is ",salary,end="\n")
print("employee name",name,end="\n")
print("age",age,end="\n") 
