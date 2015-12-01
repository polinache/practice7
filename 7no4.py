__author__ = 'student'
import numpy as np
from matplotlib import mlab
import pylab

tmin = -20.0
tmax = 20.0
dt = 0.01
tlist = mlab.frange (tmin, tmax, dt)

pylab.ion()

for a in range (1000):
        ylist = [np.cos(2*t) for t in tlist]
        xlist = [np.sin(t+a/10) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()