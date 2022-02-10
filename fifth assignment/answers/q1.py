# Presented by: Farshid Nooshi
# Part 1 
# AM Modulation and demodulation
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz

# Constants
T0 = 0.1
TS = 0.001
FS = 1000
CUT_OFF = 100
# Time 
TIME = np.linspace(0, T0, FS)
FREQUENCE = np.linspace(-FS / 2, FS / 2, 1024 * 1024)


#  sinc signal
def input_function(t):
    if t >= 0 and t <= T0:
        return np.sinc(100 * t)
    else:
        return 0


# DSB-AM
def am(t):
    return input_function(t) * np.cos(2 * np.pi * 250 * t)


# demodulation
def dam(t):
    return am(t) * np.cos(2 * np.pi * 250 * t)


# Fourier transform
def CTFT(s, fs, m):
    signal = np.fft.fft(s, m)
    shift_fft = np.abs(np.fft.fftshift(signal))

    return shift_fft


# Low pass filter
# Copied from internet
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# signals
y1 = [input_function(x) for x in TIME]
y2 = [am(x) for x in TIME]
y3 = [dam(x) for x in TIME]
y4 = butter_lowpass_filter(y3, CUT_OFF, FS, 5)
# CTFT signals
x1 = CTFT(y1, FS, m=len(FREQUENCE))
x2 = CTFT(y2, FS, m=len(FREQUENCE))
x3 = CTFT(y3, FS, m=len(FREQUENCE))
x4 = CTFT(y4, FS, m=len(FREQUENCE))

# Plot
fig, s1 = plt.subplots(8)

s1[0].plot(TIME, y1)
s1[1].plot(FREQUENCE, x1)
s1[2].plot(TIME, y2)
s1[3].plot(FREQUENCE, x2)
s1[4].plot(TIME, y3)
s1[5].plot(FREQUENCE, x3)
s1[6].plot(TIME, y4)
s1[7].plot(FREQUENCE, x4)

plt.show()
