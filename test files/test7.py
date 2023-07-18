
p_size = [4.75,2,0.85,0.425,0.25,0.18,0.15,0.075]
mass = [0,40,60,89,140,122,210,56,12]
mt = sum(mass)
cumm = 0
finer = []
for i in mass:
    cumm +=i
    fine = ((mt-cumm)/mt)*100
    finer.append(fine)
[print(cumm)]
axis = {k:v for k,v in zip(p_size,finer)}
print(axis)


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
    print(f'D{v} value: {intp(axis,v)}')

