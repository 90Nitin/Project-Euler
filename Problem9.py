import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

a, b = np.meshgrid(np.arange(1, 1001), np.arange(1, 1001))

c = np.sqrt(np.power(a, 2) + np.power(b, 2))

c1 = c.astype(int)

z = a+b+c

# z_cond = np.where(z!=1000)

# z[z_cond] = np.nan

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(a, b, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()


