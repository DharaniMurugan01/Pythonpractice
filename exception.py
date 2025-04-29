# try:
#     fh=open("text.txt","w")
#     try:
#         fh.write("hi")
#     finally:
#         print("hlo")
#         fh.close()
# except IOError:
#    print("File is not found")
# else:
#     print("i will execute when no error has occured")
# finally:
#     print("i am always run")

# try:
#     num=int(input("enter positive number"))
#     if(num<=0):
#        raise ValueError("this is negative error")
# except ValueError as e:
#     print(e)
# finally:
#     print("hello all")

# class Error(Exception):
#     pass
# class  ValueToosmall(Error):
#     pass
# class ValueToolarge(Error):
#     pass
# number=10
# while True:
#     try:
#        n=int(input("enter number"))
#        if n>number:
#            raise ValueToolarge
#        elif n<number:
#            raise ValueToosmall
#        break
#     except ValueToosmall:
#         print("value must be minimal")
#     except ValueToolarge:
#         print("value must be higher")
# print("congratulations you guess it right")
# from operator import*
# a,b=10,20
# print(mul(a,b))
# print(gt(a,b))
# print(mod(a,b))
# print(concat("gayu","lichi"))
# from  random import*
# print(randint(10,20))
# list1=[30,36,37,29,98]
# print(choice(list1))
# print(uniform(10,20))

# from random import*
# num=randint(1,20)
# count=0
# name=input("enter your name")
# while count<6:
#     n=int(input("enter number"))
#     if num<n:
#         print(name,",you are Too large bro")
#         count+=1
#     elif num>n:
#         print(name,"you are too small bro")
#         count+=1
#     elif n==num:
#         print(name,",you guess it right....")
#         break
# else:
#     print("you are cross the limit")

# from math import*
# print(sqrt(16))
# print(factorial(5))

# import mymodule
# mymodule.fun("Dhara")
# print("course name",mymodule.course)

# opencv-want install,argparse-default ,subprocess,
