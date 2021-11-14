from matplotlib import pyplot as plt
from scipy.special import erfc
import numpy as np

color_list = ['b', 'k', 'r']
marker_list = ['o', '^', 'x']
iteration_list = [1, 2, 3]

SNR_list = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
BER_result = [[0.03801587301587302, 0.029523809523809525, 0.023015873015873017, 0.015714285714285715, 0.009523809523809525, 0.004841269841269841, 0.0019793650793650795, 0.000595, 0.0001507936507936508, 2.380952380952381e-05], [0.035793650793650794, 0.028650793650793652, 0.02246031746031746, 0.014682539682539682, 0.008015873015873016, 0.0030952380952380953, 0.0005626984126984127, 7.817460317460317e-05], [0.037619047619047614, 0.028095238095238093, 0.023015873015873017, 0.01674603174603175, 0.00992063492063492, 0.0024603174603174604, 0.00024444444444444443, 1.7777777777777777e-05]]
# print(H_list_results_iterations)
BER_theory = 0.5 * erfc(np.sqrt(10 ** (np.array(SNR_list) / 10)))
plt.semilogy(SNR_list, BER_theory, '--g', label='Theory')



plt.semilogy(SNR_list, BER_result[0], color=color_list[0], linestyle='--', marker=marker_list[0],
             label=f'(1260, 1369) Iteration = {iteration_list[0]}')
plt.legend()


BER_result = [[0.036580086580086574, 0.02623376623376623, 0.01751082251082251, 0.010735930735930736, 0.005974025974025974, 0.0023593073593073596, 0.0008181818181818182, 0.00024783549783549783, 5.629004329004329e-05, 1.2987012987012988e-05], [0.033766233766233764, 0.026125541125541125, 0.016406926406926408, 0.00803030303030303, 0.0032683982683982685, 0.0006926406926406926, 0.00011471861471861471, 2.0779220779220778e-05], [0.036082251082251084, 0.025497835497835495, 0.01551948051948052, 0.00683982683982684, 0.0011471861471861473, 0.00015151515151515154, 2.51965367965368e-05, 3.03030303030303e-06]]

plt.semilogy(SNR_list, BER_result[0], color=color_list[1], linestyle='--', marker=marker_list[0],
             label=f'(462, 569)Iteration = {iteration_list[0]}')
plt.legend()
plt.show()