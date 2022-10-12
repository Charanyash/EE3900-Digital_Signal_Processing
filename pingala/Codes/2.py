import numpy as np
import matplotlib.pyplot as plt
import scipy

def Pingala(n):
    if n < 0 :
        return 0
    elif n <2 :
        return 1
    else :
        return Pingala(n-1) + Pingala(n-2)

def y(n):
    if n >=0:
        return Pingala(n-1) + Pingala(n+1)
    else :
        return 0
#2.2

Pingala_series = scipy.vectorize(Pingala)

n = np.arange(10)

plt.figure(1)
plt.stem(n,Pingala_series(n))
plt.xlabel("n")
plt.ylabel("$x(n)$")
plt.grid()
plt.savefig("../Figs/2.2.png")
#plt.show()

#2.5
vec_y = scipy.vectorize(y)

plt.figure(2)
plt.stem(n,vec_y(n))
plt.xlabel("n")
plt.ylabel("$y(n)$")
plt.grid()
plt.savefig("../Figs/2.5.png")
plt.show()


