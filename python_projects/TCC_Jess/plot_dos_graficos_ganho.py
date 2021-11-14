from matplotlib import pyplot as plt
from scipy.special import erfc, erfcinv
import numpy as np
import matplotlib.ticker as tck
from matplotlib import rc

def SNR_dB_BER_in(BER_out):
    return 20*np.log10(erfcinv(2*BER_out))

rc('font', **{'family':['serif'],'serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
color_list = ['b', 'k', 'r', 'y', 'm', 'g']
marker_list = ['o', 4, 'x', '^', 5, 's']
iteration_list = [1, 2, 3, 4, 5, 6]
code = ['(1369, 1260)']
SNR_list = np.array([0., 0.55555556, 1.11111111, 1.66666667, 2.22222222, 2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.0, 5.25])
H_list=[0]
H_list_results_iterations = np.array([[0.07924603174603174, 0.06566666666666666, 0.05302380952380953, 0.04176984126984127, 0.03290476190476191, 0.023253968253968256, 0.015253968253968252, 0.008261904761904762, 0.003373015873015873, 0.0013015873015873015, 0.0007801587301587301],
                                      [0.07832539682539683, 0.06567460317460318, 0.05424603174603174, 0.04221428571428571, 0.03230952380952381, 0.02184920634920635, 0.012484126984126985, 0.005595238095238095, 0.0017142857142857144, 0.00023015873015873014, 8.412698412698413e-05],
                                      [0.08031746031746032, 0.06620634920634921, 0.05463492063492064, 0.04338095238095238, 0.03378571428571429, 0.02207142857142857, 0.011373015873015873, 0.004396825396825397, 0.0007222222222222223, 4.761904761904762e-05, 1.3492063492063494e-05],
                                      [0.07895238095238095, 0.06517460317460318, 0.05361904761904762, 0.04230952380952381, 0.03212698412698412, 0.022595238095238095, 0.012357142857142858, 0.0033333333333333335, 0.0005793650793650794, 3.1746031746031745e-05, 5.4380952380952384e-06],
                                      [0.07914285714285714, 0.06622222222222222, 0.05323809523809524, 0.042888888888888886, 0.031230158730158733, 0.02211904761904762, 0.010476190476190476, 0.002746031746031746, 0.0002777777777777778, 1.5873015873015872e-05, 3.96031746031746e-06],
                                      [0.07767460317460317, 0.06674603174603175, 0.05257936507936508, 0.04386507936507937, 0.03150793650793651, 0.022174603174603177, 0.012476190476190478, 0.0023174603174603175, 0.00020634920634920634, 7.936507936507936e-06, 2.5634920634920636e-06]])
plt.figure(1, figsize = (9.5, 7.5))

plt.ylabel(r'$\textrm{Ganho de codificação}_{\textrm{dB}}$', fontsize = 16)
plt.xlabel(r'BER', fontsize = 16)
plt.ylim(0, 5)
plt.xlim(np.min(H_list_results_iterations), np.max(H_list_results_iterations))

BER_theory = 0.5 * erfc(np.sqrt(10 ** (np.array(SNR_list)/ 10)))
print(BER_theory)
SNR_in_correspondente = []
ganho_dB = []
for ber_out in H_list_results_iterations:
    SNR_in_correspondente.append(SNR_dB_BER_in(ber_out))

for snr_in in SNR_in_correspondente:
    ganho_dB.append(snr_in - SNR_list)


for i, x in enumerate(zip(H_list_results_iterations, ganho_dB)):
    for j in range(0, len(code)):
        plt.semilogx(x[0], x[1], color=color_list[j], linestyle='-', marker=marker_list[i],
                     label=f'Iteração = {iteration_list[i]}')
plt.legend()
plt.legend(prop={"size":14})
plt.savefig('figure5.pdf', format='pdf', dpi=1000)
plt.show()