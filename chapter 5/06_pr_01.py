#WRITE A PROGRAM TO CREATE A DICTIIONARY OF URDU WORDS WITH THE VALUE OF ENGLISH TRANSLATION PROVIDE USER AN OPTION TO LOOK IT UP
myDict = {
    "pankha": "fan",
    "dabba" : "box",
    "cheez" : "thing"
}
print("options are", myDict.keys())
a = input("enter the urdu word\n")

# print("the meaning of your worf is:", myDict[a])  # it willthrow an error when there's no word found in the dictonary

#Below line will not throw an error if the key is not present in the dictionary
print("the meaning of your word is:", myDict.get(a))

