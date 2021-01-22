class Employee:
    company="google"
    def getSalary(self):
        print(f" In {self.company} salary is {self.salary}")

vignesh=Employee()
vignesh.salary=100000
vignesh.getSalary()               #Employee.getSalary(vignesh)
