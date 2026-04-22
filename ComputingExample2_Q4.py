import numpy as np

def f(x):
    return x**2 * np.sin(x**2)

def d_f(x):
    return 2*x*np.sin(x**2) + x**3 * 2 * np.cos(x**2)


def complex_step(x, h):
    return (f(complex(x, h)).imag) / h

def symmetric(x, h):
    return (f(x+h) - f(x-h))/(2*h)

x = [10, 100, 1000, 10000]
h = [1e-9, 1e-12, 1e-15]

for i in x:
    print(f"Testing x={i}")
    for j in h:
        print(f"h = {j}:\nComplex: {abs((complex_step(i, j) - d_f(i))/d_f(i))}\nSymmetric: {abs((symmetric(i, j) - d_f(i))/d_f(i))}")

