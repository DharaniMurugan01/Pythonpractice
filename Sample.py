import sys
# i=2
# for i in range(2):
#     name=input("enter your name\n")
#     print("hello",name)

# weight = float(input("Enter your weight: ")) 
# height = float(input("Enter your height in meters: "))

# if weight > 0 and height > 0:
#     bmi = weight / (height ** 2)
#     print("Your BMI is:", round(bmi, 2))
# else:
#     print("Weight and height must be greater than 0")
# limit = int(sys.argv[1])  

# if limit > 40:
#     print("over speed")
# else:
#     print("hii")

# print("Happy journey")

# a=int(sys.argv[2])
# b=int(sys.argv[3])
# if a>b :
#     print(f"{a} is greater")
# elif b>a:
#     print(f"{b} is greater")
# elif a>b or a==0:
#     print("a not equal to zero")
# elif b>a or b==0:
#     print("b not equal to zero")
# else:
#     print("both are equal")

# a=int(input("enter num1"))
# b=int(input("enter num2"))
# c=int(input("enter num3"))
# if a>b:
#     if a>c:
#         print("a is greater")
#     elif b>c:
#         print("b is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# n = int(input("enter n value: "))
# i = 1
# even = odd = 0

# while i < n:
#     if i % 2 != 0:
#         odd += 1
#     else:
#         even += 1

#     i += 1  
# print(odd, even)


# fact=1
# if n==0:
#     print("factorial is 1")
# elif n<0:
#     print("not correct")
# else:
#    for i in range(1,n+1):
#        fact=fact*i
#    print(fact)
# n=int(input("enter the num"))
# for i in range(1,n+1):
#     print(i,"* 15 =",i*15)
# for i in range(1,5):
#     for j in range(1,5):
#         # pass
#         print(i,end=" ")
#     print("\n")
# else:
#     print("hii")

# num = int(input("enter num: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not a prime")
#             break
#     else:
#         print("num is prime")
# else:
#     print("invalid input")
# i=2
# if num > 1:
#     while i<num:
#         if num % i == 0:
#             print("not a prime")
#             break
#         i += 1
#     else:
#         print("num is prime")
# else:
#     print("invalid input")

# lowerlimit=int(input("enter lower"))
# upperlimit=int(input("enter upper"))
# for i in range(lowerlimit,upperlimit+1):
#     if i>1:
#         for i in range(2,i,1):
#             if(i%2==0):
#                 print(i,"not prime10")
#                 break
#             i+=1
#         else:
#             print("num is prime")
#     else:
#         print("invalid input")

# tablenum=int(input("table num"))
# for i in range(1,tablenum+1):
#     for j in range(1,10+1):
#          print(i,"*",j,"=",j*i)
#     print("------")

# def f(a,b,c):
#     return a+b+c
# print(f(4,5,6))

# def f(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# n=int(input("num"))
# f(n)

# def circle(r):
#     print(22/7*r*r)
# def rectangle(length,breadth):
#     print(length*breadth)
# def square(side):
#     print(side*side)
# choice=int(input("enter your choice\n1.Area of circle\n2.area of rectangle \n3.area of square"))
# if choice==1:
#     r=float(input("enter radious"))
#     circle(r)
# elif choice==2:
#     length=float(input("enter length"))
#     breadth=float(input("enter breadth"))
#     rectangle(length,breadth)
# elif choice==3:
#     side=int(input("enter side"))
#     square(side)
# else:
#     print("not a valid choice")

# nu=2
# def f():
#     global nu
#     nu=nu+2
#     print(nu)
# f()
# print(nu)

# def outer():
#     fn = 1
#     def inner():
#         ln = 3
#         print(fn)  
#         print(ln) 
#     inner()
# outer()

# def outer():
#     fn=1
#     def inner():
#         nonlocal fn
#         fn=0
#         sn=1
#         print(sn)
#         inner()
# # outer()
# def add(a,msg):
#     print(a,msg)
# add(msg="what",a="hello")

# def employee(*names):
#     for i in names:
#         print(i)
# employee("dhara","gayu","Thoushi","Jeevu")

# def make(**sentence):
#     sen = []
#     for key, value in sentence.items():
#         sen.append("{}uses{}".format(key, value))
#     return sen
# print(make(a="dhara", b="what", c="doing"))

print((lambda x:x+6)(5))
print((lambda x: (x*x + 1)//2)(10))
print(r"hello\n")
k="hi"
m="Welcome"
print(m[-7])
name="dhara"
n=len(name)
for i in range(0,n):
    print(name[i])
for i in name:
    print(i)
j=0
while j<n:
    print(name[j],end="")
    j+=1
print(name[0:2])
print(name[-1:])
gayu="lichigayuu"
print(gayu[1:2:1])
print(gayu[0:4:2])
print(gayu[::2])
print(gayu[2::])
s = "helloworld"
modified = "j" + s[1:]
print(modified)
print(s.upper())
print(s.lower())
print(s.find('h'))
print(s.replace("hello","bow"))
print(s)
print(s.find('e'))
print("123".isalnum())
print("abcha".isalpha())
print("123".startswith("1"))
print("abc".endswith("c"))
# immutable
h="mom"
k=h[::-1]
print(k)
if h.__eq__(k):
    print("palindrome")
check="123age56f"
alphabet=0;
num=0
for i in range(0,len(check)):
    if check[i].isalpha(): 
        alphabet+=1
    elif check[i].isalnum():
        num+=1
print(alphabet,num)
t=[1,2,3,[4,5]]
t.insert(len(t),60)
print(t)
t.insert(2,300)
print(t)
def yes(word):
    return len(word)  
li = ["dhar", "ga", "jee"]
li.sort(key=yes)
print(li)
a=[1,2,3]
b=a
b[0]=17
print(b)
# print(t[3][0])
# a=["a","b","c"]
# a[0:2]=["x","y"]
# print(a)
# print(dir(list))
# k="why"
# print(/k.append("hi"))
def fun(b):
    for i in range(len(b)):
         b[i]=2*b[i]
a=[1,2,3]
fun(a)
print(a)
e=[x**2 for x in range(2,5)]
print(e)
s=[1,2,3,4,5]
ev=[x for x in s if x%2!=0]
print(ev)
d=[(n*(n+1)//2) for n in range(10)]
print(d)