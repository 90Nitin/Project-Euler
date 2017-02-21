import numpy as np

a = [1, 2]

b = 1

c = 2

while True:
    a.append(b+c)
    t = c
    c = b+c
    b = t
    if c > 4*10**6:
        break

a_2 = [i for i in a if i%2==0]

sum(a_2)  # done!