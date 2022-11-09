myDict = {
    "Fast": "In a quick manner",
    "Faisal": "A code",
    "marks": [12,34,66],
    "anotherDict":{'harry': 'player'}  # here we create another dictionary

}

print(myDict) # print myDict 
# print(myDict['Fast'])  #print 'Fast' In myDict
myDict["marks"] = [12,78]   # here we change the value of marks
print(myDict['marks'])   #print the new value of marks

print(myDict["anotherDict"]["harry"])     #print newDict what we created earlier