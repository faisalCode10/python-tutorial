num = int (input("Enter the Number: "))
prime = True
for i in range (2,num):
    if (num%i == 0 and num!= 0):
        prime = False
        break

if prime:
    print("this number is prime")

else:
    print("This numberis not prime")
    