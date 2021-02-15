import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
type(fig)
ax = Axes3D(fig)
#T = np.arange(1, 2, 0.1)
#Y = np.arange(-3, 4, 0.1)

T = np.arange(1, 2, 0.1)
Y = np.arange(-2, 5, 0.1)

T, Y = np.meshgrid(T, Y)
#R = T * np.abs(Y)
R = (0.5 * Y / T) + T**T * np.exp(T)
ax.plot_surface(T, Y, R, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.set_zlim(-1, 10)

pl.show()



