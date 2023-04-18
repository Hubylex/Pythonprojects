

def decor(func):
    def wrap():
        print('-------')
        func()
        print('-------')
    return wrap

def text():
    print('hey hubert')

text = decor(text)
text()

## different ways of achieving same things
@decor
def num():
    print('2 4 6 8')
num()

## problem
def decor(func):
    def wrap(num):
        print('***')
        func(num)
        print('***')
        print('END OF PAGE')
    return wrap

@decor 
def invoice(num):
    print("INVOICE #"+num)

invoice(input())

