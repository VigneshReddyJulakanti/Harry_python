class C2d:
    def __init__(self,icap,jcap):
        self.icap=icap
        self.jcap=jcap
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3d(C2d):
    def __init__(self,icap,jcap,kcap):
        super().__init__(icap,jcap)
        self.kcap=kcap

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

a=C2d(3,4)
b=C3d(30,7,5,)
print(a)
print(b)
