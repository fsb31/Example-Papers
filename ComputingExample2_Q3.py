def f(x):
    return x**2 - 1

def d_f(x):
    return 2*x


def one_side(x, h):
    return (f(x+h) - f(x))/h

def symmetric(x, h):
    return (f(x+h) - f(x-h))/2*h


print(f"one sided, h=.04: {one_side(5, .04) - d_f(5)}")
print(f"one sided, h=.03: {one_side(5, .03) - d_f(5)}")
print(f"one sided, h=.02: {one_side(5, .02) - d_f(5)}")
print(f"one sided, h=.01: {one_side(5, .01) - d_f(5)}")

print(f"Errors multiplied by x100 for symmetric")
print(f"symmetric, h=4: {(symmetric(5, 4) - d_f(5))*100}")
print(f"symmetric, h=3: {(symmetric(5, 3) - d_f(5))*100}")
print(f"symmetric, h=2: {(symmetric(5, 2) - d_f(5))*100}")
print(f"symmetric, h=1: {(symmetric(5, 1) - d_f(5))*100}")


