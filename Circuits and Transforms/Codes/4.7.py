import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

def y_cont(t):
    if t < 0:
        return 0
    else :
        return  2*(1 - np.exp(-1.5*t*10**6))/3 
def y_disc(n):
    if n < 0 :
        return 0
    else :
        return  2/3 * (1 - (1 - 7.5e5 * 1e-7)**(n*1e7)/(1 + 7.5e5 * 1e-7)**(n*1e7))

#def y_diff(n):
#    a = (1 - 7.5*10**5)/(1 + 7.5*10**5)
#    b = 10**6/(1 + 7.5*10**5)
#    if n < 0 :
#        return 0
#    else :
#        return a*y_diff(n-1) + b
def u(n):
    if n>=0:
        return 1.00
    else:
        return 0.00
def y_diff(n):
    if n < 0:
        return 0
    else:
        return y_diff(n-1)*(((1 - 0.075)/(1 + 0.075))**(n*1e7))+((u(n)+u(n-1))*2/3)*(1 - ((1 - 0.075)/(1 + 0.075))**(n*1e7))

y_con = sc.vectorize(y_cont)    

y_dis = sc.vectorize(y_disc)

y_dif = sc.vectorize(y_diff)

t = np.linspace(0,5e-6,101)
spice = np.loadtxt("4.7.dat")

plt.grid()
plt.plot(t,y_con(t))
plt.plot(spice[:,0],spice[:,1],'o')
plt.plot(t,y_dis(t),'o')
plt.plot(t,y_dif(t),'.')
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.legend(["$y(t)$","ngspice","$y(n)$","$y_{diff}(n)$"])
plt.savefig("../Figs/4.7.png")
plt.show()
