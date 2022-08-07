import numpy as np

x  = np.array([2,-1])
h  = np.array([-1,2,1])

y = np.convolve(x,h)
print(y)