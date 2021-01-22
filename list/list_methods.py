
###                              .sort()                                   ###
list1=[1,2234,34.5,-3]
list1.sort()
print(list1) #will arrange the list in the accending order 

list1=["a","dbc","b"]
list1.sort()
print(list1) #will arrange the list in the accending order of starting alphabet

#Note : If str and int in same list then .sort() can not be used


###                              .reverse()                                   ###
list1=[1,2234,"dfg",-3]
list1.reverse()
print(list1) #will reverse the list


###                              .append()
list1=[1,2234,"dfg",-3]
list1.append("added")    #will add "added" at the end of the list
print(list1)

###                              .insert()
list1=[1,2234,"dfg",-3]
list1.insert(1,"added")    #will add "added" at the index 1
print(list1)


###                         .pop()
list1=[1,2234,"dfg",-3]
list1.pop(1)    #will remove element at the index 1
print(list1)

###                           .remove()
list1=[1,2234,"dfg",-3]
list1.remove(1)    #will remove 1 from the list
print(list1)

###                           .count()
list1=[1,2234,"dfg",-3]
print(list1.count(1) )   #will count no of elements named 1 in the list

###                           .index()
list1=[1,2234,"dfg",-3]
print(list1.index(-3) )   #will print the index of the element -3 

###                           sum()
list1=[1,2234,34.5,-3]
print(sum(list1))         #finds the sum

