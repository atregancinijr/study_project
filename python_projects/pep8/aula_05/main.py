from aula_05.fila_normal import FilaNormal
from aula_05.fila_prioritaria import FilaPrioritaria
from aula_05.fabrica_fila import FabricaFila
from aula_05.estatistica_resumida import EstatisticaResumida
from aula_05.estatistica_detalhada import EstatisticaDetalhada


# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

# teste_fabrica = FabricaFila.pega_fila('normal')
# teste_fabrica.atualizafila()
# teste_fabrica.atualizafila()
# teste_fabrica.atualizafila()
# print(teste_fabrica.chama_cliente(10))

fila = FabricaFila.pega_fila('prioritaria')
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaResumida('20/03/2025', 1245)))

fila2 = FabricaFila.pega_fila('normal')
fila2.atualiza_fila()
fila2.atualiza_fila()
fila2.atualiza_fila()
print(fila2.chama_cliente(5))
print(fila2.estatistica(EstatisticaDetalhada('20/03/2025', 1245)))
