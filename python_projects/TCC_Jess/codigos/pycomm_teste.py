import multiprocessing as multip
import numpy as np
from pyldpc.decoder import decode
from pyldpc import make_ldpc, encode, get_message, utils
from matplotlib import pyplot as plt
from scipy.special import erfc

def my_function(iteration, H, G, SNR_list, frames):
    BER = []
    k = G.shape[1]
    for snr in SNR_list:
        bit_erros = 0
        for ii in range(0, frames):
            v = np.random.randint(1, size=k)
            y = encode(G, v, snr)
            d = decode(H, y, snr, iteration)
            x = get_message(G, d)
            bit_erros +=abs(x - v).sum()
        BER.append(bit_erros / frames / k)
    return BER
if __name__ == '__main__':
    poolv = multip.Pool(multip.cpu_count())
    d_v = 3
    d_c = 23
    n = d_c**2

    H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

    frames = 10
    SNR_list = [6.5]
    color_list = ['b', 'k', 'r']
    marker_list = ['o', '^', 'x']
    iteration_list = [1]

    BER_result = poolv.starmap(my_function, [(iteration, H, G, SNR_list, frames) for iteration in iteration_list])
    print(SNR_list)
    print(BER_result)
    poolv.close()
    # print(H_list_results_iterations)
    BER_theory = 0.5 * erfc(np.sqrt(10 ** (np.array(SNR_list) / 10)))
    plt.semilogy(SNR_list, BER_theory, '--g', label='Theory')

    for i, x in enumerate(BER_result):
        print(x, i)
        plt.semilogy(SNR_list, x, color=color_list[i], linestyle='--', marker=marker_list[i],
                     label=f'Iteration = {iteration_list[i]}')
        plt.legend()
    plt.show()