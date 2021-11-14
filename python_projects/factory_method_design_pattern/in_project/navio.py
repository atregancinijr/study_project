from in_project.transporte import Transporte


class Navio(Transporte):

    _meio_de_entrega = 'mar'


    def entregar(self, mercadoria, pacote, local):
        return f'Pelo {self._meio_de_entrega}, saindo ' \
               f'para entregar {mercadoria} em {pacote} diretamente ' \
               f'para {local} com meu navio.'
