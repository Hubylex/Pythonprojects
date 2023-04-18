class Rectangle:
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def calc_area(self):
        return self.w * self.h
    @classmethod
    def new_square(cls,side_len):
        return cls(side_len,side_len)


square = Rectangle.new_square(5)
print(square.calc_area())


