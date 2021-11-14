from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_network_lines(self, lines):
        pass

    @abstractmethod
    def set_client_ports(self, ports, ports_type):
        pass

    @abstractmethod
    def set_client_subports(self, subports, ports_type):
        pass

    @abstractmethod
    def max_rate_per_line(self, rate):
        pass

    @abstractmethod
    def higher_modulation(self, modulation):
        pass