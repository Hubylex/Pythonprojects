'''magic methods / dunders - special methods which have double underscores
t the begining and end of their names eg: __init__, __add__'''

class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2d(self.x+other.x,self.y+other.y)

first = Vector2d(4,2)
second = Vector2d(6,9)

addition = first + second 
print(addition.x)
print(addition.y)


#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |'''


