import numpy as np
import matplotlib.pyplot as plt

#friction
def F(x_dot):
    f = 0.025 #'damping' force
    if (x_dot < 0): return f
    if (x_dot > 0): return -f
    return 0

#define variables
m = 1
k = 40
delta_t = 0.01

#creates x values
x = np.array([0.0]*int(20/delta_t))

#initial conditions
x[0] = 0.01
x[1] = 0.01

#loop
for t in range(1, int(20/delta_t)-1, 1):
    x_dot = (x[t] - x[t-1])/delta_t
    x[t+1] = (delta_t ** 2)*F(x_dot)/m + (2 - k*(delta_t**2)/m )*x[t] - x[t-1]


#plot
t = np.arange(0, 20, delta_t)
plt.plot(t, x, label="numerical")
plt.plot(t, 0.01*np.cos((k / m)**0.5 * t), label="analytical")

plt.xlabel("time")
plt.ylabel("x")
plt.legend()
plt.show()
