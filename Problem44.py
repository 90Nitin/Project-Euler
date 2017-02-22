import numpy as np

vec_a = np.arange(1,5*10**3+1,1)

A, B = np.meshgrid(vec_a, vec_a)


def to_pentagon(n):
    return ((3*n**2)-n)/2


def is_pentagon(k):
    if k.all<=0:
        return False
    else:
        n = (1+np.sqrt(1 + 24*k))/6
        return np.equal(np.mod(n, 1), 0)


sum_pentagon = is_pentagon(to_pentagon(A) + to_pentagon(B))
diff_pentagon = is_pentagon(to_pentagon(A) - to_pentagon(B))


np.where((sum_pentagon==True)*(diff_pentagon==True)==True)
# 2167 and 1020
D = to_pentagon(2167) - to_pentagon(1020)