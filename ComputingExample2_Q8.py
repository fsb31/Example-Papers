import numpy as np


class Rosenbrock:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f(self, x):
        return (self.a - x[0])**2 + self.b*(x[1] - x[0]**2)**2
    
    def g(self, x):
        return np.array([-2*(self.a-x[0]) - 4*self.b*x[0]*(x[1]-x[0]**2), 2*self.b*(x[1]-x[0]**2)])
    
    def j(self, x):
        return np.array([[2 - 4*self.b*x[1] + 12*self.b*x[0]**2, -4*self.b*x[0]], [-4*self.b*x[0], 2*self.b]])




def minimise(rb, x, tol):
    x_0 = x
    itrs = 0
    
    while True:
        itrs += 1
        x = x - np.linalg.solve(rb.j(x), rb.g(x))
        if (np.linalg.norm(rb.g(x))/np.linalg.norm(rb.g(x_0))) < tol or itrs > 50:
            print(f"Minimum: {rb.f(x)}\nx0 = {x[0]}, x1 = {x[1]},\nIterations: {itrs}")
            return x



rb = Rosenbrock(2, 100)
minimise(rb, [1.1, 1.1], 1e-9)
