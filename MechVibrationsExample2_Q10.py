import numpy as np
import matplotlib.pyplot as plt

freq = 190 #Hz of input signal
input_amplitude = 0.1 #amplitude of input
time = 100 #Length of time shown on graph



w_n = np.deg2rad(100) #natural freq of system
damping = 0.03
t = np.linspace(0, time*w_n, freq*time)

x = input_amplitude * np.sin(np.deg2rad(freq) * t)

if (damping == 1):
    impulse = w_n * t * np.exp(damping * -w_n * t)

else:
    w_d = w_n * np.sqrt(1-(damping ** 2))
    impulse = np.exp(damping * -w_n * t) * np.sin(w_d * t) / np.sqrt(1 - (damping ** 2))


resp = np.convolve(impulse, x, "full")[0:len(t)] #trim convolution to remove 'edge' effects

#doesnt trim, so edge effects still seen
#resp = np.convolve(impulse, x, "same")
#t2 = np.linspace(0, time*w_n, len(resp))



plt.plot(t, impulse, label="Impulse Resp.")
plt.plot(t, x, label="Input to system")
plt.plot(t, resp, label="Convolved output")
plt.xlabel("w_n * t")
plt.ylabel("Amplitude")
plt.legend()
plt.show()