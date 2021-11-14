from abc import ABC, abstractmethod

class Graphic(ABC):

    @abstractmethod
    def move(self, x, y):
        pass

    def draw(self, plot):
        pass