from director import Director
from concrete_builder import TransponderBuilder


director = Director()
transp_builder = TransponderBuilder()
director.builder = transp_builder

director.build_800g_transponder()
transp_builder.product.list_parts()
print('\n')
director.build_1200g_transponder()
transp_builder.product.list_parts()



#Não preciso necessariamente do director
builder = TransponderBuilder()

builder.max_rate_per_line('400')
builder.higher_modulation('DP-32QAM')
builder.set_network_lines('1')
builder.set_client_ports(['1', '2', '3', '4'],
                              ['QSFP28', 'QSFP28', 'QSFP28', 'QSFP28'])
print('\n')
transponder = builder.product
transponder.list_parts()
