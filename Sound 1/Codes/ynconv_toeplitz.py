import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,2,1])
n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2
nx = len(x)
nh = len(h)

#Convolution using toeplitz matrix
def Conv(x,h):
  h_new = np.zeros([nx+nh-1,nx]) #h_new is intialised with zeros.  
  for i in range(nx+nh-1):
    if i < nh:
     for j in range(nx):
      if j <= i :
        h_new[i][j] = h[i-j]
    else :
     for j in range(nx-1):
      h_new[i][j+1] = h_new[i-1][j]  
  return h_new @ x #Multiplying the two matrices gives the convolution of x and h.

y = Conv(x,h)

plt.stem(range(0,nx+nh-1),y)
plt.grid()
plt.xlabel("n")
plt.ylabel("y(n)")
plt.title("Filter Output using Convolution")
plt.savefig("Sound 1/Figs/ynconv_toeplitz.png")
plt.show()  