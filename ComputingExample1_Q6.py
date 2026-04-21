def f(x):
    return x**3 + x**2

def integrate(a, b, f, x, w):
    result = 0

    for i in range(0, len(x), 1):
        result += w[i] * f(x[i])

    return result * (b-a)



actual = 8500/3

a = 0
b = 10

#trapezoidal
x = [a, b]
w = [.5, .5]

i = integrate(a, b, f, x, w)
print(f"Trapezoidal: {i}\nError: {abs(actual - i)}")



#simpson
x = [a, (a+b)*0.5, b]
w = [1/6, 2/3, 1/6]

i = integrate(a, b, f, x, w)
print(f"Simpson's: {i}\nError: {abs(actual - i)}")

#gauss
x = [.5*(a+b+(b-a)/(3**0.5)), .5*(a+b-(b-a)/(3**0.5))]
w = [.5, .5]

i = integrate(a, b, f, x, w)
print(f"Gauss's: {i}\nError: {abs(actual - i)}")

"""

For all above, the accuracy could be improved by increasing the number of points to integrate / decreasing the size of the 'polygons'.

"""
