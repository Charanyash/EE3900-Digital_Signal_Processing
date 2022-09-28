import numpy as np
import matplotlib.pyplot as plt
import scipy

x_n = np.array([1,2,3,4,2,1])
pad_x_n = np.pad(x_n,(0,2),'constant',constant_values = (0))
def DFT(x_n):
    N = len(x_n)

    W = np.exp((-2*np.pi*1j)/N)

    F_n = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            F_n[i][j] = W**(j*i)

    X_k = np.dot(F_n,x_n)

    return np.real(X_k)


plt.stem(DFT(pad_x_n))
plt.grid()
plt.xlabel("k")
plt.ylabel("X(k)")
plt.savefig("../Figs/X_k_dft.png")
plt.show()







