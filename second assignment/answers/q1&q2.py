import numpy as np
import matplotlib.pyplot as plt


# function for question 1
# step is difference between signal inputs, since we are integrating in CTE we need dt
def conv(x, h, step):
    length = len(h) - 1
    arr1 = np.zeros((length,))
    arr2 = np.zeros((length,))
    x = np.concatenate([arr1, x, arr2])
    h = h[::-1]
    y = np.zeros((len(x) - len(h) + 1,))
    for i in range(len(y)):
        y[i] = np.sum(x[i:i + len(h)] * h * step)
    return y


# functions for 2 a
def x1(n):
    return np.exp(2 * n) * (-np.heaviside(n - 2, 1) + np.heaviside(n + 3, 1))


def a_h1(n):
    return np.heaviside(n + 10, 1) - np.heaviside(n, 1)


def a_h2(n):
    return 3 * delta(n - 5) - delta(n)


def delta(n):
    return np.heaviside(n, 1) - np.heaviside(n - 1, 1)


# functions for 2 b

def x2(t):
    return np.power(0.25, 2 * t) * np.heaviside(t + 3, 1)


def b_h1(t):
    return np.fabs(t) * (np.heaviside(t - 2, 1) - np.heaviside(t, 1))


def b_h2(t):
    return np.heaviside(t + 5, 1)


n1 = np.arange(-10, 11, 1)
n2 = np.arange(-20, 21, 1)
plt.stem(n1, x1(n1), markerfmt='ro')
plt.show()
plt.stem(n2, conv(x1(n1), a_h1(n1), 1), markerfmt='bo')
plt.show()
plt.stem(n2, conv(x1(n1), a_h2(n1), 1), markerfmt='go')
plt.show()

t1 = np.arange(-15, 15, 0.1)
t2 = np.arange(-30, 30, 0.1)
plt.plot(t1, x2(t1), 'r')
plt.show()
plt.plot(t2[1:], conv(x2(t1), b_h1(t1), 0.1), 'b')
plt.show()
plt.plot(t2[1:], conv(x2(t1), b_h2(t1), 0.1), 'g')
plt.show()

# Red is the main function, blue is after first convolve, green is after second convolve
