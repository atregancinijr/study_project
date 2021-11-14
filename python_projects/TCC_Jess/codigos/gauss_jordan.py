import numpy as np

def gauss_jordan(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    n=len(b)
    #mainloop
    for k in range(n):
        #partial Pivoting
        if np.fabs(a[k, k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    for j in range(k, n):
                        a[k, j], a[i, j] = a[i, j], a[k, j]
                    b[k], b[i] = b[i], b[k]
                    break
        #division of pivot row
        pivot = a[k, k]
        for j in range(k, n):
            a[k, j] /= pivot
            a[k,j]=np.mod(a[k, j], 2)
        b[k] /= pivot
        b[k]=np.mod(b[k], 2)
        #elimination loop
        for i in range(n):
            if i == k or a[i, k] == 0: continue
            factor = a[i, k]
            for j in range(k, n):
                a[i, j] -= factor * a[k, j]

            b[i] -= factor * b[k]
    return b.astype(int), a.astype(int)

if __name__=='__main__':
    import matriz_BIBD as BIBD_class
    bbdi = BIBD_class.BIBD(tc=3, tr=5)
    H = bbdi.h_bibbd()


    x, A = gauss_jordan(a, b)
    print(f'Solution:\n{x}')
    print(f'The transformed [a]:\n{A}')
    np.savetxt('Output.txt', A, fmt='%d')