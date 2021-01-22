'''
class Employee:
    salary=500
    bonus=500
    @property
    def totalSalary(self):
        return self.salary + self.bonus

vignesh=Employee()
vignesh.bonus=1000
print(vignesh.totalSalary)

'''

#Make it a little advanced

class Employee:
    salary=500
    # bonus=500
    @property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter            # as this is set to totalSalary.setter and same def name , the value returned in the total salary is taken and stored in the parameter here followed by self
    def totalSalary(self,totsal):  
        self.bonus=totsal-self.salary
        return self.bonus
   
vignesh=Employee()

vignesh.bonus=1000
print(vignesh.totalSalary)

vignesh.totalSalary=1000
print(vignesh.bonus)










'''
# or 
#but in this it acts as a function , in above it acts as a parameter


class Employee:
    salary=500
    bonus=500
    def totalSalary(self):
        return self.salary + self.bonus

vignesh=Employee()
vignesh.bonus=1000
print(vignesh.totalSalary())
'''


