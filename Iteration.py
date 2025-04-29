# Q4
# num=int(input("Enter the number"))
# sum=0
# for i in range(0,num):
#     print(num-i)
#     sum+=(num-i)
# print("sum is ",sum)

# Q5
# startingroom=int(input("enter the room number"))
# for i in range(startingroom,100,10):
#     print(i)

# Medium Q1
# n=int(input("enter number"))
# odd=even=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print("odd",odd,"even",even)

# Q2
# n=input("enter number")
# length=len(n)
# k=int(n)
# if length==5:
#     while k>0:
#         print(int(k%10),end="")
#         k=int(k/10)
# else:
#     print("Not a valid number")

# Q3
# count=0
# num=int(input("Enter number"))
# if num==0 or num==1:
#     print("not a prime number")
# elif num%2==0:
#     print("not a prime number")
# else:
#     for i in range(2,num):
#         if (num%i)==0:
#             count+=1
#     if count>1:
#         print("not a prime number")
#     else:
#         print("It is prime number")

# Q4,6
# count=0
# a=int(input("enter start"))
# b=int(input("enter stop"))
# for i in range(a,b+1):
#     for j in range(2,i):
#          if i%j==0:
#               count+=1
#     if count<1:
#          print(i)
#     count=0
