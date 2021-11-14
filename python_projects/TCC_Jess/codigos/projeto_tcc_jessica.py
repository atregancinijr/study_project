import pyldpc
import matriz_BIBD as BIBD_class
import matriz_de_gallager as Gallager_class
from Utils import Utils_class
import numpy as np
import sys
from matplotlib import pyplot as plt
from scipy.special import erfc

def coding_matrix(H):
    n_lin, n_col = H.shape
    P = np.identity(n_col, dtype=int)

    H_reduzida = pyldpc.utils.gaussjordan(H)
    #print(H_reduzida) #H_reduzida NÃO tratada
    k = n_col - sum([a.any() for a in H_reduzida]) #retornará 'False' se a linha da matriz for de zeros.

######Depois do while abaixo, H_reduzida apresentará a forma padrão : | I_(n-k)  A |
    while (True):
        zeros = [i for i in range(min(n_lin, n_col))
                 if not H_reduzida[i, i]]
        if len(zeros):
            indice_coluna_a = min(zeros)
        else:
            break
        lista_de_1s = [j for j in range(indice_coluna_a + 1, n_col)
                     if H_reduzida[indice_coluna_a, j]]
        if len(lista_de_1s):
            indice_coluna_b = min(lista_de_1s)
        else:
            break
        aux = H_reduzida[:, indice_coluna_a].copy()
        H_reduzida[:, indice_coluna_a] = H_reduzida[:, indice_coluna_b]
        H_reduzida[:, indice_coluna_b] = aux

        aux = P[:, indice_coluna_a].copy()
        P[:, indice_coluna_a] = P[:, indice_coluna_b]
        P[:, indice_coluna_b] = aux

# --------------------------------------------------------------------------------------------------------------------------
    #print('H sistematica: \n')
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
    #print('Antes de remover linhas de zeros: ')
    #print(H_reduzida)
    #print(f'\nNumero de linhas de H_reduzida: {H_reduzida.shape[0]}, numero de colunas de H: {H_reduzida.shape[1]}')
    #print(f'\n')
#-----------------------------------------------------------------------
    #print('Depois de remover linhas de zeros: ')
    H_reduzida = Utils_class.remove_zeros_lines(H_reduzida)
    #print(H_reduzida) ###### Agora, H_reduzida tem a forma: | I_(n-k)  A |
    #print(f'\nNumero de linhas de H_reduzida: {H_reduzida.shape[0]}, numero de colunas de H_reduzida: {H_reduzida.shape[1]}')
#----------------------------------------------------------------------
    G_sistematica = np.zeros((k, n_col), dtype=int)
    G_sistematica[:, (n_col-k):] = np.identity(k)
    G_sistematica[:, :(n_col-k)] = (H_reduzida[:n_col - k, n_col - k:]).T
    #### Temos como rusultado G sistematica na forma |A^T | I_(k)|
    return G_sistematica, H_reduzida

def coding_message(u, G):
    u = np.array(u)
    G = np.array(G)
    v = u.dot(G)%2
    return v
def get_N0_value(SNR_dB, Eb):
    SNR = 10 ** (SNR_dB / 10)
    #print(f'Eb: {Eb}')
    N0 = Eb/SNR
    #N0 = 1/np.exp(SNR_dB*np.log(10)/10)
    return N0
def BPSK_modulation(input_PRBS):
    return (-1 * (-1)**input_PRBS)

def add_noise(modulated_signal, SNR_dB):
    x = np.copy(modulated_signal)  #mapeamento de binário para BPSK
    #print(x)
    avg_energy = sum(abs(x) * abs(x)) / len(x)  #Eb
    N0 = get_N0_value(SNR_dB, avg_energy)
    if isinstance(x[0], complex):
        n = np.sqrt(N0/2)*(np.random.randn(*x.shape) + 1j*np.sqrt(N0/2)*np.random.randn(*x.shape))
    else:
        n = np.sqrt(N0/2)*np.random.randn(*x.shape)
    y = x + n
    #print(y)
    return y, N0
def decode___bit_flip(y, H, iteration = 1):
    '''
    ENTRADAS
    y : sinal recebido
    H : matriz LDPC
    iteration : numero de iterações'''
    m, n = np.array(H).shape
    #Prior hard-decision
    c_i = (np.sign(y)+1)/2
    decoded_vector = np.zeros(n)
    r_ji = np.zeros([m, n])
    q_ij = H*(np.tile(c_i, [m, 1]))    #q_ij é a multiplicação da 'matriz da palavra código' e H.  (*Observação: a matriz palavra código é a palavra código repetida 'm' vezes e colocada linha sobre linha para formar um matriz compatível com as dimensões de H).
    H2 = np.copy(H)
    #print(H)
    #print(q_ij)
    for ii in range(0, iteration):
        #print(f'Iteration : {ii+1}:')
        #Horizontal step
        for jj in range(0, m):
            c1= np.nonzero(H[jj, :]) #Aqui coleta os índices dos elementos linha-a-linha (Horizontal Step) da matriz H que NÃO são zero.
            #print(c1)
            for kk in range(0, len(c1[0])):
                r_ji[jj, c1[0][kk]] = np.mod(np.sum(q_ij[jj,c1[0]]) + q_ij[jj, c1[0][kk]], 2)     #np.sum(q_ij[jj,c1[0]]) --> conta o numero de 1's de q_ij.
            #print(r_ji)  #sindrome?
        # Vertical step
        #print(r_ji)
        for jj in range(0, n):
            r1 = np.transpose(np.nonzero(H[:, jj]))
            num_de_uns = len(np.nonzero(r_ji[r1, jj])[0])
            for kk in range(0, len(r1)):   #'reajusta' q_ij para repetir em uma outra interação com esse 'novo' q_ij
                if (num_de_uns + int(c_i[jj])) >= (len(r1) - num_de_uns + int(r_ji[r1[kk],jj][0])):
                    q_ij[r1[kk], jj] = 1
                else:
                    q_ij[r1[kk], jj] = 0

            if num_de_uns + int(c_i[jj]) >= len(r1) - num_de_uns:
                decoded_vector[jj] = 1
            else:
                decoded_vector[jj] = 0

    return decoded_vector.astype(int)

def get_message(G, x):
    k, n = G.shape
    #print(x)
    return x[n-k:n]

def decode_bit_flip(y, H, iteration = 1):
    N1, N2 = np.array(H).shape
    # Prior hard-decision
    y = (np.sign(y) + 1) / 2
    E = np.zeros([N1, N2])
    yd = np.zeros([N2])

    for i in range(0, iteration):
        for j in range(0, N1):
            ci = np.nonzero(H[j, :])[0]
            for k in range(1, len(ci)):
                E[j, ci[k]] = np.mod(np.sum(y[ci])+y[ci[k]], 2)
        for j in range(0, N2):
            ri = np.transpose(np.nonzero(H[:, j]))
            numofones= len(np.nonzero(E[ri, j])[0])
            numofzeros=len(ri)-numofones
            if numofones == numofzeros:
                yd[j] = y[j]
            elif numofones > numofzeros:
                yd[j] = 1
            elif numofones < numofzeros:
                yd[j] = 0
            else:
                pass
        y=yd
    return y.astype(int)


def decode_sum_product(y, H, iteration = 1,SNR_dB=0.0):  #Probability-domain sum product algorithm LDPC decoder
    m, n = np.array(H).shape
    decoded_vector = np.zeros(n)
    N0 = get_N0_value(SNR_dB, 1)
    P1 = np.ones(len(y))/(1 + np.exp(-2*y/(N0/2)))
    #print(P1)
    P0 = 1 - P1
    K0 = np.zeros([m, n])
    K1 = np.zeros([m, n])
    r_ji0 = np.zeros([m, n])
    r_ji1 = np.zeros([m, n])
    q_ij0 = H * (np.tile(P0, [m, 1]))
    q_ij1 = H * (np.tile(P1, [m, 1]))

    for ii in range(0, iteration):
    # Horizontal step
        for jj in range(0, m):
            c1 = np.nonzero(H[jj, :])
            for kk in range(0, len(c1[0])):
                dr_ji = 1
                for ll in range(0, len(c1[0])):
                    if ll != kk:
                        dr_ji = dr_ji*(q_ij0[jj,c1[0][ll]] - q_ij1[jj, c1[0][ll]])
                r_ji0[jj,c1[0][kk]] = (1 + dr_ji)/2
                r_ji1[jj,c1[0][kk]] = (1 - dr_ji)/2
    # Vertical step
        for jj in range(0, n):
            r1 = np.transpose(np.nonzero(H[:, jj]))
            for kk in range(0, len(r1)):
                prodO_fr_ij0 = 1
                prodO_fr_ij1 = 1
                for ll in range(0, len(r1)):
                    if ll != kk:
                        prodO_fr_ij0 = prodO_fr_ij0 * r_ji0[r1[ll], jj]
                        prodO_fr_ij1 = prodO_fr_ij1 * r_ji1[r1[ll], jj]

                K0[r1[kk], jj] = P0[jj]*prodO_fr_ij0
                K1[r1[kk], jj] = P1[jj]*prodO_fr_ij1
                q_ij0[r1[kk],jj] = K0[r1[kk], jj][0]/(K0[r1[kk], jj][0] + K1[r1[kk], jj][0])
                q_ij1[r1[kk], jj] =K1[r1[kk], jj][0]/(K0[r1[kk], jj][0] + K1[r1[kk], jj][0])


            Ki0 = P0[jj]*np.prod(r_ji0[r1,jj], axis = 0)
            Ki1 = P1[jj]*np.prod(r_ji1[r1,jj], axis = 0)
            Qi0 = Ki0/(Ki0 + Ki1)
            Qi1 = Ki1/(Ki0 + Ki1)

            decoded_vector[jj] = 1 if Qi1 > Qi0 else 0
        if sum(decoded_vector)==0:
            #print(f'{ii} -> break')
            break
    return decoded_vector.astype(int)


if __name__=='__main__':
    bbdi = BIBD_class.BIBD(tc=3, tr=37)
    mgallager = Gallager_class.Matriz_de_gallager(37**2, 3, 37)
    #print('Limites para construção dos slopes: ')
    #bbdi.show_parameters_range()
    H = bbdi.h_bibbd()
    HGA = mgallager.H_GA()
    #print('\n')

    #print('Grid retangular: ')
    #bbdi.plot_retangular_grid()
    #print('\n')

    #print('Matriz H: \n')
   # np.savetxt('Output.txt', H, fmt='%d')

    #print("fim_")

    #print(f'\nNumero de linhas de H: {H.shape[0]}, numero de colunas de H: {H.shape[1]}')

    #print('coding_matrix: \n')
    #print(H)
    #print('G sistematica: \n')
    #print(G)
    #print(f'\nNumero de linhas de G: {G.shape[0]}, numero de colunas de G: {G.shape[1]}')

    BER_sum_product =[]
    BER_sum_product_list = []
    BER_sem_codf=[]
    H_list=[H, HGA]
    H_list_results = [('BIBD', []), ('Gallager', [])]
    H_list_results_iterations=[]
    maxiter = 10
    SNR_list = np.linspace(4.5, 5, 2)
    color_list=['b','k']
    marker_list=['o',4,'x']
    iteration_list=[1, 2]
    for iteration in iteration_list:
        for i, H in enumerate(H_list):
            G, H_new = coding_matrix(H)
            k, n = G.shape
            BER_sum_product = []
            for SNR_dB in SNR_list:
                bit_erros=0
                #bit_erros2=0
                bit_erros3=0
                for ii in range(0, maxiter):
                    #u = np.random.binomial(1, 0.5, size=k)
                    u = np.zeros(k)   #VETOR DE ZERO
                    #print(f'Mensagem original: {u}')
                    v = coding_message(u, G)
                    #print(f'Mensagem codificada: {v}')
                    v2 = BPSK_modulation(v)
                    y = add_noise(v2, SNR_dB)
                    #print(f'Mensagem + ruído: {y}')
                    x = decode_sum_product(y, H, iteration=iteration, SNR_dB=SNR_dB)
                    #print(x)
                    u_linha = get_message(G, x)
                    #u_linha2 = get_message(G, x2)
                    #print(f'Mensagem codificada  : {v}')
                    #print(f'Mensagem decodificada: {x} \n')

                    #print(f'Mensagem original  : {u}')
                    #print(f'Mensagem recuperada: {u_linha}\n')
                    #print(f'Iteração {ii+1}.:')
                    #print(f'Numero de erros do "sum product" para {SNR_dB} dB de SNR : {sum(abs(u - u_linha))}')
                    #print(f'Numero de erros do "sem codificação" para {SNR_dB} dB de SNR : {sum(abs(u - np.array((np.sign(add_noise(u, SNR_dB)) + 1) / 2).astype(int)))}')
                    bit_erros += sum(abs(u - u_linha))
                    #bit_erros2 += sum(abs(u - u_linha2))
                    #bit_erros3 += sum(abs(u - np.array((np.sign(add_noise(u, SNR_dB)) + 1) / 2)).astype(int))
                BER_sum_product.append(bit_erros/maxiter/k)
                #BER_sem_codf.append(bit_erros3/maxiter/k)
            #BER_sum_product_list.append(BER_sum_product)
            H_list_results[i][1].append(BER_sum_product)
        H_list_results_iterations.append(H_list_results)
        H_list_results=[('BIBD', []), ('Gallager', [])]
    print(H_list_results_iterations)
    BER_theory = 0.5 * erfc(np.sqrt(10 ** (np.array(SNR_list) / 10)))
    plt.semilogy(SNR_list, BER_theory, '--r', label='Theory')

    with open("Output.txt", "w") as text_file:
        text_file.write(f'{[H_list_results_iterations, BER_theory, SNR_list]}')

    for i,x in enumerate(H_list_results_iterations):
        for j in range(0, len(H_list)):
            print(x[j][1][0])
            print(x[j][0])
            plt.semilogy(SNR_list, x[j][1][0], color=color_list[j], linestyle='--', marker=marker_list[i], label=f'{x[j][0]} Sum Product - Iteration = {iteration_list[i]}')
    plt.legend()
    plt.show()


