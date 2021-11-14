import numpy as np
class Matriz_de_gallager:
    def __init__(self, N, ds, dc):
        self.N = N
        self.ds = ds
        self.dc = dc

    def __submatriz_H1(self):
        subm=np.hstack([np.ones(self.dc, dtype=int), np.zeros(int(self.N - self.dc), dtype=int)])
        for ii in range(1, int(self.N/self.dc)):
            subm = np.vstack([subm, np.hstack([np.zeros(ii*self.dc, dtype=int), np.ones(self.dc, dtype=int),
                            np.zeros(int(self.N - (ii+1)*self.dc), dtype=int)])])
        return subm

    def ds_evaluate(self, matrix):
        line_vet = []
        Nn = np.shape(matrix)[1]
        for n in range(0, Nn):
            line_vet.append(sum(np.transpose(matrix)[n]))
        return line_vet

    def dc_evaluate(self, matrix):
        line_vet = []
        Mm =np.shape(matrix)[0]
        for m in range(0, Mm):
            line_vet.append(sum(matrix[m]))
        return line_vet

    def __submatriz_Hx(self):
        idx = range(0, self.N)
        new_idx = np.random.permutation(idx)
        subm = np.transpose(self.__submatriz_H1())
        new_subm = subm[new_idx[0]]
        for c in new_idx[1:]:
            new_subm = np.vstack([new_subm, subm[c]])
        return np.transpose(new_subm)

    def H_GA(self):
        HGA = self.__submatriz_H1()
        for ll in range(0, self.ds-1):
            HGA = np.vstack([HGA, self.__submatriz_Hx()])
        return HGA
if __name__=='__main__':
    mgallager = Matriz_de_gallager(23**2, 3, 23)

    hga = mgallager.H_GA()
    print('Matriz H Gallager:')
    print(hga)
    print(np.shape(hga))
