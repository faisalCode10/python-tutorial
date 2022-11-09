# class Employee:
#     company = "google"  
#     def __init__(self, name, salary, subunit):
#         self.name = name
#         self.salary = salary
#         self.subunit = subunit
#         print("Employee is created")
    
#     def getDetails(self):
#         print(f"The name of the employee is {self.name}")
#         print(f"The salary of the employee is {self.salary}")
#         print(f"The subunit of the employee is {self.subunit}")


#     def getSalary(self, signature):
#         print(f"salary for the employee of  {self.company} is {self.salary}\n{signature}")

#     @staticmethod
#     def greet():
#         print("Good morning sir")

# harry = Employee("faisal", 100, "youtube")
# harry.getDetails()

from _typeshed import Self


class data():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def display():
        print("your name is "+ Self.name)
        print("your adress is "+ Self.adress)

d = data()
d.name = input("enter name")
d.adress = input("Enter adress")

d.display()
