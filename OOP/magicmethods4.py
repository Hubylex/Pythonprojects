#There are several magic methods for making classes act like containers.
#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in


import random

class VagueList:
    def __init__(self,cont):
        self.cont = cont
    
    def __getitem__(self,index):
        return self.cont[index + random.randint(-1,1)]

    def __len__(self):
        return random.randint(0,len(self.cont)*2)

vague_list = VagueList(['A','B','C','D','E'])
print(len(vague_list))   ## the len() calls the  __len__ func
print(len(vague_list))
print(vague_list[1])     ## the vague_list[] calls the __getitem__ func
print(vague_list[1])
