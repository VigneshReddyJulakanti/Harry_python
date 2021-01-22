a=open("\\‪..\\..\\..\\Users\\DELL\\question\\cfiletest.txt","r")

print(a.read(5))  #this will read the first 5 chars of the files and prints them

print(a.read())  #this will continue reading from the place where it is stopped reading



a.close()