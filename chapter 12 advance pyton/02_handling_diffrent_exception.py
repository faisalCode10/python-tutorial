while True:
    print("press Q to quit")
    try:
        a = int(input("enter a number: "))
        c = 1/a
        print(c)
    except ValueError as e:
        print("Please Enter a Valid Value :")
        # print(e)

    except ZeroDivisionError as e:
        print("Make sure you are not dividing by 0 :")
        # print(e)


print("thanks for using this code!")