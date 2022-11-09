class Employee:
    company = "amazon"
    salary = 5600
    slarayBounus = 500
    # total salary = 6100
    @property
    def totalsalary(self):
        return self.salary + self.slarayBounus

e = Employee()
print(e.totalsalary)
