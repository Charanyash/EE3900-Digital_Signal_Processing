import  numpy as np
import scipy 
import matplotlib.pyplot as plt

def H(z):
    num  = np.polyval([1,0,1],z**-1)
    den  = np.polyval([0.5,1],z**-1)
    H = num/den
    return H
def Theo_H(w):
    return np.abs(4*np.cos(w))/np.sqrt(5 + 4*np.cos(w))
vec_Theo_H = scipy.vectorize(Theo_H)
omega = np.linspace(-3*np.pi,3*np.pi,100)
vec_H = scipy.vectorize(H)

plt.plot(omega,abs(vec_H(np.exp(1j*omega))))
plt.plot(omega,vec_Theo_H(omega),"o")
plt.title("Filter Frequency Response")
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("$|H(e^{\jmath\omega})| $")
plt.savefig("Assignment 1/Figs/dtft.png")
plt.show()




