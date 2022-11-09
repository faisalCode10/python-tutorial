# n = int(input("enter number: "))
# for i in range(1 , n+1): 
#     print(f"{i}")

# from itertools import *

# s,k = input().split(' ')

# for l in range(1,int(k)+1):
#     for c in combinations (sorted(s),l):
#         print(''.join(c))



# while True:
#     year = int(input("Enter a year: "))

#     # To get year (integer input) from the user
#     # year = int(input("Enter a year: "))

#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("{0} is a leap year".format(year))
#             else:
#                 print("{0} is not a leap year".format(year))
#         else:
#             print("{0} is a leap year".format(year))
#     else:
#         print("{0} is not a leap year".format(year))




def is_leap(year):
    leap = False
    
    # Write your logic here

    if ((year%400==0)or((year%4==0)and(year%100!=0))):
        print("%d is a leap year"%year);
    else:
        print("%d is not a leap year"%year);

    return leap

year = int(input())
print (is_leap(year))