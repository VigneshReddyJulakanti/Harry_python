#The key value in the dictionary are universal can be used in the functions to
#creating a dictionary and asigning it a name and value
a={
    "hlo":"hlo vignesh",
    "bye":"bye vignesh",
    "marks":[0,50,100],
    "another_dic":{"hlo":"hlo vignesh Reddy"}  #creating another dic inside a dic and assignining a name and value

}


print(a["hlo"])   #accesing 
print(a["marks"])
print(a["another_dic"]["hlo"]) #accesing a value in a dic which is in an another dic


#updating
a["hlo"]="Vignesh Reddy Julakanti"
print(a["hlo"])


