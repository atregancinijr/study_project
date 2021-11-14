class Cilindro:

    _id = 'cilindro'

    def __init__(self, raio, altura):
        self._raio = raio
        self._altura = altura

    @property
    def id(self):
        return self._id

    @property
    def raio(self):
        return self._raio

    @property
    def altura(self):
        return self._altura

    @property
    def area_da_base(self):
        return 3.14159 * self._raio**2

    @property
    def volume(self):
        return self.area_da_base*self._altura

    def __str__(self):
        return f'Este cilindro tem {self._raio} cm de raio, {self._altura} cm de altura. ' \
               f'Com uma área de {self.area_da_base} cm², totalizando um volume de {self.volume} cm³.'