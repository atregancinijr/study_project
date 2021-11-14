
class Buraco:

    def __init__(self, raio, profundidade):
        self._raio = raio
        self._profundidade = profundidade

    @property
    def raio(self):
        return self._raio

    @property
    def profundidade(self):
        return self._profundidade

    def fits(self, cilindro):
        return cilindro.raio <= self.raio and cilindro.altura <= self.profundidade

    def __str__(self):
        return f'Este buraco tem {self._raio} centimetros de raio ' \
               f'e {self._profundidade} centrimetros de profundidade'
