from abc import ABC, abstractmethod
from pacman_game.elemento_movel import ElementoMovel


class ValidadorElementoMovel(ABC):

    @abstractmethod
    def adicionar_elemento_movivel(self, elemento_movel: ElementoMovel) -> None:
        pass
