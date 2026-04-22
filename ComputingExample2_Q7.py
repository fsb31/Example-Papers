import numpy as np





def minimise(f, x, tol):
    x_0 = x
    df = f.deriv()
    d2f = f.deriv(2)
    
    itrs = 0
    while True:
        itrs+=1
        x = x - (d2f(x))**-1 * df(x)
        if (abs(df(x)) / abs(df(x_0))) < tol or itrs > 50:
            print(f"x = {x}, \nf(x) = {f(x)}, \nIterations: {itrs}")
            return x


a = 2
b = 100

def f2(x):
    return (a - x[0])**2 + b*(x[1] - x[0]**2)**2

def g(x):
    return np.array([-2*(a-x[0]) - 4*b*x[0]*(x[1]-x[0]**2), 2*b*(x[1]-x[0]**2)])

def j(x):
    return np.array([[2 - 4*b*x[1] + 12*b*x[0]**2, -4*b*x[0]], [-4*b*x[0], 2*b]])

def minimise_multi(x, tol):
    x_0 = x
    itrs = 0

    while True:
        itrs += 1
        x = x - np.linalg.solve(j(x), g(x))
        if (np.linalg.norm(g(x))/np.linalg.norm(g(x_0))) < tol or itrs > 50:
            print(f"Minimum: {f2(x)}\nx0 = {x[0]}, x1 = {x[1]},\nIterations: {itrs}")
            return x


f = np.polynomial.polynomial.Polynomial([0, 0, 1, 1])

minimise(f, 2, 1e-9)

minimise_multi([1.1, 1.1], 1e-9)
