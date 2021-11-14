import numpy as np
from pyldpc import make_ldpc, decode, get_message, encode
from matplotlib import pyplot as plt
from scipy.special import erfc
n = 1369
d_v = 3
d_c = 37
maxiteration = 1

seed = np.random.RandomState(42)

H, G = make_ldpc(n, d_v, d_c, seed=seed, systematic=True, sparse=True)

n, k = G.shape
print("Number of coded bits:", k)

errors = []
snrs = np.linspace(-2, 10, 5)
n_trials = 100  # number of transmissions with different noise
for snr in snrs:
    v = np.arange(k) % 2  # fixed k bits message
    V = np.tile(v, (n_trials, 1)).T  # stack v in columns
    y = encode(G, V, snr, seed=seed)
    D = decode(H, y, snr, maxiteration)
    error = 0.
    for i in range(n_trials):
        x = get_message(G, D[:, i])
        error += abs(v - x).sum() / (k * n_trials)
    errors.append(error)

BER_theory = 0.5 * erfc(np.sqrt(10 ** (np.array(snrs) / 10)))
plt.figure()
plt.semilogy(snrs, errors, marker='o', color="indianred")
plt.semilogy(snrs, BER_theory)
plt.ylabel("Bit error rate")
plt.xlabel("SNR")
plt.show()

