# Sieve of Erastothenes

import numpy as np

a_all = np.arange(2, (2 * 10 ** 6) + 1).tolist()

# a_all = np.arange(2, (10) + 1).tolist()

# a_all = np.arange(2, (50) + 1).tolist()


i = 0

while a_all[i] * 2 <= max(a_all):
    temp = set([a_all[i] * j for j in np.arange(2, int(max(a_all) / a_all[i]) + 1)])
    i += 1
    a_all = list(set(a_all) - temp)
    # print(a_all, a_all)

# print(sum(a_all))