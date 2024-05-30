# Narysuj wykres 3D powierzchni
# z=x^2+y^2 dla x z zakresu od -2 do 2
# i y z zakresu od -2 do 2.

import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x = np.arange(-2, 2, 0.10)
y = np.arange(-2, 2, 0.10)
x, y = np.meshgrid(x, y)
z = x ** 2 + y ** 2

ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=plt.cm.coolwarm)
plt.show()
