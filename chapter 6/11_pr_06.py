#WRITE A PROGRAM TO CALCULATE THE GRADE OF A STUDENTS FROM HIS MARKS FROM THE FOLLOWING SCHEME

marks = int(input('enter your marks :'))

if marks>=90:
    grade ="Ex"

elif marks>=80:
    grade = "A"

elif marks>=70:
    grade = "B"

elif marks>=60:
    grade = "C"


elif marks>=50:
    grade = "D"

else:
    grade = "F"

print("your grade is " + grade)

 