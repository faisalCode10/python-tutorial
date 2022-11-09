def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "       Harry is  a good boy       "
n = remove_and_split(this, "good")
print(n)


