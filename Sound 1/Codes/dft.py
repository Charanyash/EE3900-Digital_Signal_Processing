import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20
def u(n):
    if n <0:
        return 0
    else :
        return 1
def x(n):
    if n < 0 or n >5 :
        return 0
    elif n < 4:
        return n+1
    else :
        return 6-n

def h(n):
    return (-1/2)**n*u(n) + (-1/2)**(n-2)*u(n-2)

def X(k,N):
    sum  = 0
    for i in range(N):
        sum += x(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum

def H(k,N):
    sum  = 0
    for i in range(N):
        sum += h(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum

vec_X = scipy.vectorize(X)
vec_H = scipy.vectorize(H)

k = np.arange(N)
plt.subplot(211)

plt.stem(k,np.real(vec_X(k,N)))

plt.ylabel("$X(k)$")
plt.grid()

plt.subplot(212)

plt.stem(k,np.real(vec_H(k,N)))
plt.xlabel("k")
plt.ylabel("$H(k)$")
plt.grid()


plt.savefig("Sound 1/Figs/dft.png")
plt.show()