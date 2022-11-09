list1 = [3,4,5,False,6.2, "harry"]
#IF WE WANT TO PRINT THE INDEX NUMBER OF A LIST
# index = 0
# for item in list1:
#     print(item, index)
#     index +=1

for index, item in enumerate(list1):
    print(item, index)

