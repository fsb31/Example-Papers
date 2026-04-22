import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf



def DFT(data): #slow
    N = len(data)
    X = np.zeros(N, dtype=complex)
    for k in range(0, N-1):
        for n in range(0, N-1):
            X[k] += data[n] * complex(np.cos(-2 * np.pi * k * n/N), np.sin(-2 * np.pi * k * n/N))
    return X


def PadData(data):
    N = len(data)
    if (N <= 1): return data
    if (N.bit_count() != 1):
        New = int(np.pow(2, np.ceil(np.log2(N)))) - N
        return np.pad(data, (0, New))


def FFT(data):
    N = len(data)

    if (N <= 1): return data
    
    X_1 = FFT(data[::2])
    X_2 = FFT(data[1::2])
    a = np.exp(-2j*np.pi*np.arange(N) * 1/N)

    return np.concatenate([X_1 + X_2*a[:N//2], X_1 + X_2*a[N//2:]])



#read data
data, rate = sf.read("Armstrong_Small_Step.ogg")
no_samples = len(data)
T = no_samples // rate #Sample length
print(f"Audio Length: {T}s, Sample Rate: {rate}.") 


t = np.linspace(0, T, no_samples, endpoint=False) #Sample times

#tmp_data = np.sin((2*np.pi*240) * t) + np.sin((2*np.pi *440) * t) #temporary data

#fft needs data length to be a power of 2 for recursion
data = PadData(data)

#fft
X = FFT(data)

#Remove 'mirrored' data
N = len(X)//2
X = X[:N]/N



#Plot
freq_axis = np.linspace(0, rate/2, N)

#plt.plot(t, tmp_data)
plt.plot(freq_axis, np.abs(X))
plt.xlabel("Freq (Hz)")
plt.ylabel("Amplitude")
plt.show()

