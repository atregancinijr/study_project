from project.mobilia_abstract import MobiliaAbstrata
from project.produtos_concretos import *


class MobiliaVitoriana(MobiliaAbstrata):
    @property
    def sofa(self):
        return SofaVitoriano()

    @property
    def cama(self):
        return CamaVitoriana()

    @property
    def cadeira(self):
        return CadeiraVitoriana()

    def __str__(self):
        return 'Mobília estilo Vitoriano.'


class MobiliaModerna(MobiliaAbstrata):
    @property
    def sofa(self):
        return SofaModerno()

    @property
    def cama(self):
        return CamaModerna()

    @property
    def cadeira(self):
        return CadeiraModerna()

    def __str__(self):
        return 'Mobília estilo Moderno.'
