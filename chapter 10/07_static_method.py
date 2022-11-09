class Employee:
    company = "google"  
    def getSalary(self, signature):
        print(f"salary for the employee of  {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning sir")

faisal = Employee()
Employee.salary = 200000
faisal.getSalary("thanks!")
# Employee.getSalary(faisal)

faisal.greet()