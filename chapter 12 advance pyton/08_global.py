a = 54   #Global variable
def func1():
    global a
    print(f"print statement 1 : {a}")

    a = 8  #local variable  if global keyword is not used
    print(f"print statement 2 : {a}")


func1()
print(f"print statement 3 : {a}")

