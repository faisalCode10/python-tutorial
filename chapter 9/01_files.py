#use Open function to read the contenet of a file
# f = open('sample.txt', 'r')
f = open('sample.txt',)#by default the mode is r
# data = f.read() #READ THE DATA IN THE FILE
data = f.read(6)  #READ FIRST 6 CHARACTER 
print(data)
f.close()
