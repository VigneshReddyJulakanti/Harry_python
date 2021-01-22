#######################
# will give an unbound error

# a=2
# def hl():
    
#     a=a+1
#     print(a)
# hl()
######################


di={"a":"2"}
def hl():
    
    di['a']=int(di['a'])+1
    print(di['a'])
hl()

#This resolves the problem 
#as the key value pairs in the dictionary are universal