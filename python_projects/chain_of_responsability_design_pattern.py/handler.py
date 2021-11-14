from abc import ABC, abstractmethod

"""<<<Interface>>>"""


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass
