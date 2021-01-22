# single inheritance occurs when child class inherits only a single parent class
class Employee:   #Base class
     company="google"
     salary=50000
     def hlo(self):
         print(f"hlo {self.name}")

class Programmer(Employee):   # declaring in heritence class
    company="pro"
    

vignesh=Employee()
jarvis=Programmer()
print(vignesh.company)
print(jarvis.company)
print(vignesh.salary)     #50000
print(jarvis.salary)      #50000


# in basic inheritance we used single inheritance as an example