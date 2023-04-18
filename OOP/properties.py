from multiprocessing.sharedctypes import Value
from turtle import Turtle


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(['cheese','tomato'])
print(pizza.pineapple_allowed)
print(pizza.toppings[0])


class person:
    def __init__(self,age):
        self.age = int(age)
    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

kwes = person('34')
print(kwes.isAdult)



'''properties - also used to define setter/getter functions
    setter - stes the corresponding prop value
    getter - gets the value'''
print('------------------------')
class pizza:
    def __init__(self,toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input('enter password')
            if password == 'swordfish':
                self._pineapple_allowed = Value

            else:
                raise ValueError('Alert!Intruder!')
pizza = Pizza(['cheesee','tomato'])
print(pizza.pineapple_allowed)

print(pizza.pineapple_allowed)

