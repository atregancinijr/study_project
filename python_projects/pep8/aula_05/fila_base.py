from abc import ABC, abstractmethod
from typing import List, Union

from aula_05.estatistica_detalhada import EstatisticaDetalhada
from aula_05.estatistica_resumida import EstatisticaResumida
from aula_05.constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]

class FilaBase(ABC):

    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self):
        pass

    @abstractmethod
    def chama_cliente(self, caixa: int):
        pass

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
