from project.cilindro import Cilindro
from project.paralelepipedo_regular import ParalelepipedoRegular


class ParapelepipedoAdapter(ParalelepipedoRegular, Cilindro):

    def __init__(self, lado, altura):
        super().__init__(lado, altura)

    @property
    def raio(self):
        return self.lado / (2 ** (1 / 2))