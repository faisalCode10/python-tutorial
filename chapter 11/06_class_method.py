class Employee:
    company = "Camel"
    salary = 100
    location = "islamabad"

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
