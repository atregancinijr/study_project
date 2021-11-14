from abc import ABC, abstractmethod


class Cama(ABC):

    @abstractmethod
    def deitar(self):
        pass


class Cadeira(ABC):

    @abstractmethod
    def sentar(self):
        pass


class Sofa(Cadeira, Cama, ABC):
    pass
