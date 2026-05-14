import numpy as np


#Q3
'''
m = np.matrix([[1, 0], 
              [0, 2]])

k = np.matrix([[2, -1], 
              [-1, 3]])
'''

#Q5
m1 = 1
m2=3
k1=9

m = np.matrix([[m1, 0, 0], 
              [0, m2, 0],
              [0, 0, m1]])

k = k1 * np.matrix([[1, -1, 0], 
              [-1, 2, -1],
              [0, -1, 1]])


#Finds eigenvalues and vectors of M^-1 * K
freq, modes = np.linalg.eig(np.linalg.inv(m) * k)

#sometimes if a freq = 0, it is stored as -0, so sqrt throws error... just ignore

for i in range(len(freq)):
    print(f"Natural Freq Squared: {round(freq[i],3)}, Natural Freq: {round(np.sqrt(freq[i]),3)}")
    print(f"Mode Shape: {np.round(np.array((modes[:,i]/modes[0,i])).flatten().squeeze(),3)}") #converts from matrix to 2d array and removes extra dimensions
