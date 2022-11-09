class Employee:
    company = "Youtube"
    def showDetail(self):
        print("this is an employee")

class programmer(Employee):
    company = "Google"
    langauge = "python"
    def getLanguage(self):
        print(f"the language is {self.langauge}")
    #OVERWRITE FUNCTION
    def showDetail(self):
        print("this is an programmer")

e = Employee()
e.showDetail()

p = programmer()
p.showDetail()

print(p.company)
