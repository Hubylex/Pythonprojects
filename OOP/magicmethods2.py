class SpecialString:
    def __init__(self,cont):
        self.cont = cont
    def __truediv__(self,other):
        line = '=' * max(len(other.cont),len(self.cont))
        return '\n'.join([self.cont,line,other.cont])


spam = SpecialString('spam')
hello = SpecialString('Hel')
print(spam/hello)