import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + np.cos(10*x)/5

x = np.arange(0, 50, 1) * (2 * np.pi)/50

y = f(x)

mean = np.array([0.0]*50)

mean[0] = (y[0] + y[1])/2
mean[-1] = (y[-1] + y[-2])/2

for i in range(1, 49, 1):
    mean[i] = (y[i-1] + y[i] + y[i+1])/3


plt.plot(x, y, label="actual")
plt.plot(x, mean, label="average")
plt.legend()
plt.show()
