sub1 = int(input("enter first subject marks: "))
sub2 = int(input("enter second subject marks: "))
sub3 = int(input("enter third subject marks: "))


if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33%  in one of the subject")

if(sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percantage less than 40")

else:
    print("congrates you are passed!!!")