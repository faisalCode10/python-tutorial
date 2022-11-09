myDict = {
    "fast": "In a quick manner",
    "faisal": "A coder",
    "marks": [12,34,66],
    "anotherDict":{'harry': 'player'},  # here we create another dictionary
    1 : 2
     
}
#Dictionary Method
print(list( myDict.keys())) #  prints the keys of the dictionary
print( myDict.values()) # prints the keys of the dictionary
print( myDict.items()) # prints the keys,value for all content of the dictionary
print(myDict)
updateDict = {
    "lovish":"friend",
    "yusra" : "friend"
}
myDict.update(updateDict)  # update the dictionary by adding key-values pairs from update dict

print(myDict)

print(myDict.get("faisal"))  #print value associate with key value  "faisal"
print(myDict["faisal"])   # print value associate with key value  "faisal"

#THE DIFFRENCE BETWEEN .get and [] syntax in dictionary?
print(myDict.get("faisal2"))  #RETURNS NONE as faisal2 is not present in the dict
# print(myDict["faisal2"])   # throw an error as faisal2 is not present in the dict

