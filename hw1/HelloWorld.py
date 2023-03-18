
import fileinput
 
n = 0
for line in fileinput.input():
    if(n != 0):
        print("Hello, "+str(line.rstrip())+"!")
    n+=1
