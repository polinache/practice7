__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt


def V(x):
    s = 0
    for n in range (300):
        s += (1/2)**n * np.cos((3**n)*np.pi*x)
    return s

x=np.arange(-2,2.01,0.01)
plt.plot(x, V(x))
plt.show()