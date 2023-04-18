class Arc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        len_lon = max(len(self.a),len(self.b))+2
        len_a = len_lon - len(self.a)
        len_b = len_lon - len(self.b) - 1
        soln = int(self.a) + int(self.b)
        len_s = len_lon - len(str(soln))
        print('\n'.join([' '*len_a+ self.a,'+' + ' '*len_b +self.b,'-'*len_lon,' '*len_s+ str(soln)]))
a = Arc('346','3')
a.add()


print('----------------')
list = ["32 + 8", "1 + 3801"]
print(tuple(list[0].split('+')))


a = '32 + 8'
print(a.split('+'))


list = ["32 + 8", "1 + 3801"]