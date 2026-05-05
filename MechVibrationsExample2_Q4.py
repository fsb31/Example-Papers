import numpy as np
import matplotlib.pyplot as plt

freq = np.linspace(0, 26, 260)
time = 10
x = 0.1
damping = 0.125

w_n = 128

freq_table = [0, 14, 16, 18, 20, 22, 24, 26]
resp_table = [.1, .19, .24, .34, .40, .29, .19, .13]

resp = x / np.sqrt((1 - ((2 * np.pi * freq/w_n) ** 2))**2 + (2 * damping * (2 * np.pi * freq/w_n))**2)





plt.plot(freq_table, resp_table, "x", label="Table Data")
plt.plot(freq, resp, label="Formula Data")
plt.xlabel("w / w_n")
plt.ylabel("Amplitude (mm)")
plt.legend()
plt.show()