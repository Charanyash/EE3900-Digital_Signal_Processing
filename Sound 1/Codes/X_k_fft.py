import numpy as np

x_n = np.array([1,2,3,4,2,1])
pad_x_n = np.pad(x_n,(0,2),'constant',constant_values = (0))

N = len(pad_x_n)
def Perm(N):
    P = np.zeros((N,N))
    for i in range(N):
        if i%2 == 0:
            P[i][i//2] = 1
        else :
            P[i][(N+i-1)//2] = 1
    return P
def diag(N):
    
    W = np.exp(-2*np.pi*1j/N)

    v = [W**k for k in range(int(N/2))]
    D_n = np.diag(v)
    return D_n

def F_n_decom(N):
    if N==1 :
        return [[1]]
    else :
        v = np.dot(F_n_decom(N//2),diag(N)).T
        u = -v
        k = F_n_decom(N//2)
        F_n = np.matmul(np.bmat([[k,v],[k,u]]),Perm(N))
        return F_n
F_N = np.dot(F_n_decom(N),Perm(N))
X_k = np.dot(F_N,pad_x_n)

print(X_k)
plt.stem(np.real(X_k.T))
plt.grid()
plt.xlabel("k")
plt.ylabel("X(k)")
plt.title("DFT using FFT")
plt.savefig("../Figs/X_k_fft.png")
plt.show()
