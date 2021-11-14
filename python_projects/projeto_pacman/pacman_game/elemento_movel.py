from typing import List
from abc import ABC, abstractmethod


class ElementoMovel(ABC):

    @abstractmethod
    def aceitar_movimento(self) -> None:
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes: List[int]) -> None:
        pass

    @abstractmethod
    def esquina(self, direcoes: List[int]) -> None:
        pass
