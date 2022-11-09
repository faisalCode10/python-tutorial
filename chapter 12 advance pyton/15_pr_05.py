# num = int(input("enter your number :"))

# table = [num*i for i in range(1,11)]
# print(str(table))


# with open("table.txt", "a")as f:
#     f.write(str(table))
#     f.write('\n')



if __name__ == '__main__':
    n = int(input("enter number"))
while True:
    if n%1==0:
        print("Weired") 
        break
while True:
    for i in range(2,5):
        if n%2==0:
            print("Not Weird")
            break
while True:
    for i in range (6,20):
        if n%2==0:
            print("Weird")
            break
while True:
        if n%2==0 and n>20:
            print("Not Weird")
            break