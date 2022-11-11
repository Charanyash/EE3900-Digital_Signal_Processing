import numpy as np
import matplotlib.pyplot as plt

import scipy as sc

f = 50

A_0 = 12

def x(t) :
    return A_0*abs(np.sin(2*np.pi*f*t))

def c(k):
    if k%2 ==0:
        return (2*A_0)/(np.pi*(1 - k**2))
    else :
        return 0

vec_c = sc.vectorize(c)  

def a(k):
    if k %2 != 0:
        return 0
    elif k == 0:
        return (2*A_0)/np.pi
    else :
        return (4*A_0)/(np.pi*(1 - k**2))

vec_a = sc.vectorize(a)

def b(k):
    return 0 
vec_b = sc.vectorize(b)

def x_fou(t):
 k = np.arange(-10,10,dtype = int)
 x_t = np.dot(vec_c(k),np.exp(2j*np.pi*k*f*t))
 return x_t

def x_real_fou(t):
    k = np.arange(0,10,dtype = int)
    x_t = np.dot(vec_a(k) , np.cos(2*np.pi*k*f*t)) + np.dot(vec_b(k) , np.sin(2*np.pi*k*f*t)) 
    return x_t

t = np.linspace(-5/(2*f),5/(2*f),2000)

t_2 = np.linspace(-5/(2*f),5/(2*f),200)
vec_x = sc.vectorize(x)
vec_x_fou = sc.vectorize(x_fou)
vec_x_real_fou = sc.vectorize(x_real_fou)


plt.plot(t,vec_x(t))
plt.plot(t_2,vec_x_real_fou(t_2),'.')
plt.legend(["Original","Real Fourier "])
plt.grid()
plt.savefig("../Figs/2.6.png")
plt.show()
