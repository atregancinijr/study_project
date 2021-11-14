from abc import ABC, abstractmethod


class AbstractProductA(ABC):

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def do_another_thing(self):
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def do_a_normal_thing(self):
        pass

    @abstractmethod
    def do_a_crazy_thing(self):
        pass