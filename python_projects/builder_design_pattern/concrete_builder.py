from builder import Builder
from transponder import Transponder
from utils import to_group


class TransponderBuilder(Builder):

    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Transponder()

    def set_network_lines(self, lines):
        lines = to_group(lines)
        for line in lines:
            self._product.add(f'LINE {line}')

    def set_client_ports(self, ports, ports_type):
        ports = to_group(ports)
        ports_type = to_group(ports_type)
        for port, port_type in zip(ports, ports_type):
            self._product.add(f'Port {port} : {port_type}')

    def set_client_subports(self, subports,  ports_type):
        subports = to_group(subports)
        ports_type = to_group(ports_type)
        for subport, port_type in zip(subports, ports_type):
            self._product.add(f'Port {", ".join(subport)} : {port_type}')

    def max_rate_per_line(self, rate):
        self._product.add(f'{rate} Gb/s')

    def higher_modulation(self, modulation):
        self._product.add(f'{modulation}')

    @property
    def product(self):
        product = self._product
        self.reset()
        return product


