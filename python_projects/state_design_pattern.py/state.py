from abc import ABC, abstractmethod


class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle_request1(self):
        pass

    @abstractmethod
    def handle_request2(self):
        pass
