user_name = input("enter user name :")
name = len(user_name)
if(name>=10):
    print("user_name  has 10 letter")
elif(name!=10):
    print("user_name has less than 10 letter")

elif(name==0):
    print("user dead")