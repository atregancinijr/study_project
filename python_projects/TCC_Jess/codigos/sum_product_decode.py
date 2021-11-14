import numpy as np

H = np.array([[1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0 ,0, 1]])
m = np.array([0, 0, 0, 0])
c = np.array([0, 0, 0, 0, 0, 0, 0, 0])  #c=mG
c_mod = -(-1)**c
print(c_mod)
Eb = sum(abs(c_mod) * abs(c_mod)) / len(c_mod)  # Eb
SNR_dB = 0
SNR = 10 ** (SNR_dB / 10)
N0 = Eb/SNR
n = np.sqrt(N0/2)*np.random.randn(*c_mod.shape)
y = c_mod + n
print(y)