from abstract_products import AbstractProductA, AbstractProductB


class ConcreteProductAType1(AbstractProductA):

    def do_something(self):
        print("ProductA with Type 1: I'm doing something...")

    def do_another_thing(self):
        print("ProductA with Type 1: I'm doing anotherthing...")


class ConcreteProductAType2(AbstractProductA):

    def do_something(self):
        print("ProductA with Type 2: I'm doing something...")

    def do_another_thing(self):
        print("ProductA with Type 2: I'm doing anotherthing...")


class ConcreteProductBType1(AbstractProductB):

    def do_something(self):
        print("ProductB with Type 1: I'm doing something...")

    def do_a_normal_thing(self):
        print("ProductB with Type 1: I'm doing a normal thing...")

    def do_a_crazy_thing(self):
        print("ProductB with Type 1: I'm doing a crazy thing...")


class ConcreteProductBType2(AbstractProductB):

    def do_something(self):
        print("ProductB with Type 2: I'm doing something...")

    def do_a_normal_thing(self):
        print("ProductB with Type 2: I'm doing a normal thing...")

    def do_a_crazy_thing(self):
        print("ProductB with Type 2: I'm doing a crazy thing...")
