a='hlo'
b="bye"
print(a+b)  #concatenation #output:hlobye
print(a[1]) #accesing  index #output:l
#can only acess the string but cant change its value
print(a[1:]) #accesing all the indexes from the index 1 to end #output:hl
print(a[:1]) #accesing all the indexes from starting to 1 #output:h
print(a[0:3]) #0 is inclusive and 3 is exclusive
print(a[:-1]) #negative index are started from ending with -1,-2,-3
 

a="hlo my name is vignesh"
print(a[1:8:2]) #output:l yn #Here 2 was the step i.e it will skip 2 letters in between
