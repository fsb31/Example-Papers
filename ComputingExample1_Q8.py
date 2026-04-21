import numpy as np

def f(x, y):
    return np.exp(x * y) * (np.cos(y) ** 2) * np.sin(x**2)

def g(x, y):
    tmp = x**2 + y**2
    if (tmp >= 1.0): return 0.0
    return (1.0 - tmp)**0.5


def mean(a, b, N):
    f_bar = 0

    for i in range(0, N-1, 1):
        f_bar += f(np.random.uniform(-a, a), np.random.uniform(-b, b))

    return 4*a*b*f_bar / N

def pi_approx(a, b, N):
    g_bar = 0

    for i in range(0, N-1, 1):
        g_bar += g(np.random.uniform(-a, a), np.random.uniform(-b, b))

    return 6*a*b*g_bar / N

if (False):
    print(f"N = 10^2: mean = {mean(1, 1, 10**2)}")
    print(f"N = 10^5: mean = {mean(1, 1, 10**5)}")
    print(f"N = 10^6: mean = {mean(1, 1, 10**6)}")

if (True):
    print(f"N = 10^2: pi = {pi_approx(1, 1, 10**2)}")
    print(f"N = 10^5: pi = {pi_approx(1, 1, 10**5)}")
    print(f"N = 10^6: pi = {pi_approx(1, 1, 10**6)}")
    
