from product import Product


class ConcreteProductA(Product):

    def operation(self):
        return 'Result of the ConcreteProductA'


class ConcreteProductB(Product):

    def operation(self):
        return 'Result of the ConcreteProductB'


class ConcreteProductC(Product):

    def operation(self):
        return 'Result of the ConcreteProductC'
