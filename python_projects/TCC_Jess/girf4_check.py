import numpy as np
from matriz_BIBD import BIBD
from matriz_de_gallager import Matriz_de_gallager

def check_LDPC_girth4(H):
    H = np.array(H)
    girth = []
    rows, cols = np.shape(H)
    print(H, '\n', np.transpose(H))
    O = np.dot(H, np.transpose(H))
    print(O)
    for i in np.arange(0, rows):
        O[i, i] = 0
    print(np.shape(O))
    print(O)
    for i in np.arange(0, rows):
        girth.append(np.max(O[i, :]))
    print(girth)
    girth4 = np.max(girth)
    print(girth4)
    if girth4 < 2 :
        print('No girth 4 \n')
    else:
        print('The H matrix has girth 4 \n')

if __name__ == '__main__':
    bbdi = BIBD(wc=3, wr=5)
    mgallager = Matriz_de_gallager(5 ** 2, 3, 5)
    #H  = bbdi.h_bibbd()
    H = mgallager.H_GA()

    check_LDPC_girth4(H)

