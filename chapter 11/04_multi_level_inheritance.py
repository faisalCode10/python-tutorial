class person:
    name = "faisal"
    country = "pakistan"
    city = "swat"

    def takeBreath(self):
        print(f"my name is  {self.name}")
        print("i am breathing")
        print(f"i am from {self.city}")
       
class employee(person):
    company = "Tesla"


    def getSalary(self):
        salary = 1000
        print(f"salary is {self.salary}")
    
    def takeBreath(self):
        print("i am an employee so i am luckily breathing...")
    
class programmer(employee):
    company ="fiverr"

    def getsalary(self):
        print(f"no salary to programmer")

    def takeBreath(self):
        print("i am an programmer so i am  breathing++...")
    

p = person()
p.takeBreath()
# print(p.company) #throw an ERROR

e = employee()
e.takeBreath()
print(e.company)
salary = 10000
print(salary)

pr = programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)