import sys
import numpy as np

#A, B, C - params
def f(x):
    return A * x**2 + B*x + C

#a,b - borders



def golden_search(f, a, b, tol=1e-5):
    tau = (np.sqrt(5) + 1) / 2.0
    y = a + (b - a) / tau**2
    z = a + (b - a) / tau
    f_y = f(y)
    f_z = f(z)
    f_list = []
    while b - a > tol:
        if f_y <= f_z:
            b = z
            z = y
            y = a + (b - a) / tau**2
            f_z = f_y
            f_y = f(y)
        else:
            a = y
            y = z
            z = a + (b - a) / tau
            f_y = f_z
            f_z = f(z)
        f_list.append(f((a + b) / 2.0))
    return f_list

def binary_search(f, a, b, epsilon):
    c = (a + b) / 2
    f_a = f(a)
    f_b = f(b)
    f_c = f(c)
    f_list = []
    while abs(b - a) > epsilon:
        y = (a + c) / 2.0
        z = (b + c) / 2.0
        f_y = f(y)
        f_z = f(z)
        if f_y <= f_c:
            b = c
            c = y
            f_b = f_c
            f_c = f_y
        else:
            if f_c <= f_z:
                a = y
                b = z
                f_a = f_y
                f_b = f_z
            else:
                a = c
                c = z
                f_a = f_c
                f_c = f_z
        f_list.append(f_c)
    return f_list

#A, B, C, x1, x2, eps = map( float, input().split(' '))
#A, B, C, x1, x2, eps = 1.2986050270005514, -2.0641037352976244, 2.745841060547063 -1.104085030607, 3.068794869526759, 1e-07
#A, B, C, x1, x2, eps = -1.8936826187859033, -1.3167532137043012, -1.3029782083232486, -4.903400730538973, 4.801199616683266, 1e-07
A, B, C, x1, x2, eps =

#f_app = golden_search(f, x1, x2, eps)

f_app


print (len(f_app) * sum(f_app[-5:]))