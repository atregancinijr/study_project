import numpy as np
class BIBDclass:

    def __init__(self, N, v, k):
        self.N = N
        self.v = v
        self.k = k
        self.m = np.sqrt(N)


    def h_bibbd(self):
        H = np.zeros([self.v, self.N], dtype=int)