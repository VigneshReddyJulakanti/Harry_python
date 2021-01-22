# multiple  inheritance occurs when the child class has more than one parent class
class Employee:
    company="google"
    initial_salary=20000
    salaryincrementpermonth=10000
    def Gsalary(self):
        print(f"Google salary is :{int(self.initial_salary) + (int(self.month)-1)*self.salaryincrementpermonth}")

class Freelancer:
    company="Fiverr"
    level=0
    def upgradelevel(self):
        self.level=self.level+1
        
class programmer(Freelancer,Employee):
    def name(self):
        print(f"this.name")

vignesh=programmer()  
print(vignesh.company)  # will print "Fiverr" as in line 6 , Freelancer is the first parameter

vignesh.upgradelevel()
print(vignesh.level)  

vignesh.month=3
vignesh.Gsalary()



