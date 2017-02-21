import numpy


def fib(a1, a2, ind):
    return a1+a2, ind+1

index = 2
a1 = 1
a2 = 1

while True:
    t, index = fib(a1, a2, index)
    a1 = a2
    a2 = t
    # print(a2, index)
    if a2 > 10**999-1:
        break
print(index)
