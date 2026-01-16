num=int(input("How many students you want to enter :"))
with open("students.txt","a") as file:
    for i in range(num):
        name=input(f"Enter the student name {i+1}")
        file.write(name+"\n")
print("Names added successfully")
print("Student names :")
with open("students.txt","r") as file:
    for i in file:
        print(i)

         