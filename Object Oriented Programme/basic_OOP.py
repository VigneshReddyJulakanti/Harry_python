#we use PascalCase in Class i.e ex--> EmployeeName

class Employee:                #creating a class
    company="google"


vignesh=Employee()            # creating an object vignesh from the class Employee
julakanti=Employee()          # creating another object named julakanti

print(vignesh.company)        # gets company of vignesh and prints
print(julakanti.company)      # gets company if julakanti and prints 

Employee.company="youtube"    #changes the value of company in the Employee class to youtube

print(vignesh.company)        # gets company of vignesh and prints
print(julakanti.company)      # gets company if julakanti and prints 


vignesh.salary=100000         #creates an attribute salary for the object vignesh and asign it a value 100000
print(vignesh.salary)         # gets the value assigned to vignesh with attribute salary and prints it


