import matriz_BIBD as BIBD_class
from Utils import Utils_class
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import erfc

def coding_matrix(H):
    """Entrada:
            H: matriz de paridade não sistematica.
       Saída:
           H_reduzida: matriz de paridade sistemática
           G_sistematica: matriz geradora na forma sistemática"""

    n_lin, n_col = H.shape                                          #n_lin: número de linhas, n_col: número de colunas
    P = np.identity(n_col, dtype=int)                               #cria uma matriz identidade I_(n_col)

    H_reduzida = Utils_class.gaussjordan(H)                         #realiza a eliminação de gauss jordan, para colocar a matriz na forma sistemática
    #print(H_reduzida)                                              #H_reduzida NÃO tratada, ou seja, não elimina as linhas de zero
    k = n_col - sum([a.any() for a in H_reduzida])                  #retornará 'False' se a linha específica da matriz for de zeros.

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
    #### Temos como resultado G sistematica na forma |A^T | I_(k)|
    return G_sistematica, H_reduzida

def coding_message(u, G):
    """Realiza a codificação da mensagem
       Entradas:
               u: mensagem binária a ser codificada
               G: matriz geradora
        Saída:
              v: mensagem codificada (informação + redundância)"""
    u = np.array(u)
    G = np.array(G)
    v = u.dot(G)%2
    return v

def get_N0_value(SNR_dB, Es):
    """Calcula o valor de N0
       Entradas:
               SNR_dB: SNR em dB
               Es: Energia do simbolo
        Saída:
              N0"""
    SNR = 10 ** (SNR_dB / 10)
    N0 = Es/SNR
    return N0

def BPSK_modulation(input_PRBS):
    """Modula uma sequencia binária em BPSK
       Entrada:
            input_PRBS: vetor informação binária
       Saída: vetor modulado em BPSK (+1 e -1)"""
    return (-1 * (-1)**input_PRBS)

def add_noise(input_signal, SNR_dB):
    """Modula uma sequencia binária em BPSK
       Entrada:
            input_signal: vetor informação binária
            SNR_dB: SNR em dB
       Saída: y: vetor modulado com ruído"""
    x = BPSK_modulation(input_signal)   #mapeamento de binário para BPSK
    avg_energy = sum(abs(x) * abs(x)) / len(x)  #Es
    N0 = get_N0_value(SNR_dB, avg_energy)
    if isinstance(x[0], complex):
        n = np.sqrt(N0/2)*(np.random.randn(*x.shape) + 1j*np.sqrt(N0/2)*np.random.randn(*x.shape))
    else:
        n = np.sqrt(N0/2)*np.random.randn(*x.shape)
    y = x + n
    return y

def get_message(G, x):
    """Função responsável por separar a informção e a redundância,
       retornando apenas a informação.
       Entrada:
            G: matriz geradora
            x: vetor binário com a informação + redundância
       Saída: vetor modulado em BPSK (+1 e -1)"""
    k, n = G.shape
    #print(x)
    return x[n-k:n]


def decode_sum_product(y, H, iteration = 1,SNR_dB=0.0):  #nome: Probability-domain sum product algorithm LDPC decoder
    """Função principal que é responsável por decodificar/corrigir uma informação iterativamente.
       Entrada:
            y: informação modulada com ruído awgn
            H: Matriz de paridade na forma NÃO sistemática
            iteration: número de interações
            SNR_dB: SNR em dB
       Saída:
            decoded_vector: vetor binário codificado/corrigido (info + redundância)"""
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

def my_function(iteration, H_list, SNR_list, frames):
    """Função principal que retorna o desempenho de acordo com a SNR_dB.
        Foi colocado desta forma para utilizar dos artifícios da computação paralela.
       Entrada:
            H_list: lista que contém uma (ideal) ou mais matrízes de paridade. Usadado para plotar resultados de matrízes
                    diferentes de uma única vez. Entretanto é bem mais demorado.
            iteration: número de interações máximo dentro do algortimo de sum product
            SNR_dB: SNR em dB
            frames: quantidade de quadros transmitidos
       Saída:
            H_list_results_iterations: lista que contem o desempenho da BER para cada valor de SNR_dB. Para cada valor de iteration"""
    BER_sum_product_list = []
    H_list_results = [('BIBD', []), ('BIBD', [])]
    H_list_results_iterations = []
    for i, H in enumerate(H_list):
        G, H_new = coding_matrix(H)
        k, n = G.shape
        BER_sum_product = []
        for SNR_dB in SNR_list:
            bit_erros=0
            #bit_erros2=0
            bit_erros3=0
            for ii in range(0, frames):
                u = np.zeros(k)   #VETOR DE ZEROS para simular apenas o desempenho da matriz H
                #print(f'Mensagem original: {u}')
                v = coding_message(u, G)
                #print(f'Mensagem codificada: {v}')
                y = add_noise(v, SNR_dB)
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
            BER_sum_product.append(bit_erros/frames/k)
        #BER_sum_product_list.append(BER_sum_product)
        H_list_results[i][1].append(BER_sum_product)
    H_list_results_iterations.append(H_list_results)
    H_list_results=[('BIBD', []), ('BIBD', [])]
    return H_list_results_iterations

if __name__=='__main__':
    import multiprocessing as multip
    poolv = multip.Pool(multip.cpu_count()) #parâmetros da computação paralela
    """OS PARAMETROS SÃO INICIADOS AQUI:"""
    bbdi = BIBD_class.BIBD(wc=3, wr=37)    #wc peso de "1s" nas colunas e wr peso de "1s" nas linhas
    frames = 10000                          #número de quadros transmitidos. Cada quadro vai conter o vetor informação + redundância modulado com ruído. Usado para avaliar o desempenho pelas simulações de Mont Carlo
    SNR_list = [7.0]             #Numero de pontos de SNR_dB (eixo x nos plots)
    iteration_list=[2]                  #número de máximo iteração que o algortimo sum product pode fazer (Usar no máximo até 6 apoximadamente. Custo computacional alto)
    """Não precisa alterar nada daqui em diante"""
    H = bbdi.h_bibbd()
    H_list = [H]
    H_list_results = [('BIBD', []), ('BIBD', [])]
    color_list=['b','k']
    marker_list=['o','^','x']

    H_list_results_iterations = poolv.starmap(my_function, [(iteration, H_list, SNR_list, frames) for iteration in iteration_list])
    print(H_list_results_iterations)
    poolv.close()
    #print(H_list_results_iterations)
    BER_uncoded = 0.5 * erfc(np.sqrt(10 ** (np.array(SNR_list) / 10)))
    plt.semilogy(SNR_list, BER_uncoded, '--r', label='Uncoded')

    with open("Output.txt", "w") as text_file:            #salva os resultados da BER simulada, uncoded e vetor SNR_dB utilizado da última simulação em um arquivo texto
        text_file.write(f'{[H_list_results_iterations, BER_uncoded, SNR_list]}')
    H_list_results_iterations= np.reshape(H_list_results_iterations,[len(iteration_list), 2, 2])
    for i, x in enumerate(H_list_results_iterations):
        for j in range(0, len(H_list)):
            plt.semilogy(SNR_list, x[j][1][0], color=color_list[j], linestyle='--', marker=marker_list[i], label=f'{x[j][0]} Sum Product - Iteration = {iteration_list[i]}')
            plt.legend()
    plt.show()


