class Employee:
    comapny = "google"
    salary = 100

faisal = Employee()
harry = Employee()

#CREATING INSTANCE ATTRIBUTE  SALARY FOR BOTH THE OBJECT
faisal.salary = 300
# harry.salary = 500

print(faisal.salary)
print(harry.salary)

#BELOW LINE WILL THROW AN ERROR AS ADRESS IS NOT PRESENT IN INSTANCE/CLASS 
# print(harry.Adress)