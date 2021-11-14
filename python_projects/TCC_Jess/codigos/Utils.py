import numpy as np


class Utils_class:
    def __init__(self):
        pass

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