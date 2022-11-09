def greter_than_5(num):
    if num>5:
        return True
    else:
        return False

lam = lambda num: num>10
l = [1,2,3,4,5,6,7,78,8]
print(list(filter(greter_than_5, l)))
print(list(filter(lam, l)))