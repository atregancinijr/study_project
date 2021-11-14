from typing import List

from aula_05.fila_base import FilaBase
from aula_05.constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
	def gera_senha_atual(self) -> None:
		self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

	def chama_cliente(self, caixa: int) -> List[str]:
		display = []
		cliente_atual: str = self.fila.pop(0)
		display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

		if len(self.fila) >= 3:
			display.append(f'Próximo: {self.fila[0]}')
			display.append(f'Fique atento: {self.fila[1]}')

		self.clientes_atendidos.append(cliente_atual)

		return display
