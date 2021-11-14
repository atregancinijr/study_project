from classes.classes import *

def test_pedido_pode_ser_atendido_se_existe_estoque():
    estoque = Mock()
    estoque.diminuir.return_value = True

    pedido = Pedido("Produto A", 5)
    atendido = pedido.atender(estoque)

    assert atendido is True
    estoque.diminuir.assert_called_once_with("Produto A", 5)


def test_pedido_nao_diminui_o_estoque_se_nao_pode_ser_atendido():
    estoque = Mock()
    estoque.diminuir.side_effect = SemEstoque()
    estoque.quantidade.return_value = 1

    pedido = Pedido("Produto A", 5)
    atendido = pedido.atender(estoque)

    estoque.diminuir.assert_called_once_with("Produto A", 5)
    assert atendido is False