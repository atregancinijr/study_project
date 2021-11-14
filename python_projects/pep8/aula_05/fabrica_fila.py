from typing import Union

from aula_05.constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from aula_05.fila_normal import FilaNormal
from aula_05.fila_prioritaria import FilaPrioritaria


class FabricaFila:

	@staticmethod
	def pega_fila(tipo_fila) -> Union[TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA]:
		if tipo_fila == TIPO_FILA_NORMAL:
			return FilaNormal()
		elif tipo_fila == TIPO_FILA_PRIORITARIA:
			return FilaPrioritaria()
		else:
			raise NotImplementedError('Tipo não cadastrado')
