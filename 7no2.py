__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
plt.plot(x, x ** 2 - x - 6)
plt.show()

x = -10
n = False
y = x ** 2 - x - 6
while x < 10.01:
    if y > 0:
        while y > 0:
            y = x ** 2 - x - 6
            x += 0.01
        print (x)
        n = True
    if y < 0:
         while y < 0:
             y = x ** 2 - x - 6
             x += 0.01
         print (x)
         n = True
if n == False:
    print('Нет корней')