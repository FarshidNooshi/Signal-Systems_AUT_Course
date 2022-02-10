import numpy as np
import matplotlib.pyplot as plt

F_ZERO = [0,1/8,1/4,3/8,1/2,5]



def x1(t, inp):
    return np.cos(np.pi * 0.5 * inp * t) * np.cos(np.pi * 0.5 * inp * t)


def x2(n, val):
    return np.cos(np.pi * 2 * val * n)


t = np.arange(0.0, 10.0, 0.001)
n = np.arange(0.0, 11.0, 1)
for inp in F_ZERO:
    print(inp)
    plt.plot(t, x1(t, inp), "r")
    plt.plot(n, x2(n, inp), "bo")
    plt.show()

