import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x*y*(2 - x - 2*y)

x = np.linspace(-20, 20, 400)
y = np.linspace(-20, 20, 400)

_x, _y = np.meshgrid(x, y)

z = f(_x, _y)


plt.contour(_x, _y, z)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(_x, _y, z, cmap='cool')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
