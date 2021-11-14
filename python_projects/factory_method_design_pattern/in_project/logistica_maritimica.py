from in_project.logistica import Logistica
from in_project.navio import Navio


class LogisticaMaritimica(Logistica):

    def cria_transporte(self):
        print('Criando um navio para o transporte maritimo...')
        return Navio()