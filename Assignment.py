# Q1
# age=int(input("enter age"))
# if age<1:
#     print("invalid")
# elif age>=1 and age<14:
#     print("cartoon club")
# elif age>=15 and age<=20:
#     print("Teens club")
# else:
#     print("not allowed")

# Q2
# num=int(input("enter num"))
# if num%2==0:
#     print(num//2)
# else:
#     print((num*3)+1)

# Q3
# total=int(input("enter total"))
# rabit=int(input("enter rabit count"))
# deer=int(input("enter deer"))
# bird=int(input("enter bird count"))
# squirells=int(input("enter squirells count"))
# sum=rabit+deer+bird+squirells
# if sum==total:
#     print("Baby lion is well behaved")
# elif total>sum:
#     print("baby lion is not well behaved")
# elif total<sum:
#     print("count wrongly")
# else:
#     print("invlaid")

total=int(input("total class attended"))
attend=int(input("attended class"))

percentage=(attend*100)/total
if(percentage<75):
    medicalcause=input("medical case Y or N ")
    if medicalcause=='Y':
        print(percentage,"allowed")
    elif medicalcause=='N':
        print(percentage,"Not allowed")
else:
    print(percentage,"Allowed")