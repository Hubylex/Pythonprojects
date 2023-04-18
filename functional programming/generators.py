# def countdown():
#     i = 5
#     while i > 0 :
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)


# def infinite():
#     while True:
#         yield 7
# ##for i in infinite():
#  #   print(i)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))