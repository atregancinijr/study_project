from creator import Creator
from concrete_products import ConcreteProductA, ConcreteProductB, ConcreteProductC

class ConcreteCreatorA(Creator):

    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):

    def factory_method(self):
        return ConcreteProductB()

class ConcreteCreatorC(Creator):

    def factory_method(self):
        return ConcreteProductC()