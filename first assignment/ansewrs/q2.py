import numpy as np
import matplotlib.pyplot as plt


def x3(t):
    res = 0
    for n in range(-20, 21):
        res += np.exp((abs(n+2*t))*-1)
    return res

def dirac(n):
    return int(n == 0)


def dirac_array(n):
    res=np.ndarray(shape=n.shape)
    for i in range(len(n)):
        res[i]=dirac(n[i])
    return res

def x4(n):
    return np.heaviside(n - 3, 1) - np.heaviside(3-n, 1) + dirac_array(n)*2


t = np.arange(-6.0, 6.0, 0.01)
n = np.arange(-6.0, 7.0, 1.0)
plt.plot(t, x3(t), "r")
plt.plot(n, x4(n), "bo")
plt.show()