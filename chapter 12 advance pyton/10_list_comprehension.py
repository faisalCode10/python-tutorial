a = [3,5,6,7,8,8,99,23,44,22,48,50]
# b = []
# for item in a:
#     if  item%2==0:
#         b.append(item)

# print(b)

#Shortcut to write the above program
b = [i for i in a if i%2==0]
c = [i for i in a if i>8]
print(b)
print(c)




