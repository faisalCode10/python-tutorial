class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "fiverr"
    level = 0
    def upgradelevl(self):
        self.level = self.level + 1

class programer(Employee, Freelancer):
    name = "Faisal"

p = programer()
p.upgradelevl()
print(p.company)