b= set()    # create set

print(type(b))
# Adding value to a set 
b.add(4)
b.add(4)
b.add(5)  # Adding a value repetedly does not changes a set
b.add(5)

#Accessing element
# b.add([1,2,34,5])  #we cannot add list in set becuase its unhashable
b.add((1,2,34,5))  #we can add tuple in set....
# b.add({1:5})  #we cannot add dictionary in set becuase its unhashable


#length of the set
print(len(b))  # print the length of this set

#removal
b.remove(5)    #remove 5 from the set
# b.remove(15) #  will give us error b/c 15 is not presnet in set

print(b.pop())

# b.clear()  # the set will be emptys
print(b)
