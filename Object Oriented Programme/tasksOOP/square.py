class number:
    def __init__(self,num):
        self.number=num

    def getSquare(self):
        print(f"{int(self.number)*int(self.number)}")
    def getSquareRoot(self):
        print(f"{self.number **0.5}")
    def getCube(self):
        print(f"{self.number **3}")
        
a5=number(5)
a5.getSquare()
a5.getSquareRoot()
a5.getCube()
