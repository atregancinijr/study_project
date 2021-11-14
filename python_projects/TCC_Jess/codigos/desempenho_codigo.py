import pyldpc
import numpy as np
import matriz_BIBD
import matplotlib.pyplot as mpl
bbdi = matriz_BIBD.BIBD(tc=3, tr=37)
maxiter = [1]
SNR =np.arange(6.0, 10.0, 0.5)
nsamples=1000
H = bbdi.h_bibbd()
H, G = pyldpc.coding_matrix_systematic(H, sparse=True)
print(G)
k = G.shape[1]
erros = 0
BER = np.zeros([len(maxiter), len(SNR)])
for z, Z in enumerate(maxiter):
    for i, snr in enumerate(SNR):
        for jj in np.arange(0, nsamples):
            v = np.random.randint(2, size=k)
            y = pyldpc.encode(G, v, snr)
            d = pyldpc.decode(H, y, snr, Z)
            x = pyldpc.get_message(G, d)
            erros += np.sum(abs(x - v))
            #print(erros)
        BER[z, i] = erros/(k*nsamples)
        erros = 0
print(BER)
for kkk in range(0, len(maxiter)):
    mpl.semilogy(SNR, BER[kkk])
mpl.show()

