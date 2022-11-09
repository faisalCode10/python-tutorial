while True:
    print("press Q to quit") 
    a = input("enter a number: ")
    if a == 'q': 
        break
    try:
        print("trying...")
        a = int(a)
        if a>6:
            print("you enterd a number greater than 6")
        else:
            print("Enter greater number")
    except Exception as e:
        print(f"your input resulted in an error: {e}")

print("Thanks for playing")

