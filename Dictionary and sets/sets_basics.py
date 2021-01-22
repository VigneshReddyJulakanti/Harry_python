#set will store a num once (i.e set will have only non repeatable elements)
# declaring a set
a={3,5,8,1,1}

print(a) #will delete the repeated number and only store a num once



a={} #will create an empty dictionary
a=set() #will create an empty set


a.add(1)   #will add 1 to the set
a.add(4)   #append() function cant be used sets
print(a)
# a.add(1,3)  #will return an error bcoz list cant be added bcoz list is editable
a.add((1,3))  #will add a tuple bcoz it cant be chenged any more
a.add("df")
print(a)

# set will think 2.0 and 2 are same 