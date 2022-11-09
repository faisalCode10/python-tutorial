class person:
    country = "pakistan"
    def __init__(self):
        print("Initializing person...\n")
    city = "swat"

    def takeBreath(self):
        print("i am breathing")
        print(f"i am from {self.city}")
       
class employee(person):
    def __init__(self):
        print("Initializing Employee...\n")
    company = "Tesla"


    def getSalary(self):
        salary = 1000
        print(f"salary is {self.salary}")
    
    def takeBreath(self):
        print("i am an employee so i am luckily breathing...")
    
class programmer(employee):
    def __init__(self):
        print("Initializing Programmer...\n")
    company ="fiverr"

    def getsalary(self):
        print(f"no salary to programmer")

    def takeBreath(self):
        super().takeBreath()
        print("i am an programmer so i am  breathing++...")
    

p = person()
p.takeBreath()


e = employee()
e.takeBreath()


pr = programmer()
pr.takeBreath()
