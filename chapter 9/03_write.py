from os import write


f = open('sample.txt', 'a')
f.write(" I am writing")  #can be called multiple times

f.close()