from in_project.logistica import Logistica
from in_project.caminhao import Caminhao

class LogisticaRodoviaria(Logistica):

    def cria_transporte(self):
        print('Criando um caminhao para o transporte rodoviario...')
        return Caminhao()