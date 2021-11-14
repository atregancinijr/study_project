from abstract_factory import AbstractFactory
from concrete_producties import ConcreteProductAType1, ConcreteProductBType1, ConcreteProductAType2, ConcreteProductBType2

class ConcreteFactory_Type1(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductAType1()

    def create_product_b(self):
        return ConcreteProductBType1()


class ConcreteFactory_Type2(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductAType2()

    def create_product_b(self):
        return ConcreteProductBType2()