from unittest.mock import MagicMock, Mock, patch


class Pedido:
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

    def atender(self, estoque):
        try:
            estoque.diminuir(self.produto, self.qtd)
        except SemEstoque:
            return False
        else:
            return True


class SemEstoque(Exception):
    pass


class Estoque:
    def __init__(self):
        self.produtos = {}

    def aumentar(self, produto, qtd):
        self.produtos[produto] = self.produtos.get(produto, 0) + qtd

    def diminuir(self, produto, qtd):
        if self.quantidade(produto) >= qtd:
            self.produtos[produto] -= qtd
            return True
        raise SemEstoque

    def quantidade(self, produto):
        if produto in self.produtos.keys():
            return self.produtos[produto]
        return 0