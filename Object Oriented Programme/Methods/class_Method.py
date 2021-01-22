class Employee:
    company="Google"
    salary=100
    @classmethod
    def changeSalary(self,sal):
        self.salary=sal

vignesh=Employee()
print(f"vignesh salary : {vignesh.salary}")
print(f"Employee salary : {Employee.salary}")
vignesh.changeSalary(500)
print(f"vignesh salary : {vignesh.salary}")
print(f"Employee salary : {Employee.salary}")
Employee.changeSalary(100)
print(f"vignesh salary : {vignesh.salary}")
print(f"Employee salary : {Employee.salary}")


