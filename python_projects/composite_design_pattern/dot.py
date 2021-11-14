from graphic import Graphic
import numpy as np

class Dot(Graphic):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, x, y):
        self._x = x
        self._y = y

    def draw(self, plot):
        plot.plot(self._x, self._y, 'o')


class Circle(Dot):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius

    def draw(self, plot):
        angle = np.linspace(0, 2 * np.pi, 150)
        x = self._radius * np.cos(angle) + self._x
        y = self._radius * np.sin(angle) + self._y
        plot.plot(x, y)
