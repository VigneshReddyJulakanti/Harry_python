# To say we dont need self here but if we dont take self as a parameter then it will return error
# To over come that problem @staticmethod is used in front of the function
class Employee:
    @staticmethod
    def getSalary():
        print("salary is 100k")

vignesh=Employee()
vignesh.getSalary()