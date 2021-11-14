from graphic import Graphic


class CompoundGraphic(Graphic):

    def __init__(self):
        self._graphic = []
        self._x = None
        self._y = None

    def add(self, graphic):
        self._graphic.append(graphic)

    def remove(self, graphic):
        self._graphic.remove(graphic)

    def move(self, x, y):
        self._x = x
        self._y = y

    def draw(self, plot):
        for p in self._graphic:
            p.draw(plot)
