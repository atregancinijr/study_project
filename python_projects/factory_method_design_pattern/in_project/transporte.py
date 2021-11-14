from abc import ABC, abstractmethod

class Transporte(ABC):

    @abstractmethod
    def entregar(self, mercadoria, pacote, local):
        pass