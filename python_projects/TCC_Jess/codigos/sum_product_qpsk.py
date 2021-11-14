import numpy as np
import modulations as mod
import mpmath as mp
import projeto_tcc_jessica as tcc
if __name__=='__main__':
    H = np.array([[1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
                  [1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
                  [0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
                  [0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                  [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]])
    cn = np.array([0, 0, 0, 1, 0, 1, 0, 1, 0, 1])
    c_mod=tcc.BPSK_modulation(cn)
    r = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0, 1])
    #c_mod = mod.bit_to_QPSK(np.array([c]))[0]
    #SNR_dB = 2
    #y, N0 = tcc.add_noise(c_mod, SNR_dB)
    #print(y)
    #print(N0)
    #sigma = np.sqrt(N0/2)
    #gn_1 = np.exp(-((y-1)**2)/(2*sigma**2))
    #gn_0 = 1 - gn_1
    iteration=3
    #gn_1 = (1/(sigma*np.sqrt(2)))*np.exp(-((y+1)**2)/(2*sigma**2))
    #f= np.array([(a, b) for a, b in zip(gn_0, gn_1)])
    #print(f)
    f= np.array([[0.78, 0.22], [0.84, 0.16], [0.81, 0.19], [0.52, 0.48], [0.45, 0.55], [0.13, 0.87], [0.82, 0.18], [0.21, 0.79], [0.75, 0.25], [0.24, 0.76]]) #forced
    for inter in range(0, iteration):
        #print(f'{f}\n')
        Q= np.array([np.array([a*y for a in x]) for x, y in zip(H.T, f)])
        c,l,e = np.shape(Q)
        print(f'{c},{l},{e}')
        #print(Q)
        idxs=np.array([np.argwhere(i) for i in H]).T[0].T
        #print(idxs)
        a, b= np.shape(idxs)
        x2=[]
        for i in range(0,2**(b-1)):
            x=bin(i).split('0b')[1].rjust((b-1),'0')
            xl=np.array(list(x), dtype=int)
            #print(xl)
            if sum(xl)%2 >0:
                x2.append(xl)
        #print(x2)
        Rcol= []
        for i in range(0, l):
            #print(idxs[i])
            #print(x2[i])
            R_line =[]
            for j in range(0,len(idxs[i])):
                rmn = 0
                idxs2= np.delete(idxs[i], j)
                #print(idxs2)
                #print(f[idxs2])
                for w in x2:
                    prod = 1
                    #print(f'{f[idxs2]}, {w}')
                    for k,k2 in zip(f[idxs2], w):
                        #print(f'{k}, {k2}, {k[k2]}')
                        prod *=k[k2]
                    rmn += prod
                #print(f'SUM: {rmn}')
                R_line.append([1-rmn, rmn])
            Rcol.append(R_line)
        #print(Rcol)
        Rcol=np.array(Rcol)
        R=np.array([])
        for a, i in enumerate(H):
            #rint(i)
            Raux = []
            aux = 0
            #print(f'{a}, {i}')
            for b, j in enumerate(i):
                #print(f'{b}, {j}')
                if j == 1:
                    Raux.append(Rcol[a][aux])
                    aux+=1
                else:
                    Raux.append([0, 0])
            R= np.copy(np.reshape(np.array(Raux), [c, 1, e])) if a==0 else np.hstack([R, np.reshape(np.array(Raux), [c, 1, e])])
        #print(Q)
        #print(R)
        prod_vet = []
        Q_pos = []
        for i in range(0, c):
            q_val = 0
            for j in range(0, l):
                prod = [1, 1]
                q_val = Q[i][j]
                #print(f'q_val: {q_val}')
                R2 = np.copy(np.delete(R[i], j, 0))
                for k in R2:
                    if np.prod(k)==0:
                        pass
                    else:
                        prod*=k
                        #print(prod)
                if np.prod(q_val)==0:
                    prod_vet.append(np.inf)
                else:
                    prod_vet.append(prod*q_val)
                Q_pos.append(1/np.sum(prod*q_val)*prod*q_val) if np.sum(prod*q_val) > 0 else Q_pos.append([0, 0])
        #beta_nm = np.array([1/np.sum(x) for x in prod_vet])
        Q_pos = np.reshape(Q_pos,[10, 5, 2], 'C')
        #print(Q_pos)

        prod_vet = []
        Q_linha = []
        for i in range(0, c):
            q_val = 0
            for j in range(0, l):
                prod = [1, 1]
                q_val = Q[i][j]
                # print(f'q_val: {q_val}')
                R3 = np.copy(R[i])
                #print(R3)
                for k in R3:
                    if np.prod(k) == 0:
                        pass
                    else:
                        prod *= k
                    #print(f'{i},{j},{k}')
                if np.prod(q_val) == 0:
                    prod_vet.append(np.inf)
                else:
                    prod_vet.append(prod * q_val)
                    Q_linha.append(1 / np.sum(prod * q_val) * prod * q_val) if np.sum(prod * q_val) > 0 else Q_linha.append([0, 0])
                    break
        c_chapeu=[]
        print(Q_linha)

        [c_chapeu.append(0) if x[0]>x[1] else c_chapeu.append(1) for x in Q_linha]
        print(f'iter:{inter} -> {np.array(c_chapeu)}')

        if (np.array(c_chapeu) == cn).all():
            break
        f = np.copy(Q_linha)





