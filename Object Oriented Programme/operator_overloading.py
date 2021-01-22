# Operator overloading means to add an extrafeature to an existing operator , here we add a feature which will add the two objects 

class Number:
    def __init__(self,num):
        self.num=num

    def __add__(num1,num2):      #when + operator
        return num1.num + num2.num

    def __mul__(num1,num2):    # when * operator
        return num1.num * num2.num

    def __str__(self):         #when we try to print a object
        return f"{self.num}"

    def __len__(self):        #when we want the length
        num=str(self.num)
        return len((num))

n1=Number(5)
n2=Number(10)
n3=n1+n2
print(n3)
n4=n1*n2
print(n4)
print(n1)
print(len(n2))
