import numpy as np
import matplotlib.pyplot as plt

import scipy

def u(t):
    if t > 0.0 :
       return 1.0
    elif t ==0.0:
        return 1/2 
    else :
        return 0.0

def V_c(t):
    return 4*u(t)*(1 - np.exp(-3*1e6*t/2))/3

t = np.linspace(0,0.000001,1000000)

vec_V_c  = scipy.vectorize(V_c)
spice = np.loadtxt("2.8.dat")

plt.grid()
plt.plot(t,vec_V_c(t))
plt.plot(spice[:,0],spice[:,1],'o')
plt.xlabel("$t$")
plt.ylabel("$V_c(t)$")
plt.legend(["analytical","ngspice"])
plt.savefig(r"../Figs/2.8.png")
plt.show()
