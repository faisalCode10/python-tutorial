def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is Not Good")

a = increment(34)
print(a)
