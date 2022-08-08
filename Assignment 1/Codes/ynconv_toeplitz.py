import numpy as np
x = np.array([1,2,3,4,2,1])
n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2
def Conv(x,h):
  nx = len(x)
  nh = len(h)
  h_new = np.zeros([nx+nh-1,nx])
  for i in range(nx+nh-1):
    for j in range(nx):
        h_new[i][j] = h[i]
