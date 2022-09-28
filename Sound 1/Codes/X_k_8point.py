import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt('fft.dat', dtype=float)
plt.stem(X)
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('$8$-point FFT')
plt.grid()
plt.savefig('../Figs/X_k_8point.png')
plt.show()

