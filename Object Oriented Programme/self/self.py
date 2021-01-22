# "self" is used to pass as a parameter for a function, which says self is nothing but the object instance

class Employee:
    def getSalary(self):
        print("salary is 100k")

vignesh=Employee()
vignesh.getSalary()