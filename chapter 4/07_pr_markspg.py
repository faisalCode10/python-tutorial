#write a  program to accept marks of 6 students and display them in a sorted manner


m1 = int(input("enter marks for student number 1: "))
m2 = int(input("enter marks for student number 2: "))
m3 = int(input("enter marks for student number 3: "))
m4 = int(input("enter marks for student number 4: "))
m5 = int(input("enter marks for student number 5: "))
m6 = int(input("enter marks for student number 6: "))

myList = [m1,m2,m3,m4,m5,m6]

myList.sort()

print(myList)

