class Employee:
    comapny = "google"
    salary = 100

faisal = Employee()
harry = Employee()
faisal.salary = 300
harry.salary = 500


print(faisal.comapny)
# print(harry.comapny)


Employee.comapny = "youtube"
# print(faisal.comapny)
print(harry.comapny)

print(faisal.salary)
print(harry.salary)