__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt


def mn1(x):
    return x ** 2 + 1


def a(x):
    return abs(x)/10


def mn2(x):
    return np.exp((-1) * a(x))


def podlog(x):
    m = mn1(x)
    n = mn2(x)
    return m * n


def base(x):
    return 1 + np.tan(1 / (1 + np.sin(x) ** 2))


def f1(x):
    return np.log(podlog(x)) / np.log(base(x))

x=np.arange(-100,100.01,0.01)
plt.plot(x, f1(x))
plt.show()