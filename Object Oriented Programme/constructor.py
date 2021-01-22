 #  __init__()
 # This is called constructor
 # This is a special function which runs when a object is created
 # Takes argument "self" additional arguments can also be given

class Employee:
     company="google"
     def __init__(self):
             print("Employee created")

vignesh=Employee()

########################################

class Employee2:
    company="youtube"
    def __init__(self,n,s):
        print(f"{n} works in {self.company} for a salary of {s}")
         
vignesh=Employee2("vignesh",100000)


##############################################

class Employee2:
    company="youtube"
    def __init__(self,n,s):
        self.name=n
        self.salary=s
        print(f"{n} works in {self.company} for a salary of {s}")
         
vignesh=Employee2("vignesh",100000)
print(vignesh.name)