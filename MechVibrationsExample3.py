import numpy as np


m = np.array([[1, 0], [0, 2]])

k = np.array([[2, -1], [-1, 3]])

#Finds eigenvalues and vectors of M^-1 * K
freq, modes = np.linalg.eig(np.linalg.inv(m) * k)

print(freq)
print(modes)