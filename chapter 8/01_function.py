def percent(marks):
    p = ((marks[0]+ marks[1]+ marks[2] +marks[3]+ marks[4])/500)*100
    return p

marks1 = [89, 90, 85, 75, 66]
percentage1 =  percent(marks1)

marks2 = [75, 98, 88, 79, 87]
percentage2 = percent(marks2)

print(percentage1, percentage2 )