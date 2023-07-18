r = {
  63   :  100,
  37.5 :  94.46,
  19   :  88.5,
  13.2 :  84.6,
  9.5  :  80.9,
  6.7  :  69.9,
  4.575:  59.3,
  2.36 :  30.1,
  1.18 :  20.3,
  0.6  :  13.7,
  0.212:  6.4,
  0.075:  0
}
mass = [0,26,28,18,20,49,50,137,46,31,34,30]
mt = sum(mass)
cumm = 0
finer = []
for i in mass:
    cumm +=i
    fine = ((mt-cumm)/mt)*100
    finer.append(fine)

r2 = {k:v for k,v in zip(r.keys(),finer)}
print(r2)


def intp(r,value):
    rev_dict = {v:k for k,v in r.items()}

    if value in r.values():
        for k,v in r.items():
          if value == v:
              return k
    else:
        l = list(r.values())
        for i in range(len(l)-1):
            if value < l[i] and value >l[i+1]:
                ub = l[i]
                lb = l[i+1]
                return ((((rev_dict.get(ub)-rev_dict.get(lb))/(ub-lb))*(ub-value)) - rev_dict.get(ub))*(-1)
    
for v in [10,30,60]:
    print(f'D{v} value: {intp(r,v)}')
print('--------------------')
for s in [10,30,60]:
    print(f'D{s} value: {intp(r2,s)}')

