import numpy as np
import copy

class GaussElimination:

    def __init__(self, A):
        self.A = A

    def find_max_column_element_under_identity(self, c, A):
        B = np.transpose(A)
        #print(B)
        max_el = np.max(B[c][c:])
        row_idx = B[c][c:].argmax()
        #print(B[c][c:])
        return max_el, row_idx + c

    def swap_rows(self, A, idx1, idx2):
        B= np.copy(A)
        A_tmp = A[idx2]
        B[idx2] = A[idx1]
        B[idx1] = A_tmp
        return B

    def make_all_rows_below_this_0(self, i, A):
        B = np.transpose(A)
        for k in range(i+1, len(B)):
            B[i][k:] = 0
        return np.transpose(B)

    def sum_rows(self, c, A):
        B = np.transpose(A)
        C = np.copy(A)
        idx_list = []
        #print(f'print(B[{c}][{c}:]): {B[c][c:]}')
        for i in range(0, len(B[c][c:])):
            #print(f'len(B[c][c:]): {len(B[c][c:])}')
            print(c, i, i+c)
            if B[c][i+c] > 0 and c != i+c:
                idx_list.append(i)
                C[i+c] = (A[c] ^ A[i+c])
                if sum(C[i+c]) == 0:
                    print(f'c = {c}, A[c]: {A[c]}')
                    print(f'i = {i+c}, A[i]: {A[i+c]}')
                    print(f'i = {i+c}, C[i]: {C[i+c]}')

            else:
                pass
        #print(idx_list)
        idx_list.clear()
        return C

    def sum_rows2(self, c, A):
        B = np.copy(A)
        max_idx = self.get_first_one_last_line_pos(A)
        vector_idx = self.find_ones_in_a_line(B[c])
        #print(vector_idx)
        for i in range(0, len(A)):
            if (i != c) and (i <= max_idx) and (i in vector_idx[0]):
                B[c] = (B[c] ^ B[i])
                #print(B[c])
                vector_idx = self.find_ones_in_a_line(B[c])
        return B



    def get_first_one_last_line_pos(self, A):
        pos_idx = None
        for i, x in enumerate(A[len(A)-1]):
            if x == 0:
                pass
            else:
                pos_idx = i
                break
        return pos_idx


    def find_ones_in_a_line(self, A):
        list_idx = []
        idxs_tmp = []
        for j in range(0, len(A)):
            if A[j] == 1:
                #print(j)
                idxs_tmp.append(j)
                #print(idxs_tmp)
        idxs_tmp2 = np.copy(idxs_tmp)
        list_idx.append(idxs_tmp2)
        idxs_tmp.clear()
        return list_idx

    def gauss_elimination(self):
        B = self.A
        for i in range(0, len(B)):
            max_el, max_row_idx = self.find_max_column_element_under_identity(i, B)
            B = self.swap_rows(B, i, max_row_idx)
        for i in range(0, len(B)):
            B = self.sum_rows(i, B)
        B = self.check_and_remove_line_zero(B)
        for i in range(0, len(B)):
            B = self.sum_rows2(i, B)
        return(B)


    def check_and_remove_line_zero(self, B):
        idx_list = []
        for i in range(0, np.shape(B)[0]):
            if sum(B[i]) > 0:
                idx_list.append(i)
            else:
                pass
        return B[idx_list]


if __name__ == '__main__':
    import matriz_BIBD
    import matriz_de_gallager
    gallager = matriz_de_gallager.Matriz_de_gallager(20, 3, 4)
    bbdi = matriz_BIBD.BIBD(tc=3, tr=5)
    H =  bbdi.h_bibbd()
    #H = gallager.H_GA()
    print(H)

    gauss = GaussElimination(H)
    H = gauss.gauss_elimination()
    print(H)
#for i in range(0, len(H)):
    #    print(f'!!!{i}') if sum([list(H[i]) == list(H[j]) for j in range(0, len(H)) if i != j]) else None



