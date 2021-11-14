import multiprocessing as multip
import numpy as np
from pyldpc.decoder import decode
from pyldpc import make_ldpc, encode, get_message, utils

n = 529
d_v = 3
d_c = 23
snr = 8
H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

print(H)
print('\n')
print(G)
print(H.shape)
print('\n')
print(G.shape)
k = G.shape[1]
print(k)
v = np.random.randint(1, size=k)
print(v)
y = encode(G, v, snr)
print(y)
d = decode(H, y, snr, 10)
print(d)
x = get_message(G, d)
print(x)
print(f'pass: {abs(x - v).sum() == 0}, {abs(x - v).sum()}')
