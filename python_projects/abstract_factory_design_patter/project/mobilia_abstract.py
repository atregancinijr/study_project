from abc import ABC, abstractmethod
"""<<Interface>>"""


class MobiliaAbstrata(ABC):

    @property
    @abstractmethod
    def cadeira(self):
        pass

    @property
    @abstractmethod
    def sofa(self):
        pass

    @property
    @abstractmethod
    def cama(self):
        pass
