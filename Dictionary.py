# def show_menu():
#     print("\n1.Show all student marks")
#     print("2.Show roll numbers")
#     print("3.Show marks")
#     print("4.Search for a student mark")
#     print("5.Add new student mark")
#     print("6.Delete a student mark")
#     print("7.Exit")

# def show_all(marks):
#     print("Student Marks:", marks)

# def show_keys(marks):
#     print("Roll Numbers:", list(marks.keys()))

# def show_values(marks):
#     print("Marks:", list(marks.values()))

# def search_student(marks):
#     r = input("Enter roll number: ")
#     if r in marks:
#         print(marks[r])
#     else:
#         print("Student not found.")

# def add_student(marks):
#     r = input("Enter new roll number: ")
#     m = int(input("Enter mark: "))
#     marks[r] = m
# def delete_student(marks):
#     r = input("Enter roll number to delete: ")
#     if r in marks:
#         del marks[r]
#     else:
#         print("Student not found.")
# marks = {
#     "101": 77,"104": 60, "107": 99,
#     "102": 84,"105": 45, "108": 86,
#     "2103": 83,"106": 40, "109": 67
# }
# while True:
#     show_menu()
#     choice = input("Enter choice: ")

#     if choice == "1":
#         show_all(marks)
#     elif choice == "2":
#         show_keys(marks)
#     elif choice == "3":
#         show_values(marks)
#     elif choice == "4":
#         search_student(marks)
#     elif choice == "5":
#         add_student(marks)
#     elif choice == "6":
#         delete_student(marks)
#     elif choice == "7":
#         break
#     else:
#         print("Invalid choice!")

set1={1,2,3,2}
print(set1)
set1.add(6)
set1.update([1,2],[4,5])
print(set1)
set1.remove(3)
print(set1)
set1.discard(4)
print(set1)
# set1.remove(10)
# print(set1)
set1.pop()
print(set1," hilo")
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
A={1,2,3,4,5}
B={5,6,7,8,4}
print(A|B)
print(A.union(B))
print(A&B)
print(A.intersection(B))
print(B&A)
print(A-B)
print(A.difference(B))
print(B.difference(A))
print(A^B)
print(A.symmetric_difference(B))
name="dhara"
age=20
print("my name is {1} and age is {0}".format(age,name))
print("my name is %s and my age is %d"%(name,age))
print(f"name is {name} and age is {age}")
print("Hello all how are you ")