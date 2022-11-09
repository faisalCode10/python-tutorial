
from typing import Text


text = input("Enter the text")
spam = False

if("make a lot of money" in text ):
    spam = True

elif("buy now" in text):
    spam = True

elif("click this" in text):
    spam = True

elif("subscribe this" in text):
    spam = True

else:
    spam = False

if (spam):
    print("this text is spam")

else:
    print("this is not a spam")
