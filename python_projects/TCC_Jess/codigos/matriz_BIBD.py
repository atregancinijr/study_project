import matplotlib.pyplot as plt
import numpy as np
class BIBD:
    def __init__(self, tc, tr):
        self.k = tc
        self.m = tr

    def show_parameters_range(self):
        print(f'0 <= s <= {self.m - 1}')
        print(f'0 <= x <= {self.k - 1}')
        print(f'0 <= a <= {self.m- 1}')

    def plot_retangular_grid(self):
        x, y, t = self.__get_grid_points()
        for i in range(0, len(x)):
            plt.text(x[i], y[i], t[i], horizontalalignment='left', verticalalignment='bottom')
        plt.scatter(x, y, edgecolors='k')
        plt.show()

    def __get_grid_points(self):
        counter = 1
        dict_points = {}
        for s in range(0, self.m):
            for x in range(0, self.k):
                for a in range(0, self.m):
                    if (x, a + s * (divmod(x, self.m)[0])) in list(dict_points.values()):
                        pass
                    else:
                        dict_points.update({counter: (x, a + s * (divmod(x, self.m)[0]))})
                        counter += 1
        #print(dict_points)
        x, y = np.transpose(list(dict_points.values()))
        t = np.transpose(list(dict_points.keys()))
        return x, y, t

    def __build_s0_lattice2_table_design(self):
        t = self.__get_grid_points()[2]
        t = np.reshape(t, [self.k, self.m])
        return np.transpose(t)

    def __build_sx_lattice2_table_design(self, s):
        sx = self.__build_s0_lattice2_table_design()
        sx_t = np.transpose(sx)
        for x in range(0, len(sx_t)):
            sx_t[x] = np.roll(sx_t[x], -s*x)
        #print(sx_t)
        return(np.transpose(sx_t))
    def dependent_lines_elimination(self, Ht):
        for i in range(0, np.shape(Ht)[0]):
            for j in range(0, np.shape(Ht)[0]):
                if i != j:
                    print(i, j, sum([(list(Ht[i] ^ Ht[j]) == list(row)) for row in Ht]))
                    print(i, j, list(Ht[i]) == list(Ht[j]))

    def h_bibbd(self):
        Ht = np.zeros([self.m ** 2, self.k * self.m], dtype=int)
        #print(np.shape(Ht))
        h = self.__build_sx_lattice2_table_design(0)
        for s in range(1, self.m):
            h = np.vstack([h, self.__build_sx_lattice2_table_design(s)])
        for i, vect_idx in enumerate(h):
            Ht[i][vect_idx-1] = 1
        return np.transpose(Ht)

if __name__=='__main__':
    import pyldpc
    bbdi = BIBD(tc=3, tr=5)
    bbdi.show_parameters_range()
    maxiter =5
    #print('\n')
    #bbdi.plot_retangular_grid()
    H = bbdi.h_bibbd()
    print(H)
    print(H.shape)
    H, Gt = pyldpc.coding_matrix_systematic(H, sparse=True)
    print('G: \n')
    print(Gt.T)
    print(Gt.shape)
    k = Gt.shape[1]

    v = np.random.randint(2, size=k)
    print(v)
    print(v.shape)

    y = pyldpc.encode(Gt, v, 0)
    print(y)
    print(y.shape)
    d = pyldpc.decode(H, y, 5, maxiter)
    print(d)
    print(d.shape)
    x = pyldpc.get_message(Gt, d)
    print(x)
    print(f'pass: {abs(x - v).sum() == 0}')














