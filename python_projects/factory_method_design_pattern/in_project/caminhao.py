from in_project.transporte import Transporte


class Caminhao(Transporte):

    _meio_de_entrega = 'terra'

    def entregar(self, mercadoria, pacote, local):
        return f'Pela {self._meio_de_entrega}, saindo para entregar ' \
               f'{mercadoria} em {pacote} diretamente para {local} ' \
               f'com meu caminhão'

