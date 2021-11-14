from abc import ABC, abstractmethod

from pygame import Surface
from pygame.event import Event

class ElementoJogo(ABC):

    @abstractmethod
    def pintar(self, tela: Surface) -> None:
        pass

    @abstractmethod
    def calcular_regras(self) -> None:
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass
