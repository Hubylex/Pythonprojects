class ArrangeCalc:
    def __init__(self,top,down):
        self.t = top
        self.d = down
    def __add__(self):
        return self.t , self.d

a = ArrangeCalc(2,4)
print(a)