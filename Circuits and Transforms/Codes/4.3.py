import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def H(s):
    return (5*10**5)/(s + 1.5*10**6)

vec_H = sp.vectorize(H)

s = np.linspace(-5e6,2e6,1000)

plt.grid()
plt.plot(s,vec_H(s),color ="red")
plt.savefig("../Figs/4.3.png")
plt.show()
