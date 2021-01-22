a={
    "hlo":"hlo vignesh",
    "bye":"bye vignesh",
    "marks":[0,50,100],
    "another_dic":{"hlo":"hlo vignesh Reddy"}  #creating another dic inside a dic and assignining a name and value

}

print(list(a))  #will print the value names( i.e keys)
print(a.values())  #will retun the values in list form
print(a.items())  #Will return key value pair as list
update_dic={
    "name":"vigneh Reddy Julakanti"
}
a.update(update_dic)  #updates the dic a by adding new key value pairs from update_dic
print(a)



########                     diff between .get and []                          ####
# print(a.get("hloooo")) #will return None if hlooo key is not found
# print(a["hlooooo"])    #will return an error
