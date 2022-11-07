import numpy as np
import matplotlib.pyplot as plt

import scipy as sc

f = 50

A_0 = 12

def x(t) :
    return A_0*abs(np.sin(2*np.pi*f*t))

t = np.linspace(-5/(2*f),5/(2*f),2000)

vec_x = sc.vectorize(x)

plt.plot(t,vec_x(t))
plt.grid()
plt.savefig("../Figs/1.1.png")
plt.show()
