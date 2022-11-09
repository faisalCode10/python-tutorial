# class programmer:
#     company = "Microsoft"
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#     def getinfo(self):
#         print(f"The Name Of The {self.company} Programmer Is {self.name} And The Product Is {self.product}")

# faisal = programmer("faisal", "skype")
# yusra = programmer("yusra", "GITHUB")
# faisal.getinfo()
# yusra.getinfo()
       

def fsl():
  while True:
        print("jutter")
        print("1) Write a story")
        print("2) Read story")

        a = int(input("enter your choice  "))
        if a == 1:
            b =  input("enter your story")
            with open("file.txt", 'w') as f:
                f.write(b)
        elif a ==2:
            with open("file.txt", 'r') as f:
                f.read(a)





fsl()