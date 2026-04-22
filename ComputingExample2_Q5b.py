import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("southwing.jpg")
x, y = img.size

A = np.array(img.split()[0])
B = np.zeros(A.shape)

G = np.array([[-1, -1, -1], 
              [-1,  8, -1],
              [-1, -1, -1]])

n = len(G[0])
d = n//2

for i in range(1, x-1):
    for j in range(1, y-1):
        #convolve
        for k in range(0, n-1, 1):
            for l in range(0, n-1, 1):
                B[j,i] += G[l, k] * A[j-d+l, i-d+k]


plt.imshow(B, cmap='gray_r', vmin = 0, vmax=255)
plt.show()
