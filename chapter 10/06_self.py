class Employee:
    company = "google"  
    def getSalary(self):
        print(f"salary for the employee of  {self.company} is {self.salary}")

faisal = Employee()
Employee.salary = 200000
faisal.getSalary()
# Employee.getSalary(faisal)