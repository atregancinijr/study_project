from classes.classes import *


def test_pedido_pode_ser_atendido_se_existe_estoque():
    estoque = Estoque()
    estoque.aumentar("Produto A", 5)

    pedido = Pedido("Produto A", 5)
    atendido = pedido.atender(estoque)

    assert atendido is True
    assert 0 == estoque.quantidade("Produto A")


def test_pedido_nao_diminui_o_estoque_se_nao_pode_ser_atendido():
    estoque = Estoque()
    estoque.aumentar("Produto A", 1)

    pedido = Pedido("Produto A", 5)
    atendido = pedido.atender(estoque)

    assert atendido is False
    assert 1 == estoque.quantidade("Produto A")