# Q2) write a python program to fill in a letter template given below with a name and date

letter = '''  Dear <|NAME|>,
Greeting form ABC coding house. i am happy to tell you about your selection 
you are selected
Have a great day
Thanks and regards, 
BILL
Date:<|DATE|>
'''

name = input("enter your Name\n")
date = input("Enter date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)