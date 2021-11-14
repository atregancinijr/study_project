class ParalelepipedoRegular:

    _id = 'paralelepipedo'

    def __init__(self, lado, altura):
        self._lado = lado
        self._altura = altura

    @property
    def id(self):
        return self._id

    @property
    def lado(self):
        return self._lado

    @property
    def altura(self):
        return self._altura

    @property
    def area_da_base(self):
        return self._lado*self._lado

    @property
    def volume(self):
        return self.area_da_base * self._altura

    def __str__(self):
        return f'Este paralelepipedo regular tem {self._lado} cm de lado, {self._altura} cm de altura. ' \
               f'Com uma área de {self.area_da_base} cm², totalizando um volume de {self.volume} cm³'
