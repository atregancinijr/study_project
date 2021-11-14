
class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_800g_transponder(self):
        self.builder.max_rate_per_line('400')
        self.builder.higher_modulation('DP-16QAM')
        self.builder.set_network_lines(['1', '2'])
        self.builder.set_client_ports(['1', '2', '3', '4', '5', '6', '7', '8'],
                                      ['QSFP28', 'QSFP28', 'QSFP28', 'QSFP28',
                                       'QSFP28', 'QSFP28', 'QSFP28', 'QSFP28'])

    def build_1200g_transponder(self):
        self.builder.max_rate_per_line('600')
        self.builder.higher_modulation('DP-64QAM')
        self.builder.set_network_lines(['1', '2'])
        self.builder.set_client_ports(['1', '2', '3', '4'],
                                      ['QSFP28', 'QSFP28', 'QSFP28', 'QSFP28'])
        self.builder.set_client_subports([('5.1', '5.2'), ('6.1', '6.2'), ('7.1', '7.2'), ('8.1', '8.2')],
                                         ['QSFPDD', 'QSFPDD', 'QSFPDD', 'QSFPDD'])

