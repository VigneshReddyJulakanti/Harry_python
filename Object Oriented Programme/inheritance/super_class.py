class Person:
    country="India"

    def takeBreath(self):
        print("I am breathing")
class Company(Person):
    company="Google"
    def takeBreath(self):
        print("I am also taking breath")
class Youtuber(Company):
    platform="Youtube"
    def takeBreath(self):
        super().takeBreath()                # used to implement its super class functions
        print("I am also taking a long breath")

vignesh=Youtuber()
vignesh.takeBreath()