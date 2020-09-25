import numpy as np
import matplotlib.pyplot as plt


def displayDualSpectrum(x, fs):
    N = len(x)
    Xk = np.fft.fft(x)/N
    Xk = np.concatenate((Xk[range(int(N/2), N)], Xk[range(int(N/2))]))
    f = np.array(np.arange(-fs/2, fs/2, fs/N))
    plt.axis([-fs/2, fs/2, 0, round(max(abs(Xk))*1.2)])
    plt.plot(f, np.abs(Xk))
    plt.xlabel("Frekvens (Hz)")
    #plt.ylabel("Amplitude")
    plt.grid()