__author__ = 'student'
import math


def mn1(x):
    return (math.e ** math.sin(x)) + 1


def mn2(x):
    return 5 * (x ** 15) + 4


def znam(x):
    m = mn1(x)
    n = mn2(x)
    return m * n


def chisl(x):
    return 4 * (x **15)


def podlog(x):
    z = znam(x)
    c = chisl(x)
    return c/z


def base(x):
    return x**2 + 1


def f1(x):
    b = base(x)
    p = podlog(x)
    return math.log(p, b)


print(f1(float(input())))