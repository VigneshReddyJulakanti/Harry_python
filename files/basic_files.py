
 #use open function to open the file 
 #by default it will be in the location of the python file , so to get a file from diff location go relative 
 #by default mode  sets to read mode
a=open("\\‪..\\..\\..\\Users\\DELL\\question\\cfiletest.txt","r")   # will open a in read mode
data=a.read()    #will the data in a
print(data)    
a.close()       #will close the file


