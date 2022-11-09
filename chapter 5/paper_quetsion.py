odd = lambda x: bool(x%2)
numbers = [n for n in range(10)]
print(numbers)
n = list()
for i in numbers:
    if odd(i):
        continue
    else:
        break

# class Demo:
#     def __new__(self):
#         self.__init__(self)
#         print("Demo")

# def main():
#     obj = Demo()
# main()


