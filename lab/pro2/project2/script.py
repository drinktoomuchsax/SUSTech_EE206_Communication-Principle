import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

alpha = np.arange(0.1, 1, 0.1)
roll_off = 0.3
baud_rate = 100000 # in symbols per second
osf = 16 # oversampling factor
samples_per_sym = osf
sym_rate = baud_rate / samples_per_sym

for a in alpha:
    # generate a signal with random symbols
    symbols = np.random.randint(4, size=int(1e5))
    sigdata = np.zeros(samples_per_sym * len(symbols), dtype=np.float32)
    for idx, sym in enumerate(symbols):
        sigdata[idx * samples_per_sym:(idx + 1) * samples_per_sym] = \
            (2 * (sym & 1) - 1) * (1 + 1j * (2 * (sym >> 1) - 1)) / np.sqrt(2)

    # apply pulse-shaping filter
    tx_filter = sig.root_raised_cosine(int(osf * 10), osf, roll_off, taps=None)
    filtered_sig = sig.convolve(sigdata, tx_filter)

    # plot the spectrum of the transmitted signal
    freq = np.fft.fftshift(np.fft.fftfreq(len(filtered_sig), d=1.0 / sym_rate))
    psd = abs(np.fft.fftshift(np.fft.fft(filtered_sig))) ** 2
    plt.plot(freq, psd, label='alpha={}'.format(a))

plt.legend()
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (dB/Hz)')
plt.show()
