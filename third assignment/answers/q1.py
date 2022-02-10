import matplotlib.pyplot as plt
import numpy as np

step = 0.001
t = np.arange(-3, 3 + step * 2, step)


def integrate(x):
    return np.sum(x) * step


def a(sig, k, T0):
    w0 = 2 * np.pi / T0
    x = sig * np.cos(k * w0 * t)
    return (2 / T0) * integrate(x)


def b(sig, k, T0):
    w0 = 2 * np.pi / T0
    x = sig * np.sin(k * w0 * t)
    return (2 / T0) * integrate(x)


def fourier_series(sig, C, T0):
    y = np.zeros((len(t),))
    y += a(sig, 0, T0) / 2
    w0 = 2 * np.pi / T0
    for k in range(1, C + 1):
        y += b(sig, k, T0) * np.sin(k * w0 * t) + a(sig, k, T0) * np.cos(k * w0 * t)
    return y


def plot(x, s, name):
    x_count = 0
    y_count = 0
    for c in range(0, 12):
        s[x_count, y_count].plot(t, x, 'r', label=f"{name}(t)")
        s[x_count, y_count].plot(t, fourier_series(x, c, 6), 'g', label=f'C = {c}')
        s[x_count, y_count].set(xlabel='t', title=name)
        s[x_count, y_count].legend()
        s[x_count, y_count].grid()
        y_count += 1
        if y_count == 2:
            y_count = 0
            x_count += 1


def first_signal():
    x1 = np.zeros((len(t),))
    for idx, val in enumerate(t):
        if 4000 <= idx < 5000:
            x1[idx] = val - 2
        elif 1000 <= idx < 2000:
            x1[idx] = val + 2
        elif 2000 <= idx < 4000:
            x1[idx] = -val
    fig, s1 = plt.subplots(6, 2)
    plot(x1, s1, "x1")


def second_signal():
    x2 = np.heaviside(-t, 1) + np.heaviside(t - 3, 1)
    fig, s2 = plt.subplots(6, 2)
    plot(x2, s2, "x2")


first_signal()
second_signal()
plt.show()
