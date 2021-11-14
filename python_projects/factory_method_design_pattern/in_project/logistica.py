from abc import ABC, abstractmethod

class Logistica(ABC):

    @abstractmethod
    def cria_transporte(self):
        pass

    def entregar(self, mercadoria, pacote, local):
        transporte = self.cria_transporte()
        print('Iniciando processo de entrega...')
        return transporte.entregar(mercadoria, pacote, local)