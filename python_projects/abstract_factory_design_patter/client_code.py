from abstract_factory import AbstractFactory
from concrete_factories import ConcreteFactory_Type1, ConcreteFactory_Type2

def client_code(factory):

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print("     Product A:")
    product_a.do_something()
    product_a.do_another_thing()
    print("     Product B:")
    product_b.do_something()
    product_b.do_a_normal_thing()
    product_b.do_a_crazy_thing()

if __name__ == "__main__":
    print("Client: Testing client code. Factory type 1:")
    client_code(ConcreteFactory_Type1())
    print("Client: Testing client code. Factory type 2:")
    client_code(ConcreteFactory_Type2())