from compound_graphic import CompoundGraphic
from dot import Dot, Circle
import matplotlib.pyplot as plt
import numpy as np


plot = plt
plot.figure()

dot = Dot(1, 1)
circle = Circle(2, 1, 1)

circle2 = Circle(1, 1, 1)

dot3 = Dot(2, 0)
circle3 = Circle(3, 2, 1)

composite = CompoundGraphic()
composite.add(dot)
composite.add(circle)
composite.add(circle2)

composite2 = CompoundGraphic()
composite2.add(composite)


composite2.add(dot3)
composite2.add(circle3)
composite2.draw(plot)

dot2 = Dot(3, 3)
dot2.draw(plot)

plot.show()
