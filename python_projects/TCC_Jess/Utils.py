import numpy as np


class Utils_class:
    def __init__(self):
        pass

    @staticmethod
    def write_matrix_to_textfile(a_matrix, file_to_write):

        def compile_row_string(a_row):
            return str(a_row).strip(']').strip('[').replace(' ', '')

        with open(file_to_write, 'w') as f:
            for row in a_matrix:
                f.write(compile_row_string(row) + '\n')

        return True

    @staticmethod
    def hstack_vect_to_matrix(A, b):
        if len(b) == np.shape(A)[0]:
            A_ = np.hstack([A[0], b[0]])
            for i in range(1, len(b)):
                A_ = np.vstack([A_, np.hstack([A[i], b[i]])])
            return A_
        else:
            raise Exception(f'len(B) -> {len(b)} != np.shape(A)[0] -> {np.shape(A)[0]}.')

    @staticmethod
    def remove_zeros_lines(M):
        B = []
        for x in M:
            if sum(x) == 0:
                pass
            else:
                B.append(x)
        return np.array(B, dtype=int)

    @staticmethod
    def gaussjordan(X, change=0):
        A = np.copy(X)
        m, n = A.shape

        if change:
            P = np.identity(m).astype(int)

        pivot_old = -1
        for j in range(n):
            filtre_down = A[pivot_old + 1:m, j]
            pivot = np.argmax(filtre_down) + pivot_old + 1

            if A[pivot, j]:
                pivot_old += 1
                if pivot_old != pivot:
                    aux = np.copy(A[pivot, :])
                    A[pivot, :] = A[pivot_old, :]
                    A[pivot_old, :] = aux
                    if change:
                        aux = np.copy(P[pivot, :])
                        P[pivot, :] = P[pivot_old, :]
                        P[pivot_old, :] = aux

                for i in range(m):
                    if i != pivot_old and A[i, j]:
                        if change:
                            P[i, :] = abs(P[i, :] - P[pivot_old, :])
                        A[i, :] = abs(A[i, :] - A[pivot_old, :])

            if pivot_old == m - 1:
                break

        if change:
            return A, P
        return A